import tkinter as tk
from tkinter import messagebox
import cadastro
import user 
#conexao = sqlite3.connect("ProjetoCompras.db")
#cursor = conexao.cursor()




def tela_login(conexao):
 
    cursor = conexao.cursor()


    def cadastro2(conexao):
        janela.destroy()
        cadastro.tela_cadastro(conexao)
         




    def inserir_login():
            
       
        nome = entry_nome.get()
        senha = entry_senha.get()

        
        

        if nome.strip() == "" or senha.strip() == "":
            messagebox.showerror("Erro", "Campos não podem estar vazios")   
            return


        else:
            try:
                cursor.execute("select ID, Usuario from usuarios where Usuario = ? and Senha = ?",
                                (nome, senha))
                resultado = cursor.fetchone()

                if resultado is None:
                    messagebox.showerror("Erro", "Nome ou senha incorretos")
                    return
                
                else:
                    user.id = resultado[0]  # ID do usuário
                    user.nome = resultado[1]  # Nome do usuário
                    user.aprovado = True
                    janela.destroy()
                    

            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao inserir dados: {e}")


    janela = tk.Tk()
    janela.title("Tela de Login")
    janela.configure(bg="#F0F8FF")

    largura = 400
    altura = 320
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


    label_titulo = tk.Label (janela, text="Tela de Login", font=("TkHeadingFont", 30), fg="blue", bg="#F0F8FF")
    label_titulo.place(x = 50, y = 30)

    label_nome = tk.Label (janela, text="Nome de Usuário:", font=("Arial", 15), fg="black", bg="#F0F8FF")
    label_nome.place(x = 170, y = 100)


    entry_nome = tk.Entry(janela)
    entry_nome.place(x = 170, y = 130)


    label_senha = tk.Label(janela, text="Senha:",    font=("Arial", 15), fg="black", bg="#F0F8FF")
    label_senha.place(x = 170, y = 160)

    entry_senha = tk.Entry(janela, show="*")
    entry_senha.place(x = 170, y = 200)





    btn_inserir = tk.Button (
        janela, 
        text="Entrar", 
        command= inserir_login,   
        width=20,    # largura em caracteres
        height=2 
        )

    btn_inserir.place(x = 170, y = 230)

    btn_cad = tk.Button (
        janela, 
        text="Cadastrar", 
        command= lambda: cadastro2(conexao)
        )

    btn_cad.place(x = 20, y = 270)

    # Fechar cursor quando a janela for fechada
    def fechar_janela():
        cursor.close()
        janela.destroy()
    
    janela.protocol("WM_DELETE_WINDOW", fechar_janela)
    janela.mainloop()


