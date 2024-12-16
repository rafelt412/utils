import pandas as pd
def banco_de_comidas():
    """
    Lê um arquivo de texto contendo uma lista de comidas e retorna um DataFrame do pandas.
    Returns:
        pd.DataFrame: Um DataFrame com uma coluna 'comida' contendo cada comida do arquivo.
    """
    # Abre o arquivo 'dados.txt' no modo de leitura
    with open("dados.txt", "r") as file:
        # Lê todas as linhas do arquivo
        lines = file.readlines()
        # Remove espaços em branco e cria uma lista de comidas
        comidas = [line.strip() for line in lines]
        # Cria um DataFrame do pandas com a lista de comidas
        df = pd.DataFrame(comidas, columns=["comida"])
        return df
def validar_animal(animal):
    """
    Valida o nome do animal de acordo com critérios específicos.
    Args:
        animal (str): O nome do animal a ser validado.
        
    Returns:
        bool: True se o nome do animal for válido, False caso contrário.
    """
    while True:
        # Verifica se o nome do animal não está vazio
        if not animal:
            print("Não deixe o animal em branco.")
            return False
        
        # Verifica se o nome do animal é uma string
        if not isinstance(animal, str):
            print("erro: O nome do animal deve ser uma string.")
            return False
        
        # Verifica se o nome do animal excede 10 caracteres
        if len(animal) > 10:
            print("erro: O nome do animal deve ter no maximo 10 caracteres.")
            return False
        
        # Verifica se o nome do animal contém números
        if any(char.isdigit() for char in animal):
            print("erro: O nome do animal nao pode conter numeros.")
            return False
        
        # Se todas as verificações passarem, retorna True
        return True
