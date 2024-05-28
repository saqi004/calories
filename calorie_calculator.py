# Calorie Calculator using Harris-Benedict Equation
# For more information and other tools, visit my website: https://www.yoursite.com

def calculate_bmr(gender, weight, height, age):
    """
    Calculate Basal Metabolic Rate (BMR) using Harris-Benedict equation.
    
    Parameters:
    gender (str): 'male' or 'female'
    weight (float): Weight in kilograms
    height (float): Height in centimeters
    age (int): Age in years
    
    Returns:
    float: BMR value
    """
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Please choose 'male' or 'female'.")
    return bmr

def calculate_calories(bmr, activity_level):
    """
    Calculate daily caloric needs based on activity level.
    
    Parameters:
    bmr (float): Basal Metabolic Rate
    activity_level (str): Activity level ('sedentary', 'light', 'moderate', 'active', 'very active')
    
    Returns:
    float: Daily caloric needs
    """
    activity_factors = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }
    
    if activity_level not in activity_factors:
        raise ValueError("Invalid activity level. Please choose from 'sedentary', 'light', 'moderate', 'active', 'very active'.")
    
    return bmr * activity_factors[activity_level]

def main():
    # User inputs
    gender = input("Enter your gender (male/female): ").strip().lower()
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))
    age = int(input("Enter your age in years: "))
    activity_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ").strip().lower()
    
    # Calculate BMR and daily caloric needs
    bmr = calculate_bmr(gender, weight, height, age)
    daily_calories = calculate_calories(bmr, activity_level)
    
    # Display the result
    print(f"Your BMR is: {bmr:.2f} calories/day")
    print(f"Your daily caloric needs are: {daily_calories:.2f} calories/day")

if __name__ == "__main__":
    main()
