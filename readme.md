**💱 Conversor de Moedas (Currency Converter)**

Este é um aplicativo de conversão de moedas simples desenvolvido em Python. Ele permite converter valores entre diferentes moedas, utilizando uma API de taxas de câmbio atualizadas em tempo real.

---

📌 Funcionalidades

Conversão entre moedas como USD, EUR, BRL, etc.

Validação de entrada do usuário (moeda e valor).

Busca de taxas de câmbio em tempo real usando a API pública ExchangeRate-API

---

🧰 Tecnologias utilizadas

Python 3.

Biblioteca requests

API pública de câmbio: https://api.exchangerate-api.com

---

🗂️ Estrutura do Projeto
.
├── app.py              # Script principal da aplicação
├── validation.py       # Função para validação do valor inserido
└── README.md           # Este arquivo

---

▶️ Como usar

Clone o repositório:

git clone https://github.com/seu-usuario/conversor-moedas.git
cd conversor-moedas


Instale as dependências:

pip install requests


Execute o programa:

python app.py


Siga as instruções no terminal:

Insira o código da moeda de origem (ex: USD, BRL, EUR).

Insira o código da moeda de destino.

Digite o valor a ser convertido.

---

✅ Licença

Which is your exchange rate (ex: USD, BRL, EUR, etc)? USD
Which exchange rate do you want to convert to (ex: USD, BRL, EUR, etc)? BRL
Enter the amount you want to convert: 10
=== Currency Converter ===
10.0 USD = 55.23 BRL

---

⚠️ Observações

O terminal é limpo entre as interações para melhorar a experiência do usuário (uso de os.system('cls'), compatível com Windows).

A API utilizada pode ter limite de requisições por dia na versão gratuita.

---

### 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.

---

### LinkedIn

🔗 Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/bruno-rodrigues-923a61155)



