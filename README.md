# Agenda de Contatos Django Python

Este repositório contém uma aplicação web desenvolvida em Django Python que implementa uma agenda de contatos completa. Com esta aplicação, você poderá gerenciar seus contatos, criar, visualizar, atualizar e excluir informações dos contatos de forma simples e intuitiva.

## Funcionalidades

A aplicação Agenda de Contatos Django Python possui as seguintes funcionalidades:

1. **Cadastro de Contatos:** Os usuários podem criar novos contatos, especificando o nome, número de telefone, endereço de e-mail e outras informações relevantes.

2. **Visualização de Contatos:** É possível visualizar todos os contatos da agenda em uma lista organizada, apresentando os principais detalhes de cada contato.

3. **Atualização de Contatos:** Caso ocorra alguma mudança nas informações de um contato, os usuários podem atualizá-lo facilmente através do formulário de edição.

4. **Exclusão de Contatos:** Os usuários podem remover contatos da agenda que não sejam mais necessários.

## Como executar o projeto

Para executar o projeto localmente em sua máquina, siga os passos abaixo:

1. **Pré-requisitos:**
   - Certifique-se de que você possui o Python instalado. Caso não tenha, você pode baixá-lo em [python.org](https://www.python.org/downloads/).
   - Instale o Django usando o gerenciador de pacotes do Python:
     ```
     pip install django
     ```

2. **Clone o repositório:**
   ```
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

3. **Acesse o diretório do projeto:**
   ```
   cd nome-do-repositorio
   ```

4. **Crie um ambiente virtual (recomendado):**
   ```
   python -m venv venv
   ```

5. **Ative o ambiente virtual:**
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - Linux / macOS:
     ```
     source venv/bin/activate
     ```

6. **Realize as migrações do banco de dados:**
   ```
   python manage.py migrate
   ```

7. **Inicie o servidor de desenvolvimento:**
   ```
   python manage.py runserver
   ```

8. **Acesse a aplicação:**
   Abra o navegador e visite [http://localhost:8000/](http://localhost:8000/)

## Contribuição

Se você deseja contribuir para este projeto, fique à vontade para enviar um pull request. Será um prazer receber novas funcionalidades, correções de bugs ou melhorias na aplicação.

Espero que esta aplicação seja útil para gerenciar seus contatos de forma eficiente e simplificada!
