from validate_docbr import CPF
import re
import os


class Validate:
    def valide_typeuser(self, typeuser):
        if (typeuser != 1 and typeuser != 2):
            print("É preciso informar se você é um cliente ou um funcionário!")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            return True

    def valide_name(self, name):
        validar = []

        for x in name:
            if (x not in validar):
                validar.append(x)

        if (len(name) == len(validar) or len(name) == len(validar) + 1
                or len(name) == len(validar) + 2):
            return True
        if (len(name) == 0):
            print("Você precisa inserir um nome!")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print(
                "Tem certeza que inseriu seu nome corretamente? Tente novamente"
            )
            os.system("cls" if os.name == "nt" else "clear")

    def valide_cpf(self, cpf):
        doc = CPF()
        valida = doc.validate("{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9],
                                                   cpf[9:]))
        if (valida == False):
            print("CPF inválido, tente novamente!")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            return True

    def valide_phone(self, phone):
        if (len(
                re.findall(
                    r"^\(?(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$",
                    phone)) == 1):
            return True
        else:
            print("Número de telefone inválido")

    def valide_email(self, email):
        min_len = 6
        max_len = 30
        min_upper_char = 1
        min_lower_char = 1
        msg = []

        if (len(re.findall(r"[a-zA-Z]", email)) < min_lower_char):
            msg.append("O email deve ter o mínimo um caracter alfabético!")
        if (len(email) < min_len):
            msg.append("Tamanho mínino de: {} caracteres".format(min_len))
        if (len(email) > max_len):
            msg.append("Tamanho máximo de: {} caracteres".format(max_len))
        if (len(re.findall(r"^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$", email))
                != 1):
            msg.append(
                "Endereço do provedor informado está incorreto ou é inválido!")

        if (len(msg) >= 1):
            print("\n".join(msg))
            os.system("cls" if os.name == "nt" else "clear")
        else:
            return True

    def valide_password(self, password):
        min_number = 1
        min_upper_char = 1
        min_lower_char = 1
        min_special_char = 1
        min_len = 6
        max_len = 20

        msg = []

        if (len(password) < min_len):
            msg.append("Tamanho mínino de: {} caracteres".format(min_len))
        if (len(password) > max_len):
            msg.append("Tamanho máximo de: {} caracteres".format(max_len))
        if (len(re.findall(r"[A-Z]", password)) < min_upper_char):
            msg.append("Precisa conter no mínimo {} letra maiúscula!".format(
                min_upper_char))
        if (len(re.findall(r"[a-z]", password)) < min_lower_char):
            msg.append("Precisa conter no mínimo {} letra minúscula!".format(
                min_lower_char))
        if (len(re.findall(r"[0-9]", password)) < min_upper_char):
            msg.append(
                "Precisa conter no mínimo {} número!".format(min_number))
        if (len(re.findall(r"[@#$_%&*+-=/]", password)) < min_lower_char):
            msg.append("Precisa conter no mínimo {} caracter especial!".format(
                min_special_char))

        if (len(msg) >= 1):
            print("\n".join(msg))
            os.system("cls" if os.name == "nt" else "clear")
        else:
            return True

    def valide_accept(self, agreement):
        if (agreement != 1):
            print(
                "Para continuar é necessário que você aprove o termo de acordo!"
            )
            os.system("cls" if os.name == "nt" else "clear")
        else:
            return True
