import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, send_file, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, read_bin_file, generate_pdf_file
from datetime import datetime, date, timedelta
from flask import make_response


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///inventory.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    # Create list of lists with item# and location
    bin_list = read_bin_file()

    # Retrive today day
    today = date.today()

    return render_template('index.html', bin_list=bin_list, today=today)


# Generete PDF page
@app.route('/generate-label', methods=['GET', 'POST'])
def generate_label():
    label_dict = {}
     # Retrieve user ID from the session
    user_id = session["user_id" ]

    # Handle POST request
    if request.method == 'POST':
        # Retrieve user input from the form
        part_number = request.form.get("part_number")
        revision = request.form.get("revision")
        qty = request.form.get("qty")
        date_open = request.form.get("date_open")
        lot = request.form.get("lot")
        location = request.form.get("location")

        # Validate does part number provided and store the user input
        if part_number:
            label_dict = {
                'part_number': part_number,
                'revision': revision,
                'qty': qty,
                'date_open': date_open,
                'lot': lot,
                'location': location
            }

            # Get the current timestamp
            current_timestamp = datetime.now()

            # Insert the information into the operations table
            db.execute( "INSERT INTO label (user_id, part_number, revision, quantity, date, lot, location, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   user_id, part_number, revision, qty, date_open, lot, location, current_timestamp)

        pdf_file = generate_pdf_file(label_dict)
        # Create a response with the PDF file
        response = make_response(send_file(pdf_file, as_attachment=False, download_name='label.pdf'))

        return response


@app.route("/history", methods=["GET", "POST"])
@login_required
def history():
    """Show history of printed labels"""


    user_id = session["user_id"]

    # Retrive information from forms fileds where filter can be applied
    part_number_filter = request.args.get("partNumberFilter", "")
    date_filter = request.args.get("dateFilter", "")
    lot_filter = request.args.get("lotFilter", "")
    location_filter = request.args.get("locationFilter", "")

    # Define the quety to with retriverd information
    query = """
        SELECT u.fname, u.lname, l.part_number, l.revision, l.quantity, l.date, l.lot, l.location, l.time
        FROM label l
        JOIN users u ON u.id = l.user_id
        WHERE user_id = ? AND
              part_number LIKE ? AND
              date LIKE ? AND
              lot LIKE ? AND
              location LIKE ? ORDER BY l.time DESC
    """

    # Execute query and assign the query result to labels
    labels = db.execute(query, user_id, f"%{part_number_filter}%", f"%{date_filter}%", f"%{lot_filter}%", f"%{location_filter}%")

    # Return updated history page
    return render_template("history.html", labels=labels)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrieve form data
        uname = request.form.get("username")
        fname = request.form.get("firstname")
        lname = request.form.get("lastname")
        pw = request.form.get("password")
        confirmpw = request.form.get("confirmation")

        # Check if username is provided
        if not uname:
            return apology("Enter username")

        # Check db for username
        dbuname = db.execute("SELECT * FROM users WHERE LOWER(username) = LOWER(?)", uname)

        # Check if username exists
        if dbuname:
            return apology("Username already exists")

        # Check if First name exist
        if not fname:
            return apology("Enter First Name")

        # Check if Last name exist
        if not lname:
            return apology("Enter Last Name")

        # Check if password entered
        if not pw:
            return apology("Enter password")

        # Check if the password contains at least one letter
        if not any(c.isalpha() for c in pw):
            return apology("Password must contain at least one letter")

        # Check if the password contains at least one number
        if not any(c.isdigit() for c in pw):
            return apology("Password must contain at least one number")

        # Chek if confirmation entered
        if not confirmpw:
            return apology("Confirm the password")

        # Chek if confirmation and password are same
        if pw != confirmpw:
            return apology("Passwords do not match")

        # Insert user into db. Generate hash before addind to db
        token = generate_password_hash(pw)
        db.execute("INSERT INTO users (username, hash, fname, lname) VALUES (?, ?, ?, ?)", uname, token, fname, lname)

        return redirect("/")

    else:
        # Display the registration form for GET requests
        return render_template("register.html")


@app.route("/pwchange", methods=["GET", "POST"])
@login_required
def pwchange():
    """Update password"""
    # Retrive user id
    user_id = session["user_id"]

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrive pw and confirmation fron submited form
        new_pw = request.form.get("new_password")
        new_confirmpw = request.form.get("new_confirmation")

        # Chek password entered
        if not new_pw:
            return apology("Enter new password")

        # Check if new password contains at least one letter
        if not any(c.isalpha() for c in new_pw):
            return apology("Password must contain at least one letter")

        # Check if new password contains at least one number
        if not any(c.isdigit() for c in new_pw):
            return apology("Password must contain at least one number")

        # Chek if confirmation entered
        if not new_confirmpw:
            return apology("Confirm the new password")

        # Chek if confirmation and password are same
        if new_pw != new_confirmpw:
            return apology("Passwords do not match")

        # Modefying existing user entry with new pw and hash
        new_token = generate_password_hash(new_pw)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_token, user_id)

        return redirect("/")

    else:
        # Display the password change form for GET requests
        return render_template("pwchange.html")
