def calculate_bmi(height, weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))

    bmi = weight / (height * height)

    print("BMI value=" + str(bmi))

    if bmi < 18.5:
        print("Underweight")
    elif bmi > 18.5 or bmi <= 25:
        print("Normal weight")
    else:
        print("Overweight")

calculate_bmi(1.73,57)