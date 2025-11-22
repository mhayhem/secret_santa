# @Author Daniel Grande (Mhayhem)

import time
import os
import random

def random_friend(array: list):
    
    choice = random.choice(array)
    
    return choice

def get_participants_name():
    names = input("Separados por una coma, intriduce los nombres de los participantes en el amigo invisible\n")
    participants = [person.capitalize() for person in names.split(", ")]
    return participants

def secret_santa(array: list):
    selector = []
    
    while len(array) > 0:
        person = input("Escribe tu nombre:\n").capitalize()
        if person not in selector:
            secret_santa = random_friend(array)
            if secret_santa == person:
                print("No puedes ser tu amigo invisible, repetimos la seleccion")
                secret_santa = random_friend(array)
                continue
            else:
                selector.append(person)
                array.remove(secret_santa)
                print(f"{person} tu amigo invisible es: {secret_santa}.")
        else:
            print("Ya has elegido amigo invisible. LLama a otra persona.")
            continue
        print("En 3 segundos borraremos la pantalla, recuerda o apunta el nombre de tu amigo invisible.")
        time.sleep(3)
        os.system("clear")

def main():
    participants = get_participants_name()
    secret_santa(participants)

if __name__=="__main__":
    main()