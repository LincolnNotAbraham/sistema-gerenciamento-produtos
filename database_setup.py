import sqlite3
import os

def criar_banco_dados():
    """
    Cria o banco de dados e as tabelas necessárias caso não existam.
    Esta função deve ser chamada antes de usar o sistema.
    """
    
    # Conecta ao banco (cria o arquivo se não existir)
    conexao = sqlite3.connect("ProjetoCompras.db")
    cursor = conexao.cursor()
    
    try:
        # Cria a tabela de usuários se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Usuario TEXT NOT NULL UNIQUE,
                Senha TEXT NOT NULL
            )
        ''')
        
        # Cria a tabela de produtos se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Produtos (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USER_ID INTEGER NOT NULL,
                NomeProduto TEXT NOT NULL,
                Categoria TEXT,
                Descrição TEXT,
                Data TEXT,
                Preço REAL NOT NULL,
                FOREIGN KEY (USER_ID) REFERENCES usuarios(ID)
            )
        ''')
        
        # Salva as alterações
        conexao.commit()
        print("✅ Banco de dados criado/verificado com sucesso!")
        
        # Verifica se existem usuários, se não, cria um usuário padrão
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        total_usuarios = cursor.fetchone()[0]
        
        if total_usuarios == 0:
            # Cria um usuário padrão para teste
            cursor.execute("INSERT INTO usuarios (Usuario, Senha) VALUES (?, ?)",
                         ("admin", "123"))
            conexao.commit()
            print("👤 Usuário padrão criado: admin / senha: 123")

        
    except sqlite3.Error as e:
        print(f"❌ Erro ao criar banco de dados: {e}")
    
    finally:
        cursor.close()
        conexao.close()
    
    return True

def verificar_banco_existe():
    """Verifica se o arquivo do banco de dados existe"""
    return os.path.exists("ProjetoCompras.db")

if __name__ == "__main__":
    # Se executar este arquivo diretamente, cria o banco
    criar_banco_dados()
