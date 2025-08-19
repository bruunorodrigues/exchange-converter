# 💱 Conversor de Moedas (Currency Converter)

Um **conversor de moedas** simples feito em Python que permite converter valores entre diferentes moedas usando **taxas de câmbio em tempo real** da API [ExchangeRate API](https://www.exchangerate-api.com/).  

---

## 📌 Funcionalidades

- Consulta taxas de câmbio atualizadas.
- Conversão entre qualquer par de moedas suportadas.
- Validação de valores digitados pelo usuário (apenas números positivos).
- Interface limpa no terminal, com atualizações automáticas.
- Mensagens de erro amigáveis para moedas ou valores inválidos.

---

🧰 Tecnologias utilizadas

-Python 3.
-Biblioteca requests
-API pública de câmbio: https://api.exchangerate-api.com

## 🔹 Estrutura do Projeto

```
currency-converter/
│
├── app.py           # Script principal do conversor
├── validation.py    # Função para validar valores de entrada
└── README.md        # Este arquivo
```
---

## ▶️ Como usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/currency-converter.git
```

2. Entre na pasta do projeto:

```bash
cd currency-converter
```

3. Instale as dependências:

```bash
pip install requests
```

---

## ▶️ Como Executar

Execute o programa no terminal:

```bash
python app.py
```

Siga as instruções:

1. Digite a moeda de origem (ex: `USD`, `BRL`, `EUR`).
2. Digite a moeda de destino.
3. Digite o valor que deseja converter.

O resultado será exibido no terminal formatado com duas casas decimais.

---

## ✅ Exemplo de uso

```
Which is your exchange rate (ex: USD, BRL, EUR, etc)? USD
Which exchange rate do you want to convert to (ex: USD, BRL, EUR, etc)? BRL
Enter the amount you want to convert: 100

=== Currency Converter ===
100 USD = 514.50 BRL
```

## 🔹 API

- **ExchangeRate API**: [https://www.exchangerate-api.com/](https://www.exchangerate-api.com/)
- Sem necessidade de chave para uso básico.
- Fornece taxas de câmbio de mais de 160 moedas.

---

## 📄 Licença

Projeto livre para estudo e modificações.

---

## LinkedIn

Conecte-se comigo no: [Bruno Rodrigues](https://www.linkedin.com/in/bruno-rodrigues-923a61155)
