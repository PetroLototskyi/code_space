# Inventory Label Generator and Tracker
#### Video Demo:  <https://youtu.be/-EU3blaD4qo>
#### Description:

I've created an inventory labeling system for a manufacturing company's Inventory department. It generates PDF label prints for label printers using data from the "bin_location.tsv" file, supporting autocomplete, PDF generation, label printer compatibility, and robust entry tracking with filtering.

The entry fields for label information are strategically positioned to mirror their appearance on the printed label. While all fields are mandatory, they remain adjustable. Even if an item is already in the database and the autocomplete function has populated the location field, users have the flexibility to modify it as needed. Numeric entry fields are designed to exclusively accept positive integers.

Upon pressing the "Generate Label" button, the resulting PDF file opens in a new windows tab. This PDF features a graphical design incorporating the company logo, Inventory ticket name, revision details of the utilized form, and part information (including part#, revision, quantity, date, lot#, and location) presented in a table format. The PDF file is formatted to match the physical label size, making it suitable for direct printing on label printers.

An essential aspect of this project is the "history" page, allowing users to track all entries used for label generation. This page boasts a user-friendly scroll-down table showcasing data entered into each field. To enhance usability, a filtering functionality has been implemented, simplifying searches within this comprehensive table. Beyond these core functionalities (Label Generation and Data Tracking), the project encompasses Registration, Login, and password-changing features, drawing inspiration from the design principles of the last CS50 homework.

The primary areas of contention in the project were the autocomplete function, the method for rendering PDF files, and the decision regarding the inclusion of a "Regenerate" button. The autocomplete function was implemented using JavaScript. I found a helpful example of "How to create PDF files in Flask" (a link to which was included as a comment for the "generate_pdf_file()" function) and used it for creating PDF. The decision to omit the "Regenerate" button was made due to its limited utility and lack of real necessity.

### Here is the complete structure of my project with a short description of all files:

**flask_session folder:** &nbsp;&nbsp;&nbsp;&nbsp; Stores user data on the server.

**static folder:** &nbsp;&nbsp;&nbsp;&nbsp; Contains styles.css, logo.png, and favicon_inv2.ico. *Favicon_inv2.ico* is the icon of the project; *logo.png* is the logo used in the generated label; *styles.css* is the file that describes how HTML elements are displayed on the screen, including colors, layouts, and fonts. It allows for greater flexibility and control over the visual aspects of a web page by separating the presentation style from the content.

**Templates folder:** &nbsp;&nbsp;&nbsp;&nbsp; The folder where all web pages of the product are stored:

* ```apology.html:``` Returns an apology to the user if incorrect data is entered on this page.

* ```history.html:``` Implements the HTML code for the history page.

* ```index.html:``` Implements the HTML code for the index page.

* ```layout.html:``` Used to define the overall structure and common elements of web application. It serves as a template that can be reused across multiple pages, providing a consistent look and feel.

* ```login.html:``` Implements the HTML code for the login page.

* ```pwchange.html:``` Implements the HTML code for the password change page.

* ```register.html:``` Implements the HTML code for the registration page.

**app.py:** &nbsp;&nbsp;&nbsp;&nbsp; The main entry point for a web application. It contains the application's configuration, routes, and server setup. My app.py includes these route functions:

* ```after_request(response):``` Designed to modify the HTTP response headers to ensure that the response is not cached by the client's browser or any intermediate caches.

* ```index():``` Responsible for rendering an HTML page that displays information related to item numbers, their locations, and the current date.

* ```generate_label():``` Handles user input, validates it, stores it in a database, generates a PDF label, and returns the label as a response to the user's browser.

* ```history():``` Handles the display of the history of printed labels, retrieving filter parameters from the URL, executing a SQL query, and rendering an HTML template.

* ```login():``` Checks the submitted username and password against the database, logs in the user if the credentials are valid, and redirects the user to the home page.

* ```logout():``` Logs the user out by clearing the session and redirects them to the home page.

* ```register():``` Validates the submitted data, checks for existing usernames, hashes passwords, inserts user information into the database, and redirects the user to the home page upon successful registration.

* ```pwchange():``` Validates the submitted data, hashes the new password, updates the user's information in the database, and redirects the user to the home page upon successful password change.

**bin_location.tsv:** &nbsp;&nbsp;&nbsp;&nbsp; The file that stores tab-separated values of items, part numbers, and locations.

**helpers.py:** &nbsp;&nbsp;&nbsp;&nbsp; Contains methods used by app.py. My helpers.py includes these functions:

* ```apology():``` Used to render an apology message to the user.

* ```login_requires():``` A decorator used to restrict access to certain routes, requiring that the user must be logged in to access those routes.

* ```read_bin_file():``` Designed to parse a TSV file containing item numbers and their locations, creating a list of lists where each inner list represents an item with its associated location.

* ```generate_pdf_file():``` Dynamically generates a PDF file that represents a label suitable for a label printer. The label includes various details related to inventory items, such as part number, quantity, location, date open, revision, and lot. The label is structured using rectangles, lines, and text elements to create a visually organized format.

**inventory.db:** &nbsp;&nbsp;&nbsp;&nbsp; The database of the project, containing two tables: users and label. The information of all registered users is stored in the users table, and information about all generated labels is stored in the label table. The label table is connected to the users table by the foreign key "user_id," referencing users (id).

**README.md:** &nbsp;&nbsp;&nbsp;&nbsp; A file that describes this project.
