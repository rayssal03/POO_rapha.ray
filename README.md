# POO_rapha.ray

# SISTEMA DE CADASTRO

## 1. Sobre o projeto

O Sistema de Cadastro é uma aplicação desenvolvida em Python que permite cadastrar, consultar e listar clientes, funcionários e produtos. O projeto utiliza conceitos de Programação Orientada a Objetos (POO).

## 2. Integrantes
Rayssa e Raphaela

## 3. Tecnologias utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- Biblioteca `re` para validação de e-mail.

## 4. Arquitetura do projeto

O projeto está organizado em classes e funções:

- **Pessoa:** classe principal com dados pessoais e validações.
- **Cliente:** herda os atributos de Pessoa.
- **Funcionario:** herda de Pessoa e adiciona o cargo.
- **Produto:** armazena nome e preço.
- **Funções de cadastro:** realizam o registro de clientes, funcionários e produtos.
- **Funções de consulta:** permitem listar, consultar e gerar relatórios.
- **Menu principal:** controla as opções do sistema.

Os dados são armazenados temporariamente em uma lista chamada `cadastros`.

## 5. Como executar o projeto

**1. Instale o Python**

Baixe em: https://www.python.org/downloads/

**2. Salve o código**

Salve o arquivo com o nome `main.py`.

**3. Abra o terminal**

Acesse a pasta onde o arquivo está salvo.

**4. Execute o programa**

```bash
python main.py
```

No Windows, também é possível utilizar:

```bash
py main.py
```

**5. Utilize o menu**

Escolha uma das opções disponíveis:

- 1 – Cadastrar cliente
- 2 – Cadastrar funcionário
- 3 – Cadastrar produto
- 4 – Listar cadastros
- 5 – Consultar cadastro
- 6 – Relatório de produtos
- 0 – Sair

## 6. Observação

Os dados ficam armazenados apenas enquanto o programa está em execução. Ao encerrá-lo, os cadastros são perdidos.

**Projeto:** Sistema de Cadastro  
**Linguagem:** Python  
**Paradigma:** Programação Orientada a Objetos