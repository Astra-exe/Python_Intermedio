import hangmanpics as hpics
import random as r
import os
import time

def interface():
    texto = open("./files/interface.txt", encoding = "utf-8")
    print(texto.read())

def normalize(word):
    word = word.lower()
    word = word.replace("á", "a")
    word = word.replace("é", "e")
    word = word.replace("í", "i")
    word = word.replace("ó", "o")
    word = word.replace("ú", "u")
    word = word.replace("ü", "u")
    return word

def actualizar_tablero(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra
    return tablero

def run():
    data = []
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(line)
    
    data = [x[:-1] for x in data]
    data = [normalize(x) for x in data]
    palabra = r.choice(data)
    winword = ""
    count = 0
    base = ["_"] * len(palabra)
    while len(winword) < len(palabra):
        interface()
        print(f"{base}   Palabra con  {len(palabra)}  letras")
        print(hpics.HANGMANPICS[count])
        letra = input("Ingresa una letra: ")
        if letra in palabra:
            winword += letra
            print("Ahí la llevas!")
            base = actualizar_tablero(letra, palabra, base)
        else:
            print("No está esa letra")
            count += 1
        if count == 6:
            print("Perdiste la palabra era: " + palabra)
            print(hpics.HANGMANPICS[count])
            break
        if len(winword) == len(palabra):
            print("***************G A N A S T E***************")
        time.sleep(2)
        os.system("cls")
    

if __name__ == "__main__":
    run()