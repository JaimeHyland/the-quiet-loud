from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

class Mood(models.Model):
    # CONSIDER ADDING AN OBJECT PROPERTY CONTAINING ALL MOOD CALCULATIONS 
    # INSTEAD OF JUST THE MAIN MOOD
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mood_predictions",
    )
    user_mood_text = models.TextField(validators=[MinLengthValidator(100)], max_length=2000)
    # LOOK AT RESTRICTING THIS FURTHER
    predicted_emotion = models.CharField(max_length=100)

    # NEW FIELDS
    date = models.DateField(auto_now_add=True)
    sleep = models.CharField(null=True, blank=True, max_length=100)
    gratitude= models.TextField(max_length=2000)
    habits= models.JSONField(null=True)