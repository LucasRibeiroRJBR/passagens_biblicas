from tkinter import *
from tkinter import ttk
import customtkinter as ctk

root = CTk()

# Cria uma lista de opções
opcoes = ['Opção 1', 'Opção 2', 'Opção 3', 'Opção 4', 'Opção 5', 'Opção 6', 'Opção 7', 'Opção 8']

# Cria uma variável para armazenar a opção selecionada
opcao_selecionada = ctk.StringVar()

# Define a opção padrão
opcao_selecionada.set(opcoes[0])

# Cria o objeto OptionMenu e associa à variável opcao_selecionada
opcao_menu = ctk.CTkOptionMenu(root, opcao_selecionada, *opcoes)

# Cria um objeto Listbox com as mesmas opções
lista_opcoes = Listbox(root, selectmode=SINGLE)
for opcao in opcoes:
    lista_opcoes.insert(END, opcao)

# Cria uma barra de rolagem
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=lista_opcoes.yview)

# Configura o Listbox para usar a barra de rolagem
lista_opcoes.config(yscrollcommand=scrollbar.set)

# Coloca o OptionMenu e a barra de rolagem no frame usando grid()
opcao_menu.grid(row=0, column=0, sticky="ew")
scrollbar.grid(row=0, column=1, sticky="ns")
lista_opcoes.grid(row=0, column=0, sticky="nsew")

root.mainloop()
