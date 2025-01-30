from django import forms
from .models import User, Request, Attachment, Drawing, Approval, DrawingReview

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'requested_by', 'request_type',
            'due_date', 'description', 'reason_for_action'

        ]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3, }),
            'reason_for_action': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'requested_by': 'Requested By',
            'request_type': 'Request Type',
            'due_date': 'Due Date',
            'description': 'Description of Required Action',
            'reason_for_action': 'Reason for Action',
        }
    #TODO: Make the loin user as requested_by without option to change
    # DONE: The originator of the request cannot be changed and is automatically assigned to the logged-in user.
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Remove 'user' from kwargs and assign it to 'user'
        super(RequestForm, self).__init__(*args, **kwargs)  # Initialize the form
        if user:
            self.fields['requested_by'].initial = user  # Set 'requested_by' field to the user's username
            self.fields['requested_by'].widget = forms.HiddenInput()  # Make the field hidden. Originator can not be changed


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file']


class EngineeringForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['status', 'assigned', 'date_completed', 'notes' , 'description_of_action', 'validation_of_action']
        #
        widgets = {
            'date_completed': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'description_of_action': forms.Textarea(attrs={'rows': 3}),
            'validation_of_action': forms.Textarea(attrs={'rows': 3}),
        }


class DrawingSubmissionForm(forms.ModelForm):
    class Meta:
        model = Drawing
        fields = ['file', 'drawing_comments']

    reviewer = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Reviewers'), label='Select Reviewer')





