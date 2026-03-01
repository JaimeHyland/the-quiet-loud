from django.urls import path
from .views import ai_chat_view
urlpatterns = [
        path("test_harness/", ai_chat_view, name='thought_shift'),
]
