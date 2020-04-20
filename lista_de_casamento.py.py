lista_conivdados = []

numero_de_convidados = int(input('Quantos convidados você quer para o casamento? '))
for contador in range(numero_de_convidados):
    nome_convidados = str(input('Digite o nome do convidado: '))
    lista_conivdados.append(nome_convidados.title())
    lista_conivdados.sort()
print(f'Sua lista de casamento em ordem alfabética {lista_conivdados}')
print('Deseja adiconar, remover, limpar a lista ou está finalizada a lista do seu casamento?')

while True:
    opcao = str(input('[adicionar] | [remover] | [limpar] [finalizar] '))

    if opcao == 'adicionar' or opcao == 'Adicionar':
        adionar_a_lista = str(input('Escreva o nome do convidado que queira adicionar: '))
        lista_conivdados.append(adionar_a_lista.title())
        print(f'Lista de casamento atualizada..')
        print(lista_conivdados)

    elif opcao == 'Remover' or opcao == 'remover':
        remover_da_lista = str(input('Qual o nome da pessoa que queira remover da lista? (escrava com a inicial em maiscúla) '))
        
        if remover_da_lista not in lista_conivdados:
            print('Nome não está na lista. ERROR')

        elif remover_da_lista in lista_conivdados:
            pessoa_removida = lista_conivdados.remove(remover_da_lista)
            print(f'{remover_da_lista} não faz mas parte da lista')
            print(f'Lista de casamento atualizada..')
            print(lista_conivdados)
    
    elif opcao == 'limpar' or opcao == 'Limpar':
        lista_conivdados.clear()
        print(f'Lista de casamento atualizada..')
        print('lista vazia.')
               
    elif opcao == 'finalizar' or opcao == 'Finalizar':
            print('Programa finaliaddo.')
            break

    else:
        print('Comando invalido. ERROR')