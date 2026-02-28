from django.contrib import admin
from .models import ChatMessage, QuestionnaireResponse


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "questionnaire", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "message")


@admin.register(QuestionnaireResponse)
class QuestionnaireResponseAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("user__username",)
