class Pessoa:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def exibir_dados(self):
        return f"Nome: {self.nome} | CPF: {self.cpf}"


class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, email):
        super().__init__(nome, cpf, telefone, email)

    # Sobrescrita de método
    def exibir_dados(self):
        return f"CLIENTE: {self.nome} | CPF: {self.cpf} | E-mail: {self.email}"


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, email, cargo):
        super().__init__(nome, cpf, telefone, email)
        self.cargo = cargo

    # Sobrescrita de método
    def exibir_dados(self):
        return f"FUNCIONÁRIO: {self.nome} | Cargo: {self.cargo}"


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_dados(self):
        return f"PRODUTO: {self.nome} | Preço: R$ {self.preco:.2f}"


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

if __name__ == "__main__":

    cliente = Cliente(
        "Maria Silva",
        "123.456.789-09",
        "(11) 98888-7777",
        "maria@email.com"
    )

    funcionario = Funcionario(
        "João Silva",
        "987.654.321-00",
        "(11) 97777-6666",
        "joao@email.com",
        "Gerente"
    )

    produto = Produto("Cheesecake de Morango", 60.00)

    # Lista heterogênea: objetos de classes diferentes
    cadastro = [cliente, funcionario, produto]


    # Polimorfismo: mesmo método, comportamentos diferentes
    for item in cadastro:
        print(item.exibir_dados())


