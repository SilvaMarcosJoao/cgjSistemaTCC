from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox
from modulos.fornecedor import Fornecedor
from modulos.fornecimento import Fornecimento


fornecedor = Fornecedor()
fornece = Fornecimento()


appFornecedor = Tk()

class FornecedorTela():

    def __init__(self) -> None:
        self.appFornecedor = appFornecedor
        self.configTelafornecedor()
        self.frame_fornecedor()
        self.widgets_frameCadfornecedor()
        self.listaFrameResfornecedor()
        appFornecedor.mainloop()

    # Configurações da tela fornecedor
    def configTelafornecedor(self) -> None:
        self.appFornecedor.title('Fornecedor - Sistema de Gerenciamento (SGZurc)')
        self.largTela = 1200
        self.alturTela = 700
        self.lMonitor = self.appFornecedor.winfo_screenwidth()
        self.aMonitor = self.appFornecedor.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.largTela / 2)
        self.posY = (self.aMonitor / 2) - (self.alturTela / 2)
        self.appFornecedor.geometry("%dx%d+%d+%d" % (self.largTela, self.alturTela, self.posX, self.posY))
        self.appFornecedor.minsize(width=1200, height=400)
        self.appFornecedor.resizable(False, False)
        self.appFornecedor.configure(background='#FFFFFF')


    # Configurações do frame da tela fornecedor
    def frame_fornecedor(self) -> None:
        self.frameCadTelaFornecedor = Frame(self.appFornecedor, bd=1, bg='#d9d9d9')
        self.frameCadTelaFornecedor.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.47)

        self.frameResTelaFornecedor = Frame(self.appFornecedor, bd=1, bg='#d9d9d9')
        self.frameResTelaFornecedor.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.47)

    # Configurações botões, textos e etc...
    def widgets_frameCadfornecedor(self) -> None:

        self.lbl_cnpj_fornecedor = Label(self.frameCadTelaFornecedor, text='Cnpj: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cnpj_fornecedor.place(relx=0.075, rely=0.08, height=20)
        self.et_cnpj_fornecedor = Entry(self.frameCadTelaFornecedor)
        self.et_cnpj_fornecedor.place(relx=0.115, rely=0.08, width=125, height=20)

        self.lbl_nome_fornecedor = Label(self.frameCadTelaFornecedor, text='Fornecedor: ', font=('Roboto', 12, 'bold'),bg='#d9d9d9')
        self.lbl_nome_fornecedor.place(relx=0.225, rely=0.08, height=20)
        self.et_nome_fornecedor = Entry(self.frameCadTelaFornecedor)
        self.et_nome_fornecedor.place(relx=0.32, rely=0.08, width=300, height=20)

        self.lbl_email_fornecedor = Label(self.frameCadTelaFornecedor, text='E-mail: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_email_fornecedor.place(relx=0.58, rely=0.08, height=20)
        self.et_email_fornecedor = Entry(self.frameCadTelaFornecedor)
        self.et_email_fornecedor.place(relx=0.635, rely=0.08, width=350, height=20)

        self.lbl_logr_fornecedor = Label(self.frameCadTelaFornecedor, text='Logradouro: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_logr_fornecedor.place(relx=0.325, rely=0.2, height=20)
        self.et_logr_fornecedor = Entry(self.frameCadTelaFornecedor)
        self.et_logr_fornecedor.place(relx=0.42, rely=0.2, width=602, height=20)

        self.lbl_num_fornecedor = Label(self.frameCadTelaFornecedor, text='Número: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_num_fornecedor.place(relx=0.075, rely=0.3, height=20)
        self.et_num_fornecedor = Entry(self.frameCadTelaFornecedor)
        self.et_num_fornecedor.place(relx=0.145, rely=0.3, width=60, height=20)

        self.lbl_cep_fornecedor = Label(self.frameCadTelaFornecedor, text='Cep: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cep_fornecedor.place(relx=0.2, rely=0.3, height=20)
        self.et_cep_fornecedor = Entry(self.frameCadTelaFornecedor)
        self.et_cep_fornecedor.place(relx=0.24, rely=0.3, width=80, height=20)

        self.lbl_cidade_fornecedor = Label(self.frameCadTelaFornecedor, text='Cidade: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cidade_fornecedor.place(relx=0.32, rely=0.3, height=20)
        self.et_cidade_fornecedor = Entry(self.frameCadTelaFornecedor)
        self.et_cidade_fornecedor.place(relx=0.38, rely=0.3, width=300, height=20)

        self.lbl_estado_fornecedor = Label(self.frameCadTelaFornecedor, text='Estado: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_estado_fornecedor.place(relx=0.64, rely=0.3, height=20)
        self.et_estado_fornecedor = Entry(self.frameCadTelaFornecedor)
        self.et_estado_fornecedor.place(relx=0.7, rely=0.3, width=272, height=20)

        self.lbl_qtd_fornecida_fornecedor = Label(self.frameCadTelaFornecedor, text='Qtd Fornecida: ', font=('Roboto', 12, 'bold'),bg='#d9d9d9')
        self.lbl_qtd_fornecida_fornecedor.place(relx=0.075, rely=0.4, height=20)
        self.et_qtd_fornecida_fornecedor = Entry(self.frameCadTelaFornecedor)
        self.et_qtd_fornecida_fornecedor.place(relx=0.19, rely=0.4, relwidth=0.06, height=20)

        self.lbl_data_fornecimento = Label(self.frameCadTelaFornecedor, text='Data do Fornecimento: ', font=('Roboto', 12, 'bold'),bg='#d9d9d9')
        self.lbl_data_fornecimento.place(relx=0.26, rely=0.4, height=20)
        self.et_data_fornecimento = Entry(self.frameCadTelaFornecedor)
        self.et_data_fornecimento.place(relx=0.44, rely=0.4, relwidth=0.07, height=20)

        self.btn_calendario = Button(self.frameCadTelaFornecedor, text='Selecionar Data', font=('Roboto', 12, 'bold'), bg='#d9d9d9', command=self.calendario_cadastro)
        self.btn_calendario.place(relx=0.52, rely=0.4, height=20)

        self.img_consultar = PhotoImage(file="imagens/consultar.png")
        self.btn_consultar = Button(self.frameCadTelaFornecedor, image=self.img_consultar, bg="#d9d9d9")
        self.btn_consultar.place(relx=0.25, rely=0.55, relwidth=0.12, height=50)

        self.et_consultar = Entry(self.frameCadTelaFornecedor, font=('Roboto', 16))
        self.et_consultar.place(relx=0.38, rely=0.55, width=445, height=50)

        self.img_salvar = PhotoImage(file="imagens/adicionar.png")
        self.btn_salvar = Button(self.frameCadTelaFornecedor, image=self.img_salvar, bg='#d9d9d9', command=self.inter_add_fornecedor)
        self.btn_salvar.place(relx=0.25, rely=0.8, relwidth=0.12, height=50)
        
        self.img_listar = PhotoImage(file="imagens/listar.png")
        self.btn_listar = Button(self.frameCadTelaFornecedor, image=self.img_listar, bg='#d9d9d9', command=self.lista_fornecedor)
        self.btn_listar.place(relx=0.38, rely=0.8, relwidth=0.12, height=50)

        self.img_alterar = PhotoImage(file="imagens/editar.png")
        self.btn_alterar = Button(self.frameCadTelaFornecedor, image=self.img_alterar, bg='#d9d9d9')
        self.btn_alterar.place(relx=0.51, rely=0.8, relwidth=0.12, height=50)

        self.img_excluir = PhotoImage(file="imagens/excluir.png")
        self.btn_excluir = Button(self.frameCadTelaFornecedor, image=self.img_excluir, bg='#d9d9d9')
        self.btn_excluir.place(relx=0.64, rely=0.8, relwidth=0.12, height=50)

        



    #Função para criar o calendario janela
    def calendario_cadastro(self):
        self.calendario1 = Calendar(self.frameCadTelaFornecedor, fg='gray75', bg='blue', font=('Roboto', 12, 'bold'), locale='pt_br')
        self.calendario1.place(relx=0.5, rely=0.1)
        self.calData = Button(self.frameCadTelaFornecedor, text='Inserir Data', command=self.printCal)
        self.calData.place(relx=0.55, rely=0.75, width=100, height=25)

    #função para inserir a data
    def printCal(self):
        dataIni = self.calendario1.get_date()
        self.calendario1.destroy()
        self.et_data_fornecimento.delete(0, END)
        self.et_data_fornecimento.insert(END, dataIni)
        self.calData.destroy()

    def listaFrameResfornecedor(self):
        #criando treeview , dizemos qual é o pai dele(frameResFornecedor), posição que ele vai ficar, as colunas
        self.listaForn = ttk.Treeview(self.frameResTelaFornecedor, height=3, columns=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8', 'Col9', 'Col10', 'Col11'))
        # vamos especificar o cabeçalho de cada coluna criada
        self.listaForn.heading("#0", text='')
        self.listaForn.heading('#1', text='Cnpj')
        self.listaForn.heading('#2', text='Fornecedor')
        self.listaForn.heading('#3', text='Email')
        self.listaForn.heading('#4', text='Telefone')
        self.listaForn.heading('#5', text='Logradouro')
        self.listaForn.heading('#6', text='Número')
        self.listaForn.heading('#7', text='Cep')
        self.listaForn.heading('#8', text='Cidade')
        self.listaForn.heading('#9', text='Estado')
        self.listaForn.heading('#10', text='Produto')
        self.listaForn.heading('#11', text='Qtd')
        #Agora especificar o tamanho em largura de cada coluna
        '''
            A largura tem como número referência o 500, então dividimos o 500 em partes para  cada coluna
            na coluna 1 a largura 50, equivale a 10% de 500 na coluna 2 200 equivale a 40% de 500 e assim vai.
        '''
        self.listaForn.column('#0', width=1)
        self.listaForn.column('#1', width=100)
        self.listaForn.column('#2', width=200)
        self.listaForn.column('#3', width=250)
        self.listaForn.column('#4', width=105)
        self.listaForn.column('#5', width=300)
        self.listaForn.column('#6', width=80)
        self.listaForn.column('#7', width=100)
        self.listaForn.column('#8', width=250)
        self.listaForn.column('#9', width=250)
        self.listaForn.column('#10', width=200)
        self.listaForn.column('#11', width=80)

        #definindo a posição do treeview na tela
        self.listaForn.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.9)
        
        #criando barra de rolagem
        self.scrollLista = Scrollbar(self.frameResTelaFornecedor, orient='vertical')
        #informando que a barra de rolagem pertence a lista treeview e unindo os dois elementos
        self.listaForn.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.97, rely=0.01, relwidth= 0.02, relheight=0.85)

        #barra de rolagem horizontal
        self.scrollHor = Scrollbar(self.frameResTelaFornecedor, orient='horizontal')
        self.listaForn.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.01, rely=0.9, relwidth=0.1, relheight=0.1)

    def inter_add_fornecedor(self):
        self.variaveis_campos()
        fornecedor.cadastrar_fornecedor(self.cnpj, self.nome_fornecedor, self.email, self.telefone, self.logradouro, self.numero, 
        self.cep, self.cidade, self.estado)
        fornece.cadastrar_fornecimento(self.cnpj, self.qtd, self.data)
        


    def lista_fornecedor(self):
        self.listaForn.delete(*self.listaForn.get_children())
        self.lista = fornecedor.consultarFornecedor()
       
        for i in self.lista:
            self.listaForn.insert('',END, values=i)

    def variaveis_campos(self):
        self.cnpj = self.et_cnpj_fornecedor.get()
        self.nome_fornecedor = self.et_nome_fornecedor.get()
        self.email = self.et_email_fornecedor.get()
        self.telefone = self.et_tel_fornecedor.get()
        self.logradouro = self.et_logr_fornecedor.get()
        self.numero = self.et_num_fornecedor.get()
        self.cep = self.et_cep_fornecedor.get()
        self.cidade = self.et_cidade_fornecedor.get()
        self.estado = self.et_estado_fornecedor.get()
        self.qtd = self.et_qtd_fornecida_fornecedor.get()
        self.data = self.et_data_fornecimento.get()


'''
        
        self.btn_voltar = Button(self.abaCadastrar, text='Voltar', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.btn_voltar.place(relx=0.01, rely=0.91, relwidth=0.12, relheight=0.08)
   
'''
FornecedorTela()