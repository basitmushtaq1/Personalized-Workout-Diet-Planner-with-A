"""
Basic test script for the AI-Powered Personalized Workout & Diet Planner
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all modules can be imported successfully"""
    
    print("Testing module imports...")
    
    try:
        from modules.ui import render_sidebar
        print("PASS: UI module imported successfully")
    except ImportError as e:
        print(f"FAIL: UI module import failed: {e}")
        return False
    
    try:
        from modules.workout_generator import generate_workout_plan
        print("PASS: Workout generator module imported successfully")
    except ImportError as e:
        print(f"FAIL: Workout generator module import failed: {e}")
        return False
    
    try:
        from modules.diet_generator import generate_diet_plan
        print("PASS: Diet generator module imported successfully")
    except ImportError as e:
        print(f"FAIL: Diet generator module import failed: {e}")
        return False
    
    try:
        from modules.pdf_export import export_to_pdf
        print("PASS: PDF export module imported successfully")
    except ImportError as e:
        print(f"FAIL: PDF export module import failed: {e}")
        return False
    
    try:
        from modules.utils import calculate_bmi, calculate_bmr, get_calorie_needs
        print("PASS: Utils module imported successfully")
    except ImportError as e:
        print(f"FAIL: Utils module import failed: {e}")
        return False
    
    return True

def test_utility_functions():
    """Test utility functions"""
    
    print("\nTesting utility functions...")
    
    try:
        from modules.utils import calculate_bmi, calculate_bmr, get_calorie_needs
        
        # Test BMI calculation
        bmi = calculate_bmi(170, 70)
        print(f"PASS: BMI calculation: {bmi:.1f}")
        
        # Test BMR calculation
        bmr = calculate_bmr(25, 'Male', 170, 70)
        print(f"PASS: BMR calculation: {bmr:.1f} calories/day")
        
        # Test calorie needs
        user_data = {
            'age': 25,
            'gender': 'Male',
            'height': 170,
            'weight': 70,
            'workout_frequency': '4-5 days',
            'activity_level': 'Moderate Exercise (3-5 days/week)',
            'fitness_goal': 'Weight Loss'
        }
        calorie_needs = get_calorie_needs(user_data)
        print(f"PASS: Calorie needs: {calorie_needs}")
        
        return True
        
    except Exception as e:
        print(f"FAIL: Utility functions test failed: {e}")
        return False

def test_workout_generation():
    """Test workout plan generation"""
    
    print("\nTesting workout plan generation...")
    
    try:
        from modules.workout_generator import generate_workout_plan
        
        user_data = {
            'age': 25,
            'gender': 'Male',
            'height': 170,
            'weight': 70,
            'fitness_goal': 'Weight Loss',
            'equipment': ['Dumbbells'],
            'location': 'Home',
            'time_available': '30-45 minutes',
            'workout_frequency': '4-5 days',
            'experience_level': 'Beginner'
        }
        
        workout_plan = generate_workout_plan(user_data)
        print(f"PASS: Workout plan generated: {len(workout_plan.get('weekly_schedule', {}))} days")
        print(f"   - Workout days: {workout_plan.get('workout_days', 0)}")
        print(f"   - Rest days: {workout_plan.get('rest_days', 0)}")
        
        return True
        
    except Exception as e:
        print(f"FAIL: Workout generation test failed: {e}")
        return False

def test_diet_generation():
    """Test diet plan generation"""
    
    print("\nTesting diet plan generation...")
    
    try:
        from modules.diet_generator import generate_diet_plan
        
        user_data = {
            'age': 25,
            'gender': 'Male',
            'height': 170,
            'weight': 70,
            'dietary_preference': 'Vegetarian',
            'cultural_food': 'Indian',
            'budget': 20,
            'fitness_goal': 'Weight Loss',
            'activity_level': 'Moderate Exercise (3