from django.db import models
from django.contrib.auth.models import User, AbstractUser



class Request(models.Model):
    request_number = models.IntegerField(unique=True)  # Auto-generated, linked to external DB
    # requested_by = models.CharField(max_length=10, blank=True)  # Initials of the user
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='originator')
    request_type = models.CharField(max_length=100)  # Short description
    request_date = models.DateField(auto_now_add=True)  # Automatically set to current date
    due_date = models.DateField()  # User-specified
    description = models.TextField()  # Detailed description
    reason_for_action = models.TextField()  # Explanation for action
    status = models.CharField(max_length=50, blank=True, default="Unprocessed")  # Default is "Unprocessed"
    assigned = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)  # Linked to registered users
    # assigned = models.CharField(max_length=100, blank=True, null=True)  # Engineering-assigned user/role
    date_completed = models.DateField(blank=True, null=True)  # Completed date, if applicable
    notes = models.TextField(blank=True, null=True)  # Engineering notes
    # attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    # New fields
    description_of_action = models.TextField(blank=True, null=True)
    validation_of_action = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Request #{self.request_number}"

    @staticmethod
    def generate_request_number():
        # Get the last request, and increment the numeric part.
        last_request = Request.objects.last()

        if not last_request:
            return 1


        last_number = last_request.request_number
        new_number = last_number + 1

        return new_number

    def save(self, *args, **kwargs):
        if not self.request_number:  # If request_number is not set
            self.request_number = Request.generate_request_number()  # Generate it automatically
        super().save(*args, **kwargs)

class Attachment(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name="attachments")
    file = models.FileField(upload_to="attachments/")


class Drawing(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Rejected', 'Rejected'),
        ('Obsolete', 'Obsolete'),
        ('Subm. for Review', 'Subm. for Review'),
        ('Approval Pending', 'Approval Pending')
        # ('Ready for Distribution', 'Ready for Distribution')
    ]

    drawing_number = models.CharField(max_length=50, blank=False, default="0")
    drawing_revision = models.CharField(max_length=5, blank=False, default="0")
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='drawing_request')
    file = models.FileField(upload_to='drawings/')
    drawing_status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=False, default='Active')
    drawing_comments = models.TextField(blank=True, null=True)
    drawing_reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates on save

    def __str__(self):
        return f"Drawing #{self.drawing_number}, for Request #{self.request.request_number}"

class DrawingReview(models.Model):

    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE, related_name='drawing_review_drawing')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='review_username')

    review_comments = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='drawing_reviews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Review by {self.reviewer.username} on Drawing #{self.drawing.drawing_number} at {self.created_at}"



class Approval(models.Model):
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]

    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE, related_name='drawing_approval')
    approval_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approval_person')
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    reviewer = models.BooleanField(default=False)
    originator = models.BooleanField(default=False)
    dir_qc = models.BooleanField(default=False)
    dir_eng = models.BooleanField(default=False)


    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Approval {self.status} for for Drawing {self.drawing.drawing_number}"
