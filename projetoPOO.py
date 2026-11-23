class Cliente:
    def __init__(self, nome, cpf, telefone, email):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_email(email)

    # Getters
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    # Setters com Validação
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            self.__nome = nome.strip()
        else:
            print(f"Erro de Validação: Nome '{nome}' é inválido.")
            self.__nome = "Nome Inválido"

    def set_cpf(self, cpf):
        if isinstance(cpf, str) and len(cpf.strip()) >= 11:
            self.__cpf = cpf.strip()
        else:
            print(f"Erro de Validação: CPF '{cpf}' inválido.")
            self.__cpf = "000.000.000-00"

    def set_telefone(self, telefone):
        if isinstance(telefone, str) and len(telefone.strip()) >= 8:
            self.__telefone = telefone.strip()
        else:
            print(f"Erro de Validação: Telefone '{telefone}' inválido.")
            self.__telefone = "(00) 0000-0000"

    def set_email(self, email):
        if isinstance(email, str) and "@" in email and "." in email and len(email.strip()) >= 5:
            self.__email = email.strip()
        else:
            print(f"Erro de Validação: E-mail '{email}' inválido.")
            self.__email = "email@invalido.com"


class Produto:
    def __init__(self, nome, preco):
        self.set_nome(nome)
        self.set_preco(preco)

    # Getters
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    # Setters com Validação
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            self.__nome = nome.strip()
        else:
            print(f"Erro de Validação: Nome do produto '{nome}' é inválido.")
            self.__nome = "Produto Inválido"

    def set_preco(self, preco):
        if isinstance(preco, (int, float)) and preco >= 0:
            self.__preco = float(preco)
        else:
            print(f"Erro de Validação: Preço '{preco}' inválido.")
            self.__preco = 0.0


# ==============================================================================
# TESTE DE VALIDAÇÃO DO PROJETO FINAL
# ==============================================================================
if __name__ == "__main__":
    print("=== TESTANDO AS CLASSES DO PROJETO FINAL ===\n")
    
    
    print("--- Testando Classe Cliente ---")
    cliente_valido = Cliente("Maria Silva", "123.456.789-09", "(11) 98888-7777", "maria@email.com")
    print(f"Cliente Criado: {cliente_valido.get_nome()} | E-mail: {cliente_valido.get_email()}")
    
    print("\nTentando cadastrar cliente com dados inválidos:")
    cliente_invalido = Cliente("Ab", "123", "12", "emailsemarroba")
    print(f"Resultado seguro -> Nome: {cliente_invalido.get_nome()} | Tel: {cliente_invalido.get_telefone()}")

    
    print("\n--- Testando Classe Produto ---")
    produto_valido = Produto("Cheesecake de Morango", 60.00)
    print(f"Produto Criado: {produto_valido.get_nome()} - R$ {produto_valido.get_preco():.2f}")
    
    print("\nTentando cadastrar produto com preço negativo:")
    produto_invalido = Produto("Pão de Queijo", -10.00)
    print(f"Resultado seguro -> Preço: R$ {produto_invalido.get_preco():.2f}")
