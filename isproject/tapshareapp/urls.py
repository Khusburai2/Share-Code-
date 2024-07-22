from django.urls import path
from .views import create_content, share_content

urlpatterns = [
    path('', create_content, name='home'),  # Redirect the root URL to create_content
    path('create/', create_content, name='create_content'),
    path('share/', share_content, name='share_content'),  # Handle GET requests with code
    path('share/<str:code>/', share_content, name='share_content_with_code'),  # Direct access by code
]
