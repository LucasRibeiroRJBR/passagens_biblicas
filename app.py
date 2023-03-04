import customtkinter as ctk
import sqlite3
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)
        self.grid_columnconfigure(5,weight=1)

        self.lb_title = ctk.CTkFont(family='Trebuchet MS',size=48,weight='bold')
        self.lb_general = ctk.CTkFont(family='Trebuchet MS',size=18,weight='bold')
        self.lb_res = ctk.CTkFont(family='Trebuchet MS',size=24,weight='bold')

        self.img_biblia = ctk.CTkImage(Image.open('img/bible.png'),size=(64,64))

        self.letreiro = ctk.CTkLabel(master=self,text='   Consultar Bíblia',image=self.img_biblia,compound='left',font=self.lb_title)

        self.versoes_nomes = ['Almeida Corrigida e Fiel','Almeida Revista e Atualizada','Almeida Revista e Corrigida',
                              'Almeida Século XXI','Almeida Atualizada','King James Atualizada','King James Fiel',
                              'Nova Almeida Atualizada','Nova Bíblia Viva','Nova Tradução na Linguagem de Hoje',
                              'Nova Versão Internacional','Nova Versão Transformadora','Tradução Brasileira']
        
        self.livros = ['Gênesis','Êxodo','Levítico','Números','Deuteronômio','Josué','Juízes','Rute','1 Samuel',
                       '2 Samuel','1 Reis','2 Reis','1 Crônicas','2 Crônicas','Esdras','Neemias','Ester','Jó','Salmos',
                       'Provérbios','Eclesiastes','Cânticos','Isaías','Jeremias','Lamentações','Ezequiel','Daniel',
                       'Oséias','Joel','Amós','Obadias','Jonas','Miquéias','Naum','Habacuque','Sofonias','Ageu','Zacarias',
                       'Malaquias','Mateus','Marcos','Lucas','João','Atos dos Apóstolos','Romanos','1 Coríntios',
                       '2 Coríntios','Gálatas','Efésios','Filipenses','Colossenses','1 Tessalonicenses',
                       '2 Tessalonicenses','1 Timóteo','2 Timóteo','Tito','Filemom','Hebreus','Tiago','1 Pedro',
                       '2 Pedro','1 João','2 João','3 João','Judas','Apocalipse']
        
        self.vLivro = ctk.StringVar()
        self.vCapitulo = ctk.StringVar()
        self.vVersiculo = ctk.StringVar()
        self.vVersao = ctk.StringVar()

        self.lb_livro = ctk.CTkLabel(master=self,text='Livro',font=self.lb_general)
        self.in_livro = ctk.CTkOptionMenu(master=self,
                                             values=self.livros,
                                             variable=self.vLivro,                                             
                                             font=self.lb_general,
                                             corner_radius=12,
                                             width=200)

        self.lb_capitulo = ctk.CTkLabel(master=self,text='Capítulo',font=self.lb_general)
        self.in_capitulo = ctk.CTkEntry(master=self,textvariable=self.vCapitulo)
        self.lb_versiculo = ctk.CTkLabel(master=self,text='Versículo',font=self.lb_general)
        self.in_versiculo = ctk.CTkEntry(master=self,textvariable=self.vVersiculo)
        
        self.menu_versao = ctk.CTkOptionMenu(master=self,
                                             values=self.versoes_nomes,
                                             variable=self.vVersao,
                                             font=self.lb_general,
                                             corner_radius=12,
                                             width=380)

        self.bt_consultar = ctk.CTkButton(master=self,text='Consultar',font=self.lb_general,command=lambda: self.conectar(self.vVersao.get(),
                                                                                                     self.vLivro.get(),
                                                                                                     self.vCapitulo.get(),
                                                                                                     self.vVersiculo.get()))
        
        self.lb_res = ctk.CTkLabel(master=self,text='',fg_color=('gray20'),corner_radius=12,height=300,font=self.lb_res,wraplength=1200)
        
        self.letreiro       .grid(row=0,columnspan=6,padx=15,pady=(5,30))
        self.lb_livro       .grid(row=1,column=0,padx=15,pady=15)
        self.in_livro       .grid(row=1,column=1,padx=15,pady=15)
        self.lb_capitulo    .grid(row=1,column=2,padx=15,pady=15)
        self.in_capitulo    .grid(row=1,column=3,padx=15,pady=15)
        self.lb_versiculo   .grid(row=1,column=4,padx=15,pady=15)
        self.in_versiculo   .grid(row=1,column=5,padx=15,pady=15)
        self.menu_versao    .grid(row=2,columnspan=6,padx=15,pady=15)
        self.bt_consultar   .grid(row=3,columnspan=6,padx=15,pady=15)
        self.lb_res         .grid(row=4,columnspan=6,padx=15,pady=15,sticky='nsew')

    def conectar(self,versao,l,c,v):
        arquivo = ''
        match versao:
            case 'Almeida Corrigida e Fiel': arquivo = 'biblias/ACF.sqlite'
            case 'Almeida Revista e Atualizada': arquivo = 'biblias/ARA.sqlite'
            case 'Almeida Revista e Corrigida': arquivo = 'biblias/ARC.sqlite'
            case 'Almeida Século XXI': arquivo = 'biblias/AS21.sqlite'
            case 'Almeida Atualizada': arquivo = 'biblias/JFAA.sqlite'
            case 'King James Atualizada': arquivo = 'biblias/KJA.sqlite'
            case 'King James Fiel': arquivo = 'biblias/KJF.sqlite'
            case 'Nova Almeida Atualizada': arquivo = 'biblias/NAA.sqlite'
            case 'Nova Bíblia Viva': arquivo = 'biblias/NBV.sqlite'
            case 'Nova Tradução na Linguagem de Hoje': arquivo =  'biblias/NTLH.sqlite'
            case 'Nova Versão Internacional': arquivo = 'biblias/NVI.sqlite'
            case 'Nova Versão Transformadora': arquivo = 'biblias/NVT.sqlite'
            case 'Tradução Brasileira': arquivo = 'biblias/TB.sqlite'

        conn = sqlite3.connect(arquivo)
        print(f'Conectado a: {versao}')

        cur = conn.cursor()

        id_book = cur.execute(f"SELECT book_reference_id FROM book WHERE name = '{l}'").fetchall()[0][0]
        resultado = cur.execute(f'SELECT text FROM verse WHERE book_id = {int(id_book)} AND chapter = {int(c)} AND verse = {int(v)}').fetchall()
        self.lb_res.configure(text=resultado[0][0])


if __name__ == '__main__':
    App().mainloop()

