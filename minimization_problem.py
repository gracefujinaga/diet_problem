# import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# First Problem
print("First Linear Programming Problem (can have 0 values for certain items):")

# define variables
O = LpVariable("O", 0, None) # Overnight Oats
S = LpVariable("S", 0, None) # Mango Chili Salad
C = LpVariable("C", 0, None) # Cottage Cheese
T = LpVariable("T", 0, None) # Tofu
CB = LpVariable("CB", 0, None) # Chicken Bowl
SB = LpVariable("SB", 0, None) # Salmon Burger

# defines the problem - minimization of cost problem
prob = LpProblem("problem", LpMinimize)

weekly_sodium = 7*5000 #mg
weekly_energy = 7*2000 #cal
weekly_protein = 7 *50 #grams
weekly_vit_d = 7 *20 #mcg
weekly_iron = 7*18 # mg
weekly_potass = 7 *4700 # mg
weekly_calcium = 7 * 1300 # mg

print("\nweekly values: ")
print("sodium: ", weekly_sodium)
print("energy: ", weekly_energy)
print("protein: ", weekly_protein)
print("vitamin d: ", weekly_vit_d)
print("iron: ", weekly_iron)
print("potassium: ", weekly_potass)
print("calcium: ", weekly_calcium)
print("\n \n ")

# define constraints for each nutrient
prob += 210*O + 240*S + 320*C + 15*T + 630*CB + 330*SB <= weekly_sodium # sodium (max)
prob += 270*O + 130*S + 110*C + 130*T + 370*CB + 100*SB >= weekly_energy # energy
prob += 12*O + 3*S + 12*C + 14*T + 22*CB + 15*SB     >= weekly_protein # protein
prob += 0.2*C + 20.9 *SB  >=  weekly_vit_d # Vitamin D
prob += 30*O + 50*S + 100*C + 60*T + 130*CB >=  weekly_calcium # Calcium
prob += 1.5*O + 1.2*S + 2.7*T + 2.6*CB + 0.3*SB >=  weekly_iron # Iron
prob += 290*O + 280*S + 100*C + 110*T + 690*CB + 320*SB >=  weekly_potass # Potassium

# define objective function - minimize cost
prob += 1.99*O + 1.33*S + 0.5*C + 1.35*T + 2.69*CB + 1.8725*SB

# solve the problem
status = prob.solve()
print(f"Problem")

# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")
    
print(f"Objective = {value(prob.objective)}")
print(f"")


# -------------------- Part 4 --------------------------------------
print(" \n\n ----------------------------------- \n \n")
print("Second Linear Programming Problem (Part 4: No zero values for certain items):")
# Problem (Initial)
# define variables - make each value be at least 1 
O = LpVariable("O", 1, None) # Overnight Oats
S = LpVariable("S", 1, None) # Mango Chili Salad
C = LpVariable("C", 1, None) # Cottage Cheese
T = LpVariable("T", 1, None) # Tofu
CB = LpVariable("CB", 1, None) # Chicken Bowl
SB = LpVariable("SB", 1, None) # Salmon Burger

# defines the problem - minimization of cost problem
prob = LpProblem("problem", LpMinimize)

# define constraints for each nutrient
prob += 210*O + 240*S + 320*C + 15*T + 630*CB + 330*SB <= weekly_sodium # sodium (max)
prob += 270*O + 130*S + 110*C + 130*T + 370*CB + 100*SB >= weekly_energy # energy
prob += 12*O + 3*S + 12*C + 14*T + 22*CB + 15*SB     >= weekly_protein # protein
prob += 0.2*C + 20.9 *SB  >=  weekly_vit_d # Vitamin D
prob += 30*O + 50*S + 100*C + 60*T + 130*CB >=  weekly_calcium # Calcium
prob += 1.5*O + 1.2*S + 2.7*T + 2.6*CB + 0.3*SB >=  weekly_iron # Iron
prob += 290*O + 280*S + 100*C + 110*T + 690*CB + 320*SB >=  weekly_potass # Potassium

# define objective function - minimize cost
prob += 1.99*O + 1.33*S + 0.5*C + 1.35*T + 2.69*CB + 1.8725*SB

# solve the problem
status = prob.solve()
print(f"Problem Part 4")

# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")
    
print(f"Objective (Part 4) = {value(prob.objective)}")
print(f"")
