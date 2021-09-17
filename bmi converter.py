def bmi():
    #to calculate BMI = kg/m square
    weight_in_kg = float(input("enter weight in kg:"))
    height_in_meter = float(input("enter height in meter:"))
    BMI = weight_in_kg / (height_in_meter*height_in_meter)
    print("BMI is :",BMI)
