def calculate_bmi(height, weight):
    return weight / ((height/100) ** 2)

def calculate_bmr(age, gender, height, weight):
    if gender == 'Male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    return 10 * weight + 6.25 * height - 5 * age - 161

def get_calorie_needs(data):
    bmr = calculate_bmr(data['age'], data['gender'], data['height'], data['weight'])
    return int(bmr * 1.55) # Moderate activity multiplier