import transformers
from transformers import pipeline


emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def detect_emotion(text):
    scores = emotion_classifier(text)[0]
    top = max(scores, key=lambda x: x['score'])
    return top['label'], round(top['score'], 3)

#code for testing
print(detect_emotion("I feel mentally exhausted but calm"))
