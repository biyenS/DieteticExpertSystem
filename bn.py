import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data (make sure 'food.csv' exists in the same directory as the script)
df = pd.read_csv('food.csv')

# Filter data based on meal types
breakfast_df = df[df['Breakfast'] == 1]
lunch_df = df[df['Lunch'] == 1]
dinner_df = df[df['Dinner'] == 1]

# Split data into train and test sets
breakfast_train, breakfast_test = train_test_split(breakfast_df, test_size=0.2, random_state=42)
lunch_train, lunch_test = train_test_split(lunch_df, test_size=0.2, random_state=42)
dinner_train, dinner_test = train_test_split(dinner_df, test_size=0.2, random_state=42)

# Function to recommend meals based on meal type
def recommend_meals(data, meal_type):
    recommended_meals = []
    for index, row in data.iterrows():
        if meal_type == 'Breakfast':
            recommended_meals.append(row['Food_items'])
        elif meal_type == 'Lunch':
            recommended_meals.append(row['Food_items'])
        elif meal_type == 'Dinner':
            recommended_meals.append(row['Food_items'])
    return recommended_meals

# Recommendations for training and test sets
breakfast_recommendation_train = recommend_meals(breakfast_train, 'Breakfast')
lunch_recommendation_train = recommend_meals(lunch_train, 'Lunch')
dinner_recommendation_train = recommend_meals(dinner_train, 'Dinner')

breakfast_recommendation_test = recommend_meals(breakfast_test, 'Breakfast')
lunch_recommendation_test = recommend_meals(lunch_test, 'Lunch')
dinner_recommendation_test = recommend_meals(dinner_test, 'Dinner')

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_meters = height / 100  # Convert height to meters
    bmi = weight / (height_meters ** 2)
    return bmi

# GUI setup
root = tk.Tk()
root.title("Diet Recommendation System")
root.geometry("800x600")  # Set window size

# Customizing styles
style = ttk.Style()
style.configure('TLabel', font=('Arial', 14), background='lightblue', foreground='black', anchor='w')
style.configure('TButton', font=('Arial', 12, 'bold'), background='lightgray', foreground='black')
style.configure('TFrame', background='lightblue', pady=20, padx=20)

home_frame = ttk.Frame(root)
home_frame.pack(fill='both', expand=True)

input_frame = ttk.Frame(root)
input_frame.pack(fill='both', expand=True)

result_frame = ttk.Frame(root)
result_frame.pack(fill='both', expand=True)

age_label = ttk.Label(input_frame, text="Age:", style='TLabel')
age_label.grid(row=0, column=0, sticky=tk.W)
age_entry = ttk.Entry(input_frame)
age_entry.grid(row=0, column=1, sticky=tk.W)

weight_label = ttk.Label(input_frame, text="Weight (kg):", style='TLabel')
weight_label.grid(row=1, column=0, sticky=tk.W)
weight_entry = ttk.Entry(input_frame)
weight_entry.grid(row=1, column=1, sticky=tk.W)

height_label = ttk.Label(input_frame, text="Height (cm):", style='TLabel')
height_label.grid(row=2, column=0, sticky=tk.W)
height_entry = ttk.Entry(input_frame)
height_entry.grid(row=2, column=1, sticky=tk.W)

goal_label = ttk.Label(input_frame, text="Goal:", style='TLabel')
goal_label.grid(row=3, column=0, sticky=tk.W)
goal_var = tk.StringVar(value="Gain Weight")

gain_weight_radio = ttk.Radiobutton(input_frame, text="Gain Weight", variable=goal_var, value="Gain Weight")
gain_weight_radio.grid(row=3, column=1, sticky=tk.W)

lose_weight_radio = ttk.Radiobutton(input_frame, text="Lose Weight", variable=goal_var, value="Lose Weight")
lose_weight_radio.grid(row=3, column=2, sticky=tk.W)

result_label = ttk.Label(result_frame, text="", style='TLabel')
result_label.pack()

recommendation_label = ttk.Label(result_frame, text="", style='TLabel')
recommendation_label.pack()

def back_to_home():
    home_frame.pack()
    input_frame.pack_forget()
    result_frame.pack_forget()

def calculate_bmi_and_recommend():
    age = int(age_entry.get())
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = calculate_bmi(weight, height)
    
    goal = goal_var.get()
    if goal == "Gain Weight":
        recommended_breakfast = ", ".join(breakfast_recommendation_train)
        recommended_lunch = ", ".join(lunch_recommendation_train)
        recommended_dinner = ", ".join(dinner_recommendation_train)
        recommendation_label.config(text=f"Recommended Breakfast:\n{recommended_breakfast}\nRecommended Lunch:\n{recommended_lunch}\nRecommended Dinner:\n{recommended_dinner}")
    elif goal == "Lose Weight":
        recommended_breakfast = ", ".join(breakfast_recommendation_test)
        recommended_lunch = ", ".join(lunch_recommendation_test)
        recommended_dinner = ", ".join(dinner_recommendation_test)
        recommendation_label.config(text=f"Recommended Breakfast:\n{recommended_breakfast}\nRecommended Lunch:\n{recommended_lunch}\nRecommended Dinner:\n{recommended_dinner}")
    
    result_label.config(text=f"Age: {age}\nWeight (kg): {weight}\nHeight (cm): {height}\nBMI: {bmi:.2f}\nGoal: {goal}")
    home_frame.pack_forget()
    input_frame.pack_forget()
    result_frame.pack()

calculate_button = ttk.Button(input_frame, text="Calculate BMI and Recommend Diet", command=calculate_bmi_and_recommend, style='TButton')
calculate_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
