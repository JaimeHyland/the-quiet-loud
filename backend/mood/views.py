from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from django.contrib.auth.decorators import login_required

from . ml_service import model, tfidf, label_encoder
from .models import Mood

# ADD GET ALL USER_LOGGED_EMOTIONS

@csrf_exempt
@login_required
def predict_emotion(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_text = [data.get('text', '')]
        
        user_nn = tfidf.transform(user_text)
        user_dense = user_nn.toarray()
        
        probabilities = model.predict(user_dense, verbose=0)[0]
        predicted_index = np.argmax(probabilities)
        predicted_emotion = label_encoder.inverse_transform([predicted_index])[0]
        confidence = float(np.max(probabilities))
        
        # DB Manipulation
        mood = Mood.objects.create(
            user=request.user,
            user_mood_text=user_text,
            predicted_emotion=predicted_emotion,
            sleep=data["sleep"],
            gratitude=data["gratitude"],
            habits=data["habits"]
        )

        # CONSIDER INSTEAD ADDING A REDIRECT TO JOURNEY PAGE
        return JsonResponse({
            'emotion': predicted_emotion,
            'confidence': confidence
        })
    else:
        return JsonResponse({'error': 'POST request required'}, status=400)
    
@csrf_exempt
@login_required
def logged_emotions(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error":" Not authenticated"}, status=401)

    user_emotions = Mood.objects.filter(user=request.user)
    print("User emotions: ", )
    return JsonResponse({"user_emotions": list(user_emotions.values("date", "gratitude", "habits", "id", "predicted_emotion", "sleep", "user", "user_id", "user_mood_text"))}, status=200)