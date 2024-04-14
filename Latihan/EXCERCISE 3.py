Weight = float(input("Weight : "))
Unit = input("Kg or Lbs : ") 
print("Weight : ")

if Unit == "Kg":
    Weight *= 2.20462
    print(str(Weight) + "Lbs")
elif Unit == str("Lbs"):
    Weight /= 2.20462
    print(str(Weight) + "Kg")

    '''
    Other ways
    Weight = float(input("Weight : "))
    Unit = input("(K)g or (L)bs : ")
    if unit.upper() == "K"
        converted = weight / 2.20462
        print("Weight in Lbs: " + str(converted)
    else:
        converted = weight * 2.20462
        print("Weight in Kgs: " + str(converted))

    '''



