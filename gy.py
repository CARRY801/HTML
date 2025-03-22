from flask import Flask, render_template, request
import pandas as pd

app = Flask(_name_)

# Function to calculate BMI
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

# Function to generate a fitness plan
def generate_plan(bmi, goal):
    if bmi < 18.5:
        plan = "High-protein, high-calorie meals. Strength training with moderate cardio."
    elif 18.5 <= bmi <= 24.9:
        plan = "Balanced diet with moderate carbs, proteins, and fats. Mix of cardio and strength training."
    else:
        plan = "Low-carb, high-fiber meals. Intense cardio + strength training."
    
    if goal == "muscle gain":
        plan += " Focus on strength training and increase protein intake."
    elif goal == "weight loss":
        plan += " Increase cardio sessions and maintain a calorie deficit."

    return plan

# Home page (Form)
@app.route("/")
def index():
    return render_template("index.html")

# Process form and show results
@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]
    age = int(request.form["age"])
    height = float(request.form["height"])
    weight = float(request.form["weight"])
    goal = request.form["goal"]

    bmi = calculate_bmi(weight, height)
    plan = generate_plan(bmi, goal)

    # Save data to CSV
    df = pd.DataFrame([[name, age, height, weight, goal, bmi, plan]], 
                      columns=["Name", "Age", "Height", "Weight", "Goal", "BMI", "Plan"])
    df.to_csv("data.csv", mode="a", index=False, header=False)

    return render_template("result.html", name=name, bmi=bmi, plan=plan)

if _name_ == "_main_":
    app.run(debug=True)