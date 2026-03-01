from django.urls import path
from .views import predict_emotion, logged_emotions

urlpatterns = [
    path('predict/', predict_emotion, name='predict'),
    path('logged-emotions/', logged_emotions, name='logged_emotions'),
]
