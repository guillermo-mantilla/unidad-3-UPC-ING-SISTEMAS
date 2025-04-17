from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt


CALORIE_GOAL_LIMIT = 300 # kcal
PROTEIN_GOAL = 180 # gramos
FAT_GOAL = 80 # gramos
CARBS_GOAL = 300 # gramos

today = []


@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int



done = False
while not done:
    print("""
    (1) Add new food
    (2) Visualize progress
    (q) Quit
    """)

    choice = input("Choose an option: ")

    if choice == "1": 
        print("Adding a new food")
        name = input ("Name: ")
        calories = int(input("Calories:"))
        protein = int(input("Protein:"))
        fat = int(input("Fat: "))
        carbs = int(input("Carbs: "))
        food = Food (name, calories, protein, fat, carbs)
        today.append(food)
        print ("Successfully added")
    elif choice == "2": 
        calorie_sum = sum (food.calories for food in today)
        protein_sum = sum (food.protein for food in today)
        fats_sum = sum (food.fat for food in today)
        carbs_sum = sum (food.carbs for food in today)

        fig, axs = plt.subplots(2,2)
        axs [0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%")
        axs [0, 0].set_title("Macronutrients distribution")
        
        fig.tight_layout()
        plt.show()