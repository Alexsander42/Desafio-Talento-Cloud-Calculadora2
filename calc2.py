
def calculadora():
  while True:

      print("Escolha a operação:")
      print("1= Soma")
      print("2= Subtração")
      print("3= Multiplicação")
      print("4= Divisão")
      print("0= Sair")

      operacao = int(input("Qual a operação escolhida?? "))

      if operacao == 0:
        print('Saindo da calculadora')
        break
      elif operacao in range(1,5):

       num1 = int(input("Digite o primeiro número: "))
       num2 = int(input("Digite o segundo número: "))

      if operacao == '1':
            resultado = num1 + num2
      elif operacao == '2':
            resultado = num1 - num2
      elif operacao == '3':
            resultado = num1 * num2
      elif operacao == 4:
            resultado = num1 / num2 if num2 != 0 
            
            else "Erro: divisão por zero"
    
            print("Resultado:", resultado)
        else:
            print("Essa opção não existe. Tente novamente.")

calculadora() 

# Não consegui resolver o erro no final do código