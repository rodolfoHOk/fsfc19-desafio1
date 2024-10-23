# Imersão FullStack & FullCycle 19 - Desafio 1

## Informações do desafio

Neste desafio, você deverá criar uma aplicação Django que simule um pequeno blog.
Teremos uma listagem de blogs em nosso blog.

Você deverá criar um app do Django com o nome core e os seguintes models:

Post
Dados: title, content, created_at, tags (um post tem uma ou várias tags e uma tag pode ter um ou vários posts)

Tag
Dados: name

Estes 2 models devem estar plugados no admin do Django.
Crie uma página com o path /blog e liste todos os posts e tags da aplicação.
Faça tudo com SQLite3 e acrescente no controle de versão com Git.
Precisa já ter cadastrado um usuário no admin com as seguintes credenciais: admin para o username, admin para a senha.
Envie a URL do seu repositório.

## Tecnologias utilizadas

- Python
- Django
- SQLite3

## Rodar

### Requerimentos

- Python 3.12
- export PIPENV_VENV_IN_PROJECT=1 dentro do .bashrc ou .zshrc

### Comandos

- pip install pipenv
- pipenv install
- pipenv shell
- python manage.py runserver

### Acessar o admin

- [http://localhost:8000/admin](http://localhost:8000/admin)
- username: admin
- password: admin
