# This script loads the trained Simple Neural Network model, the TF-IDF vectorizer, and the label encoder 
# to make predictions on new user input. The code also includes error handling to ensure that all necessary files 
# are loaded correctly, and it provides detailed output of the predicted emotion along with confidence scores for each emotion class.
# Make sure to have the following files in the same directory as this script:
# - nn_model.pkl, - tfidf_vectorizer.pkl, and - label_encoder.pkl
# You can test the model with any user input by changing the 'user_answer' variable. 
# The script will output the predicted emotion and the confidence level for that prediction, as well as the probabilities 
# for all emotion classes: anger, fear, joy, love, sad and surprise.

import pickle
import numpy as np
import sys
import warnings
warnings.filterwarnings('ignore')

# Load the model
try:
    with open('nn_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Model file not found. Please ensure 'nn_model.pkl' is in the correct location.")
    model = None

# Load the TF-IDF vectorizer that was used during training
try:
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)
    print("TF-IDF vectorizer loaded successfully!")
except FileNotFoundError:
    print("TF-IDF vectorizer not found. Please ensure 'tfidf_vectorizer.pkl' is in the correct location.")
    tfidf = None

# Load the label encoder
try:
    with open('label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
    print("Label encoder loaded successfully!")
except FileNotFoundError:
    print("Label encoder not found. Please ensure 'label_encoder.pkl' is in the correct location.")
    label_encoder = None

# Check if all artifacts loaded properly
if None in [model, tfidf, label_encoder]:
    print("\n❌ ERROR: Some model artifacts failed to load!")
    print("Please ensure all required files are in the correct location:")
    print("  - nn_model.pkl")
    print("  - tfidf_vectorizer.pkl")
    print("  - label_encoder.pkl")
    sys.exit()

# An example of the user answer. Entered as string. Any block of text can be entered. Feel free to try your own text.
user_answer = ["wow this is unbelievable!"]  # Example input, can be changed to test with different sentences

# Vectorise and prepare the user answer data for the model
user_nn = tfidf.transform(user_answer)
user_dense = user_nn.toarray()

print(f"Input shape: {user_dense.shape}")  # Should be (1, 5000)

# Predict using the model
y_pred = model.predict(user_dense)[0]  # MLPClassifier returns a single prediction, not an array

# Convert numeric prediction back to emotion label
predicted_emotion = label_encoder.inverse_transform([y_pred])[0]

# Get prediction probabilities
probabilities = model.predict_proba(user_dense)[0]
confidence = np.max(probabilities)

print(f"\n{'='*50}")
print(f"User input: {user_answer[0]}")
print(f"{'='*50}")
print(f"Predicted emotion: {predicted_emotion}")
print(f"Confidence: {confidence:.4f} ({confidence*100:.2f}%)")
print(f"\nAll probabilities:")
for emotion, prob in zip(label_encoder.classes_, probabilities):
    print(f"  {emotion}: {prob:.4f}")
    