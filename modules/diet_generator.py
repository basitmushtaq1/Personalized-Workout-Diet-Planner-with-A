import google.generativeai as genai
import os
import json
from modules.utils import get_calorie_needs
from dotenv import load_dotenv

load_dotenv()

def generate_diet_plan(user_data):
    # Very similar logic to workout_generator but for food
    # Returns a JSON structure for diet
    return {
        "daily_calories": get_calorie_needs(user_data),
        "daily_budget": user_data['budget'],
        "meals_per_day": 3,
        "daily_meals": {
            "Breakfast": {"name": "Oatmeal", "calories": 400, "cost": 20, "ingredients": "Oats, Milk"},
            "Lunch": {"name": "Rice & Dal", "calories": 600, "cost": 40, "ingredients": "Rice, Lentils"},
            "Dinner": {"name": "Roti & Veg", "calories": 500, "cost": 30, "ingredients": "Flour, Veggies"}
        },
        "nutritional_breakdown": {"protein": 60, "carbs": 200, "fat": 50, "fiber": 30},
        "tips": ["Eat more protein", "Avoid sugar"]
    }