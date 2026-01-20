"""
AI-Powered Personalized Workout & Diet Planner
Main Streamlit Application Entry Point
"""

import streamlit as st
import os
from modules.ui import render_sidebar
from modules.workout_generator import generate_workout_plan
from modules.diet_generator import generate_diet_plan
from modules.pdf_export import export_to_pdf
from modules.utils import calculate_bmi

# 1. Page Configuration
st.set_page_config(
    page_title="AI Workout & Diet Planner",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Load Custom CSS
def load_css():
    try:
        with open("assets/style.css", "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

# 3. Main Application Logic
def main():
    # Initialize Session State (This keeps data alive when you click buttons)
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {}
    if 'workout_plan' not in st.session_state:
        st.session_state.workout_plan = None
    if 'diet_plan' not in st.session_state:
        st.session_state.diet_plan = None

    # Header
    st.markdown("""
    <div class="main-header">
        <h1>💪 AI-Powered Personalized Workout & Diet Planner</h1>
        <p>Custom fitness and nutrition plans tailored to your needs, culture, and budget.</p>
    </div>
    """, unsafe_allow_html=True)

    # Render Sidebar (from modules/ui.py)
    with st.sidebar:
        render_sidebar()

    # Create Tabs
    tab1, tab2, tab3 = st.tabs(["🏋️ Workout Plan", "🥗 Diet Plan", "📊 Summary & Export"])

    # --- TAB 1: WORKOUT ---
    with tab1:
        st.header("🏋️ Your Personalized Workout Plan")
        
        if st.button("Generate Workout Plan", type="primary"):
            if st.session_state.user_data:
                with st.spinner("🤖 AI is designing your workout..."):
                    try:
                        plan = generate_workout_plan(st.session_state.user_data)
                        st.session_state.workout_plan = plan
                        st.success("Plan generated!")
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning("Please fill in your profile in the sidebar first.")

        # Display the Plan
        if st.session_state.workout_plan:
            plan = st.session_state.workout_plan
            
            # Overview Metrics
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Days", plan.get('total_days', 7))
            c2.metric("Workout Days", plan.get('workout_days', 0))
            c3.metric("Rest Days", plan.get('rest_days', 0))
            
            # Weekly Schedule Loop
            st.subheader("📅 Weekly Schedule")
            schedule = plan.get('weekly_schedule', {})
            
            for day, exercises in schedule.items():
                with st.expander(f"{day}", expanded=True):
                    if exercises == "Rest Day":
                        st.info("🛌 Rest Day - Light stretching or walking.")
                    elif isinstance(exercises, list):
                        for ex in exercises:
                            st.markdown(f"""
                            <div class="workout-card">
                                <b>{ex.get('name', 'Exercise')}</b><br>
                                Sets: {ex.get('sets')} | Reps: {ex.get('reps')}<br>
                                <i>Note: {ex.get('instructions', '')}</i>
                            </div>
                            """, unsafe_allow_html=True)

    # --- TAB 2: DIET ---
    with tab2:
        st.header("🥗 Your Personalized Diet Plan")
        
        if st.button("Generate Diet Plan", type="primary"):
            if st.session_state.user_data:
                with st.spinner("🤖 AI is planning your meals..."):
                    try:
                        plan = generate_diet_plan(st.session_state.user_data)
                        st.session_state.diet_plan = plan
                        st.success("Menu ready!")
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning("Please fill in your profile in the sidebar first.")

        # Display Diet Plan
        if st.session_state.diet_plan:
            plan = st.session_state.diet_plan
            
            c1, c2 = st.columns(2)
            c1.metric("Daily Calories", plan.get('daily_calories'))
            c2.metric("Budget", f"${plan.get('daily_budget')}")
            
            st.subheader("🍽️ Daily Menu")
            meals = plan.get('daily_meals', {})
            
            for meal_type, info in meals.items():
                st.markdown(f"""
                <div class="meal-card">
                    <h4>{meal_type}: {info.get('name', 'Meal')}</h4>
                    <p>🔥 {info.get('calories')} kcal | 💰 ${info.get('cost', 0)}</p>
                    <p>🛒 Ingredients: {info.get('ingredients', 'N/A')}</p>
                </div>
                """, unsafe_allow_html=True)

    # --- TAB 3: SUMMARY & EXPORT ---
    with tab3:
        st.header("📊 Summary")
        
        if st.session_state.user_data:
            user = st.session_state.user_data
            bmi = calculate_bmi(user['height'], user['weight'])
            st.metric("Your BMI", f"{bmi:.2f}")
            
            # PDF Export Button
            if st.session_state.workout_plan and st.session_state.diet_plan:
                if st.button("📄 Download PDF Report"):
                    pdf_file = export_to_pdf(user, st.session_state.workout_plan, st.session_state.diet_plan)
                    with open(pdf_file, "rb") as f:
                        st.download_button("Click to Download", f, file_name="My_Fitness_Plan.pdf")
            else:
                st.info("Generate both Workout and Diet plans to download the PDF.")

if __name__ == "__main__":
    main()