print("Welcome to PolyCalc")

while True:
    print("Select option: 1.circuit 2.surface area")

    option = int(input("Enter option number: "))

    if (option == 1):
        print("Select option: 1.square 2.rectangle")
        optionC = int(input("Enter option number: "))

        if (optionC == 1):
            aCS = float(input("Enter side A length: "))
            cS = aCS * 4
            print("Circuit: " + str(cS))
        if (optionC == 2):
            aCR = float(input("Enter side A length: "))
            bCR = float(input("Enter side B length: "))
            cR = aCR * 2 + bCR * 2
            print("Circuit: " + str(cR))
    if (option == 2):
        print("Select option: 1.square 2.rectangle 3.trapeze")
        optionA = int(input("Enter option number: "))

        if (optionA == 1):
            aSAS = float(input("Enter side A length: "))
            sAS = aSAS * aSAS
            print("Surface area: " + str(sAS))
        if (optionA == 2):
            aSAR = float(input("Enter side A length: "))
            bSAR = float(input("Enter side B length: "))
            sAR = aSAR * bSAR
            print("Surface area: " + str(sAR))
        if (optionA == 3):
            aSAT = float(input("Enter base A length: "))
            bSAT = float(input("Enter base B length: "))
            hSAT = float(input("Enter height: "))
            sAT = (aSAT + bSAT) * hSAT / 2
            print("Surface area: " + str(sAT))