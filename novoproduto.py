import tkinter as tk
from tkinter import messagebox
import user
import main

def novo(conexao, callback = None):
    
    cursor = conexao.cursor()

    def commitar():
        nome = entry_nome.get()
        categoria = entry_cat.get()
        descricao = entry_des.get()
        data = entry_dat.get()
        preco = entry_pre.get()

        # Limpa mensagem anterior
        lbl_erro.config(text="")

        if nome == "" or preco == "":
            lbl_erro.config(text="Campo NOME ou PREÇO não pode ser vazio", fg="red")
            return
        try:
            float(preco)
        except ValueError:
            lbl_erro.config(text="Preço deve ser um número válido", fg="red")
            return

        cursor.execute(
            "INSERT INTO Produtos (USER_ID, NomeProduto, Categoria, Descrição, Data, Preço) VALUES (?, ?, ?, ?, ?, ?)",
            (user.id, nome, categoria, descricao, data, preco)
        )
        conexao.commit()
        janela.destroy()
        if callback:
            callback()


    janela = tk.Toplevel()
    largura = 400
    altura = 320
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

    janela.title("Cadastrar Produto")
    janela.resizable(False, False)
    janela.configure(bg="#f5f5f5")
    


    # Labels e Entrys alinhados
    tk.Label(janela, text="Nome do Produto:", font=("Arial", 12),
              bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=8, sticky="e")
    entry_nome = tk.Entry(janela, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(janela, text="Categoria:", font=("Arial", 12),
              bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=8, sticky="e")
    entry_cat = tk.Entry(janela, width=30)
    entry_cat.grid(row=1, column=1, padx=10, pady=8)

    tk.Label(janela, text="Descrição:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=8, sticky="e")
    entry_des = tk.Entry(janela, width=30)
    entry_des.grid(row=2, column=1, padx=10, pady=8)

    tk.Label(janela, text="Data:", font=("Arial", 12), bg="#f5f5f5").grid(row=3, column=0, padx=10, pady=8, sticky="e")
    entry_dat = tk.Entry(janela, width=30)
    entry_dat.grid(row=3, column=1, padx=10, pady=8)

    tk.Label(janela, text="Preço:", font=("Arial", 12), bg="#f5f5f5").grid(row=4, column=0, padx=10, pady=8, sticky="e")
    entry_pre = tk.Entry(janela, width=30)
    entry_pre.grid(row=4, column=1, padx=10, pady=8)

    # Label para mensagens de erro (já criado, só atualiza o texto)
    lbl_erro = tk.Label(janela, text="", font=("Arial", 10), fg="red", bg="#f5f5f5")
    lbl_erro.grid(row=5, column=0, columnspan=2)

    # Botões
    btn_salvar = tk.Button(janela, text="Salvar", width=35, command=commitar)
    btn_salvar.grid(row=6, column=0, columnspan=2, padx=10, pady=(18, 5))

    btn_cancelar = tk.Button(janela, text="Cancelar", width=35, command=janela.destroy)
    btn_cancelar.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

   # janela.mainloop()


