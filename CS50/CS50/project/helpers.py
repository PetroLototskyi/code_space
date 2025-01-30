import csv
import datetime
from io import BytesIO
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Frame
from flask import redirect, render_template, session
from functools import wraps

BINS = "bin_location.tsv"  # tab separated file
LOGO = "static/logo.png"

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


    # Reed the *.tsv file and create list of lissts ( in this case 2 elements in exh list)
def read_bin_file():

    bin_list = []

    with open(BINS) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        next(tsvreader)   # Skip firs row
        for line in tsvreader:
            item = line[0]

            #  Handle Item numbers without location
            bin_id = line[1] if len(line) > 1 else " "
            bin_list.append([item, bin_id])

    return bin_list


    # Generate label with sutable size for Label printer printer
    # https://www.geeksforgeeks.org/how-to-create-pdf-files-in-flask/
def generate_pdf_file(label_dict):
    # Creating empy buger
    buffer = BytesIO()

    # reating empty space to draw
    p = canvas.Canvas(buffer)

    # Retrive logo
    logo = ImageReader(LOGO)

    # Size of the PDF page
    w, h = 4 * inch, 2.31 * inch
    pagesize = (w, h)
    p.setPageSize(pagesize)

    # Position the Logo on the page
    p.drawImage(logo, w * 0.09, h - 0.55 * inch, 1.28 * inch, 0.44 * inch, mask='auto')

    # Position the "Inventory Ticket" text
    p.setFont("Helvetica-Bold", 10)
    p.drawString(w * 0.46, h - 0.45 * inch, "Inventory Ticket")

    # Position the "QF15-04.  Rev 1." text
    p.setFont("Helvetica", 5)
    p.drawString(w * 0.8, h - 0.35 * inch, "QF15-04.  Rev 1.")

    p.setFont("Helvetica", 9)

    # Set width of the line
    p.setLineWidth(0.5)
    story = []

    # Draw ouside rectangle
    frame = Frame(.25 * inch, .25 * inch, w - .5 * inch, 1.50 * inch, showBoundary=1)
    frame.addFromList(story, p)

    # Draw horisontal lines
    p.line(.25 * inch, 1.30 * inch, w - .25 * inch, 1.30 * inch)
    p.line(.25 * inch, .80 * inch, w - .25 * inch, .80 * inch)

    # Draw vertical lines
    p.line(1.33 * inch, .80 * inch, 1.33 * inch, 1.30 * inch)
    p.line(2.53 * inch, .80 * inch, 2.53 * inch, 1.75 * inch)

    # Position text/cell names
    y = h - 0.7 * inch
    p.drawString(w * 0.09, y, f"Part number")
    p.drawString(w * 0.09, y - 35, f"Quantity")
    p.drawString(w * 0.09, y - 70, f"Location")

    p.drawString(w * 0.35, y - 35, f"Date Open")

    p.drawString(w * 0.65, y, f"Revision")
    p.drawString(w * 0.65, y - 35, f"Lot")

    # Create spases to thousands
    qty = label_dict['qty']
    qty = '{:,}'.format(int(qty)).replace(',', ' ')

    # Position the values for each cell
    a = 17
    p.setFont("Helvetica", 12)
    p.drawString(w * 0.09,  y - a, f"{label_dict['part_number']: >23}")
    p.drawString(w * 0.09,  y - 34 - a, f"{qty: >10}")
    p.drawString(w * 0.09,  y - 70 - a, f"{label_dict['location']: >35}")

    # Take curent date
    datetime_object = datetime.strptime(label_dict['date_open'], '%Y-%m-%d')
    date = f"{datetime_object:%d-%b-%Y}"
    p.drawString(w * 0.36, y - 34 - a, f"{date: >10}")

    p.drawString(w * 0.65, y - a, f"{label_dict['revision']: >12}")
    p.drawString(w * 0.65, y - 35 - a, f"{label_dict['lot']: >12}")

    # p.showPage()
    p.save()

    buffer.seek(0)

    return buffer

