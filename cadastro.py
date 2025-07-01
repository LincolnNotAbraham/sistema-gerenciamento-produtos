
import tkinter as tk
from tkinter import messagebox
import login 

#conexao = sqlite3.connect("ProjetoCompras.db")
#cursor = conexao.cursor()

def tela_cadastro(conexao):


    cursor = conexao.cursor()

    def login2(conexao):
        janela.destroy()
        login.tela_login(conexao)
    
    def inserir_dados(nome, senha):


        if nome == "" or senha == "":
            messagebox.showerror("Erro", "Campo não pode ser vazio")   
            return

        for r in cursor.execute("SELECT Usuario FROM usuarios"):
            if nome == r[0]:
                messagebox.showerror("Erro", "Nome já cadastrado")
                return  

        else:
            try:
                cursor.execute("INSERT INTO usuarios (Usuario,Senha) VALUES (?,?)", (nome, senha))
                conexao.commit()
                messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")

            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao inserir dados: {e}")

        


    janela = tk.Tk()
    janela.title("Tela de cadastro")
    janela.configure(bg="#F5DEB3")
    largura = 400
    altura = 320
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

    label_nome = tk.Label (janela, text="Tela de Cadastro", font=("TkHeadingFont", 30), fg="Orange", bg="#F5DEB3")
    label_nome.place(x = 50, y = 30)

    label_nome = tk.Label (janela, text="Nome de Usuário:", font=("Arial", 15), fg="black", bg="#F5DEB3")
    label_nome.place(x = 170, y = 100)


    entry_nome = tk.Entry(janela)
    entry_nome.place(x = 170, y = 130)


    label_senha = tk.Label(janela, text="Senha:",    font=("Arial", 15), fg="black", bg="#F5DEB3")
    label_senha.place(x = 170, y = 160)

    entry_senha = tk.Entry(janela, show="*")
    entry_senha.place(x = 170, y = 200)







    btn_inserir = tk.Button (
        janela, 
        text="Inserir", 
        command= lambda: inserir_dados(entry_nome.get(), entry_senha.get()),
        width=20,    # largura em caracteres
        height=2 
        )

    btn_inserir.place(x = 170, y = 230)


    btn_cad = tk.Button (
        janela, 
        text="Login", 
        command= lambda: login2(conexao)
        )

    btn_cad.place(x = 20, y = 270)





    janela.mainloop()


