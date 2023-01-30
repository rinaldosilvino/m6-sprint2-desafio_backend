# m6-sprint2-desafio_backend 

## Nome do projeto:

cnab_reader

## Projeto e Funcionalidades:

A aplicação tem como objetivo criar uma interface web que aceite upload de arquivos CNAB, normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

### Executando com o Docker:

# Clone do projeto

```
git clone git@github.com:rinaldosilvino/m6-sprint2-desafio_backend.git
```

### Requisito:

Docker

### Inicie o projeto
```
docker compose up --build

```
#### Para acessar a API coloque o end point
```
http://127.0.0.1:8000/api/cnab/
```

### Caso não tenha o docker instalado, siga as instruções abaixo

### Executando com o python

## Tecnologias utilizadas:

Python
Django
Djangorestframework
Streamlit

## Instalação:

# Criação de ambiente virtual
```
python -m venv venv
```

# Iniciando ambiente virtual

(Windows)
```
.\venv\Scripts\activate
```

(Linux)
```
source venv/bin/activate
```

# Instalação de dependencias

```
pip install -r requirements.txt
```

# Execução de Migrations

```
python manage.py migrate
```

# Execução de Servidor

```
python manage.py runserver
```