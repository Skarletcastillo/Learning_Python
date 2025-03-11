
#❀┉┅━━━━━━━ Sangrado ━━━━━━━┅┉❀
#(identar):Es una forma de organizar visualmente el código para facilitar su lectura:
edad = 10

if edad == 10:
    print("Verdadero")
else:
    print("Falso")
# Aquí el sangrado indica que la línea print("Verdadero") está dentro del bloque if, mientras que la línea print("Falso") está dentro del bloque else.   

#❀┉┅━━━━━━━ Variables ━━━━━━━┅┉❀
# No inician en numero, no contienen espacios, estan en minusculas (variables) y mayusculas (constantes) inician o se separan por guion bajo:
nombre_persona = "Juan"
_nombre_persona_2= "Lucia"
NOMBRE_CONSTANTE = "Alberto"


#Snake case (Palabras en minusculas separadas con guines bajos): 
numero_de_usuarios = 100
nombre_completo = "Juan Pérez"

# En una clase (usar PascalCase)



#❀┉┅━━━━━━━Tipos de datos━━━━━━━┅┉❀

# Cadenas " " ' ' 
nombre_propio = "Skarlet"
apellido = 'Castillo'


# Listas [] 
# Secuencias ordenadas de valores, contienen cualquier tipo de datos
frutas = ["manzana", "banana", "pera"]
numeros = [1, 2, 3, 4, 5]


# Tuplas () 
# Similares a las listas pero son inmutables y no se pueden modificar una vez creadas
colores = ("rojo", "verde", "azul")


# Diccionarios {}
# Estructuras de datos no ordenadas que asocian claves con valores
persona = {
 "nombre": "John Doe",
 "edad": 30,
 "ciudad": "New York"
}


#❀┉┅━━━━━━━ Función print()  ━━━━━━━┅┉❀
#mostrar información en la pantalla 
#Parametros: cadenas de texto, variables, expresion, etc..

# Imprimir una cadena de texto
print("Hola mundo!")
# Imprimir una variable
nombre_propio2 = "Ana"
print(nombre_propio2)
# Imprimir una expresión
suma = 1 + 2
print(suma)
# Imprimir múltiples objetos
print("El resultado es:", suma, "y el nombre es:", nombre_propio2)


##❀┉┅━━━━━━━ Argumentos de función print()  ━━━━━━━┅┉❀

# Sep: Separa los objetos con el valor entre parentesis que asignemos (por defecto es un espacio)
print("a", "b", "c", sep=" - ")

# End: Agrega caracteres al final de una salida e imprime en la misma linea el siguiente print
print("línea 1", end=", Contenido agregado,  ")
print("línea 2")

# F: Formateo de cadenas, ayuda a que sea mas sencillo imprimir sin convertir a str o int
nombre = "Skarlet"
edad = 25

# Con F -->
print(f"Hola, me llamo {nombre} y tengo {edad} años.")

# Sin F -->
print("Hola, me llamo " + str(nombre) + " y tengo " + str(apellido) + "años")


#❀┉┅━━━━━━━ Función input()  ━━━━━━━┅┉❀
# obtener información que seintroduzca por el teclado.
#Esta funcion siempre devuelve STRING aun si la persona introduce numeros 
prompt = "Texto"

entrada = input(prompt)


##❀┉┅━━━━━━━ Argumentos de la función input()  ━━━━━━━┅┉❀
# prompt: Es una cadena de texto que se muestra al usuario antes de que introduzca la información
# Pedir el nombre del usuario
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}!")
# Solicitar dos números y sumarlos
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
suma = num1 + num2
print(f"La suma es: {suma}")