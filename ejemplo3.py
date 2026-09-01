sexo = input("{H}: Hombre / {M}: Mujer: ").upper()
edad=int(input("Dame tu edad: "))

if sexo == "H" and edad > 65:
    print("te jubilaras")

elif sexo == "M" and edad > 60:
    print("te jubilaras")

else:
    print("aun no te toca")


