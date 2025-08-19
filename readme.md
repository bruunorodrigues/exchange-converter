# Conversor de Moeda - Python

Este é um simples conversor de moedas feito em Python que permite a conversão entre diferentes moedas utilizando a API de taxas de câmbio. O código recebe a moeda de origem, a moeda de destino e o valor a ser convertido, e retorna o valor convertido com base nas taxas de câmbio atuais.

## Funcionalidades

- **Entrada de Moeda**: O programa solicita ao usuário a moeda de origem (ex: USD, BRL, EUR) e a moeda de destino (ex: USD, BRL, EUR).
- **Conversão de Valor**: O usuário também informa o valor que deseja converter. O programa então consulta as taxas de câmbio em tempo real para realizar a conversão.
- **Validação de Entrada**: O código inclui validações para garantir que o valor e as moedas inseridas sejam válidos.
- **Limpeza de Tela**: O programa limpa a tela a cada nova entrada ou erro para melhorar a experiência do usuário.

## 🚀 Tecnologias Usadas

- **Python 3**: A linguagem de programação utilizada.
- **requests**: Para realizar requisições HTTP à API de taxas de câmbio.
- **API de Câmbio (exchangerate-api)**: A API é usada para obter as taxas de câmbio em tempo real.

## Arquivos

- **`app.py`**: O arquivo principal que executa a lógica de conversão de moeda.
- **`validation.py`**: Contém a função `valid_value` para validar o valor inserido pelo usuário.

## ⚙️ Como usar

Passo 1. Clone este repositório para a sua máquina;

Passo 2. Execute o arquivo app.py;

Passo 3. O programa irá solicitar que você insira a moeda de origem (ex: USD) e a moeda de destino (ex: BRL);

Passo 4. Em seguida, insira o valor que deseja converter;

Passo 5. O resultado será exibido com o valor convertido de acordo com as taxas de câmbio atuais.

### Pré-requisitos

1. Ter o Python 3.x instalado em sua máquina.
2. Instalar a biblioteca `requests`. Caso não tenha, instale com o seguinte comando:

   ```bash
   pip install requests
   
### LinkedIn

🔗 Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/bruno-rodrigues-923a61155)

   




