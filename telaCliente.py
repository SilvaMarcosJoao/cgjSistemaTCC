from tkinter import *
from modulos.cliente import Cliente
from modulos.funcionalidades import Funcionalidades
from tkinter import ttk


class TelaCliente(Funcionalidades, Cliente):
    
    def __init__(self) -> None:
        self.appCliente  = Toplevel()
        self.config_tela_cliente()
        self.widgets_tela_cliente()
        
    def config_tela_cliente(self):
        self.appCliente.title("Sistema de Gerenciamento (SGZurc) - Adição de Cliente")
        self.appCliente.configure(background='#585858')
        
        self.largTela = 600
        self.alturTela = 350
        self.lMonitor = self.appCliente.winfo_screenwidth()
        self.aMonitor = self.appCliente.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.largTela / 2)
        self.posY = (self.aMonitor / 2) - (self.alturTela / 2)
        self.appCliente.geometry("%dx%d+%d+%d" % (self.largTela, self.alturTela, self.posX, self.posY))
        self.appCliente.focus_force()
        self.appCliente.grab_set()
        self.appCliente.resizable(False, False)
    
    def widgets_tela_cliente(self):
        self.cliente_frame = Frame(self.appCliente, bd=1, bg='#d9d9d9')
        self.cliente_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        self.lbl_consultar_cliente = Label(self.cliente_frame, text='Buscar Cliente: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_consultar_cliente.place(relx=0.01, rely=0.07)
        
        self.et_consultar_cliente = Entry(self.cliente_frame, font=('Roboto', 9), bg='#FFF')
        self.et_consultar_cliente.place(relx=0.2, rely=0.07, width=180, height=20)
        
        self.btn_consultar_cliente = Button(self.cliente_frame, text=' Procurar', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.buscar_cliente)
        self.btn_consultar_cliente.place(relx=0.55, rely=0.07, width=62, height=20)
        
        self.btn_lista_cliente = Button(self.cliente_frame,   text=' Listar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3',  command=self.lista_cliente)
        self.btn_lista_cliente.place(relx=0.87, rely=0.07, width=62, height=20)
        
        self.listaCliente = ttk.Treeview(self.cliente_frame, height=3 ,columns=('Col1','Col2', 'Col3'), show = 'headings')
        
        self.listaCliente.heading("#0", text='')
        self.listaCliente.heading("#1", text='Código')
        self.listaCliente.heading('#2', text='CPF')
        self.listaCliente.heading('#3', text='Nome')

        self.listaCliente.column('#0', width=1, anchor='center')
        self.listaCliente.column('#1', width=60, anchor='center')
        self.listaCliente.column('#2', width=120, anchor='center')
        self.listaCliente.column('#3', width=240, anchor='center')

        self.listaCliente.place(relx=0.02, rely=0.47, relwidth=0.95, relheight=0.49)
        
        self.scrollLista = Scrollbar(self.cliente_frame, orient='vertical', command=self.listaCliente.yview)
        self.listaCliente.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.975, rely=0.47, relwidth= 0.02, relheight=0.48)

        self.scrollHor = Scrollbar(self.cliente_frame, orient='horizontal', command=self.listaCliente.xview)
        self.listaCliente.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.02, rely=0.96, relwidth=0.075, relheight=0.035)
        
