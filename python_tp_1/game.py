import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de fallas 
max_fallas = 10
i= 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)

# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

nivel_dificultad= input(print("Escoja la nivel de dificultad."))

if nivel_dificultad == "facil":
     vocales= ["a", "e", "i", "o", "u"]
     vocales_secre= []
     print("Las vocales que contienen la palabra a adivinar son:")
     for letter in secret_word:
         if letter in vocales:
             if letter in vocales_secre:
                 continue
             else:
                 vocales_secre.append(letter)
                 print(letter)             
else:
     nivel_dificultad == "media"
     print(f" la palabra empieza con  {secret_word[0]} y termina con {secret_word[(len(secret_word)) -1]}")

while i < max_fallas:
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()

     #verifico que sea valido, si no lo es igual contara como intento
     if letter== "":
         print("El valor es invalido. Por favor ingrese otra letra")
         continue
     
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
     
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)

     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         i+= 1

     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")

     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
         break
     
if i == max_fallas and word_displayed != secret_word:  
     print(f"¡Oh no! Has alcanzado la cantidad de fallas.")
     print(f"La palabra secreta era: {secret_word}")