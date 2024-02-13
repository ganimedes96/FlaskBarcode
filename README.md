# FlaskBarcode

FlaskBarcode é uma aplicação Python baseada em Flask que simplifica a gestão de inventário e rastreamento de produtos através da geração de códigos de barras. Com uma interface intuitiva, os usuários podem criar, visualizar e monitorar etiquetas de produtos de forma eficiente. Simplifique seu inventário com BarcodeBuddy!

## Configuração do Ambiente

1. Clone o repositório do projeto:


git clone https://github.com/seu-usuario/seu-projeto.git


2. Navegue até o diretório do projeto:

- cd seu-projeto

3. Instale as dependências utilizando pip:

- pip install -r requirements.txt



## Endpoints

O projeto possui os seguintes endpoints:

### 1. `/create_tag` (POST)

Este endpoint é responsável por criar uma nova tag com base no código do produto fornecido.

- **Método HTTP:** POST
- **Corpo da Requisição (JSON):**
  ```json
  {
    "product_code": "1244"
  }

- Resposta:
  - 200 OK: A tag foi criada com sucesso e um código de barras foi gerado.
  - 400 Bad Request: O corpo da requisição está ausente ou malformado.
  - 500 Internal Server Error: Ocorreu um erro ao processar a requisição.

    
## Testes Unitários
Os testes unitários são realizados utilizando o framework pytest. Eles estão localizados em diferentes diretórios dentro de src/ e podem ser executados da seguinte maneira:

`pytest -s -v`


## Executando o Projeto
Para executar o projeto, basta executar o arquivo run.py:

 `python run.py`

Isso iniciará o servidor Flask e o aplicativo estará disponível no endereço `http://localhost:3000` .




