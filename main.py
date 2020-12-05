from usuario import Usuario
from cliente import Cliente
from time import sleep
import os

class Window:
    def main(self, usuarios):
        print("==================================")
        print("|                                |")
        print("|         PIZZARIA LUIGI         |")
        print("|                                |")
        print("==================================")
        resp = int(input("Seja bem-vindo! Escolha uma opção:\n<<1>> Logar\n<<2>> cadastrar\n<<3>> Sair\nRESPOSTA: "))

        if(resp == 1):
            os.system("cls" if os.name == "nt" else "clear")
            entrar = Usuario.logar(self)
            if(entrar == 1):
              os.system("cls" if os.name == "nt" else "clear")
              self.menu_funcionario()
            if(entrar == 2):
              os.system("cls" if os.name == "nt" else "clear")
              self.menu_cliente()
            if(entrar == False):
              Usuario.logar(self)
            os.system("cls" if os.name == "nt" else "clear")
            self.main(usuarios)
        elif(resp == 2):
            os.system("cls" if os.name == "nt" else "clear")
            Usuario.cadastrar(self, usuarios)
            sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            self.main(usuarios)
        elif(resp == 3):
            exit()
        else:
            print("Resposta inválida, tente novamente!")
            sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            self.main(usuarios)

    def menu_cliente(self):
        print("==================================")
        print("|                                |")
        print("|         PIZZARIA LUIGI         |")
        print("|         menu do cliente        |")
        print("==================================")
        resp = int(input("Seja bem-vindo! Escolha uma opção:\n<<1>> Alterar Dados\n<<2>> Fazer Pedido\n<<3>> Voltar a tela inicial\nRESPOSTA: "))
        
        if(resp == 1):
            os.system("cls" if os.name == "nt" else "clear")
            Usuario.alterarDados(self)
            os.system("cls" if os.name == "nt" else "clear")
            self.menu_cliente()
        elif(resp == 2):
            os.system("cls" if os.name == "nt" else "clear")
            Cliente.efetuarPedido(self)
            sleep(5)
            os.system("cls" if os.name == "nt" else "clear")
            self.menu_cliente()
        elif(resp == 3):
            os.system("cls" if os.name == "nt" else "clear")
            self.main(usuarios)
        else:
            print("Resposta inválida, tente novamente!")
            sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            self.menu_cliente()

    def menu_funcionario(self):
        print("==================================")
        print("|                                |")
        print("|         PIZZARIA LUIGI         |")
        print("|       menu do funcionário      |")
        print("==================================")
        resp = int(input("Seja bem-vindo! Escolha uma opção:\n<<1>> Alterar Dados\n<<2>> Fazer Pedido\n<<3>> Voltar a tela inicial\nRESPOSTA: "))
        
        if(resp == 1):
            os.system("cls" if os.name == "nt" else "clear")
            Usuario.alterarDados(self, usuarios)
            os.system("cls" if os.name == "nt" else "clear")
            self.menu_funcionario()
        elif(resp == 2):
            os.system("cls" if os.name == "nt" else "clear")
            Usuario.cadastrar(self, usuarios)
            os.system("cls" if os.name == "nt" else "clear")
            self.menu_funcionario()
        elif(resp == 3):
            os.system("cls" if os.name == "nt" else "clear")
            self.main(usuarios)
        else:
            print("Resposta inválida, tente novamente!")
            sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            self.menu_funcionario()

a = Window()
usuarios = {}
a.main(usuarios)