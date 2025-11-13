# 📚 Analisador Sintático com Django

![Status](https://img.shields.io/badge/Status-Concluído-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-darkgreen?logo=django&logoColor=white)

Sistema web desenvolvido em Django para catalogar e analisar a estrutura morfossintática de períodos. Este projeto demonstra a implementação da arquitetura MVT (Model-View-Template), modelagem de banco de dados relacional (ORM) e criação de um front-end dinâmico com DTL.

Este projeto foi desenvolvido como avaliação acadêmica e agora faz parte do meu portfólio de desenvolvimento web.

---

## Tabela de Conteúdos

* [Sobre o Projeto](#-sobre-o-projeto)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Screenshots do Projeto](#-screenshots-do-projeto)
* [Como Executar (Instalação)](#-como-executar-o-projeto)
* [Nota sobre o Desenvolvimento](#-nota-sobre-o-desenvolvimento)

---

## 🎯 Sobre o Projeto

O objetivo principal é "Desenvolver um sistema de banco de dados para catalogar orações e seus componentes sintáticos essenciais (sujeito, predicado) e morfológicos (tipo de oração)".

### Principais Funcionalidades

* **🗃️ Modelagem de Dados (3 Entidades):**
    * O `models.py` define 3 classes (`Periodo`, `Oracao`, `ComponenteSintatico`) que são traduzidas pelo ORM do Django em tabelas.
    * A hierarquia sintática é garantida pelo uso de `ForeignKey`, criando relacionamentos 1:N (Um-para-Muitos).

* **⚙️ Admin Hierárquico (CRUD):**
    * O painel de administração (`/admin`) foi configurado para ser a principal interface de **C**reate, **R**ead, **U**pdate e **D**elete (CRUD).
    * Utiliza a biblioteca `django-nested-admin` para permitir o cadastro aninhado das 3 entidades em uma única tela, refletindo visualmente a hierarquia do banco de dados.

* **🖥️ Front-End Dinâmico (MVT):**
    * Uma página inicial pública foi criada para "ler" (Read) os dados do banco.
    * A `views.py` busca todos os Períodos no banco e os envia para o template.
    * O `home.html` usa a **DTL (Django Template Language)** (`{% for ... %}`) para listar dinamicamente todos os períodos e seus componentes.
    * O design da página foi feito com **CSS** (arquivos `static`).

---

## ✨ Tecnologias Utilizadas

* **Python:** Linguagem principal do projeto.
* **Django:** Framework web para o backend, MVT e ORM.
* **Django-Nested-Admin:** Biblioteca para melhorar a interface do admin.
* **SQLite3:** Banco de dados padrão do Django, utilizado neste projeto.
* **HTML5:** Linguagem de marcação para o template.
* **CSS3:** Linguagem de estilização para o design do front-end.
* **Git & GitHub:** Para versionamento e hospedagem do código.

---


## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em um ambiente local.

### 1️⃣ Clonar o repositório
(Substitua pela URL do seu repositório no GitHub)
```bash
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd projeto_sintaxe
2️⃣ Criar e ativar o ambiente virtual
Bash

# Criar o ambiente
python -m venv .venv

# Ativar no Windows (PowerShell)
.venv\Scripts\activate
3️⃣ Instalar as dependências
Bash

pip install django django-nested-admin
4️⃣ Aplicar as migrações (Criar o banco)
Este comando cria o arquivo db.sqlite3 com todas as tabelas.

Bash

python manage.py makemigrations nucleo
python manage.py migrate
5️⃣ Criar um superusuário
Você precisará de um login e senha para acessar o painel de administração (/admin).

Bash

python manage.py createsuperuser
6️⃣ Executar o servidor
Bash

python manage.py runserver
7️⃣ Acessar o sistema
Página Inicial (Visualização): http://127.0.0.1:8000/

Painel Admin (CRUD): http://127.0.0.1:8000/admin/

🤖 Nota sobre o Desenvolvimento
Este projeto foi desenvolvido com o auxílio de IA (Gemini, do Google) para fins de depuração de código, otimização da estrutura e geração de documentação.