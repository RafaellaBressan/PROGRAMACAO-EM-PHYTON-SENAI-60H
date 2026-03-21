import sqlite3 # banco de dados
import tkinter as tk # interface 
from tkinter import messagebox # caixas de mensagens
from tkinter import ttk # interface grafica tb

def conectar():
    return sqlite3.connect('clientes.db')


def criar_tabela():
    conn = conectar()
    c= conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT,
        endereco TEXT
        )
    ''')
    conn.commit()
    conn.close()


# CREATE
def inserir_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    if nome and email:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO clientes(nome, email, telefone, endereco) VALUES(?,?,?,?)',
                  (nome, email, telefone, endereco))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Cliente cadastrado!')
        limpar_campos()
        mostrar_clientes()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO!')

# READ
def mostrar_clientes():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM clientes')
    dados = c.fetchall()
    for cliente in dados:
        tree.insert("", "end", values=cliente)
    conn.close()

# DELETE
def deletar_cliente():
    selecao = tree.selection()
    if selecao:
        id_cliente = tree.item(selecao)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM clientes WHERE id = ? ', (id_cliente,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'CLIENTE DELETADO')
        mostrar_clientes()

    else:
        messagebox.showerror('Aviso', 'Selecione um cliente')

# UPDATE 
def atualizar_cliente():
    selecao = tree.selection()
    if selecao:
        id_cliente = tree.item(selecao)['values'][0]

        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        endereco = entry_endereco.get()

        conn = conectar()
        c = conn.cursor()
        c.execute('''
            UPDATE clientes 
            SET nome=?, email=?, telefone=?, endereco=? 
            WHERE id=?
        ''', (nome, email, telefone, endereco, id_cliente))

        conn.commit()
        conn.close()

        messagebox.showinfo('Sucesso', 'Dados atualizados!')
        mostrar_clientes()
    else:
        messagebox.showwarning('Aviso', 'Selecione um cliente')

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

janela = tk.Tk()
janela.title('Sistema de Clientes')

tk.Label(janela, text='Nome').grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text='Email').grid(row=1, column=0)
entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1)

tk.Label(janela, text='Telefone').grid(row=2, column=0)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=2, column=1)

tk.Label(janela, text='Endereço').grid(row=3, column=0)
entry_endereco = tk.Entry(janela)
entry_endereco.grid(row=3, column=1)

tk.Button(janela, text='Cadastrar', command=inserir_cliente).grid(row=4, column=0)
tk.Button(janela, text='Atualizar', command=atualizar_cliente).grid(row=4, column=1)
tk.Button(janela, text='Deletar', command=deletar_cliente).grid(row=5, column=0)

colunas = ('ID', 'Nome', 'Email', 'Telefone', 'Endereço')
tree = ttk.Treeview(janela, columns=colunas, show='headings')
tree.grid(row=6, column=0, columnspan=2)

for col in colunas:
    tree.heading(col, text=col)

criar_tabela()
mostrar_clientes()

janela.mainloop()