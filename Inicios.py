
#❀┉┅━━━━━━━ Sangrado ━━━━━━━┅┉❀
#(identar):Es una forma de organizar visualmente el código para facilitar su lectura:
if condition:
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
nombre = "Skarlet"
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
nombre = "Ana"
print(nombre)
# Imprimir una expresión
suma = 1 + 2
print(suma)
# Imprimir múltiples objetos
print("El resultado es:", suma, "y el nombre es:", nombre)