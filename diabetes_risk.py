
import math

# function to define diabetes risk

def nRisk(sex, age, BMI, med, steroid, smoke, family):
    n = (6.322 + sex) - (0.063 * age) - BMI - med - steroid - smoke - family
    risk = 100 / (1 + math.e ** n)
    return risk


# Determine the ‘Sex’ parameter based on the input of ‘male’ or ‘female’

sex = input("Enter your sex (M/F): ").upper()

if sex == 'm' or sex == 'M' or sex == "MALE":
    sex = 0
if sex == 'f' or sex == 'F' or sex == "Female":
    sex = .879

age = int(input("Enter your age (years): "))

# Determine the ‘BMI’ parameter based on range of the input given

BMI = float(input("Enter your BMI: "))

if BMI < 25:
    BMI = 0
elif 25 <= BMI <= 27.49:
    BMI = 0.699
elif 27.5 <= BMI <= 29.99:
    BMI = 1.97
elif BMI >= 30:
    BMI = 2.518

# Determine the ‘hypertension medication’ parameter based on the input of medication or none

med = input("Are you on medication for hypertension (Y/N)? ").upper()

if med == 'Y' or med == 'YES':
    med = 1.222
elif med == 'N' or med == 'NO':
    med = 0

    # Determine the ‘steroids’ parameter based on the input of using or not using steroids
    # we have comments

steroid = input("Are you on steroids (Y/N)?  ").upper()

if steroid == 'Y' or steroid == 'Yes':
    steroid = 2.191
elif steroid == 'N' or steroid == 'NO':
    steroid = 0

# Determine the ‘smoker’ parameter based on the input of non-smoker, used to smoke, or smoker
smoke = input("Do you smoke cigarettes (Y/N)? ").upper()

if smoke == 'Y' or smoke == "YES":
    smoke = 0.855
elif smoke == "N" or smoke == "NO":
    smoke = 0
    if input("Did you used to smoke (Y/N)? ").upper() == 'Y':
        smoke = -0.218
'''
elif smoked == "Y" or smoked == "YES":
    smoke = -0.218
'''

# Determine the ‘family_history’ parameter based on the input of if there is
# both parent and sibling that have diabetes, a parent or a sibling that has diabetes, or no family history of diabetes

history = input("Do you have a family history of diabetes (Y/N)? ").upper()

if history == 'N' or history == 'NO':
    family = 0
elif history == 'Y' or history == 'YES':
    bothPS = input('Both parent and sibling (Y/N)? ').upper()  # Both parent and sibling
    if bothPS == "YES" or bothPS == "Y":

        # accounting for both parent and sibling

        family = 0.753
    else:
        family = 0.728

risk = float(nRisk(sex, age, BMI, med, steroid, smoke, family))

print(f'Your risk of developing type-2 diabetes is {round(risk,1)}%')
