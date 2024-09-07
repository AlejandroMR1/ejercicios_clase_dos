#Ejercicio 1

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print("Hola,",nombre, apellido)

#Ejercicio 2

precio = 100
descuento = (15*precio)/100
total = precio - descuento

print (f"El precio asignado es de {precio} y su descuento del 15% es de {descuento}, quedando un total de: {total}")


#Ejercicio 3

edad = int(input ("Escriba su edad: "))

if edad>18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Ejercicio 4

numero = int(input("Escriba un número: "))

if numero%2==0:
    print("El número es par")
else:
    print("El número es impar")

#Ejercicio 5

numero1 = int(input("Escriba el primer número: "))
numero2 = int(input("Escriba el segundo número: "))

suma = print ("La suma de los dos números es: ", numero1+numero2)
resta = print ("La resta de los dos números es ", numero1-numero2)
multiplicacion = print ("La multiplicación de los dos números es: ", numero1*numero2)

if numero2 == 0:
    print ("No se puede dividir entre cero")
else: 
    print ("La división de los dos números es: ", numero1/numero2)

#Ejercicio 6

try:
    calificacion = int(input("Ingrese su calificación de uno a cien: "))

    if calificacion >= 70 and calificacion <= 100:
        print("Aprobado")
    elif calificacion < 70 and calificacion >= 0:
        print("Reprobado")
    else:
        print("Digite un valor correcto")
except ValueError:
    print("El valor introducido no es válido")

#Ejercicio 7

try:
    
    primernumero = int(input("Ingrese el primer número: "))
    segundonumero = int(input("Ingrese el segundo número: "))

    if primernumero > segundonumero:
        print(primernumero, " es mayor a ", segundonumero)
    elif segundonumero > primernumero:
        print(segundonumero, " es mayor a ", primernumero)
    else:
        print(primernumero, " es igual a ", segundonumero)

except ValueError:
    print("El valor introducido es invalido")

#Ejercicio 8

nombre1 = input("Saludos. Escriba su nombre, por favor: ")

print ("Bienvenido, ", nombre1)

#Ejercicio 9

tablamultiplicar = int(input("Ingrese un número, por favor: "))

for i in range (1, 11):

    resultado = i * tablamultiplicar

    print(f"{tablamultiplicar} x {i} es: {resultado}")

#Ejercicio 10

print("Ingrese dos números para encontrar su promedio: ")

numeropromedio1 = int(input("Ingresar el primer número: "))
numeropromedio2 = int(input("Ingresar el segundo número: "))
formulapromedio = (numeropromedio1+numeropromedio2)/2

print(f"El promedio de los números {numeropromedio1} y {numeropromedio2} es: {formulapromedio}")

