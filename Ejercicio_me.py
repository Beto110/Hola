print("¡Bienvenido a calduladora Don Armando!")
print("Elija que operacion prefiere utilizar")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

opcion = input("ingrese porfavor el numero de la operacion: ")
num1 = float(input("Ingrese el primer numero:"))
num2 = float(input("Ingrese el segundo numero:"))

if opcion == "1":
    print("Resultado: ", num1 + num2)
elif opcion == "2":
     print("Resultado: ", num1 - num2)
elif opcion == "3":
      print("Resultado: ", num1 * num2)
elif opcion == "4":
     if num2 != 0:
           print("Resultado: ", num1 / num2)
        else:
             print("Error: No se puede divir por cero.")

    else:
        print("Opcion no valida.")

