import os,platform,time,sys

def clearTerminal():
  if platform.system() == 'Linux':
    os.system('clear')
  elif platform.system() == 'Windows':
    os.system('cls')

def printMenu():
  print(f"1- Adicionar Contato \n2- Excluir Contato\n3- Listar todos os Contatos\n4- Alterar Contato\n5- Listar dados de um determinado contato\n6- Sair")

def timeMenu():
  time.sleep(1)
  clearTerminal()
  printMenu()  

def fecharListaContato():
  fecharLista = input('\nDeseja fechar informaçoes do contato? (S)im (N)ão: ').upper()
          
  while fecharLista != 'S':
    time.sleep(2)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    fecharLista = input('Deseja fechar informaçoes do contato? (S)im (N)ão: ').upper()
  
  timeMenu()
    
    
clearTerminal()
print("Agenda eletronica... ")

lista = []
temp = []

con = True
op = 0

printMenu()

while con:

  op = int(input('\nDigite a opção desejada: '))
  if op >= 1 and op <= 6:
    if op == 1:
      clearTerminal()
      temp.append(input("Digite o nome do contato: "))
      temp.append(input("Digite o número de telefone: "))
      temp.append(input("Digite nome da empresa: "))
      lista.append(temp[:])
      temp.clear()
      clearTerminal()
      print('Contato adicionado!')
      timeMenu()

    if op == 2:
      clearTerminal()
      if lista:
        pes = input('Digite o nome a excluir: ').lower()
        for i in range(len(lista)):
          sublista = lista[i]
          sublista2 = sublista[0]
          if sublista2.lower() == pes:
            del lista[i]
            clearTerminal()
            print("contato excluido!")
            timeMenu()
      else:
        print("Lista vazia. Tente novamente!")
        timeMenu()

    if op == 3:
      clearTerminal()
      if lista:
        for i in range(len(lista)):
          sublista = lista[i]
          print(f'\n{i+1}º Contato:\nNome: ', sublista[0])
          print('Telefone: ', sublista[1])
          print('Empresa: ', sublista[2])
          print('--------------------------------')
        
        fecharListaContato()
        
        clearTerminal()
        printMenu()
      else:
        print("Lista vazia. Tente novamente!")
        timeMenu()

    if op == 4:
      clearTerminal()
      if lista:
        pes = input('Digite o nome do contato a alterar: ').lower()

        for i in range(len(lista)):

          sublista = lista[i]
          if sublista[0].lower() == pes:
            indice = i
            sublista[0] = input("Novo nome: ")
            sublista[1] = input("Novo telefone: ")
            sublista[2] = input("Nova empresa: ")
            encontrado = True
            print("\nContato alterado!")
            timeMenu()


          else:
            print('Contato não localizado. Tente novamente!')
            timeMenu()
      else:
        print('Lista de contatos vazia. Tente novamente!')
        timeMenu()

    if op == 5:
      clearTerminal()
      if lista:
        pes = input('Digite o nome do contato do para buscar: ').lower()

        for i in range(len(lista)):

          sublista = lista[i]
          if sublista[0].lower() == pes:
            indice = i
            print('Nome: ', sublista[0])
            print('Telefone: ', sublista[1])
            print('Empresa: ', sublista[2])
          else: 
            print('Contato não localizado. Tente novamente!')
            timeMenu()

          fecharListaContato()

      else:
        print("Lista vazia. Tente novamente!")
        timeMenu()

    if op == 6:
      clearTerminal()
      print('Programa finalizado!')
      break

  else:
    print('Valor invalido!')
    timeMenu()