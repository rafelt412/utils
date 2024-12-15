import pandas as pd
def banco_comidas():
  with open("dados.txt", "r") as file:
    lines = file.readlines()
    comidas = [line.strip() for line in lines]
    df = pd.DataFrame(comidas, columns=["comida"])
    return df
def criar_animal():
    lista = []
    for _ in range(0,5):
        animal = input("Digite o nome de um animal: ")
        lista.append(animal)
    print(lista)
criar_animal()