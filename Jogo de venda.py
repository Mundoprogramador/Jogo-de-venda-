import os 
import time
print("===============================")
print("se o jogo falhar na primeira vez\nporfavor entre de novo que ele vai funcionar")
print("================================")
time.sleep(6)
os.system("clear")
with open("saldo.txt", "r")as arquivo:
    mon= arquivo.read()
    if mon <= " ":
       with open("saldo.txt","w")as filee:
           filee.write("1")
           print("criando as configurações do jogo...")
           time.sleep(6)
           print("\naguarde estamos fazendo o passos finais do jogo para você...")
           time.sleep(6)
           print("\natenção o jogo ira da um erro de codigo\nmais nao se precupa e so você entrar de novo\nque o erro vai sair")
           time.sleep(8)
           arquivo.close()
saldo = float(mon)
while True:
    print("====="*2)
    print('''1- sanduíche//10 R$
2- Coca-Cola//3.50 R$
3- servejinha//5.00 R$
4- salgados//4.50 R$''')
    print("====================")
    print('''digite 123 para ganhar 20 R$\n 
digite 0 para sair''')
    print("================"*2)
    print("seu saldo é de",saldo)
    opcao=int(input("digite o número do pedido: "))
    if saldo <= -1:
       print("saldo insuficiente")
       time.sleep(5)
       ganho= input("deseja trabalhar para ganhar")
       if ganho !="sim"or ganho !="s":
          break
       if ganho =="sim" or ganho=="s":
          os.system("clear")
          print("vamos trabalhar...")
          time.sleep(3)
          print("aguarde estamos trabalhando....")
          time.sleep(5)
          print("finalizando o trabalho...")
          print("finalizado você ganhou 20 reias")
          time.sleep(5)
          saldo += 20
    if opcao== 1:
       saldo -= 10
       print(saldo)
       os.system("clear")
    if opcao== 2:
        saldo -= 3.50
        print(saldo)
        os.system("clear")
    if opcao== 3:
         saldo-= 5
         print(saldo)
         os.system("clear")
    if opcao== 4:
         saldo-= 4.50
         print(saldo)
         os.system("clear")
    elif opcao== 0:
        break
    if opcao ==123:
        os.system("clear")
        print("vamos trabalhar...")
        time.sleep(3)
        print("aguarde estamos trabalhando....")
        time.sleep(5)
        print("finalizando o trabalho...")
        print("finalizado você ganhou 20 reias")
        time.sleep(5)
        saldo += 20
print("fim da escolhas")
saldoo = saldo
with open("saldo.txt", "w")as arquivo:
    arquivo.write(str(saldoo))
