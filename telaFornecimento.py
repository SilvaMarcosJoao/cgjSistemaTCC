from tkinter import *

class FornecimentoTela:
    def __init__(self) -> None:
        self.appFornecimento  = Toplevel()
        self.config_tela_fornecimento()
        self.widgets_tela_fornecimento()

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
        self.fornecimento_frame.place(relx=0.055, rely=0.025, relwidth=0.95, relheight=0.95)

        self.lbl_produto = Label(self.fornecimento_frame, text='Produto: ')
        self.lbl_produto.place(relx=0.06, rely=0.05, height=20)

        self.et_produto = StringVar(self.fornecimento_frame)

        self.listaProduto = ['Produto 1', 'Produto 2', ]

        self.et_produto.set('')

        self.popupProduto = OptionMenu(self.fornecimento_frame, self.et_produto, *self.listaProduto)
        self.popupProduto.place(relx=0.15, rely=0.05, width=100, height=22)



        self.lbl_produto = Label(self.fornecimento_frame, text='Fornecedor: ')
        self.lbl_produto.place(relx=0.03, rely=0.15, height=20)

        self.et_fornecedor = StringVar(self.fornecimento_frame)

        self.listaFornecedor = ['Fornecedor 1', 'Fornecedor 2', ]

        self.et_fornecedor.set('')


        self.popupFornecedor = OptionMenu(self.fornecimento_frame, self.et_fornecedor, *self.listaFornecedor)
        self.popupFornecedor.place(relx=0.15, rely=0.15, width=100, height=22)

        

