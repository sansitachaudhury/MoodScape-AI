from dotenv import load_dotenv
load_dotenv()

from huggingface_hub import InferenceClient
import os

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN environment variable not set")

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN
)

# Emotion-aware fallback messages
FALLBACK_EXPLANATIONS = {
    "stress": (
        "You seem emotionally overwhelmed and mentally tired. "
        "Calm and soothing music can help slow your thoughts and reduce stress. "
        "These songs are chosen to help you relax without overwhelming you."
    ),
    "sadness": (
        "You appear to be feeling low and emotionally heavy. "
        "Gentle and comforting music can help you feel understood and supported. "
        "These songs are meant to provide emotional reassurance."
    ),
    "joy": (
        "You seem happy and emotionally uplifted. "
        "Energetic and positive music can help maintain this good mood. "
        "These songs are chosen to match your energy and positivity."
    ),
    "anger": (
        "Your message reflects frustration and strong emotions. "
        "High-energy music can help release tension in a healthy way. "
        "These songs are chosen to help you channel your emotions constructively."
    ),
    "calm": (
        "You appear relaxed and emotionally balanced. "
        "Soft and ambient music can help maintain this sense of calm. "
        "These songs are chosen to preserve your peaceful mood."
    ),
    "fear": (
        "You seem uneasy or emotionally uncertain. "
        "Soothing music can help create a sense of safety and comfort. "
        "These songs are chosen to gently calm your emotions."
    )
}

def generate_explanation(emotion, user_text):
    prompt = f"""
You are an empathetic assistant.

User emotion: {emotion}
User message: "{user_text}"

Explain the emotional state in simple, supportive language.
Then explain what kind of music would help emotionally.
Keep it under 4 sentences.
"""

    try:
        response = client.text_generation(
            prompt,
            max_new_tokens=120,
            temperature=0.6,
            top_p=0.9
        )
        return response.strip()

    except Exception:
        # Emotion-aware fallback
        return FALLBACK_EXPLANATIONS.get(
            emotion,
            "Music can help support your emotional state. These songs are chosen to help you feel balanced."
        )


# testing
if __name__ == "__main__":
    print(generate_explanation("joy", "I feel happy and energetic today"))
    print(generate_explanation("sadness", "I feel really low and drained"))
