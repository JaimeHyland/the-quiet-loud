from openai import OpenAI
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os

from .models import ChatMessage, QuestionnaireResponse

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@login_required
def ai_chat_view(request):
    """
    AI chat view using ChatMessage and QuestionnaireResponse models.
    """

    # Retrieve all previous questionnaire responses for this user
    questionnaire_responses = QuestionnaireResponse.objects.filter(
        user=request.user
    ).order_by('-created_at')

    latest_questionnaire = questionnaire_responses.first()

    # CHANGED: Retrieve chat messages and include role
    chat_messages = ChatMessage.objects.filter(
        user=request.user,
        questionnaire=latest_questionnaire
    ).order_by('created_at') if latest_questionnaire else []

    # Handle POST request (user sends a message)
    if request.method == "POST":
        if request.POST.get("create_questionnaire"):
            category = request.POST.get("category", "").strip()

            if category:
                latest_questionnaire = QuestionnaireResponse.objects.create(
                    user=request.user,
                    category=category,
                    response_data={}
                )
            # Always redirect after POST (prevents resubmission)
            return redirect("thought_shift")

        user_message_text = request.POST.get("message", "").strip()

        # Prevent empty messages OR chatting without questionnaire
        if not user_message_text or not latest_questionnaire:
            return redirect("thought_shift")

        # Save user message
        ChatMessage.objects.create(
            user=request.user,
            questionnaire=latest_questionnaire,
            content=user_message_text,
            role="user",
        )

        # Build chat history for OpenAI
        chat_history = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

        existing_messages = ChatMessage.objects.filter(
            user=request.user,
            questionnaire=latest_questionnaire
        ).order_by("created_at")

        for msg in existing_messages:
            chat_history.append({
                "role": msg.role,
                "content": msg.content
            })

        # Call OpenAI
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=chat_history
            )
            bot_message_text = response.choices[0].message.content.strip()
        except Exception as e:
            bot_message_text = f"Error: {e}"

        # Save bot response
        ChatMessage.objects.create(
            user=request.user,
            questionnaire=latest_questionnaire,
            content=bot_message_text,
            role="bot",
        )

        return redirect("thought_shift")

    # Render GET request
    return render(request, "test_harness.html", {
        "chat_messages": chat_messages,
        "questionnaire_responses": questionnaire_responses,
        "latest_questionnaire": latest_questionnaire,
    })
