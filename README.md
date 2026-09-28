# 🏪 Sistema de Gerenciamento de Produtos

> Um sistema desktop intuitivo para cadastro e gerenciamento de produtos usando Python, Tkinter e SQLite.

![Python](https://img.shields.io/badge/Python-3.6+-3776AB.svg?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57.svg?logo=sqlite&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📸 Screenshots

![Login](https://github.com/user-attachments/assets/46954f52-5baf-4759-b413-16612cacc7e8)

![Cadastro](https://github.com/user-attachments/assets/7bf676f4-53c1-429a-933b-7061103f7466)

![Principal](https://github.com/user-attachments/assets/f2111280-2d67-4d6a-9f40-675a2b198cac)

![Produtos](https://github.com/user-attachments/assets/4e2e293d-5f2e-49fe-8885-aba9070af728)

![Filtros](https://github.com/user-attachments/assets/6431e51c-9d1f-4023-907d-2afec74a3d14)

## ✨ Funcionalidades

- 🔐 **Sistema de Autenticação**
  - Login seguro com usuário e senha
  - Cadastro de novos usuários
  - Validação de dados

- 📦 **Gerenciamento de Produtos**
  - Cadastro de produtos com categoria, descrição, data e preço
  - Edição e remoção de produtos
  - Visualização em tabela organizada
  - Filtragem por usuário (cada usuário vê apenas seus produtos)

- 🎨 **Interface Intuitiva**
  - Interface gráfica com Tkinter
  - Menu de contexto (clique direito)
  - Validação em tempo real
  - Mensagens de erro amigáveis

- 🗄️ **Banco de Dados Automático**
  - Criação automática do banco SQLite
  - Estrutura otimizada com chaves estrangeiras

## 🚀 Instalação e Uso

### Pré-requisitos

- [Python 3.6+](https://www.python.org/downloads/)
- Tkinter (geralmente incluído com Python)

### Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/LincolnNotAbraham/sistema-gerenciamento-produtos.git
   cd sistema-gerenciamento-produtos
   ```

2. **Execute o sistema:**
   ```bash
   python main.py
   ```

3. **Primeiro acesso:**
   - O banco de dados será criado automaticamente na primeira execução
   - Use o usuário padrão: **admin** / senha: **123**
   - Ou crie uma nova conta na tela de cadastro

## 📁 Estrutura do Projeto

```
sistema-gerenciamento-produtos/
├── main.py               # Arquivo principal da aplicação
├── database_setup.py     # Configuração automática do banco
├── login.py              # Sistema de autenticação
├── cadastro.py           # Cadastro de usuários
├── novoproduto.py        # Cadastro de produtos
├── user.py               # Gerenciamento de sessão do usuário
└── ProjetoCompras.db     # Banco SQLite (criado automaticamente)
```

## 📊 Banco de Dados

### Tabela `usuarios`

| Campo    | Tipo    | Descrição               |
|----------|---------|-------------------------|
| ID       | INTEGER | Chave primária (auto)   |
| Usuario  | TEXT    | Nome do usuário (único) |
| Senha    | TEXT    | Senha do usuário        |

### Tabela `Produtos`

| Campo        | Tipo    | Descrição                    |
|--------------|---------|------------------------------|
| ID           | INTEGER | Chave primária (auto)        |
| USER_ID      | INTEGER | ID do usuário (FK)           |
| NomeProduto  | TEXT    | Nome do produto              |
| Categoria    | TEXT    | Categoria do produto         |
| Descrição    | TEXT    | Descrição detalhada          |
| Data         | TEXT    | Data de cadastro             |
| Preço        | REAL    | Preço do produto             |

## 🎯 Guia Rápido

1. **Faça login** com suas credenciais ou use admin/123
2. **Cadastre produtos** através do menu ou botão "Novo"
3. **Edite produtos** clicando duas vezes ou usando o menu de contexto
4. **Remova produtos** através do botão "Deletar" ou menu
5. **Filtre produtos** usando os campos de pesquisa

## 🛠️ Tecnologias Utilizadas

- **Python 3.6+** — Linguagem principal
- **Tkinter** — Interface gráfica nativa do Python
- **SQLite3** — Banco de dados leve e sem servidor

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes.

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Add: nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
