import sqlite3
import tkinter as tk
from tkinter import messagebox
import cadastro
import login
import user
from tkinter import ttk
import novoproduto
import database_setup



def atualizar_tabela(tree):
    
    for item in tree.get_children():
        tree.delete(item)
    # Busca os dados atualizados
    cursor.execute("select * from Produtos where USER_ID = ?", (user.id,))
    dados = cursor.fetchall()
    # Insere os dados na tabela
    for linha in dados:
        tree.insert("", tk.END, values=linha[2:], iid =linha[0] )


def novo_produto(tree):
    novoproduto.novo(conexao, lambda: atualizar_tabela(tree))



def remover_item(tree):
    item = tree.selection()[0]
    id_produto = item  # Já é o ID do banco
    cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id_produto,))
    conexao.commit()
    atualizar_tabela(tree)

def menu_direito(event):

    
    item = tree.identify_row(event.y) 

    '''ao fazer q id=linha[0] todos os iten recebem um identificador, q nesse caos é ao id do sql'''

    if item:
        tree.selection_set(item)
        menu_contexto.post(event.x_root, event.y_root)

def editar_item(tree):

    itemsel = tree.selection()[0]
    valores = tree.item(itemsel, 'values')

    
    janela = tk.Toplevel()
    largura = 400
    altura = 320
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

    janela.title("Editar Produto")

    janela.configure(bg="#f5f5f5")
    


    # Labels e Entrys alinhados
    tk.Label(janela, text="Nome do Produto:", font=("Arial", 12),
             bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=8, sticky="e")
    entry_nome = tk.Entry(janela, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=8)
    entry_nome.insert(0,valores[0])

    tk.Label(janela, text="Categoria:", font=("Arial", 12),
              bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=8, sticky="e")
    entry_cat = tk.Entry(janela, width=30)
    entry_cat.grid(row=1, column=1, padx=10, pady=8)
    entry_cat.insert(0, valores[1])


    tk.Label(janela, text="Descrição:", font=("Arial", 12),
              bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=8, sticky="e")
    entry_des = tk.Entry(janela, width=30)
    entry_des.grid(row=2, column=1, padx=10, pady=8)
    entry_des.insert(0, valores[2])


    tk.Label(janela, text="Data:", font=("Arial", 12),
              bg="#f5f5f5").grid(row=3, column=0, padx=10, pady=8, sticky="e")
    entry_dat = tk.Entry(janela, width=30)
    entry_dat.grid(row=3, column=1, padx=10, pady=8)
    entry_dat.insert(0, valores[3])

    tk.Label(janela, text="Preço:", font=("Arial", 12),
              bg="#f5f5f5").grid(row=4, column=0, padx=10, pady=8, sticky="e")
    entry_pre = tk.Entry(janela, width=30)
    entry_pre.grid(row=4, column=1, padx=10, pady=8)
    entry_pre.insert(0, valores[4])



    # Label para mensagens de erro (já criado, só atualiza o texto)
    lbl_erro = tk.Label(janela, text="", font=("Arial", 10),
                         fg="red", bg="#f5f5f5")
    lbl_erro.grid(row=5, column=0, columnspan=2)





    # Botões

    def salvar_edicao():

        nome = entry_nome.get()
        categoria = entry_cat.get()
        descricao = entry_des.get()
        data = entry_dat.get()
        preco = entry_pre.get()

        if nome == "" or preco == "":
            lbl_erro.config(text="Campo NOME ou PREÇO não pode ser vazio", fg="red")
            return
        try:
            float(preco)
        except ValueError:
            lbl_erro.config(text="Preço deve ser um número válido", fg="red")
            return

        cursor.execute(
            "UPDATE Produtos SET NomeProduto=?, Categoria=?, Descrição=?, Data=?, Preço=? WHERE ID=?",
            (nome, categoria, descricao, data, preco, itemsel)
        )
        conexao.commit()
        janela.destroy()
        atualizar_tabela(tree)

    btn_salvar = tk.Button(janela, text="Salvar", width=35, command=salvar_edicao)
    btn_salvar.grid(row=6, column=0, columnspan=2, padx=10, pady=(18, 5))

    btn_cancelar = tk.Button(janela, text="Cancelar", width=35, command=janela.destroy)
    btn_cancelar.grid(row=7, column=0, columnspan=2, padx=10, pady=5)




if __name__ == "__main__":

    # Verifica e cria o banco de dados se necessário
    if not database_setup.verificar_banco_existe():
        print("🔧 Banco de dados não encontrado. Criando...")
        database_setup.criar_banco_dados()
    
    conexao = sqlite3.connect("ProjetoCompras.db")
    cursor = conexao.cursor()


    
    login.tela_login(conexao)
   

    nome = user.nome
    user_id = user.id




    if user.aprovado == True:

        '''janela principal'''
        
        janela = tk.Tk()
        janela.title("Tela Principal")
        janela.state("zoomed") 
        janela.configure(bg="#F5f5f5")


        label_nome = tk.Label (janela, text="Produtos", font=("TkHeadingFont", 15), fg="blue", bg="#F0F8FF")
        label_nome.place(x = 400, y = 50)




        tk.Label(janela, text="Nome do Produto:", font=("Arial", 11), bg="#f5f5f5").place(x=30, y=10)
        entry_nome_pesquisa = tk.Entry(janela, width=25)
        entry_nome_pesquisa.place(x=170, y=13)

        # Descrição do Produto
        tk.Label(janela, text="Categoria do Produto:", font=("Arial", 11), bg="#f5f5f5").place(x=350, y=10)
        entry_cat_pesquisa = tk.Entry(janela, width=25)
        entry_cat_pesquisa.place(x=520, y=13)



        menu_barra = tk.Menu(janela)
        janela.config(menu=menu_barra)

        menu_arquivo = tk.Menu(menu_barra, tearoff=0)
        menu_barra.add_cascade(label="Arquivo", menu =menu_arquivo)

        menu_arquivo.add_command (label="Novo Produto", command= lambda: novo_produto(tree) )

        


        cursor.execute("select * from Produtos where USER_ID = ?", (user.id,))
        dados = cursor.fetchall()
        

        colunas =  [desc[0] for desc in cursor.description][2:]
        frame_tabela = tk.Frame(janela, bg="#F5f5f5")
        frame_tabela.place(x = 0, y = 80) 

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#f8f8f8",
                        foreground="black",
                        rowheight=28,
                        fieldbackground="#f8f8f8",
                        font=("Arial", 11))
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#e0e0e0")

        tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=15)
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=180, anchor="center")
        tree.pack(padx=10, pady=10)

        
        menu_contexto = tk.Menu(janela,tearoff=0) #oq sera aberto ao apertra com botaso direeito na linha 
        menu_contexto.add_command(label="Remover",command= lambda: remover_item(tree))
        menu_contexto.add_command(label="Editar",command= lambda: editar_item(tree))
       

        tree.bind("<Button-3>", menu_direito)
        tree.bind("<Double-1>", editar_item)
        

        btn_novo = tk.Button(janela, text="Novo", width=25, height=2, font=("Arial", 16), command=lambda: novo_produto(tree))
        btn_novo.place (x = 50, y = 580)

        btn_deletar = tk.Button(janela, text="Deletar", width=25, height=2, font=("Arial", 16), command=lambda: remover_item(tree))
        btn_deletar.place(x = 500, y = 580)


        atualizar_tabela(tree)



    
    
    
        janela.mainloop()
    
    
    
    conexao.close()  