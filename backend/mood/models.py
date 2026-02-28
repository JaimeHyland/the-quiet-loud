from django.db import models
from django.conf import settings

class Mood(models.Model):
    # id - dont make, Will be auto created by django
    # user_mood_text
    # user
    # predicted_mood

    # CONSIDER ADDING AN OBJECT PROPERTY CONTAINING ALL MOOD CALCULATIONS 
    # INSTEAD OF JUST THE MAIN MOOD
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mood_predictions"
    )
    # DOUBLE CHECK TEXT LIMIT WITH IGOR OR FRONTEND TEAM
    user_mood_text = models.TextField(max_length=2000)
    # LOOK AT RESTRICTING THIS FURTHER
    predicted_mood = models.CharField
