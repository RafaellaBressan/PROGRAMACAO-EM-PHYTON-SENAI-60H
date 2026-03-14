import sqlite3
import tkinter as tk
from tkinter import messagebox


conexao = sqlite3.connect("leads.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
idade INTEGER,
email TEXT,
endereco TEXT,
trabalho TEXT,
graduacao TEXT
)
""")

conexao.commit()


def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    trabalho = entry_trabalho.get()
    graduacao = entry_graduacao.get()

    cursor.execute("""
    INSERT INTO leads (nome, idade, email, endereco, trabalho, graduacao)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, idade, email, endereco, trabalho, graduacao))

    conexao.commit()

    messagebox.showinfo("Sucesso", "Lead cadastrado!")

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_trabalho.delete(0, tk.END)
    entry_graduacao.delete(0, tk.END)


def listar():
    lista.delete(0, tk.END)

    cursor.execute("SELECT * FROM leads")

    for lead in cursor.fetchall():
        lista.insert(tk.END, lead)


janela = tk.Tk()
janela.title("Agência de Marketing - Leads")
janela.geometry("500x500")

tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Idade").pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

tk.Label(janela, text="Email").pack()
entry_email = tk.Entry(janela)
entry_email.pack()

tk.Label(janela, text="Endereço").pack()
entry_endereco = tk.Entry(janela)
entry_endereco.pack()

tk.Label(janela, text="Trabalho").pack()
entry_trabalho = tk.Entry(janela)
entry_trabalho.pack()

tk.Label(janela, text="Graduação").pack()
entry_graduacao = tk.Entry(janela)
entry_graduacao.pack()

tk.Button(janela, text="Cadastrar Lead", command=cadastrar).pack(pady=5)
tk.Button(janela, text="Mostrar Leads", command=listar).pack(pady=5)

lista = tk.Listbox(janela, width=70)
lista.pack(pady=20)

janela.mainloop()
