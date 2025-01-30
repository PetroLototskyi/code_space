# Engineering Request and Drawing Management System
#### Video Demo: <https://youtu.be/Rkeooz6oiBo>
## Project Overview:

This project is a web-based application designed to streamline the process of handling engineering requests and managing associated drawing revisions. It provides tools for request creation, modification, approval, and validation, ensuring efficient collaboration between engineers, reviewers, and other stakeholders.

### Features:

1. **Request Management**

    * Create, edit, and delete engineering requests.
    * Attach supporting documents and drawings to requests.
    * Filter and search requests by status, request number, or assigned engineer.

2. **Drawing Handling**

    * Upload, revise, and validate technical drawings.
    * Modify drawing details, including revisions, comments, and statuses.
    * Automatic filename adjustments for better organization.

3. **Approval Workflow**

    * Assign reviewers for requests and drawings.
    * Approve or reject requests with comments.
    * Maintain validation records for engineering actions.

4. **Filters & Sorting**

    * Apply filters for request status, drawing status, and assigned users.
    * Sort requests or drawings based on criteria like request number or priority.

5. **User Authentication**

    * Login System: Users must log in to access the application's full functionality. Pre-configured user accounts are available for different roles within the system, such as engineers, reviewers, and administrators.
    * Role-Based Access: Different roles have different levels of access. Users can log in and perform tasks based on their assigned permissions.


### Installation:
Install Python 3.x from the official website: <https://www.python.org/><br>
Install required dependencies:  ```pip install -r requirements.txt```<br>
Run the application:    ```python manage.py runserver```<br>
You can now access the application at http://127.0.0.1:8000/<br>
To access the admin panel, use the login: ```petro``` the password: ```ctcszseyshn```

### How It Works:
**Step 1: User Login** <br>
User can open first two tabs of application and read all posted requests without being logged, but when want to submit or work on request, users must log in. Different user roles are available, each with specific permissions. Once logged in, users can navigate to the relevant sections based on their role (e.g., request creation, engineering review, or request approval).

**Step 2: Create and Submit a Request**<br>
Users can submit new ECO requests by entering details such as:
* Description: A brief explanation of the requested change.
* Reson foe changes: A short explanation why request is being submitted.
* Attachments: Users can attach multiple files, such as updated engineering drawings.
* Request Type: The type of change (e.g., drawing update, process modification).
Once the request is submitted, it is assigned a unique request number for tracking purposes.

**Step 3: Engineering Department Handling** <br>
Once a request is submitted, the engineering department can view the request details. They can:<br>
* Review the Request: The engineering team reviews the provided information and attachments.
* Update Status: The status of the request can be changed (e.g., from Unprocessed to In Progress) based on the department's progress.
* Add Drawings: The engineering team can upload and update drawings associated with the request.

**Step 4: Reviewer Assignment and Drawing Reviews**<br>
When the request is ready for review, an assigned reviewer is notified. The reviewer can:<br>
* Review Drawings: Check the attached engineering drawings and approve or suggest revisions.
* Comment: Add comments if revisions or further work is needed before approval.
* Add Attachment: Add his own attachment. Example: redmarked drawing with review correction for implementation.

**Step 5: Final Approval**<br>
Once the request and drawings have been reviewed, the final step is approval. The reviewer or engineering lead can approve the request and move it to the next stage. If required, the approval process is updated, and further reviews or actions may be required. After a drawing is marked as reviewed, the three checkboxes related to the request originator, QC, and the Director of Engineering must be marked accordingly. All parties may provide additional reviews if required to ensure that all criteria of the request are met.

### Distinctiveness and Complexity:

This project was inspired by real-life observations of engineering department workflows, focusing on ECO request management. Input from engineers was gathered to design an app that streamlines daily tasks, simplifies communication between departments, and improves overall organization within a manufacturing company. Beyond assisting engineers, the app also provides executives with tools to track departmental workload and performance. Metrics such as request processing time can serve as key performance indicators (KPIs) for the engineering department.

Key distinctive and complex features include:

* *Custom Workflows:* Checkboxes dynamically adapt to user roles and approval statuses, incorporating conditional logic and maintaining data integrity across multiple contexts.
* *Role-Based Functionality:* Permissions vary by user role (e.g., reviewer, originator, director QC/Eng), ensuring secure and tailored access.
* *Advanced File Management:* Features like file version control (e.g., automated renaming with revision tracking) and re-upload capabilities preserve metadata and improve usability.
* *Data Integration:* The app dynamically links external data, such as reviewer assignments and approvals, to enable real-time updates and interactions.
* *Streamlined UI:* Direct actions like uploading, re-uploading, and managing drawing metadata (status, comments) within the interface offer a user-friendly experience while ensuring precise control.


### File Structure:
The ECO-Request App is organized into a structured file system to ensure maintainability, scalability, and ease of development. Below is an overview of the key files and their purposes:

The **```views.py```** file contains the core logic for handling user interactions, rendering templates, and managing data. Key functionalities include:
* *Authentication:* Handles user login, logout, and access control using decorators like ```@login_required```.
* *Request Management:* Functions for creating, editing, deleting, and listing requests with associated attachments.
* *Drawing Handling:*  Uploading, re-uploading, reviewing, and managing drawings and their reviews.
* *Dashboard and Filters:* Uploading, re-uploading, reviewing, and managing drawings and their reviews.
* *Engineering View:* Provides engineering-specific actions like assigning engineers, updating statuses, and processing actions.
* *Approval and Reviews:* Enables approval workflows, reviewer assignments, and review comments for drawings.

The **```models.py```** file defines the database structure for the application:
*   *```Request```*: Tracks ECO requests with fields for request details, assigned users, status, and dates.
*   *```Attachment```*: Manages file uploads linked to requests.
*   *```Drawing```*: Handles drawings associated with requests, including revisions, statuses, and reviewers.
*   *```DrawingReview```*: Stores reviews of drawings with comments and optional attachments.
*   *```Approval```*: Tracks drawing approvals with roles, statuses (e.g., Approved, Pending), and timestamps.



The **```urls.py```** file file defines routes for all app pages, connecting specific URL patterns to their corresponding views. It provides access to functionalities like login/logout, request management, drawing handling, reviews, and engineering-specific views, serving as a central hub for navigation across the app. It also configures media file access for uploaded files like drawings.


The **```forms.py```** file defines Django ModelForms for handling structured user input and form validation:
*   *```RequestForm```*: Handles the creation of requests, automatically setting the requester to the logged-in user and allowing input for fields like due date, description, and reason for action.
*   *```AttachmentForm```*: Facilitates file attachments by allowing users to upload files.
*   *```EngineeringForm```*: Enables updates to request status, assigned personnel, completion date, notes, description of action and validation.
*   *```DrawingSubmissionForm```*: Used for drawing submissions, including file uploads, comments, and selecting a reviewer from users in the "Reviewers" group.

The **Templates (templates/)** folder contains eleven HTML templates designed to manage different aspects of the request workflow. These templates facilitate creating, editing, and viewing requests and reviews, as well as handling drawing reviews and approvals. They include forms and interactive elements for request creation, review editing, and status management, while also supporting user authentication (login) and providing a centralized dashboard (index).

**Static Files (static/)** includes: *```action.js```*, *```enginnering.js```*, *```hide_icons.js```*, *```requests.js```*, *```review_approval.js```*, ```styles.css```. These static files handle the styling and interactivity of a web application. CSS focuses on customizing buttons, table styles, and responsive design. JavaScript files implement filtering, sorting, and dynamic behavior such as hiding elements, managing collapsible sections, and enabling tooltips. They enhance the user experience by allowing efficient data filtering, sorting, and interaction with the page elements.

**Media Folder (media/)**: Stores uploaded files:

*   *attachments/*: Stores files attached to requests.
*   *drawing_reviews/*: Stores files related to drawing reviews.
*   *drawings/*: Stores technical drawings associated with requests.


The **```admin.py```** file customizes the Django admin interface to manage the application's models efficiently:

*   *```RequesrAdmin```*: Displays key fields in the list view. Allows editing of "assigned" and "requested_by" directly from the list view. Includes JavaScript to hide action icons (e.g., add, change, view) for the "Requested By" field.
*   *```DrawingAdmin```*: Displays drawing-related fields in the list view. Makes "drawing_number" clickable and enables editing of the "drawing_reviewer" field directly. Uses JavaScript to hide icons for "Drawing Reviewer".
*   *```ApprovalAdmin```*: Makes "drawing" clicable and display approval fields in the list view.
*   *```DrawingReviewAdmin```*: Makes "drawing" clicable and shows details such as drawing, reviewer, review comments, creation date, and attached files.

The **templatetags/```custom_filters.py```** file contains custom template filters to enhance Django templates. It defines:

* *```basename(value)```*: Extracts and returns the base name of a file path.
* *```filter_by_drawing(approvals, drawing_id)```*: Filters a list of approvals to return only those associated with a specific drawing ID.

### Improvement:
The application has room for further enhancement. A few of the potential improvements could be:
*   *Automatic Email Notifications:* Implement an email notification system that automatically sends alerts to users for important actions like request submission, review assignments, status changes, or approvals.
*   *Task Reminders:* Add automated task reminders to notify users about due dates for requests or reviews, ensuring that important deadlines aren’t missed.

