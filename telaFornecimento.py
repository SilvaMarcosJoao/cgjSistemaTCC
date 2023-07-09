from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk

class FornecimentoTela:
    def __init__(self) -> None:
        self.appFornecimento  = Toplevel()
        self.config_tela_fornecimento()
        self.widgets_tela_fornecimento()

    #função para inserir a data no calendario
    def inserirData(self):
        dataIni = self.calendarioObj.get_date()
        self.calendarioObj.destroy()
        self.et_data_fornecimento.delete(0, END)
        self.et_data_fornecimento.insert(END, dataIni)
        self.calData.destroy()

    def calendario(self):
        self.calendarioObj = Calendar(self.appFornecimento, fg='gray75', bg='blue', font=('Arial', 9, 'bold'), locale='pt_br')
        self.calendarioObj.place(relx=0.5, rely=0.1)
        self.calData = Button(self.appFornecimento, text='Inserir Data', command=self.inserirData)
        self.calData.place(relx=0.5, rely=0.65, width=100, height=25)

    def config_tela_fornecimento(self):
        self.appFornecimento.title("Sistema de Gerenciamento (SGZurc) - Fornecimento")
        self.appFornecimento.configure(background='#585858')
    
        self.largTela = 600
        self.alturTela = 350
        self.lMonitor = self.appFornecimento.winfo_screenwidth()
        self.aMonitor = self.appFornecimento.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.largTela / 2)
        self.posY = (self.aMonitor / 2) - (self.alturTela / 2)
        self.appFornecimento.geometry("%dx%d+%d+%d" % (self.largTela, self.alturTela, self.posX, self.posY))
        self.appFornecimento.focus_force()
        self.appFornecimento.grab_set()
        self.appFornecimento.resizable(False, False)

    def widgets_tela_fornecimento(self):
        self.fornecimento_frame = Frame(self.appFornecimento, bd=1, bg='#d9d9d9')
        self.fornecimento_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

        self.lbl_produto = Label(self.fornecimento_frame, text='Produto: ', font=('Roboto', 10, 'bold'), bg='#d9d9d9')
        self.lbl_produto.place(relx=0.02, rely=0.05, height=20)
        self.comboxProduto = ttk.Combobox(self.fornecimento_frame, values=['Produto 1', 'Produto 2'])
        self.comboxProduto.place(relx=0.25, rely=0.05, width=120, height=22)

        self.lbl_fornecedor_fornecimento = Label(self.fornecimento_frame, text='Fornecedor: ', font=('Roboto', 10, 'bold'), bg='#d9d9d9')
        self.lbl_fornecedor_fornecimento.place(relx=0.02, rely=0.15, height=20)
        self.comboxFornecedor = ttk.Combobox(self.fornecimento_frame, values=['Produto 1', 'Produto 2'])
        self.comboxFornecedor.place(relx=0.25, rely=0.15, width=120, height=22)

        self.qtd_fornecida = Label(self.fornecimento_frame, text='Qtd Fornecida: ', font=('Roboto', 10, 'bold'), bg='#d9d9d9')
        self.qtd_fornecida.place(relx=0.02, rely=0.25, height=20)

        self.et_qtd_fornecida = Entry(self.fornecimento_frame)
        self.et_qtd_fornecida.place(relx=0.25, rely=0.25, width=120, height=20)

        self.lbl_data_fornecimento = Label(self.fornecimento_frame, text='Data Fornecimento: ', font=('Roboto', 10, 'bold'), bg='#d9d9d9')
        self.lbl_data_fornecimento.place(relx=0.02, rely=0.35, height=20)
        self.et_data_fornecimento = Entry(self.fornecimento_frame)
        self.et_data_fornecimento.place(relx=0.25, rely=0.35, width=62, height=20)
        self.btn_calendario = Button(self.fornecimento_frame, text='Inserir', font=('Roboto', 9, 'bold'), bg='#d9d9d9', command=self.calendario)
        self.btn_calendario.place(relx=0.36, rely=0.35, width=58, height=20)


        self.listaFornecimento = ttk.Treeview(self.fornecimento_frame, height=3 ,columns=('Col1','Col2', 'Col3', 'Col4'),show = 'headings')
        self.listaFornecimento.heading("#0", text='')
        self.listaFornecimento.heading("#1", text='Produto')
        self.listaFornecimento.heading('#2', text='Fornecedor')
        self.listaFornecimento.heading('#3', text='Qtd Fornecida')
        self.listaFornecimento.heading('#4', text='Data Fornecimento')

        self.listaFornecimento.column('#0', width=1, anchor='center')
        self.listaFornecimento.column('#1', width=120, anchor='center')
        self.listaFornecimento.column('#2', width=120, anchor='center')
        self.listaFornecimento.column('#3', width=80, anchor='center')
        self.listaFornecimento.column('#4', width=80, anchor='center')

        self.listaFornecimento.place(relx=0.02, rely=0.46, relwidth=0.95, relheight=0.5)

        self.scrollListaFornecimento = Scrollbar(self.fornecimento_frame, orient='vertical', command=self.listaFornecimento.yview)
        self.listaFornecimento.configure(yscrollcommand=self.scrollListaFornecimento.set)
        self.scrollListaFornecimento.place(relx=0.975, rely=0.46, relwidth= 0.02, relheight=0.5)