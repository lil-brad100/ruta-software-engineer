nombre = input("¿Cuál es tu nombre?")
edad = int(input("¿Cuál es tu edad?"))
profesion = input("¿Cuál es tu profesión?")

print(nombre)
print(edad)
print(profesion)

if edad <= 12:
    print("Eres niño")

elif edad <= 17:
    print("Eres adolescente")

else:
    print("eres adulto")

lenguaje = input("¿Cuál es tu lenguaje de programaciónfavorito?")

print(lenguaje)

if lenguaje.strip().lower() == "python":
    print("¡Python es una excelente elección!")
else:
    print("¡Eso es genial! Cada lenguaje tiene sus ventajas y desventajas")

años_programando = int(input("¿Cuántos años llevas programando?"))
print(años_programando)

if años_programando < 1:
    print("¡Estás empezando tu camino en la programación!")
else:
    print("¡Qué bien! La experiencia es valiosa en la programación.")

contador = 1

while contador <= 10:
    print(contador)
    contador = contador + 1

for numero in range(1, 11):
    print(numero)

lenguajes = ["Python", "Java", "JavaScript", "C++","peseint"]  

lenguajes.append("C#")  

lenguajes[1] = "ejemplo"

for lenguaje in lenguajes:
    print(lenguaje)


estudiante = {
    "nombre": "brad",
    "edad": 20,
    "lenguaje_favorito": "Python",
    "años_programando": 2
}

print(estudiante["nombre"])
print(lenguaje_favorito := estudiante["lenguaje_favorito"])

estudiante["edad"] = 21
print(estudiante["edad"])

estudiante["nivel"] = "principiante"
print(estudiante["nivel"])

for clave, valor in estudiante.items():
    print(clave,valor) 



def saludar():
    print("hola brad")

    saludar()

def mostrar_estudiante():
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Lenguaje favorito:", estudiante["lenguaje_favorito"]) 
    print("Años programando:", estudiante["años_programando"])
    print("Nivel:", estudiante["nivel"])


mostrar_estudiante()

saludar_persona = input("¿Cuál es tu nombre?")

def saludar_persona(nombre):
    print("¡Hola, " + nombre + "!")

saludar_persona("Brad")

def calcular_edad_futura(edad, años):
    return edad + años

resultado = calcular_edad_futura(20, 5)

print(resultado)

def calcular_edad_futura(edad, años):
    return edad + años

edad = int(input("¿Cuál es tu edad actual?"))
años = int(input("¿Cuántos años quieres agregar?"))

resultado = calcular_edad_futura(edad, años)
print(resultado)

edad = int(input("¿Cuál es tu edad?"))
def clasificar_edad(edad):
    if edad < 18:
        return "Eres menor de edad"
        
    elif edad <= 25:
        return "Eres un joven adulto"
        
    else:
        return "Eres adulto"

resultado = clasificar_edad(edad)
print(resultado)

def mostrar_resumen(estudiante):
    print("Resumen del estudiante:")
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Lenguaje favorito:", estudiante["lenguaje_favorito"])
    print("Años programando:", estudiante["años_programando"])
    print("Nivel:", estudiante["nivel"])


mostrar_resumen(estudiante)

edad = int(input("¿Cuál es tu edad?"))
def mayor_de_edad(edad):
    return edad >= 18

if mayor_de_edad(edad):
    print("true") 
else:
    print("false")  

def mostrar_lenguajes(lenguajes):              
    for lenguaje in lenguajes:
        print(lenguaje)

lenguajes = ["Python", "Java", "JavaScript", "C++", "C#"]
mostrar_lenguajes(lenguajes)    

lenguajes = ["Python", "Java", "JavaScript", "C++", "C#"]

print(len(lenguajes))

def contar_lenguajes(lenguajes):
    return len(lenguajes)

print(contar_lenguajes(lenguajes))
lenguajes = ["Python", "Java", "JavaScript", "C++", "C#"]


lenguajes = ["Python", "Java", "JavaScript", "C++", "C#"] 

lenguajes.remove("JavaScript")
print(lenguajes)

lenguajes = ["Python", "Java", "JavaScript", "C++", "C#"]

lenguajes = ["Python", "Java", "JavaScript", "C++", "C#"]

lenguajes.pop(2)
print(lenguajes)

lenguajes = ["Python", "Java", "JavaScript", "C++", "C#"]
print(lenguajes)

lenguajes.remove("JavaScript")

lenguajes.pop(3)

resultado = len(lenguajes)
print(resultado)

estudiantes = [
    {"nombre": "Brad", "edad": 20, "lenguaje_favorito": "Python"},
    {"nombre": "Alice", "edad": 25, "lenguaje_favorito": "Java"},
    {"nombre": "John", "edad": 30, "lenguaje_favorito": "JavaScript"}

]

for estudiante in estudiantes:
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Lenguaje favorito:", estudiante["lenguaje_favorito"])
    print()

def buscar_estudiante(estudiantes, nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            return estudiante
    return None
nombre = input("¿Qué estudiante quieres buscar? ")
buscar_estudiante(estudiantes, nombre)

resultado = buscar_estudiante(estudiantes, nombre)

if resultado:
    print("Nombre:", resultado["nombre"])
    print("Edad:", resultado["edad"])
    print("Lenguaje:", resultado["lenguaje_favorito"])
else:
    print("Estudiante no encontrado")


try:
    edad = int(input("¿Cuál es tu edad? "))
    print("Tu edad es:", edad)

except ValueError:
    print("Debes escribir un número.")

while True:
    try:
        edad = int(input("¿Cuál es tu edad? "))
        print("Tu edad es:", edad)
        break

    except ValueError:
        print("Debes escribir un número.")

nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")

archivo = open("datos.txt", "w")

archivo.write("Nombre: " + nombre + "\n")
archivo.write("Edad: " + edad + "\n")

archivo.close()

print("Datos guardados correctamente.")