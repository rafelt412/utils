def teste(animal):
    if any(char.isdigit() for char in animal):
        print("A string contém números.")
    else:
        print("A string não contém números.")
teste(animal='snoopy 4 anos')