edadcliente=int(input("Dame tu edad: "))

if edadcliente < 18:
    print("Eres menor de edad")

elif edadcliente < 30:
    print("Eres joven")

elif edadcliente < 65:
    print("Eres adulto menor")

else:
    print("Eres adulto mayor")