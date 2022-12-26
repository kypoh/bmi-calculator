height = input('what is your height in meters?\n')
height = float(height)

weight = input('what is your weight in kilograms?\n')
weight = float(weight)

bmi = weight / height**2


print(f'your bmi is {bmi}')

if weight > 99 :
    print(f'fat')

elif weight < 50 :
    print(f'chopstick')

else :
     print(f'healthy')