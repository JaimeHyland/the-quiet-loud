from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from django.contrib.auth.decorators import login_required

from . ml_service import model, tfidf, label_encoder
from .models import Mood


@csrf_exempt
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
        return JsonResponse({'error': 'POST request required'}, status=400)
    
    return JsonResponse({'error': 'POST request required'}, status=400)