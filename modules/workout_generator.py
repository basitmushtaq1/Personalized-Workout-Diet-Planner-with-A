import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

def generate_workout_plan(user_data):
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"Create a JSON 7-day workout plan for {user_data['fitness_goal']}."
            response = model.generate_content(prompt)
            return json.loads(response.text.replace("```json", "").replace("```", ""))
        except:
            pass # Fallback if AI fails
            
    # Fallback Data
    return {
        "total_days": 7, "workout_days": 5, "rest_days": 2,
        "weekly_schedule": {
            "Monday": [{"name": "Pushups", "sets": "3", "reps": "12", "instructions": "Keep back straight"}],
            "Tuesday": [{"name": "Squats", "sets": "3", "reps": "15", "instructions": "Go parallel"}],
            "Wednesday": "Rest Day",
            "Thursday": [{"name": "Pull-ups", "sets": "3", "reps": "8", "instructions": "Full extension"}],
            "Friday": [{"name": "Lunges", "sets": "3", "reps": "12", "instructions": "Step forward"}],
            "Saturday": [{"name": "Plank", "sets": "3", "duration": "45s", "instructions": "Core tight"}],
            "Sunday": "Rest Day"
        },
        "tips": ["Stay consistent", "Hydrate well"]
    }