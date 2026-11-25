import re


class Pessoa:
    def __init__(self, nome, cpf, telefone, email):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_email(email)

    # GETTERS
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    @staticmethod
    def _cpf_valido(digitos):
        if len(digitos) != 11 or digitos == digitos[0] * 11:
            return False

        for quantidade in (9, 10):
            soma = sum(
                int(digitos[indice]) * (quantidade + 1 - indice)
                for indice in range(quantidade)
            )
            digito = (soma * 10) % 11
            if digito == 10:
                digito = 0
            if int(digitos[quantidade]) != digito:
                return False

        return True

    # SETTERS COM VALIDAÇÃO
    @staticmethod
    def _validar_nome(nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            return nome.strip()
        raise ValueError("O nome deve possuir pelo menos 3 caracteres.")

    def set_nome(self, nome):
        self.__nome = self._validar_nome(nome)

    @classmethod
    def _validar_cpf(cls, cpf):
        if isinstance(cpf, str):
            cpf_limpo = cpf.strip()
            digitos = "".join(
                caractere for caractere in cpf_limpo if caractere.isdecimal()
            )
            formato_valido = all(
                caractere.isdecimal() or caractere in ".- "
                for caractere in cpf_limpo
            )
            if len(digitos) == 11 and formato_valido and cls._cpf_valido(digitos):
                return cpf_limpo
        raise ValueError("CPF inválido. Informe um CPF válido de 11 dígitos.")

    def set_cpf(self, cpf):
        self.__cpf = self._validar_cpf(cpf)

    @staticmethod
    def _validar_telefone(telefone):
        if isinstance(telefone, str):
            telefone_limpo = telefone.strip()
            digitos = "".join(
                caractere for caractere in telefone_limpo if caractere.isdecimal()
            )
            formato_valido = all(
                caractere.isdecimal() or caractere in " ()+-."
                for caractere in telefone_limpo
            )
            if len(digitos) >= 8 and formato_valido:
                return telefone_limpo
        raise ValueError("Telefone inválido. Informe pelo menos 8 dígitos.")

    def set_telefone(self, telefone):
        self.__telefone = self._validar_telefone(telefone)

    @staticmethod
    def _validar_email(email):
        email = email.strip() if isinstance(email, str) else ""
        if re.fullmatch(r"[^@\s]+@[^@\s.]+(?:\.[^@\s.]+)+", email):
            return email
        raise ValueError("Informe um e-mail válido.")

    def set_email(self, email):
        self.__email = self._validar_email(email)


    def exibir_dados(self):
        return (
            f"Nome: {self.get_nome()} | "
            f"CPF: {self.get_cpf()} | "
            f"Telefone: {self.get_telefone()} | "
            f"E-mail: {self.get_email()}"
        )


class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, email):
        super().__init__(nome, cpf, telefone, email)
    # OVERRIDING
    def exibir_dados(self):
        return (
            f"[CLIENTE] {self.get_nome()} | "
            f"CPF: {self.get_cpf()} | "
            f"E-mail: {self.get_email()}"
        )


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, email, cargo):
        super().__init__(nome, cpf, telefone, email)
        self.set_cargo(cargo)

    # GETTER
    def get_cargo(self):
        return self.__cargo
    
    # SETTER
    @staticmethod
    def _validar_cargo(cargo):
        if isinstance(cargo, str) and len(cargo.strip()) >= 2:
            return cargo.strip()
        raise ValueError("Informe um cargo válido.")

    def set_cargo(self, cargo):
        self.__cargo = self._validar_cargo(cargo)

    # OVERRIDING
    def exibir_dados(self):
        return (
            f"[FUNCIONÁRIO] {self.get_nome()} | "
            f"CPF: {self.get_cpf()} | "
            f"Cargo: {self.get_cargo()}"
        )


class Produto:
    def __init__(self, nome, preco):
        self.set_nome(nome)
        self.set_preco(preco)


    # GETTERS
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    # SETTERS COM VALIDAÇÃO
    @staticmethod
    def _validar_nome(nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            return nome.strip()
        raise ValueError("Nome do produto inválido.")

    @staticmethod
    def _validar_preco(preco):
        if (
            isinstance(preco, (int, float))
            and not isinstance(preco, bool)
            and preco >= 0
        ):
            return float(preco)
        raise ValueError("O preço deve ser um número positivo ou zero.")

    def set_nome(self, nome):
        self.__nome = self._validar_nome(nome)

    def set_preco(self, preco):
        self.__preco = self._validar_preco(preco)

    def exibir_dados(self):
        return (
            f"[PRODUTO] {self.get_nome()} | "
            f"Preço: R$ {self.get_preco():.2f}"
        )


cadastros = []


def _ler_resposta(prompt, validar):
    while True:
        resposta = input(prompt)
        try:
            return validar(resposta)
        except ValueError as erro:
            print(f"Resposta inválida: {erro}")


def _validar_preco_digitado(preco):
    try:
        preco = float(preco)
    except ValueError:
        raise ValueError("Informe um preço válido.")
    return Produto._validar_preco(preco)


def cadastrar_cliente():
    print("\n--- CADASTRO DE CLIENTE ---")

    nome = _ler_resposta("Nome: ", Pessoa._validar_nome)
    cpf = _ler_resposta("CPF: ", Pessoa._validar_cpf)
    telefone = _ler_resposta("Telefone: ", Pessoa._validar_telefone)
    email = _ler_resposta("E-mail: ", Pessoa._validar_email)

    cliente = Cliente(nome, cpf, telefone, email)

    cadastros.append(cliente)
    print("Cliente cadastrado com sucesso!")


def cadastrar_funcionario():
    print("\n--- CADASTRO DE FUNCIONÁRIO ---")

    nome = _ler_resposta("Nome: ", Pessoa._validar_nome)
    cpf = _ler_resposta("CPF: ", Pessoa._validar_cpf)
    telefone = _ler_resposta("Telefone: ", Pessoa._validar_telefone)
    email = _ler_resposta("E-mail: ", Pessoa._validar_email)
    cargo = _ler_resposta("Cargo: ", Funcionario._validar_cargo)

    funcionario = Funcionario(nome, cpf, telefone, email, cargo)

    cadastros.append(funcionario)
    print("Funcionário cadastrado com sucesso!")


def cadastrar_produto():
    print("\n--- CADASTRO DE PRODUTO ---")

    nome = _ler_resposta("Nome do produto: ", Produto._validar_nome)
    preco = _ler_resposta("Preço: R$ ", _validar_preco_digitado)
    produto = Produto(nome, preco)

    cadastros.append(produto)
    print("Produto cadastrado com sucesso!")


def listar_cadastros():
    if len(cadastros) == 0:
        print("\nNenhum cadastro encontrado.")
        return

    print("\n--- LISTA DE CADASTROS ---")

    quantidade = 0

    for item in cadastros:
        print(item.exibir_dados())
        quantidade += 1

    print(f"\nTotal de cadastros: {quantidade}")


def consultar_cadastro():
    if len(cadastros) == 0:
        print("\nNão existem cadastros para consultar.")
        return

    try:
        print("\n--- CONSULTAR CADASTRO ---")

        posicao = int(input("Digite a posição do cadastro (1, 2, 3...): "))

        if posicao < 1:
            raise IndexError

        cadastro = cadastros[posicao - 1]

        print("\nCadastro encontrado:")
        print(cadastro.exibir_dados())

    except ValueError:
        print("Digite apenas números para consultar.")

    except IndexError:
        print("Cadastro não encontrado. Verifique a posição informada.")


def relatorio_produtos():

    total = 0.0
    quantidade = 0

    for item in cadastros:
        if isinstance(item, Produto):
            total += item.get_preco()
            quantidade += 1
            
    print("\n--- RELATÓRIO DE PRODUTOS ---")

    print(f"Quantidade de produtos: {quantidade}")
    print(f"Valor total dos produtos: R$ {total:.2f}")

    try:
        media = total / quantidade
        print(f"Preço médio dos produtos: R$ {media:.2f}")

    except ZeroDivisionError:
        print("Não existem produtos para calcular a média.")


def menu_principal():
    while True:

        print("\n================================")
        print("       SISTEMA DE CADASTRO")
        print("================================")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Funcionário")
        print("3 - Cadastrar Produto")
        print("4 - Listar Cadastros")
        print("5 - Consultar Cadastro")
        print("6 - Relatório de Produtos")
        print("0 - Sair")
        print("================================")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        if opcao == 1:
            cadastrar_cliente()

        elif opcao == 2:
            cadastrar_funcionario()

        elif opcao == 3:
            cadastrar_produto()

        elif opcao == 4:
            listar_cadastros()

        elif opcao == 5:
            consultar_cadastro()

        elif opcao == 6:
            relatorio_produtos()

        elif opcao == 0:
            print("\nSistema encerrado. Obrigado!")
            break

        else:
            print("Opção inválida! Escolha uma opção do menu.")

if __name__ == "__main__":
    menu_principal()