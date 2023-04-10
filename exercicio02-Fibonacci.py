num_informado = int(input('Numero a ser procurado na sequencia: '))
a1 = 1
a2 = 1

if (num_informado == 1) or (num_informado == 2):
    print(f'O numero {num_informado} está na sequencia')
else:
    num_encontrado = False
    cont = 0
    while cont <= num_informado:
        sequencia = a1 + a2
        a2 = a1
        a1 = sequencia
        cont += 1
        if num_informado == sequencia:
            num_encontrado = True
            break
    if num_encontrado:
        print(f'O numero {num_informado} esta na sequencia Fibonacci')
    else:
        print(f'O numero {num_informado} nao esta na sequencia Fibonacci')
