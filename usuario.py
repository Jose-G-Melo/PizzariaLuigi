from validate import Validate
import os
import time
import json

class Usuario:
    def __init__(self):
        self.typeuser = 0
        self.username = None
        self.cpf = None
        self.telefone = None
        self.email = None
        self.senha = None
        self.accept = 0

    def cadastrar(self, usuarios):
        print("Informe seus dados abaixo para fazer o cadastro!\n")
        self.typeuser = int(input("Tipo de usuário:\n<<1>> Funcionário\n<<2>> Cliente\n1 ou 2: "))
        self.username = input("\nNome (somente o primeiro nome): ")
        self.cpf = input("\nCPF (somente números): ")
        self.telefone = input("\nTelefone (DDD + número de telefone): ")
        self.email = input("\nE-mail (ex: usuario@example.com): ")
        self.senha = input("\nSenha: ")
        self.accept = int(input("\nVocê concorda com todos os Termos de Uso da aplicação?\n<<1>> Sim\n<<2>> Não\n1 ou 2: "))
        
        while(Validate.valide_typeuser(self, self.typeuser) != True):       
            self.typeuser = int(input("Tipo de usuário:\n<<1>> Funcionário\n<<2>> Cliente\n1 ou 2: "))
        while(Validate.valide_name(self, self.username) != True):       
            self.username = input("\nNome (somente o primeiro nome): ")
        while(Validate.valide_cpf(self, self.cpf) != True):
            self.cpf = input("\nCPF (somente números): ")
        while(Validate.valide_phone(self, self.telefone) != True):
            self.telefone = input("\nTelefone (DDD + número de telefone): ")
        while(Validate.valide_email(self, self.email) != True):
            self.email = input("\nE-mail (ex: usuario@example.com): ")
        while(Validate.valide_password(self, self.senha) != True):
            self.senha = input("\nSenha: ")
        while(Validate.valide_accept(self, self.accept) != True):
            self.accept = int(input("\nVocê concorda com todos os Termos de Uso da aplicação?\n<<1>> Sim\n<<2>> Não\n1 ou 2: "))
        
        if(Validate.valide_typeuser(self, self.typeuser) == True and Validate.valide_name(self, self.username) and Validate.valide_cpf(self, self.cpf) == True and Validate.valide_phone(self, self.telefone) == True and Validate.valide_email(self, self.email) == True and Validate.valide_password(self, self.senha) == True and Validate.valide_accept(self, self.accept) == True):
            print("Seu cadastro foi concluído com sucesso!")
            usuarios['typeuser'] = self.typeuser
            usuarios['name'] = self.username 
            usuarios['cpf'] = self.cpf 
            usuarios['phone'] = self.telefone
            usuarios['email'] = self.email
            usuarios['password'] = self.senha
            usuarios['agreement'] = self.accept
            with open("user.json", "a+", encoding="utf8") as json_file:
              json.dump(usuarios, json_file)
            time.sleep(2)

    def logar(self):
        print("Informe seu email e senha para fazer o login!\n")
        email_fornecido = input("E-mail (ex: usuario@example.com): ")
        senha_fornecida = input("\nSenha: ")
        with open("user.json") as json_file:
          user = json.load(json_file)
          email = user.get("email")
          senha = user.get("password")
          tipo = user.get("typeuser")
      
        if email_fornecido == email:
          if senha_fornecida == senha:
            print("Login realizado com sucesso!")
            return tipo
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
          else:
            print("Senha incorreta, tente novamente!")
            time.sleep(2)
            return False
        else:
            print("Email incorreto, tente novamente!")
            time.sleep(2)
            return False

    def alterarDados(self):

      with open("user.json") as json_file:
        user = json.load(json_file)
        email = user.get("email")
        senha = user.get("password")
        nome = user.get("name")
        tipo = user.get("typeuser")
        cpf = user.get("cpf")
        telefone = user.get("phone")
        accept = user.get("agreement")

      dado = int(input("Informe o dado que deseja alterar:\n<<1>> Nome\n<<2>> CPF\n<<3>> Telefone\n<<4>> E-mail\n<<5>> Senha\nRESPOSTA: "))

      if(dado == 1):
        nome_anterior = input("Digite o nome salvo anteriormente: ")
        if(nome_anterior == nome):
          self.username = input("\nNome (somente o primeiro nome): ")
          while(Validate.valide_name(self, self.username) != True):       
            self.username = input("\nNome (somente o primeiro nome): ")
          nome = self.username
      if(dado == 2):
        cpf_anterior = input("Digite o CPF salvo anteriormente: ")
        if(cpf_anterior == cpf):
          self.cpf = input("\nCPF (somente números): ")
          while(Validate.valide_cpf(self, self.cpf) != True):
              self.cpf = input("\nCPF (somente números): ")
          cpf = self.cpf
      if(dado == 3):
        telefone_anterior = input("Digite o telefone salvo anteriormente: ")
        if(telefone_anterior == telefone):
          self.telefone = input("\nTelefone (DDD + número de telefone): ")
          while(Validate.valide_phone(self, self.telefone) != True):
            self.telefone = input("\nTelefone (DDD + número de telefone): ")
          telefone = self.telefone
      if(dado == 4):
        email_anterior = input("Digite o email salvo anteriormente: ")
        if(email_anterior == email):
          self.email = input("\nE-mail (ex: usuario@example.com): ")
          while(Validate.valide_email(self, self.email) != True):
            self.email = input("\nE-mail (ex: usuario@example.com): ")
          email = self.email
      if(dado == 5):
        senha_anterior = input("Digite a senha salva anteriormente: ")
        if(senha_anterior == senha):
          self.username = input("\nNome (somente o primeiro nome): ")
          self.senha = input("\nSenha: ")
          while(Validate.valide_password(self, self.senha) != True):
            self.senha = input("\nSenha: ")
          senha = self.senha
      print("Alteração feita com sucesso!")
      usuarios = {
        'typeuser':tipo,
        'name':nome,
        'cpf':cpf,
        'phone':telefone,
        'email':email,
        'password':senha,
        'agreement':accept
      }
      with open("user.json", "w", encoding="utf8") as json_file:
        json.dump(usuarios, json_file)
      time.sleep(2)
