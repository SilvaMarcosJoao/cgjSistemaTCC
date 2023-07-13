from tkinter import *
from modulos.venda import Venda
from modulos.funcionalidades import Funcionalidades
from tkinter import ttk


class TelaItens(Funcionalidades, Venda):
    
    def __init__(self) -> None:
        self.appItens  = Toplevel()
        self.config_tela_itens()
        self.widgets_tela_itens()
        
    def config_tela_itens(self):
        self.appItens.title("Sistema de Gerenciamento (SGZurc) - Carrinho de Compra")
        self.appItens.configure(background='#585858')
        
        self.largTela = 600
        self.alturTela = 450
        self.lMonitor = self.appItens.winfo_screenwidth()
        self.aMonitor = self.appItens.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.largTela / 2)
        self.posY = (self.aMonitor / 2) - (self.alturTela / 2)
        self.appItens.geometry("%dx%d+%d+%d" % (self.largTela, self.alturTela, self.posX, self.posY))
        self.appItens.focus_force()
        self.appItens.grab_set()
        self.appItens.resizable(False, False)
        
    def widgets_tela_itens(self):
        # Cabeçalho da janela do produto
        
        self.add_frame = Frame(self.appItens, bd=1, bg='#d9d9d9')
        self.add_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        

        self.lbl_prodt_venda = Label(self.add_frame, text="Produto: ", font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_prodt_venda.place(relx=0.025, rely=0.1) 
        self.prodRecebidos = self.produtosVenda()
        self.comboxProdt_venda = ttk.Combobox(self.add_frame, values=self.prodRecebidos)
        self.comboxProdt_venda.place(relx=0.15, rely=0.11, width=300, height=20)


        self.lbl_qtd_venda = Label(self.add_frame, text="Quantidade: ", font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_qtd_venda.place(relx=0.44, rely=0.15) 
        self.et_qtd_venda = Entry(self.add_frame)
        self.et_qtd_venda.place(relx=0.515, rely=0.15, width=84, height=20) 
        
        self.btn_add_prod = Button(self.add_frame, text='Adicionar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.listarVenda)
        self.btn_add_prod.place(relx=0.87, rely=0.01, width=62, height=40)
        
        self.btn_remov_prod = Button(self.add_frame, text='Remover', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.listar_vendas_por_dia)
        self.btn_remov_prod.place(relx=0.87, rely=0.07, width=62, height=40)
        
        self.btn_lista_vendaM = Button(self.add_frame,   text=' Listar Por Mês', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.listar_vendas_por_mes)
        self.btn_lista_vendaM.place(relx=0.87, rely=0.13, width=62, height=20)
        
        self.listaHistTela = ttk.Treeview(self.add_frame, height=3, columns=('Col1', 'Col2', 'Col3', 'col4'), show='headings')
        
        self.listaHistTela.heading("#0", text='')
        self.listaHistTela.heading('#1', text='Código Venda')
        self.listaHistTela.heading('#2', text='Cliente')
        self.listaHistTela.heading('#3', text='Valor')
        self.listaHistTela.heading('#4', text='Data da Venda')
        
        
        self.listaHistTela.column('#0', width=1, anchor='center')
        self.listaHistTela.column('#1', width=50, anchor='center')
        self.listaHistTela.column('#2', width=50, anchor='center')
        self.listaHistTela.column('#3', width=50, anchor='center')
        self.listaHistTela.column('#4', width=50, anchor='center')
        
        
        self.listaHistTela.place(relx=0.02, rely=0.3, relwidth=0.95, relheight=0.66)

        self.scrollListaHistTela = Scrollbar(self.add_frame, orient='vertical', command=self.listaHistTela.yview)

        self.listaHistTela.configure(yscrollcommand=self.scrollListaHistTela.set)
        self.scrollListaHistTela.place(relx=0.975, rely=0.48, relwidth= 0.02, relheight=0.48)

        self.scrollHor = Scrollbar(self.add_frame, orient='horizontal')
        self.listaHistTela.configure(xscrollcommand=self.scrollHor.set) 
        self.scrollHor.place(relx=0.02, rely=0.965, relwidth=0.1, relheight=0.03)
       