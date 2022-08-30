
decimal = int(input("Enter Decimal Value: \n"))
convert = int(input("Convert intp: [1] Binary ,[2] Octal, [3] Hexadecimal: \n"))

if convert == 1:
    print("Converted to Binary: \n", bin(decimal))

elif convert == 2:
    print("Converted to Octal: \n", oct(decimal))

elif convert == 3:
    print("Converted to Hexadecimal: \n", hex(decimal))


else:
    print("Please Review your Input ")