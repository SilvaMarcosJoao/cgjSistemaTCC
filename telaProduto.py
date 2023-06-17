from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox

appProduto = Tk()

class ProdutoTela():

    def __init__(self) -> None:
        self.appProduto = appProduto
        self.configTelaproduto()
        self.frame_produto()
        self.widgets_frameCadproduto()
        self.listaFrameResproduto()
        appProduto.mainloop()

    # Configurações da tela produto
    def configTelaproduto(self) -> None:
        self.appProduto.title('Produto - Sistema de Gerenciamento (SGZurc)')
        self.largTela = 1200
        self.alturTela = 700
        self.lMonitor = self.appProduto.winfo_screenwidth()
        self.aMonitor = self.appProduto.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.largTela / 2)
        self.posY = (self.aMonitor / 2) - (self.alturTela / 2)
        self.appProduto.geometry("%dx%d+%d+%d" % (self.largTela, self.alturTela, self.posX, self.posY))
        self.appProduto.minsize(width=1200, height=400)
        self.appProduto.resizable(False, False)
        self.appProduto.configure(background='#FFFFFF')


    # Configurações do frame da tela produto
    def frame_produto(self) -> None:
        self.frameCadTelaProduto = Frame(self.appProduto, bd=1, bg='#d9d9d9')
        self.frameCadTelaProduto.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.47)

        self.frameResTelaProduto = Frame(self.appProduto, bd=1, bg='#d9d9d9')
        self.frameResTelaProduto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.47)

    # Configurações botões, textos e etc...
    def widgets_frameCadproduto(self) -> None:

        self.lbl_cod_produto = Label(self.frameCadTelaProduto, text='Código do Produto: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cod_produto.place(relx=0.075, rely=0.08, height=20)
        self.et_cod_produto = Entry(self.frameCadTelaProduto)
        self.et_cod_produto.place(relx=0.21, rely=0.08, width=60, height=20)


        self.lbl_desc_produto = Label(self.frameCadTelaProduto, text='Descrição: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_desc_produto.place(relx=0.28, rely=0.08, height=20)
        self.et_desc_produto = Entry(self.frameCadTelaProduto)
        self.et_desc_produto.place(relx=0.635, rely=0.08, width=350, height=20)

        self.lbl_tel_fornecedor = Label(self.frameCadTelaProduto, text='Telefone: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_tel_fornecedor.place(relx=0.075, rely=0.2,  height=20)
        self.et_tel_fornecedor = Entry(self.frameCadTelaProduto)
        self.et_tel_fornecedor.place(relx=0.15, rely=0.2, width=200, height=20)

        self.lbl_logr_fornecedor = Label(self.frameCadTelaProduto, text='Logradouro: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_logr_fornecedor.place(relx=0.325, rely=0.2, height=20)
        self.et_logr_fornecedor = Entry(self.frameCadTelaProduto)
        self.et_logr_fornecedor.place(relx=0.42, rely=0.2, width=602, height=20)

        self.lbl_num_fornecedor = Label(self.frameCadTelaProduto, text='Número: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_num_fornecedor.place(relx=0.075, rely=0.3, height=20)
        self.et_num_fornecedor = Entry(self.frameCadTelaProduto)
        self.et_num_fornecedor.place(relx=0.145, rely=0.3, width=60, height=20)

        self.lbl_cep_fornecedor = Label(self.frameCadTelaProduto, text='Cep: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cep_fornecedor.place(relx=0.2, rely=0.3, height=20)
        self.et_cep_fornecedor = Entry(self.frameCadTelaProduto)
        self.et_cep_fornecedor.place(relx=0.24, rely=0.3, width=80, height=20)

        self.lbl_cidade_fornecedor = Label(self.frameCadTelaProduto, text='Cidade: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cidade_fornecedor.place(relx=0.32, rely=0.3, height=20)
        self.et_cidade_fornecedor = Entry(self.frameCadTelaProduto)
        self.et_cidade_fornecedor.place(relx=0.38, rely=0.3, width=300, height=20)

        self.lbl_estado_fornecedor = Label(self.frameCadTelaProduto, text='Estado: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_estado_fornecedor.place(relx=0.64, rely=0.3, height=20)
        self.et_estado_fornecedor = Entry(self.frameCadTelaProduto)
        self.et_estado_fornecedor.place(relx=0.7, rely=0.3, width=272, height=20)

        self.lbl_qtd_fornecida_fornecedor = Label(self.frameCadTelaProduto, text='Qtd Fornecida: ', font=('Roboto', 12, 'bold'),bg='#d9d9d9')
        self.lbl_qtd_fornecida_fornecedor.place(relx=0.075, rely=0.4, height=20)
        self.et_qtd_fornecida_fornecedor = Entry(self.frameCadTelaProduto)
        self.et_qtd_fornecida_fornecedor.place(relx=0.19, rely=0.4, relwidth=0.06, height=20)

        self.lbl_data_fornecimento = Label(self.frameCadTelaProduto, text='Data do Fornecimento: ', font=('Roboto', 12, 'bold'),bg='#d9d9d9')
        self.lbl_data_fornecimento.place(relx=0.26, rely=0.4, height=20)
        self.et_data_fornecimento = Entry(self.frameCadTelaProduto)
        self.et_data_fornecimento.place(relx=0.44, rely=0.4, relwidth=0.07, height=20)


        self.img_consultar = PhotoImage(file="imagens/consultar.png")
        self.btn_consultar = Button(self.frameCadTelaProduto, image=self.img_consultar, bg="#d9d9d9")
        self.btn_consultar.place(relx=0.25, rely=0.55, relwidth=0.12, height=50)

        self.et_consultar = Entry(self.frameCadTelaProduto, font=('Roboto', 16))
        self.et_consultar.place(relx=0.38, rely=0.55, width=445, height=50)

        self.img_salvar = PhotoImage(file="imagens/adicionar.png")
        self.btn_salvar = Button(self.frameCadTelaProduto, image=self.img_salvar, bg='#d9d9d9' )
        self.btn_salvar.place(relx=0.25, rely=0.8, relwidth=0.12, height=50)
        
        self.img_listar = PhotoImage(file="imagens/listar.png")
        self.btn_listar = Button(self.frameCadTelaProduto, image=self.img_listar, bg='#d9d9d9')
        self.btn_listar.place(relx=0.38, rely=0.8, relwidth=0.12, height=50)

        self.img_alterar = PhotoImage(file="imagens/editar.png")
        self.btn_alterar = Button(self.frameCadTelaProduto, image=self.img_alterar, bg='#d9d9d9')
        self.btn_alterar.place(relx=0.51, rely=0.8, relwidth=0.12, height=50)

        self.img_excluir = PhotoImage(file="imagens/excluir.png")
        self.btn_excluir = Button(self.frameCadTelaProduto, image=self.img_excluir, bg='#d9d9d9')
        self.btn_excluir.place(relx=0.64, rely=0.8, relwidth=0.12, height=50)


    def listaFrameResproduto(self):
        #criando treeview , dizemos qual é o pai dele(frameResFornecedor), posição que ele vai ficar, as colunas
        self.listaProd = ttk.Treeview(self.frameResTelaProduto, height=3, columns=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8', 'Col9', 'Col10', 'Col11'))
        # vamos especificar o cabeçalho de cada coluna criada
        self.listaProd.heading("#0", text='')
        self.listaProd.heading('#1', text='Cod do Produto')
        self.listaProd.heading('#2', text='Descrição')
        self.listaProd.heading('#3', text='Modelo')
        self.listaProd.heading('#4', text='Preço Compra')
        self.listaProd.heading('#5', text='Preço Venda')
        self.listaProd.heading('#6', text='Qtd Estoque')
        self.listaProd.heading('#7', text='Categoria')

        #Agora especificar o tamanho em largura de cada coluna
        '''
            A largura tem como número referência o 500, então dividimos o 500 em partes para  cada coluna
            na coluna 1 a largura 50, equivale a 10% de 500 na coluna 2 200 equivale a 40% de 500 e assim vai.
        '''
        self.listaProd.column('#0', width=1)
        self.listaProd.column('#1', width=100)
        self.listaProd.column('#2', width=200)
        self.listaProd.column('#3', width=250)
        self.listaProd.column('#4', width=105)
        self.listaProd.column('#5', width=300)
        self.listaProd.column('#6', width=80)
        self.listaProd.column('#7', width=100)
        self.listaProd.column('#8', width=250)
        self.listaProd.column('#9', width=250)
        self.listaProd.column('#10', width=200)
        self.listaProd.column('#11', width=80)

        #definindo a posição do treeview na tela
        self.listaProd.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.9)
        
        #criando barra de rolagem
        self.scrollLista = Scrollbar(self.frameResTelaProduto, orient='vertical')
        #informando que a barra de rolagem pertence a lista treeview e unindo os dois elementos
        self.listaProd.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.97, rely=0.01, relwidth= 0.02, relheight=0.85)

        #barra de rolagem horizontal
        self.scrollHor = Scrollbar(self.frameResTelaProduto, orient='horizontal')
        self.listaProd.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.01, rely=0.9, relwidth=0.1, relheight=0.1)


ProdutoTela()