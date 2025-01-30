from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import delete_attachment
from .views import delete_drawing


urlpatterns = [
    path("", views.index_view, name="index"),  # Dedicated index page
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("requests/", views.requests_view, name="requests"),  # Requests page
    path("requests/create/", views.create_request, name="create_request"),  # Form to create a request
    path('engineering/', views.engineering_view, name='engineering'),
    path('request/<int:request_id>/', views.request_detail_view, name='request_detail'),
    path('edit_request/<int:request_id>/', views.edit_request_view, name='edit_request'),
    path('delete_attachment/<int:attachment_id>/', delete_attachment, name='delete_attachment'),
    path('delete_drawing/<int:drawing_id>/', delete_drawing, name='delete_drawing'),
    path('review_approval/', views.review_approval_view, name='review_approval'),
    path('drawing/<int:drawing_id>/review-comments/', views.drawing_reviews, name='drawing_reviews'),
    path('review_comment/<int:drawing_id>/', views.review_comment, name='review_comment'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('drawing/reupload/<int:drawing_id>/', views.reupload_drawing, name='reupload_drawing'),
    path('drawing/upload/<int:request_id>/', views.upload_drawing, name='upload_drawing'),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
