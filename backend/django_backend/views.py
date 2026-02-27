from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from . ml_service import model, tfidf, label_encoder

def home(request):
    return render(request, 'index.html')

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
        
        return JsonResponse({
            'emotion': predicted_emotion,
            'confidence': confidence
        })
    
    return JsonResponse({'error': 'POST request required'}, status=400)