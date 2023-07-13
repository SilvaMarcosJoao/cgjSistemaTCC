from tkinter import *
from modulos.venda import Venda
from modulos.funcionalidades import Funcionalidades
from tkinter import ttk


class TelaHistorico(Funcionalidades, Venda):
    
    def __init__(self) -> None:
        self.appHistorico  = Toplevel()
        self.config_tela_historico()
        self.widgets_tela_historico()
        
    def config_tela_historico(self):
        self.appHistorico.title("Sistema de Gerenciamento (SGZurc) - Adição de Produtos")
        self.appHistorico.configure(background='#585858')
        
        self.largTela = 600
        self.alturTela = 450
        self.lMonitor = self.appHistorico.winfo_screenwidth()
        self.aMonitor = self.appHistorico.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.largTela / 2)
        self.posY = (self.aMonitor / 2) - (self.alturTela / 2)
        self.appHistorico.geometry("%dx%d+%d+%d" % (self.largTela, self.alturTela, self.posX, self.posY))
        self.appHistorico.focus_force()
        self.appHistorico.grab_set()
        self.appHistorico.resizable(False, False)
        
    def widgets_tela_historico(self):
        # Cabeçalho da janela do produto
        
        self.historico_frame = Frame(self.appHistorico, bd=1, bg='#d9d9d9')
        self.historico_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        self.lbl_consulta_venda = Label(self.historico_frame, text='Buscar Código Venda: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_consulta_venda.place(relx=0.01, rely=0.01)
        
        self.et_consulta_venda = Entry(self.historico_frame, font=('Roboto', 9), bg='#FFF')
        self.et_consulta_venda.place(relx=0.25, rely=0.01, width=38, height=20)
        
        self.btn_consulta_venda = Button(self.historico_frame, text=' Procurar', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.consultarVenda)
        self.btn_consulta_venda.place(relx=0.35, rely=0.01, width=62, height=20)
        
        self.btn_lista_venda = Button(self.historico_frame,   text=' Listar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.listarVenda)
        self.btn_lista_venda.place(relx=0.87, rely=0.01, width=62, height=20)
        
        self.btn_lista_vendaD = Button(self.historico_frame,   text=' Listar Por Dia', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.listar_vendas_por_dia)
        self.btn_lista_vendaD.place(relx=0.87, rely=0.07, width=62, height=20)
        
        self.btn_lista_vendaM = Button(self.historico_frame,   text=' Listar Por Mês', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.listar_vendas_por_mes)
        self.btn_lista_vendaM.place(relx=0.87, rely=0.13, width=62, height=20)
        
        self.listaHistTela = ttk.Treeview(self.historico_frame, height=3, columns=('Col1', 'Col2', 'Col3', 'col4'), show='headings')
        
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

        self.scrollListaHistTela = Scrollbar(self.historico_frame, orient='vertical', command=self.listaHistTela.yview)

        self.listaHistTela.configure(yscrollcommand=self.scrollListaHistTela.set)
        self.scrollListaHistTela.place(relx=0.975, rely=0.48, relwidth= 0.02, relheight=0.48)

        self.scrollHor = Scrollbar(self.historico_frame, orient='horizontal')
        self.listaHistTela.configure(xscrollcommand=self.scrollHor.set) 
        self.scrollHor.place(relx=0.02, rely=0.965, relwidth=0.1, relheight=0.03)
       