from scipy.optimize import linprog

# Cost per serving for each food item
cost = [1.99, 1.33, 0.50, 1.35, 2.69, 1.8725]

# Nutrient content per serving of each food item (rows represent sodium, energy, etc.)
nutrient_content = [
    [210, 240, 320, 15, 630, 330],  # Sodium (mg) - This will be handled differently for the max constraint
    [270, 130, 110, 130, 370, 100],  # Energy (cal)
    [12, 3, 12, 14, 22, 15],         # Protein (g)
    [0, 0, 0.2, 0, 0, 20.9],         # Vitamin D (mcg)
    [1.5, 1.2, 0, 2.7, 2.6, 0.3],    # Iron (mg)
    [30, 50, 100, 60, 130, 0],       # Calcium (mg)
    [290, 280, 100, 110, 690, 320]   # Potassium (mg)
]

# Weekly requirements for each nutrient
weekly_requirements = [35000, 14000, 350, 140, 126, 9100, 32900]

# Now, modify the sodium constraint to be a maximum:
# For all other nutrients, we want >=, but for sodium, we want <= 35,000
A_ub = [
    nutrient_content[0],  # Sodium - this is a max constraint
    [-x for x in nutrient_content[1]],  # Energy
    [-x for x in nutrient_content[2]],  # Protein
    [-x for x in nutrient_content[3]],  # Vitamin D
    [-x for x in nutrient_content[4]],  # Iron
    [-x for x in nutrient_content[5]],  # Calcium
    [-x for x in nutrient_content[6]]   # Potassium
]

# Adjust the bounds accordingly:
b_ub = [35000] + [-x for x in weekly_requirements[1:]]  # Max for sodium, min for others

# Minimize the cost function, subject to nutrient constraints
result = linprog(
    c=cost,  # Objective function coefficients (minimize cost)
    A_ub=A_ub,  # Nutrient constraints (upper bounds)
    b_ub=b_ub,  # Upper bounds for each constraint
    bounds=[(0, None)] * len(cost),  # Non-negative servings
    method='highs'  # Solver method
)

# Print the results
if result.success:
    servings = result.x
    print("Optimal number of servings for each food item per week:")
    print(f"Overnight Oats: {servings[0]:.2f}")
    print(f"Mango Chili Salad: {servings[1]:.2f}")
    print(f"Cottage Cheese: {servings[2]:.2f}")
    print(f"Tofu: {servings[3]:.2f}")
    print(f"Chicken Bowl: {servings[4]:.2f}")
    print(f"Salmon Burger: {servings[5]:.2f}")
    print(f"Total weekly cost: ${result.fun:.2f}")
else:
    print("No solution found.")
