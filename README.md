# Sistema de Gerenciamento de Produtos

Um sistema desktop simples para cadastro e gerenciamento de produtos usando Python, Tkinter e SQLite.

![Captura de tela 2025-06-30 223301](https://github.com/user-attachments/assets/f2111280-2d67-4d6a-9f40-675a2b198cac)

## 📋 Funcionalidades

- ✅ Sistema de login e cadastro de usuários
- ✅ Cadastro, edição e remoção de produtos
- ✅ Interface gráfica intuitiva
- ✅ Banco de dados SQLite (criado automaticamente)
- ✅ Filtros e pesquisa de produtos

## 🚀 Como usar

### Pré-requisitos

- Python 3.6 ou superior
- Tkinter (já incluído no Python)

### Instalação e execução

1. **Clone o repositório:**

   ```bash
   git clone [seu-repositório]
   cd sqlpython
   ```

2. **Execute o sistema:**

   ```bash
   python main.py
   ```

3. **Primeiro uso:**
   - O banco de dados será criado automaticamente na primeira execução
   - Um usuário padrão será criado: **admin** / senha: **123**
   - Você pode criar novos usuários usando a tela de cadastro
  


![Captura de tela 2025-06-30 223007](https://github.com/user-attachments/assets/46954f52-5baf-4759-b413-16612cacc7e8)

![Captura de tela 2025-06-30 223014](https://github.com/user-attachments/assets/7bf676f4-53c1-429a-933b-7061103f7466)

## 📁 Estrutura do projeto

```
sqlpython/
├── main.py              # Arquivo principal
├── login.py             # Tela de login
├── cadastro.py          # Tela de cadastro
├── novoproduto.py       # Tela de novo produto
├── user.py              # Gerenciamento de usuário
├── database_setup.py    # Configuração automática do banco
└── ProjetoCompras.db    # Banco de dados (criado automaticamente)
```

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Tkinter** - Interface gráfica
- **SQLite** - Banco de dados


![Captura de tela 2025-06-30 223035](https://github.com/user-attachments/assets/4e2e293d-5f2e-49fe-8885-aba9070af728)
![Captura de tela 2025-06-30 223307](https://github.com/user-attachments/assets/6431e51c-9d1f-4023-907d-2afec74a3d14)

## 📝 Como contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.
