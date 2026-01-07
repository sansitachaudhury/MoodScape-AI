from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from emotion import detect_emotion
from generator import generate_explanation
from mood_map import MOOD_MAP

app = FastAPI(title="MoodScape AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (safe for local demo)
    allow_credentials=True,
    allow_methods=["*"],   # allow POST, OPTIONS, etc.
    allow_headers=["*"],
)

class MoodInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze_mood(data: MoodInput):
    emotion, confidence = detect_emotion(data.text)

    EMOTION_ALIAS = {
        "surprise": "stress",
        "neutral": "calm"
    }

    mapped_emotion = EMOTION_ALIAS.get(emotion, emotion)
    explanation = generate_explanation(mapped_emotion, data.text)
    songs = MOOD_MAP.get(mapped_emotion, [])

    return {
        "emotion": emotion,
        "confidence": confidence,
        "explanation": explanation,
        "songs": songs
    }
