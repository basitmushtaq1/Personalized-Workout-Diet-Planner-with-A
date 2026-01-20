# FitnessAI - Intelligent Workout & Nutrition Planner

A comprehensive fitness application that leverages artificial intelligence to create personalized workout and nutrition plans. Built with modern web technologies and designed for scalability and user engagement.

## 🌟 Overview
FitnessAI combines advanced AI capabilities with intuitive user experience to deliver scientifically-backed fitness recommendations. The application analyzes user profiles, preferences, and goals to generate customized 7-day workout and nutrition plans.

## 🚀 Key Features

### Intelligent Planning
* *AI-Powered Recommendations:* Advanced algorithms analyze user data to create optimal fitness plans.
* *Personalized Profiles:* Comprehensive user profiling with health metrics and lifestyle preferences.
* *Scientific Optimization:* Plans based on exercise science and nutritional research.

### Workout Management
* *Customized Routines:* 7-day workout plans tailored to individual goals and equipment.
* *Progressive Difficulty:* Plans that adapt to user experience level (Beginner to Advanced).
* *Equipment Flexibility:* Workouts designed for home gyms, commercial facilities, or bodyweight training.

### Nutrition Planning
* *Cultural Adaptation:* Meal plans that respect cultural and regional food preferences.
* *Dietary Compliance:* Support for Veg, Non-Veg, Vegan, and Keto options.
* *Budget Optimization:* Cost-effective meal planning based on user budget.

## 🛠️ Technology Stack
* *Frontend:* Streamlit
* *AI Engine:* Google Gemini Pro
* *Backend:* Python 3.x
* *Data Handling:* Pandas & NumPy

## 🎯 Problem Statement
Most fitness applications provide generic, "one-size-fits-all" advice that fails to consider a user's unique context. Students and beginners often face:
* *Lack of Personalization:* Plans do not account for injuries, available equipment, or time constraints.
* *Cultural Disconnect:* Diet plans often ignore regional food habits (e.g., Indian vegetarian diets).
* *Budget Constraints:* Premium coaches are expensive, and free apps lack depth.

*Solution:* FitnessAI acts as a *virtual personal trainer*, using Generative AI to create hyper-personalized schedules that adapt to the user's specific life constraints.


## 🏗️ System Architecture

The application follows a modular architecture separating the UI, Logic, and AI interaction layers.

```mermaid
graph TD
    A["User Interface (Streamlit)"] -->|Input Profile Data| B["Input Processor"]
    B -->|Structured Prompt| C{"AI Engine (Gemini Pro)"}
    C -->|JSON Response| D["Plan Parser"]
    D -->|Formatted Data| E["Workout Generator"]
    D -->|Formatted Data| F["Diet Generator"]
    E --> G["Display UI"]
    F --> G
    G -->|Export| H["PDF Report"]
## 📦 Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>