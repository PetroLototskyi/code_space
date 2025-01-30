from django.contrib import admin
from .models import Request, Attachment, Drawing, Approval, DrawingReview
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class RequesrAdmin(admin.ModelAdmin):
    list_display = ("request_number", "requested_by", "request_date", "status", "assigned", "date_completed")
    list_display_links = ("request_number",)  # Make both "id" and "request_number" clickable
    list_editable = ("assigned", "requested_by")  # Allow "assigned" to be editable directly from the list view
    # autocomplete_fields = ("assigned",)  # Add a searchable dropdown for users

    class Media:
        # Hide icons (change, add, view) in admin request view for Requested by
        js = ("eco_requests/hide_icons.js",)


class DrawingAdmin(admin.ModelAdmin):
    list_display = ("id", "drawing_number", "drawing_revision", "request", "drawing_reviewer", "drawing_status")
    list_display_links = ("drawing_number",)
    list_editable = ("drawing_reviewer",)

    class Media:
         # Hide icons (change, add, view) in admin drawing view for Drawing Reviewer
        js = ("eco_requests/hide_icons.js",)

class ApprovalAdmin(admin.ModelAdmin):
    list_display = ("id", "drawing", "approval_person", "status", "reviewer", "originator", "dir_qc", "dir_eng")
    list_display_links = ("id", "drawing",)

class DrawingReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "drawing", "reviewer", "review_comments", "created_at" ,"attachment")
    list_display_links = ("drawing",)




admin.site.register(Request, RequesrAdmin)
admin.site.register(DrawingReview, DrawingReviewAdmin)
admin.site.register(Drawing, DrawingAdmin)
admin.site.register(Approval, ApprovalAdmin)
admin.site.register(Attachment)

