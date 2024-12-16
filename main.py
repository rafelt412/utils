import pandas as pd
def banco_comidas():
  with open("dados.txt", "r") as file:
    lines = file.readlines()
    comidas = [line.strip() for line in lines]
    df = pd.DataFrame(comidas, columns=["comida"])
    return df
def validar(animal):
    lista = 