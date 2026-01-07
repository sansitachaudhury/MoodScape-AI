# MoodScape AI   
**Emotion-Aware Music Recommendation System**

MoodScape AI is an end-to-end Generative AI system that analyzes user-written text to detect emotional states, generates empathetic explanations and recommends mood-aware music.  
The project combines NLP-based emotion classification with large language model–based text generation to create an explainable and user-centric recommendation system.

---

## Features
- Emotion detection from natural language text
- Generative AI explanations for emotional context
- Mood-based music recommendations (2015–2024)
- Emotion normalization for robust recommendations
- FastAPI backend
- Secure API key handling using environment variables

---

## How It Works
1. User enters text describing how they feel  
2. An NLP emotion classifier detects the emotional state  
3. Auxiliary emotions are normalized into core mood categories  
4. A generative language model produces a short, supportive explanation  
5. Songs aligned with the detected mood are recommended  

Each request triggers the pipeline once which ensures efficiency and reliability.

---

## Tech Stack
- **Python**
- **FastAPI** – backend framework
- **Hugging Face Transformers** – emotion classification
- **Hugging Face Inference API** – generative text generation
- **python-dotenv** – environment variable management
- **HTML / CSS** – frontend interface

---

## API Key Setup (IMPORTANT)
This project uses the Hugging Face Inference API.

For security reasons, the API key is not included in the repository.

### Setup Steps:
1. Create a file named `.env` in the project root  
2. Add the following line:  
   HF_TOKEN=your_huggingface_api_key_here
3. The `.env` file is excluded from version control via `.gitignore`

---

## How to Run the Project
###  Install dependencies
bash  
pip install -r requirements.txt  

### Start the backend server
uvicorn main:app --reload  

### Open the frontend
- Open index.html in a browser  
- Enter text and click Analyze Mood

---
## Output

1. Detected emotion with confidence score
2. Generative emotional explanation
3. List of mood-aligned songs

---
## Limitations

1. Static song dataset
2. Emotion detection accuracy depends on pretrained models
3. Free API usage limits restrict large-scale deployment

---
## Screenshots
<img width="915" height="471" alt="image" src="https://github.com/user-attachments/assets/5dba6c54-b863-431f-88eb-15e18bd90d62" />  


  
<img width="908" height="852" alt="image" src="https://github.com/user-attachments/assets/516b1dd1-685b-494e-8e8b-af592f545a31" />

