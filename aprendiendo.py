def sumar (a, b):
    return a + b
def restar (a, b ):
    return a - b
def multiplicar (a, b):
    return a * b
def dividir (a, b):
    if b==0: 
     return "error:no se divide entre 0"
    return a / b

print ("CALCULADORA PAVEL")
print ("1.suma |2.resta |3.multiplicacion |4.division:")
opcion=input("escoje un numero (1/2/3/4):")
num1=float(input("escribe el primer numero:"))
num2=float(input("escribe el segundo numero:"))
if opcion =="1":
    print (f"resultado de la suma es {sumar(num1,num2)}")
elif opcion == '2':
    print(f"El resultado de la resta es: {restar(num1, num2)}")
elif opcion == '3':
    print(f"El resultado de la multiplicacion es: {multiplicar(num1, num2)}")
elif opcion == '4':
    print(f"El resultado de la division es: {dividir(num1, num2)}")
else:
    print("esa opcion no existe, intente de nuevo")