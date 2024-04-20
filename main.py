print("Welcome to PolyCalc")

while True:
    print("Select option: 1.circuit 2.surface area")

    option = int(input("Enter option number: "))

    if (option == 1):
        print("Select option: 1.square 2.rectangle")
        optionC = int(input("Enter option number: "))

        if (optionC == 1):
            uCS = input("Enter the unit: ")
            aCS = float(input("Enter side A length: "))
            cS = aCS * 4
            print("Circuit: " + str(cS) + uCS)
        if (optionC == 2):
            uCR = input("Enter the unit: ")
            aCR = float(input("Enter side A length: "))
            bCR = float(input("Enter side B length: "))
            cR = aCR * 2 + bCR * 2
            print("Circuit: " + str(cR) + uCR)
    if (option == 2):
        print("Select option: 1.square 2.rectangle 3.trapeze 4.triangle")
        optionSA = int(input("Enter option number: "))

        if (optionSA == 1):
            uSAS = input("Enter the unit: ")
            aSAS = float(input("Enter side A length: "))
            sAS = aSAS * aSAS
            print("Surface area: " + str(sAS) + uSAS + "²")
        if (optionSA == 2):
            uSAR = input("Enter the unit: ")
            aSAR = float(input("Enter side A length: "))
            bSAR = float(input("Enter side B length: "))
            sAR = aSAR * bSAR
            print("Surface area: " + str(sAR) + uSAR + "²")
        if (optionSA == 3):
            uSAT = input("Enter the unit: ")
            aSAT = float(input("Enter base A length: "))
            bSAT = float(input("Enter base B length: "))
            hSAT = float(input("Enter height: "))
            sAT = (aSAT + bSAT) * hSAT / 2
            print("Surface area: " + str(sAT) + uSAT + "²")
        if (optionSA == 4):
            uSATr = input("Enter the unit: ")
            aSATr = float(input("Enter base A length: "))
            hSATr = float(input("Enter height: "))
            sATr = aSATr * hSATr / 2
            print("Surface area: " + str(sATr) + uSATr + "²")
