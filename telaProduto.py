from tkinter import *
from modulos.produto import Produto
from modulos.funcionalidades import Funcionalidades
from tkinter import ttk


class TelaProduto(Funcionalidades, Produto):
    
    def __init__(self) -> None:
        self.appProduto  = Toplevel()
        self.config_tela_produto()
        self.widgets_tela_produto()
        
    def config_tela_produto(self):
        self.appProduto.title("Sistema de Gerenciamento (SGZurc) - Adição de Produtos")
        self.appProduto.configure(background='#585858')
        
        self.largTela = 600
        self.alturTela = 350
        self.lMonitor = self.appProduto.winfo_screenwidth()
        self.aMonitor = self.appProduto.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.largTela / 2)
        self.posY = (self.aMonitor / 2) - (self.alturTela / 2)
        self.appProduto.geometry("%dx%d+%d+%d" % (self.largTela, self.alturTela, self.posX, self.posY))
        self.appProduto.focus_force()
        self.appProduto.grab_set()
        self.appProduto.resizable(False, False)
        
    def widgets_tela_produto(self):
        # Cabeçalho da janela do produto
        
        self.produto_frame = Frame(self.appProduto, bd=1, bg='#d9d9d9')
        self.produto_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        self.lbl_consulta_produto = Label(self.produto_frame, text='Buscar Produto: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_consulta_produto.place(relx=0.01, rely=0.07)
        
        self.et_consulta_produto = Entry(self.produto_frame, font=('Roboto', 9), bg='#FFF')
        self.et_consulta_produto.place(relx=0.2, rely=0.07, width=180, height=20)
        
        self.btn_consulta_produto = Button(self.produto_frame, text=' Procurar', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.consuper_produto)
        self.btn_consulta_produto.place(relx=0.55, rely=0.07, width=62, height=20)
        
        self.btn_lista_produto = Button(self.produto_frame,   text=' Listar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.listaper_produto)
        self.btn_lista_produto.place(relx=0.87, rely=0.07, width=62, height=20)
        
        self.btn_add_produto = Button(self.produto_frame,   text=' Adicionar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.produtosVenda)
        self.btn_add_produto.place(relx=0.87, rely=0.15, width=62, height=20)
        
        self.listaProdTela = ttk.Treeview(self.produto_frame, height=3, columns=('Col1', 'Col2', 'Col3', 'col4', 'col5'), show='headings')
        
        self.listaProdTela.heading("#0", text='')
        self.listaProdTela.heading('#1', text='Código')
        self.listaProdTela.heading('#2', text='Descrição')
        self.listaProdTela.heading('#3', text='Modelo')
        self.listaProdTela.heading('#4', text='Preço venda')
        self.listaProdTela.heading('#5', text='Qtd Estoque')
        
        self.listaProdTela.column('#0', width=1, anchor='center')
        self.listaProdTela.column('#1', width=50, anchor='center')
        self.listaProdTela.column('#2', width=50, anchor='center')
        self.listaProdTela.column('#3', width=50, anchor='center')
        self.listaProdTela.column('#4', width=50, anchor='center')
        self.listaProdTela.column('#5', width=50, anchor='center')
        
        self.listaProdTela.place(relx=0.02, rely=0.3, relwidth=0.95, relheight=0.66)

        self.scrollListaProdTela = Scrollbar(self.produto_frame, orient='vertical', command=self.listaProdTela.yview)

        self.listaProdTela.configure(yscrollcommand=self.scrollListaProdTela.set)
        self.scrollListaProdTela.place(relx=0.975, rely=0.48, relwidth= 0.02, relheight=0.48)

        self.scrollHor = Scrollbar(self.produto_frame, orient='horizontal')
        self.listaProdTela.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.02, rely=0.965, relwidth=0.1, relheight=0.03)
        self.listaProdTela.bind("<Double-1>", self.duplo_cliqueProdV)