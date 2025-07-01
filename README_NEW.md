# Sistema de Gerenciamento de Produtos

> Um sistema desktop intuitivo para gerenciamento de produtos com interface gráfica moderna usando Python e SQLite.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-green.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📸 Screenshots

*Sistema completo com autenticação de usuários e gestão de produtos*

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
  - Interface gráfica moderna com Tkinter
  - Menu de contexto (clique direito)
  - Validação em tempo real
  - Mensagens de erro amigáveis

- 🗄️ **Banco de Dados Automático**
  - Criação automática do banco SQLite
  - Estrutura otimizada com chaves estrangeiras
  - Usuário padrão para testes

## 🚀 Instalação e Uso

### Pré-requisitos

- Python 3.6 ou superior
- Tkinter (geralmente incluído com Python)

### Como executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/sistema-gerenciamento-produtos.git
   cd sistema-gerenciamento-produtos
   ```

2. **Execute o sistema**
   ```bash
   python main.py
   ```

3. **Primeiro acesso**
   - O banco de dados será criado automaticamente
   - Use o usuário padrão: **admin** / senha: **123**
   - Ou crie uma nova conta na tela de cadastro

## 📁 Estrutura do Projeto

```
sistema-gerenciamento-produtos/
├── 📄 README.md              # Documentação do projeto
├── 📄 .gitignore            # Arquivos ignorados pelo Git
├── 🐍 main.py               # Arquivo principal da aplicação
├── 🗄️ database_setup.py     # Configuração automática do banco
├── 🔐 login.py              # Sistema de autenticação
├── 👤 cadastro.py           # Cadastro de usuários
├── ➕ novoproduto.py        # Cadastro de produtos
├── 👤 user.py               # Gerenciamento de sessão
└── 🗄️ ProjetoCompras.db     # Banco SQLite (criado automaticamente)
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.6+** - Linguagem principal
- **Tkinter** - Interface gráfica nativa
- **SQLite3** - Banco de dados leve e eficiente
- **ttk** - Widgets modernos para interface

## 📊 Banco de Dados

### Estrutura das Tabelas

**👤 usuarios**
| Campo   | Tipo    | Descrição               |
|---------|---------|-------------------------|
| ID      | INTEGER | Chave primária (auto)   |
| Usuario | TEXT    | Nome do usuário (único) |
| Senha   | TEXT    | Senha do usuário        |

**📦 Produtos**
| Campo       | Tipo    | Descrição                    |
|-------------|---------|------------------------------|
| ID          | INTEGER | Chave primária (auto)        |
| USER_ID     | INTEGER | ID do usuário (FK)           |
| NomeProduto | TEXT    | Nome do produto              |
| Categoria   | TEXT    | Categoria do produto         |
| Descrição   | TEXT    | Descrição detalhada          |
| Data        | TEXT    | Data de cadastro             |
| Preço       | REAL    | Preço do produto             |

## 🎯 Como Usar

1. **Faça login** com suas credenciais ou use admin/123
2. **Cadastre produtos** através do menu ou botão "Novo"
3. **Edite produtos** clicando duas vezes ou menu de contexto
4. **Remova produtos** através do botão "Deletar" ou menu
5. **Filtre produtos** usando os campos de pesquisa

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add: nova funcionalidade'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Seu Nome**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)

## 🙏 Agradecimentos

- Comunidade Python pelo excelente suporte
- Documentação do Tkinter
- SQLite por ser um banco simples e eficiente

---


