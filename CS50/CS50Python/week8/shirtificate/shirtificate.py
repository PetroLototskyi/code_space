from fpdf import FPDF


class Format:
    def __init__(self, name):
        # Create a new FPDF instance
        self._pdf = FPDF()

        # Add a new page to the PDF
        self._pdf.add_page()

        # Set font for the title
        self._pdf.set_font("times", "BI", 35)

        # Set text color for the title
        self._pdf.set_text_color(116, 14, 49)

        # Create a cell for the title with border and centered alignment
        self._pdf.cell(0, 30, "CS50 Shirtificate", ln=True, border=1, align="C")

        # Add an image to the PDF with specific coordinates and width
        self._pdf.image("shirtificate.png", x=10, y=50, w=self._pdf.w - 20)

        # Set font size and text color for the additional text
        self._pdf.set_font_size(40)
        self._pdf.set_text_color(18, 125, 90)

        # Calculate the width of the text to center it
        text_width = self._pdf.get_string_width(f"{name} took CS50")

        # Calculate the x-coordinate to center the text
        x_coordinate = (self._pdf.w - text_width) / 2

        # Add the text with the calculated coordinates
        self._pdf.text(x=x_coordinate, y=125, txt=f"{name} took CS50")

    def save(self, name):
        # Output the PDF to a file with the specified name
        self._pdf.output(name)


# Get user input for the name
user_name = input("Name: ")

# Create a Format instance with the user name and save the PDF
output = Format(user_name)
output.save("shirtificate.pdf")
