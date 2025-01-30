import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    """Show portfolio of stocks"""

    # Retrieve user ID from the session
    user_id = session["user_id" ]

    # Retrieve the user's current cash balance from the db
    cash = db.execute("SELECT cash FROM users WHERE id =?", user_id)[0]["cash"]

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Retrieve the amount of cash to add from the submitted form
        add_cash = int(request.form.get("add_cash"))

        # Calculate the new cash balance
        new_amount = int(cash) + add_cash

        # Update the user's cash balance in the db
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_amount, user_id)

        # Display a flash message indicating the successful addition of cash
        flash(f"New cash added: ${add_cash}", "success")

        # Redirect to the home page after updating the cash balance
        return redirect("/")

    # Handle GET request for the home page
    else:
        # Retrieve the user's stock portfolio from the db
        stocks = db.execute("SELECT symbol, price, SUM(shares) as total_shares FROM operations WHERE user_id =? GROUP BY symbol", user_id)

        # Initialize the total value variable
        total_value = cash

        # Calculate the total value of the portfolio (cash + stocks)
        for stock in stocks:
            total_value += stock["price"] * stock["total_shares"]

        # Render the home page template with the user's portfolio information
        return render_template("index.html", stocks = stocks, cash=cash, dollar_sign=usd, total_value=total_value )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrieve the stock symbol from the submitted form and convert to uppercase
        symbol = request.form.get("symbol").upper()

        # Check if the symbol provided
        if not symbol:
            return apology("Enter a symbol")

        # Look up the stock information using the symbol
        item = lookup(symbol)

        # Check if the stock symbol is found
        if not item:
            return apology("Incorrect symbol")

        # Retrieve the number of shares to buy from the submitted form
        shares = request.form.get("shares")

        # Check if the number of shares is provided
        if not shares:
            return apology("Enter a number of shares")

        # Check if the number of shares is numeric value
        elif not shares.isdigit():
            return apology("Enter numeric value in shares field")

        # Check if the number of shares is a positive number
        elif int(shares) <= 0:
            return apology("The value in shares field must be positive number")

        # Retrieve the user's ID from the session
        user_id = session["user_id"]

        # Retrieve the user's current cash balance from the database
        cash = db.execute("SELECT cash FROM users WHERE id =?", user_id)[0]["cash"]

        # Retrieve stock price
        item_price = item["price"]

        # Calculate the total cost of the shares
        total = item_price * int(shares)

        # Check if the user has enough cash
        if cash < total:
            return apology("No enough money in the account")

        # Update the user's cash balance in the database
        db.execute("UPDATE users SET cash = ? WHERE id =?", cash - total, user_id)

        # Insert the information into the operations table
        db.execute( "INSERT INTO operations (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   user_id, symbol, shares, item_price)

        return redirect("/")
    else:
        # Handle GET request
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    operations = db.execute("SELECT symbol, price, shares, time FROM operations WHERE user_id = ?", user_id )

    return render_template("history.html", operations=operations, dollar_sign=usd)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Obtain the symbol from the submitted form
        symbol = request.form.get("symbol")

        # Check if the symbol is not provided
        if not symbol:
            return apology("Enter a symbol")

        # Look up the stock information using the symbol
        item = lookup(symbol)

        # Chek is stok exist
        if item is None:
            return apology("Invalid symbol")

        # Render the template with the stock information
        return render_template("quoted.html", item=item, dollar_sign=usd)

    else:
        # Render the quote.html template for the initial page load
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrieve form data
        uname = request.form.get("username")
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
        db.execute("INSERT INTO users (username, hash) VALUES (?,?)", uname, token)

        return redirect("/")

    else:
        # Display the registration form for GET requests
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # Retrieve the user ID from the session
    user_id = session["user_id"]

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrieve symbol and shares from the submitted form
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Check if the entered shares is a positive number
        if int(shares) <= 0:
            return apology("Enter a positive number")

        # Retrieve stock information
        item_price = lookup(symbol)["price"]
        item_symbol = lookup(symbol)["symbol"]

        # Calculate the total price of seling shares
        total_price = int(shares) * item_price

        # Check if the user owns enough shares to sell
        shares_owned = db.execute("SELECT shares FROM operations WHERE user_id =? AND symbol = ? GROUP BY symbol", user_id, symbol)[0]["shares"]
        if shares_owned < int(shares):
            return apology("Not enough shares")

        # Retrieve the user's current cash balance
        curent_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        # Update the user's cash balance after selling shares
        db.execute("UPDATE users SET cash = ? WHERE id = ?", curent_cash + total_price, user_id)

        # Record the sale in the operations table
        db.execute("INSERT INTO operations (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", user_id, item_symbol, -int(shares), item_price)

        # Redirect to the home page after selling shares
        return redirect ("/")

    # Handle GET request for rendering the sell page
    else:
        # Retrieve symbols of owned stocks for displaying in the form
        symbols = db.execute("SELECT symbol FROM operations WHERE user_id = ? GROUP BY symbol", user_id)
        return render_template("sell.html", symbols=symbols)


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
