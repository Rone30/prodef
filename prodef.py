import random

print('¡¡¡ Adivina la palabra !!!!!')

def seleccionar_palabra():
    palabras = ["comedor", "billetera", "cubierto", "solemnidad", "yamani"]
    return random.choice(palabras)

def ahorcado():
    palabra = seleccionar_palabra()
    palabra_oculta = ["_"] * len(palabra)
    intentos = 5
    letras_usadas = []

    while intentos > 0 and "_" in palabra_oculta:
        print("Palabra: " + " ".join(palabra_oculta))
        print("Intentos: " + str(intentos))
        letra = input("Ingresá una letra: ").lower()

        if letra in letras_usadas:
            print("Ya usaste esa letra! Intentá con otra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
        else:
            intentos -= 1
            print("Letra incorrecta. Te quedan " + str(intentos) + " intentos!")

    if "_" not in palabra_oculta:
        print("¡Felicidades! Acertaste la palabra: " + palabra)
    else:
        print("Ufa! Te quedaste sin intentos. La palabra era: " + palabra)

ahorcado()