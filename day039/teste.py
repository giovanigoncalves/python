lista = []

numbers = int(input("Quantos números quer adicionar? ")) # Números a serem adicionados
for n in range(0, numbers): # Loop na quantidade de números adicionados
    valor = int(input("Digite um número: ")) # Valores digitados
    if n == 0: # Se for o primeiro número digitado, já adiciona na lista na única posição disponível
        lista.append(valor)
        print(f"Added in position {n}")
    else: # Se não for o primeiro número digitado ....
        i = 0 # Valor inicial para percorrer a lista até então
        while i < len(lista): # enquanto ainda na lista...
            if valor <= lista[i]: # Se o valor digitado for menor ou igual o da posição i...
                lista.insert(i, valor) # adiciona nessa posição
                print(f"Número adicionado na posição {i}")
                break # e interrompe o loop, se não pode ficar adicionando o número várias vezes
            elif valor > lista[-1]: # se não, se for maior que o último...
                lista.append(valor) # adiciona no final da lista
                print(f"Número adicionado na posição {len(lista) - 1}")
                break # e interrompe o loop
            i += 1 # Se nenhuma das duas condições forem satisfeitas, o i recebe um incremento.

print(lista)
