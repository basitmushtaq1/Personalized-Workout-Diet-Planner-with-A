from fpdf import FPDF
import os

def export_to_pdf(user_data, workout, diet):
    if not os.path.exists("temp"): os.makedirs("temp")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Fitness Plan for {user_data['fitness_goal']}", ln=1, align='C')
    pdf.output("temp/personalized_plan.pdf")
    return "temp/personalized_plan.pdf"