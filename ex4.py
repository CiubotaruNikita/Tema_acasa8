lista_siruri = input("Introdu o listă de șiruri de caractere separate prin spațiu: ").split()
for sir in lista_siruri:
    if sir.startswith('A'):
        continue
    print(sir)