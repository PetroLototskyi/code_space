from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,  HttpResponse, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.models import User, Group
from .models import Request, Attachment, DrawingReview, Drawing, Approval
from .forms import RequestForm, AttachmentForm, EngineeringForm, DrawingSubmissionForm
from django.contrib import messages
from django.db.models import Q
from django.forms import modelformset_factory
from django.conf import settings
from django.db.models import Prefetch
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files import File
import os


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("requests"))  # Redirect to the Requests page
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def index_view(request):
    # Gather summary data for the dashboard
    total_requests = Request.objects.count()
    unprocessed_requests = Request.objects.filter(status="Unprocessed").count()
    in_progress_requests = Request.objects.filter(status="In Progress").count()
    submitted_for_review_requests = Request.objects.filter(status="Submitted For Review").count()
    cancelled_requests = Request.objects.filter(status="Cancelled").count()
    completed_requests = Request.objects.exclude(date_completed__isnull=True).count()
    unassigned_requests = Request.objects.filter(assigned__isnull=True).count()

    return render(request, "index.html", {
        "total_requests": total_requests,
        "unprocessed_requests": unprocessed_requests,
        "in_progress_requests": in_progress_requests,
        "submitted_for_review_requests": submitted_for_review_requests,
        "cancelled_requests": cancelled_requests,
        "completed_requests": completed_requests,
        "unassigned_requests": unassigned_requests,
    })



def requests_view(request):
    status_filter = request.GET.get('status', None)

    if status_filter:
        requests = Request.objects.filter(status=status_filter)
    else:
        requests = Request.objects.all()

    return render(request, 'requests.html', {'requests': requests})


@login_required
def create_request(request):
    AttachmentFormSet = modelformset_factory(Attachment, form=AttachmentForm, extra=3)  # Allow 3 attachments by default

    if request.method == "POST":

        request_form = RequestForm(request.POST, user=request.user)
        attachment_formset = AttachmentFormSet(request.POST, request.FILES, queryset=Attachment.objects.none())

        if request_form.is_valid() and attachment_formset.is_valid():
            new_request = request_form.save(commit=False)
            new_request.requested_by = request.user # take curent user and put in form
            new_request.save()

            for form in attachment_formset:
                if form.cleaned_data:
                    attachment = form.save(commit=False)
                    attachment.request = new_request
                    attachment.save()

            return redirect('index')
        else:
            return render(request, "create_request.html", {
                "form": request_form,
                "attachment_formset": attachment_formset
            })

    else:
        request_form = RequestForm(user=request.user)
        attachment_formset = AttachmentFormSet(queryset=Attachment.objects.none())
        return render(request, "create_request.html", {
            "form": request_form,
            "attachment_formset": attachment_formset
        })


@login_required
def edit_request_view(request, request_id):
    # Fetch the request object by its ID
    request_obj = get_object_or_404(Request, id=request_id)

    if request.method == "POST":
        # Handle form submission to update request fields
        description = request.POST.get('description')
        reason_for_action = request.POST.get('reason_for_action')
        notes = request.POST.get('notes')

        # Update the request object
        request_obj.description = description
        request_obj.reason_for_action = reason_for_action
        request_obj.notes = notes

         # Handle file upload for new attachments
        if 'new_attachment' in request.FILES:
            attachment_file = request.FILES['new_attachment']
            Attachment.objects.create(request=request_obj, file=attachment_file)


        # Save the updated request object
        request_obj.save()

        # Redirect to the updated request edit page
        return redirect('edit_request', request_id=request_obj.id)


    # Pre-fill the request form with the existing request details
    return render(request, 'edit_request.html', {
        'request': request_obj
    })


def delete_attachment(request, attachment_id):
    attacnt = get_object_or_404(Attachment, id=attachment_id)
    request_id = attachment.request.id
    attachment.delete()  # This deletes the attachment
    return redirect('edit_request', request_id=request_id)


@login_required
def engineering_view(request):
    if request.method == "POST":
        # Get the request object by its ID
        request_id = request.POST.get('request_id')
        engineer_id = request.POST.get("engineer_id")

        status = request.POST.get('status')
        assigned = request.POST.get('assigned')
        date_completed = request.POST.get('date_completed')
        notes = request.POST.get('notes')
        description_of_action = request.POST.get('description_of_action')
        validation_of_action = request.POST.get('validation_of_action')

        # Fetch the request object
        engineering_request = get_object_or_404(Request, id=request_id)


        # Update fields if they are provided
        engineering_request.status = status

        if date_completed:
            engineering_request.date_completed = date_completed
            engineering_request.status = "Completed"
        else:
            engineering_request.date_completed = None

        if engineer_id:
            engineer = User.objects.get(id=engineer_id)
            engineering_request.assigned = engineer
        else:
            engineering_request.assigned = None

        engineering_request.notes = notes
        engineering_request.description_of_action = description_of_action
        engineering_request.validation_of_action = validation_of_action

        # Save the updated request object
        engineering_request.save()

        return redirect('engineering')


    # Retriew users for assigned field
    engineer_group = Group.objects.get(name='Engineers')
    engineers = engineer_group.user_set.all()  # Get all users in the Engineers group

    # Search request #
    search_query = request.GET.get('search', '')

    if search_query:
        engineering_requests = Request.objects.filter(request_number__icontains=search_query).prefetch_related('drawing_request')
    else:
        # engineering_requests = Request.objects.all()
        engineering_requests = Request.objects.prefetch_related('drawing_request').all()

    return render(request, 'engineering.html', {
        'engineering_requests': engineering_requests,
        'engineers' : engineers,
    })


@login_required
def request_detail_view(request, request_id):
    # Get the specific request by ID
    request_obj = get_object_or_404(Request, id=request_id)

    if request.method == "POST":
        # Handle form submission for status, date, description, validatio, notes
        status = request.POST.get('status')
        date_completed = request.POST.get('date_completed')
        description_of_action = request.POST.get('description_of_action')
        validation_of_action = request.POST.get('validation_of_action')
        notes = request.POST.get('notes')

        # Update the request fields
        request_obj.status = status

        # If date of completion provide the status changes to Completed
        if date_completed:
            request_obj.date_completed = date_completed
        request_obj.description_of_action = description_of_action
        request_obj.validation_of_action = validation_of_action
        request_obj.notes = notes

        if date_completed:
            request_obj.status = "Completed"
        else:
            request_obj.date_completed = None


        # Save the updated request
        request_obj.save()

        # Redirect back to the same request detail page
        return redirect('request_detail', request_id=request_obj.id)

    # Get the associated drawings for this request
    drawings = Drawing.objects.filter(request=request_obj)

    return render(request, 'request_detail.html', {
        'request': request_obj,
        'drawings': drawings,
        'status_choices': Drawing.STATUS_CHOICES,  # Pass the choices to the template
    })


def delete_drawing(request, drawing_id):
    drawing = get_object_or_404(Drawing, id=drawing_id)
    request_id = drawing.request.id
    drawing.delete()
    return redirect('request_detail', request_id=request_id)

@login_required
def review_approval_view(request):
    # Retrieve all requests with associated drawings
    requests = Request.objects. prefetch_related('drawing_request').all()

    # Get reviewers from the "Reviewer" group
    reviewer_group = Group.objects.get(name='Reviewers')
    reviewers = reviewer_group.user_set.all()  # Get all users in the Reviewer group

    directors_eng_group = Group.objects.get(name="Directors of Engineering")
    directors_qc_group = Group.objects.get(name="Directors of QC")

     # Get the first user in that group
    director_eng = directors_eng_group.user_set.first()  # Returns the first user in the group or None if no user
    director_qc = directors_qc_group.user_set.first()  # Returns the first user in the group or None if no user

    # Get all Approwal objects
    approvals_obj = Approval.objects.all()

    # Handle updates for POST
    if request.method == "POST":

        request_id = request.POST.get('request_id')
        request_number= request.POST.get ('request_number')
        drawing_status = request.POST.get ('drawing_status')
        reviewer_id = request.POST.get ('reviewer_id')

        # Retrieve and update the Approval object for the selected drawing
        drawing_id = request.POST.get('drawing_id')
        drawing = get_object_or_404(Drawing, id=drawing_id)

        # Try to fetch the Approval object, create it if it doesn't exist
        approval_obj, created = Approval.objects.get_or_create(
            drawing=drawing,
            defaults={
                'approval_person': request.user,  # Assign the current user by default if created
            },
        )
        approval_status = request.POST.get ('approval_status')

        if approval_status:
            approval_obj.status = approval_status

         # Update the drawing status if it was provided
        if drawing_status:
            drawing.drawing_status = drawing_status


         # Update checkbox fields in the Approval object
        if 'reviewer' in request.POST:
            approval_obj.reviewer = True
        else:
            reviewer_hidden = request.POST.get('reviewer_hidden', 'no')
            approval_obj.reviewer = (reviewer_hidden == 'yes')

        if 'originator' in request.POST:
            approval_obj.originator = True
        else:
            originator_hidden = request.POST.get('originator_hidden', 'no')
            approval_obj.originator = (originator_hidden == 'yes')

        if 'dir_eng' in request.POST:
            approval_obj.dir_eng = True
        else:
            dir_eng_hidden = request.POST.get('dir_eng_hidden', 'no')
            approval_obj.dir_eng = (dir_eng_hidden == 'yes')

        if 'dir_qc' in request.POST:
            approval_obj.dir_qc = True
        else:
            dir_qc_hidden = request.POST.get('dir_qc_hidden', 'no')
            approval_obj.dir_qc = (dir_qc_hidden == 'yes')


        # Update reviewer field
        if reviewer_id:
            drawing.drawing_reviewer_id = reviewer_id

        # For future imlementaion if comment added to the html page
        # approval_obj.comments = request.POST.get('comments', approval_obj.comments)

        approval_obj.save()  # Save the updated approval object

        # Save the updated drawing status
        drawing.save()


        return redirect('review_approval')  # Reload the page with updated data

    return render(request, 'review_approval.html', {
        'requests': requests,
        'approvals_obj': approvals_obj,
        'reviewers': reviewers,
        'approval_status_choices': Approval.STATUS_CHOICES,
        'drawing_status_choices': Drawing.STATUS_CHOICES,
        'director_eng': director_eng,
        'director_qc': director_qc,
        'user': request.user,

    })


@login_required
def drawing_reviews(request, drawing_id):
    # Fetch the drawing object
    # drawing = Drawing.objects.get(id=drawing_id)
    drawing = get_object_or_404(Drawing, id=drawing_id)

    # Get all reviews for this drawing
    all_reviews = DrawingReview.objects.filter(drawing=drawing)

    # Render the template with the drawing and reviews
    return render(request, 'drawing_reviews.html', {
        "drawing": drawing,
        "all_reviews": all_reviews,
    })


@login_required
def review_comment(request, drawing_id):
    # Handle the post
    if request.method == "POST":
        reviewer = request.user
        drawing = get_object_or_404(Drawing, id=drawing_id)
        review_text = request.POST['new_review']
        attachment = request.FILES.get('attachment')



        # Create the review object
        new_review = DrawingReview(
            reviewer=reviewer,
            drawing=drawing,
            review_comments=review_text,
            attachment=attachment
        )
        new_review.save()

        return redirect('drawing_reviews', drawing_id=drawing_id)

    return redirect('drawing_reviews', drawing_id=drawing_id)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(DrawingReview, id=review_id)
    drawing = review.drawing  # The drawing related to the review

    # Only allow the owner to edit the review In case of user will try access review directly by URL23w
    if review.reviewer != request.user:
        return HttpResponseForbidden("You are not allowed to edit this review.")

    if request.method == "POST":
        review_text = request.POST.get('new_review')
        attachment = request.FILES.get('attachment')

        # Check if the user wants to delete the existing attachment
        if 'delete_attachment' in request.POST:
            review.attachment.delete()  # Delete the current attachment if the box is checked

        if review_text:
            review.review_comments = review_text
        if attachment:
            review.attachment = attachment

        review.save()
        return redirect('drawing_reviews', drawing_id=review.drawing.id)

    return render(request, 'edit_review.html', {
        "review": review,
        "drawing": drawing
    })


def reupload_drawing(request, drawing_id):
    # Fetch the drawing object
    drawing = get_object_or_404(Drawing, id=drawing_id)

    if request.method == "POST" and request.FILES.get('new_drawing_file'):
        # Handle file upload
        new_file = request.FILES['new_drawing_file']

        # Get the path where the file is stored
        file_path = drawing.file.path

        # Open the new file and save it with the original file name
        with default_storage.open(file_path, 'wb+') as destination:
            for chunk in new_file.chunks():
                destination.write(chunk)

        # Keep the same revision number and other details
        drawing.drawing_revision = drawing.drawing_revision  # Retain the same revision
        drawing.save()

        # Redirect back to the request details page
        return redirect('request_detail', request_id=drawing.request.id)

    # Return an error if no file is uploaded
    return HttpResponse("No file uploaded", status=400)


def upload_drawing(request, request_id):
    if request.method == 'POST' and request.FILES.get('new_drawing'):

        # Retrieve the request object using request_id
        drawing_request = get_object_or_404(Request, id=request_id)
        
        # Get the uploaded drawing file
        drawing_file = request.FILES['new_drawing']
        drawing_number = request.POST['drawing_number']
        drawing_revision = request.POST['drawing_revision']
        drawing_status = request.POST.get('drawing_status', 'Active')  # Default to 'Active' if no status provided
        drawing_comments = request.POST.get('drawing_comments', '')  # Default to empty string if no comments

        # Validate required fields
        if not drawing_number or not drawing_revision:
            messages.error(request, "Drawing number and revision are required.")
        else:
            # Modify the file name based on the drawing number and revision
            file_extension = drawing_file.name.split('.')[-1]
            new_file_name = f"{drawing_number}_R_{drawing_revision}.{file_extension}"
            saved_path = default_storage.save(f"drawings/{new_file_name}", ContentFile(drawing_file.read()))

            # Create the new drawing and associate it with the current request
            new_drawing = Drawing.objects.create(
                file=saved_path,  # Use the new file path with modified name
                drawing_number=drawing_number,
                drawing_revision=drawing_revision,
                drawing_status=drawing_status,
                drawing_comments=drawing_comments,
                request=drawing_request,  # Associate this drawing with the current request
            )

        return redirect('request_detail', request_id=request_id)  # Redirect to the request detail page

