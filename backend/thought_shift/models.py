from django.db import models
from django.conf import settings  # future-proof User reference


class QuestionnaireResponse(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.CharField(max_length=100)
    response_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class ChatMessage(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    questionnaire = models.ForeignKey(
        QuestionnaireResponse,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.created_at:%Y-%m-%d %H:%M}"
