class Cliente:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and len(valor.strip()) >= 3:
            self.__nome = valor.strip()
        else:
            self.__nome = "Inválido"


class Produto:
    def __init__(self, nome, preco):
        self.set_nome(nome)
        self.set_preco(preco)

    # Getters
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    # Setters com validações
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            self.__nome = nome.strip()
        else:
            print("Erro: Nome deve ter no mínimo 3 caracteres.")
            self.__nome = "Produto Inválido"

    def set_preco(self, preco):
        if isinstance(preco, (int, float)) and preco >= 0:
            self.__preco = float(preco)
        else:
            print("Erro: Preço não pode ser negativo.")
            self.__preco = 0.0

class Endereco:
    def __init__(self, cidade, cep, rua, numero):
        self.cidade = cidade
        self.cep = cep
        self.rua = rua
        self.numero = numero

objeto_valido = Produto("Cadeira Gamer", 850.00)
print(f"Objeto Criado: {objeto_valido.get_nome()} - R$ {objeto_valido.get_preco():.2f}")

# 2. Teste de Instanciação com dados INVÁLIDOS (Provando a validação no construtor)
print("\n--- Teste 1: Tentativa de criar com preço negativo ---")
objeto_invalido = Produto("Mesa", -150.00)
print(f"Resultado mantido com segurança: R$ {objeto_invalido.get_preco():.2f}")

print("\n--- Teste 2: Tentativa de criar um produto com nome inválido ---")
objeto_nome_invalido = Produto("AB", 120.00)
print(f"Nome do objeto protegido: {objeto_nome_invalido.get_nome()}")

# 3. Teste de alteração via Setter com dado INVÁLIDO
print("\n--- Teste 3: Tentativa de alterar o nome para um texto muito curto ---")
objeto_valido.set_nome("AB")
print(f"Nome do objeto protegido: {objeto_valido.get_nome()}")
