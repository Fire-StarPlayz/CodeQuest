for i in range(int(input())):
    temp, pw, ss, orbit = input().split(' ')
    if 0 <= float(temp) <= 100:
        if pw == "true":
            if ss == "true":
                if 0 <= float(orbit) <= 0.6:
                    print("The planet is habitable.")
                else:
                    print("The planet's orbit is not ideal.")
            else:
                print("The planet has no magnetic field.")
        else:
            print("The planet has no water.")
    elif float(temp) < 0:
        print("The planet is too cold.")
    else:
        print("The planet is too hot.")