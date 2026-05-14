# --- Workout Tracker: Sprint 1 ---

# # 1. Capture User Input (Strings)
# exercise = input("What exercise did you do?: ")
# weight_txt = input("How much weight did you lift (kg)?: ")

# # 2. Type Conversion (Fundamentals)
# weight = float(weight_txt)

# # 3. Output the result using an f-string
# print(f"Success! You logged {exercise} at {weight}kg.")

# tracker.py
print("--- Digital Gym Log ---")
session_data = []

while True:
    exercise = input("\nExercise name (or 'exit'): ")
    
    if exercise.lower() == 'exit':
        break
    
    try:
        weight = float(input("Weight (kg): "))
    except ValueError:
        print("❌ Please enter a number!")
        continue  # Jumps back to the top of the while loop
    
    session_data.append(f"{exercise}: {weight}kg")

# --- THE FOR LOOP STARTS HERE ---
# It only runs AFTER you type 'exit'
print("\n--- Session Summary ---")
for item in session_data:
    print(item)




