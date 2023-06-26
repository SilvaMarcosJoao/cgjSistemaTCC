from tkinter import *
from tkinter import ttk
from tkinter import tix
from modulos.usuario import Usuario
from modulos.funcionalidades import Funcionalidades
from modulos.validacoes import Validadores

appMenu = tix.Tk()

class MenuTela(Funcionalidades, Validadores):

    lmtsen = None
    def __init__(self) -> None:
        self.appMenu = appMenu
        self.configTelamenu()
        self.frame_menu()
        self.widgets_menu_left()
        self.appMenu.mainloop()

    def img_crud(self):
        self.imgSalvar = PhotoImage(file="imagens/salvar.png")
        self.imgAlterar = PhotoImage(file='./imagens/editar.png')
        self.imgListar = PhotoImage(file="imagens/listar.png")
        self.imgExcluir = PhotoImage(file='./imagens/excluir.png')

    def indicate(self, page):
        self.delete_page()
        page()

    def delete_page(self):
        for f in self.frameMenu_right.winfo_children():
            f.destroy()
            
    # CONFIGURAÇÕES DA TELA 
    def configTelamenu(self) -> None:
        self.appMenu.title('Menu Inicial - Sistema de Gerenciamento (SGZurc)')
        self.largTela = 1200
        self.alturTela = 600
        self.lMonitor = self.appMenu.winfo_screenwidth()
        self.aMonitor = self.appMenu.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.largTela / 2)
        self.posY = (self.aMonitor / 2) - (self.alturTela / 2)
        self.appMenu.geometry("%dx%d+%d+%d" % (self.largTela, self.alturTela, self.posX, self.posY))
        self.appMenu.resizable(False, False)
        self.appMenu.configure(background='#FFFFFF')

    # FRAME DO MENU PRINCIPAL LATERAL
    def frame_menu(self) -> None:
        self.frameMenu_left = Frame(self.appMenu, bd=1, bg='#d9d9d9')
        self.frameMenu_left.place(relx=0, rely=0, relwidth=0.15, relheight=1)

        self.frameMenu_right = Frame(self.appMenu, bd=1, bg='#FFF')
        self.frameMenu_right.place(relx=0.15, rely=0, relwidth=0.85, relheight=1)

    # FRAME DE EXIBIÇÃO DAS TELAS
    def widgets_menu_left(self) -> None:
        self.img_inicio = PhotoImage(file='./imagens/inicio.png', width=60)
        self.btn_inicio = Button(self.frameMenu_left, image=self.img_inicio, text='Início',relief='groove', font=('Verdana', 7, 'bold'), compound='left', anchor='center', bg='#d9d9d9',command=lambda: self.indicate(self.widgets_inicio))
        self.btn_inicio.place(relx=0.08, rely=0.05, width=150, height=50)

        self.img_ger_usu = PhotoImage(file='./imagens/usuario.png')
        self.btn_ger_usuario = Button(self.frameMenu_left, image=self.img_ger_usu, text=' Usuário', relief='groove', font=('Verdana', 7, 'bold'), compound='left', anchor='center', bg='#d9d9d9',command=lambda: self.indicate(self.widgets_usuario))
        self.btn_ger_usuario.place(relx=0.08, rely=0.14, width=150, height=50)

        self.img_ger_cli = PhotoImage(file='./imagens/cliente.png')
        self.btn_ger_cliente = Button(self.frameMenu_left, image=self.img_ger_cli,text=' Cliente', relief='groove', font=('Verdana', 7, 'bold'), compound='left', anchor='center', bg='#d9d9d9', command=self.widgets_cliente)
        self.btn_ger_cliente.place(relx=0.08, rely=0.23, width=150, height=50)

        self.img_ger_cat = PhotoImage(file='./imagens/categoria.png')
        self.btn_ger_categoria = Button(self.frameMenu_left, image=self.img_ger_cat, text='Categoria', relief='groove', font=('Verdana', 7, 'bold'), compound='left', anchor='center', bg='#d9d9d9', command=lambda:self.indicate(self.widgets_categoria) )
        self.btn_ger_categoria.place(relx=0.08, rely=0.32, width=150, height=50)

        self.img_ger_produto = PhotoImage(file='./imagens/produto.png')
        self.btn_ger_produto = Button(self.frameMenu_left, image=self.img_ger_produto, text=' Produto', relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#d9d9d9', command=self.widgets_produto)
        self.btn_ger_produto.place(relx=0.08, rely=0.41, width=150, height=50)
        
        self.img_ger_forn = PhotoImage(file='./imagens/fornecedor.png')
        self.btn_ger_fornecedor = Button(self.frameMenu_left, image=self.img_ger_forn, text=' Fornecedor', relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#d9d9d9', command=self.widgets_fornecedor)
        self.btn_ger_fornecedor.place(relx=0.08, rely=0.5, width=150, height=50)

        self.img_ger_serv = PhotoImage(file='./imagens/servico.png')
        self.btn_ger_servico = Button(self.frameMenu_left, image=self.img_ger_serv, text=' Serviço', relief='groove', font=('Verdana', 7, 'bold'), compound='left', anchor='center', bg='#d9d9d9', command=self.widgets_servico)
        self.btn_ger_servico.place(relx=0.08, rely=0.59, width=150, height=50)

        self.img_os = PhotoImage(file='./imagens/OS.png')
        self.btn_ger_os = Button(self.frameMenu_left, image=self.img_os, text='Ordem de Serviço', relief='groove', font=('Verdana', 7, 'bold'), compound='left', anchor='center', bg='#d9d9d9')
        self.btn_ger_os.place(relx=0.08, rely=0.68, width=150, height=50)

        self.img_ger_vend = PhotoImage(file='./imagens/venda.png')
        self.btn_ger_venda = Button(self.frameMenu_left, image=self.img_ger_vend, text=' Venda', relief='groove',font=('Verdana', 7, 'bold'), compound='left', anchor='center', bg='#d9d9d9')
        self.btn_ger_venda.place(relx=0.08, rely=0.77, width=150, height=50)

        self.img_ger_sair = PhotoImage(file='./imagens/sair.png')
        self.btn_sair = Button(self.frameMenu_left, image=self.img_ger_sair, text='Finalizar', relief='groove', font=('Verdana', 7, 'bold'), compound='left', anchor='center',bg='#d9d9d9', command=self.appMenu.destroy)
        self.btn_sair.place(relx=0.08, rely=0.86, width=150, height=50)
        self.balSair = tix.Balloon(self.frameMenu_left)
        self.balSair.bind_widget(self.btn_sair, balloonmsg='Sair')

    # CONFIGURAÇÕES DA TELA INICIO
    def widgets_inicio(self) -> None:
        self.lbl_titulo_inicio = Label(self.frameMenu_right, text='SGZurc', bg='#d9d9d9', font=('Roboto', 40, 'bold'))
        self.lbl_titulo_inicio.place(relx=0.4, rely=0.2)

        self.lbl_subtitulo_inicio = Label(self.frameMenu_right, text='Sistema de Gerenciamento', bg='#d9d9d9', font=('Roboto', 28, 'bold'))
        self.lbl_subtitulo_inicio.place(relx=0.26, rely=0.4)

    # CONFIGURAÇÕES DA TELA USUÁRIO
    def widgets_usuario(self) -> None:
        self.usuario_frame = Frame(self.frameMenu_right)
        self.usuario_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.lbl_nova_senha = Label(self.usuario_frame, text='Nova Senha:',font=('Roboto', 16))
        self.lbl_nova_senha.place(relx=0.4, rely=0.2)
        self.et_nova_senha = Entry(self.usuario_frame, font=('Roboto', 14))
        self.et_nova_senha.place(relx=0.4, rely =0.25, width=150, height=25)

        self.lbl_confir_senha = Label(self.usuario_frame, text='Confirmar Senha:', font=('Roboto', 16))
        self.lbl_confir_senha.place(relx=0.4, rely=0.3)
        self.et_confir_senha = Entry(self.usuario_frame, font=('Roboto', 14))
        self.et_confir_senha.place(relx=0.4, rely =0.35, width=180, height=25)

        self.img_confirmar = PhotoImage(file='./imagens/confirmar.png')
        self.btn_alterar_senha = Button(self.usuario_frame, image=self.img_confirmar, bg='#d9d9d9', fg='#151515', command=self.mudar_senha)
        self.btn_alterar_senha.place(relx=0.43, rely=0.45, width=120, height=50)
    
    def widgets_cliente(self) -> None:
        self.frameCadTelaCliente = Frame(self.frameMenu_right, bd=1,background='#d9d9d9')
        self.frameCadTelaCliente.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.47)
        
        self.frameResTelaCliente = Frame(self.frameMenu_right, bd=1, background='#d9d9d9')
        self.frameResTelaCliente.place(relx=0.01, rely=0.50, relwidth=0.98, relheight=0.47)
        
        self.lbl_cpf_cliente = Label(self.frameCadTelaCliente, text='CPF:',  font=('Roboto', 12, 'bold'), bg='#d9d9d9')    
        self.lbl_cpf_cliente.place(relx=0.075, rely=0.08, height=20)
        self.et_cpf_cliente = Entry(self.frameCadTelaCliente)
        self.et_cpf_cliente.place(relx=0.115, rely=0.08, width=125, height=20)
        
        self.lbl_nome_cliente = Label(self.frameCadTelaCliente, text='Nome: ', font=('Roboto', 12, 'bold'),bg='#d9d9d9')
        self.lbl_nome_cliente.place(relx=0.225, rely=0.08, height=20)
        self.et_nome_cliente = Entry(self.frameCadTelaCliente)
        self.et_nome_cliente.place(relx=0.32, rely=0.08, width=300, height=20)

        self.lbl_email_cliente = Label(self.frameCadTelaCliente, text='E-mail: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_email_cliente.place(relx=0.58, rely=0.08, height=20)
        self.et_email_cliente = Entry(self.frameCadTelaCliente)
        self.et_email_cliente.place(relx=0.635, rely=0.08, width=350, height=20)

        self.lbl_tel_cliente = Label(self.frameCadTelaCliente, text='Telefone: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_tel_cliente.place(relx=0.075, rely=0.2,  height=20)
        self.et_tel_cliente = Entry(self.frameCadTelaCliente)
        self.et_tel_cliente.place(relx=0.15, rely=0.2, width=200, height=20)

        self.lbl_logr_cliente = Label(self.frameCadTelaCliente, text='Logradouro: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_logr_cliente.place(relx=0.325, rely=0.2, height=20)
        self.et_logr_cliente = Entry(self.frameCadTelaCliente)
        self.et_logr_cliente.place(relx=0.42, rely=0.2, width=602, height=20)

        self.lbl_num_cliente = Label(self.frameCadTelaCliente, text='Número: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_num_cliente.place(relx=0.075, rely=0.3, height=20)
        self.et_num_cliente = Entry(self.frameCadTelaCliente)
        self.et_num_cliente.place(relx=0.145, rely=0.3, width=60, height=20)

        self.lbl_cep_cliente = Label(self.frameCadTelaCliente, text='Cep: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cep_cliente.place(relx=0.2, rely=0.3, height=20)
        self.et_cep_cliente = Entry(self.frameCadTelaCliente)
        self.et_cep_cliente.place(relx=0.24, rely=0.3, width=80, height=20)

        self.lbl_cidade_cliente = Label(self.frameCadTelaCliente, text='Cidade: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cidade_cliente.place(relx=0.32, rely=0.3, height=20)
        self.et_cidade_cliente = Entry(self.frameCadTelaCliente)
        self.et_cidade_cliente.place(relx=0.38, rely=0.3, width=300, height=20)

        self.lbl_estado_cliente = Label(self.frameCadTelaCliente, text='Estado: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_estado_cliente.place(relx=0.64, rely=0.3, height=20)
        self.et_estado_cliente = Entry(self.frameCadTelaCliente)
        self.et_estado_cliente.place(relx=0.7, rely=0.3, width=272, height=20)

        self.img_salvar = PhotoImage(file="imagens/adicionar.png")
        self.btn_salvar = Button(self.frameCadTelaCliente, command = self.inserir_cliente ,image=self.img_salvar, font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.btn_salvar.place(relx=0.25, rely=0.8, relwidth=0.12, height=50)
        
        self.img_listar = PhotoImage(file="imagens/listar.png")
        self.btn_listar = Button(self.frameCadTelaCliente, command= self.lista_cliente, image=self.img_listar, font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.btn_listar.place(relx=0.38, rely=0.8, relwidth=0.12, height=50)

        self.img_alterar = PhotoImage(file="imagens/editar.png")
        self.btn_alterar = Button(self.frameCadTelaCliente, command= self.alterar_cliente, image=self.img_alterar, font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.btn_alterar.place(relx=0.51, rely=0.8, relwidth=0.12, height=50)

        self.img_excluir = PhotoImage(file="imagens/excluir.png")
        self.btn_excluir = Button(self.frameCadTelaCliente, command= self.excluir_cliente, image=self.img_excluir, font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.btn_excluir.place(relx=0.64, rely=0.8, relwidth=0.12, height=50)
    
        self.listaCliente = ttk.Treeview(self.frameResTelaCliente, height=3, columns=('Col1','Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8', 'Col9'))

        self.listaCliente.heading("#0", text='')
        self.listaCliente.heading('#1', text='CPF')
        self.listaCliente.heading('#2', text='Cliente')
        self.listaCliente.heading('#3', text='Email')
        self.listaCliente.heading('#4', text='Telefone')
        self.listaCliente.heading('#5', text='Logradouro')
        self.listaCliente.heading('#6', text='Número')
        self.listaCliente.heading('#7', text='Cep')
        self.listaCliente.heading('#8', text='Cidade')
        self.listaCliente.heading('#9', text='Estado')

        self.listaCliente.column('#0', width=1, anchor='center')
        self.listaCliente.column('#1', width=100, anchor='center')
        self.listaCliente.column('#2', width=200, anchor='center')
        self.listaCliente.column('#3', width=250, anchor='center')
        self.listaCliente.column('#4', width=105, anchor='center')
        self.listaCliente.column('#5', width=300, anchor='center')
        self.listaCliente.column('#6', width=80, anchor='center')
        self.listaCliente.column('#7', width=100, anchor='center')
        self.listaCliente.column('#8', width=100, anchor='center')
        self.listaCliente.column('#9', width=50, anchor='center')

        self.listaCliente.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.85)
        
        self.scrollLista = Scrollbar(self.frameResTelaCliente, orient='vertical')
        self.listaCliente.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.97, rely=0.01, relwidth= 0.02, relheight=0.85)

        self.scrollHor = Scrollbar(self.frameResTelaCliente, orient='horizontal')
        self.listaCliente.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.01, rely=0.9, relwidth=0.1, relheight=0.1)
        self.listaCliente.bind("<Double-1>", self.duplo_clique_cliente)

    # CONFIGURAÇÕES DA TELA CATEGORIA
    def widgets_categoria(self) -> None:
        self.img_crud()
        self.categoria_frame = Frame(self.frameMenu_right)
        self.categoria_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.lbl_cod_categoria = Label(self.categoria_frame, text='Código:', bg='#d9d9d9', font=('Roboto', 12, 'bold'))
        self.lbl_cod_categoria.place(relx=0.25, rely=0.08, height=20)
        self.et_cod_categoria = Entry(self.categoria_frame)
        self.et_cod_categoria.place(relx=0.25, rely=0.11, relwidth=0.1, height=20)

        self.lbl_desc_categoria = Label(self.categoria_frame, text='Descrição da Categoria: ', bg='#d9d9d9', font=('Roboto', 12, 'bold'))
        self.lbl_desc_categoria.place(relx=0.5, rely=0.08, height=20)
        self.et_desc_categoria = Entry(self.categoria_frame)
        self.et_desc_categoria.place(relx=0.5, rely=0.11, width=171, height=20)

        self.btn_salvar_categoria = Button(self.categoria_frame, image=self.imgSalvar, bg='#d9d9d9', command=self.inserir_categoria)
        self.btn_salvar_categoria.place(relx=0.25, rely=0.2, relwidth=0.1, height=50)

        self.btn_lista_categoria = Button(self.categoria_frame, image=self.imgListar, bg='#d9d9d9', command=self.exibir_categoria)
        self.btn_lista_categoria.place(relx=0.38, rely=0.2, relwidth=0.1, height=50)

        self.btn_alterar_categoria = Button(self.categoria_frame, image=self.imgAlterar, bg='#d9d9d9', command=self.editar_categoria)
        self.btn_alterar_categoria.place(relx=0.51, rely=0.2, relwidth=0.1, height=50)

        self.btn_excluir_categoria = Button(self.categoria_frame, image=self.imgExcluir, bg='#d9d9d9', command=self.excluir_categoria)
        self.btn_excluir_categoria.place(relx=0.64, rely=0.2, relwidth=0.1, height=50)

        self.listaCategoria = ttk.Treeview(self.categoria_frame, height=3, columns=('Col1', 'Col2'))

        self.listaCategoria.heading('#0', text='')
        self.listaCategoria.heading('#1', text='Código Categoria')
        self.listaCategoria.heading('#2', text='Descrição da Categoria')

        self.listaCategoria.column('#0', width=1)
        self.listaCategoria.column('#1', width=120, minwidth=100, stretch=NO, anchor='center')
        self.listaCategoria.column('#2', width=300, minwidth=300, stretch=NO, anchor='center')
        self.listaCategoria.place(relx=0.26, rely=0.48, relwidth=0.45, relheight=0.5)

        self.scrollListaCat = Scrollbar(self.categoria_frame, orient='vertical')
        #informando que a barra de rolagem pertence a lista treeview e unindo os dois elementos
        self.listaCategoria.configure(yscrollcommand=self.scrollListaCat.set)
        self.scrollListaCat.place(relx=0.71, rely=0.48, relwidth= 0.02, relheight=0.5)
        self.listaCategoria.bind("<Double-1>", self.duplo_clique_cat)

    # CONFIGURAÇÕES DA TELA PRODUTO
    def widgets_produto(self):
        self.produto_frame = Frame(self.frameMenu_right)
        self.produto_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.lbl_cod_produto = Label(self.produto_frame, text='Código: ', font=('Roboto', 10, 'bold'))
        self.lbl_cod_produto.place(relx=0.02, rely=0.02)
        self.et_cod_produto = Entry(self.produto_frame, font=('Roboto', 10))
        self.et_cod_produto.place(relx=0.02, rely=0.06, width=80, height=20)

        self.lbl_desc_produto = Label(self.produto_frame, text='Descrição: ', font=('Roboto', 10, 'bold'))
        self.lbl_desc_produto.place(relx=0.14, rely=0.02)
        self.et_desc_produto = Entry(self.produto_frame, font=('Roboto', 10))
        self.et_desc_produto.place(relx=0.14, rely=0.06, width=200, height=20)

        self.lbl_mode_produto = Label(self.produto_frame, text='Modelo: ', font=('Roboto', 10, 'bold'))
        self.lbl_mode_produto.place(relx=0.02, rely=0.1)
        self.et_mode_produto = Entry(self.produto_frame, font=('Roboto', 10))
        self.et_mode_produto.place(relx=0.02, rely=0.14, width=190, height=20)

        self.lbl_preco_comp_produto = Label(self.produto_frame, text='Preço Compra: ', font=('Roboto', 10, 'bold'))
        self.lbl_preco_comp_produto.place(relx=0.24, rely=0.1)
        self.et_preco_comp_produto = Entry(self.produto_frame,font=('Roboto', 10))
        self.et_preco_comp_produto.place(relx=0.24, rely=0.14, width=100, height=20)

        self.lbl_preco_ven_produto = Label(self.produto_frame, text='Preço Venda: ', font=('Roboto', 10, 'bold'))
        self.lbl_preco_ven_produto.place(relx=0.02, rely=0.18)
        self.et_preco_ven_produto = Entry(self.produto_frame, font=('Roboto', 10))
        self.et_preco_ven_produto.place(relx=0.02, rely=0.22, width=80, height=20)

        self.lbl_qtd_produto = Label(self.produto_frame, text='Qtd: ', font=('Roboto', 10, 'bold'))
        self.lbl_qtd_produto.place(relx=0.14, rely=0.18)
        self.et_qtd_produto = Entry(self.produto_frame, font=('Roboto', 10))
        self.et_qtd_produto.place(relx=0.14, rely=0.22, width=60, height=20)


        self.lbl_cat_produto = Label(self.produto_frame, text='Categoria: ', font=('Roboto', 10, 'bold'))
        self.lbl_cat_produto.place(relx=0.22, rely=0.18)

        #Option Menu
        # vai armazenar a informação escolhida
        self.TipVar = StringVar(self.produto_frame)
        # outra variavel do tipo tupla, que vamos definir as opções que o usuário pode escolher
        
        #definindo uma opção padrão que sempre vai aparecer
        self.TipVar.set('')

        self.lista = self.exibir_categ_prod()
        

        #Variavel do option menu
        self.popupMenu = OptionMenu(self.produto_frame, self.TipVar, *self.lista)
        self.popupMenu.place(relx=0.22, rely=0.22, relwidth=0.12, height=22)

        #se quisermos obter essa informação para cadastrar no banco
        self.estadoCivil = self.TipVar.get()
        
    # CONFIGURAÇÕES DA TELA FORNECEDOR
    def widgets_fornecedor(self):
        self.frameCadTelaFornecedor = Frame(self.frameMenu_right, bd=1, bg='#d9d9d9')
        self.frameCadTelaFornecedor.place(relx=0, rely=0, relwidth=1, relheight=0.49)

        self.frameResTelaFornecedor = Frame(self.frameMenu_right, bd=1, bg='#d9d9d9')
        self.frameResTelaFornecedor.place(relx=0, rely=0.51, relwidth=1, relheight=0.49)

        self.lbl_cnpj_fornecedor = Label(self.frameCadTelaFornecedor, text='Cnpj: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cnpj_fornecedor.place(relx=0.02, rely=0.03, height=20)
        self.et_cnpj_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 10))
        self.et_cnpj_fornecedor.place(relx=0.02, rely=0.09, width=110, height=20)

        self.lbl_nome_fornecedor = Label(self.frameCadTelaFornecedor, text='Fornecedor: ', font=('Roboto', 12, 'bold'),bg='#d9d9d9')
        self.lbl_nome_fornecedor.place(relx=0.14, rely=0.03, height=20)
        self.et_nome_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 10))
        self.et_nome_fornecedor.place(relx=0.14, rely=0.09, width=280, height=20)

        self.lbl_email_fornecedor = Label(self.frameCadTelaFornecedor, text='E-mail: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_email_fornecedor.place(relx=0.02, rely=0.18, height=20)
        self.et_email_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 10))
        self.et_email_fornecedor.place(relx=0.02, rely=0.24, width=240, height=20)

        self.lbl_tel_fornecedor = Label(self.frameCadTelaFornecedor, text='Telefone: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_tel_fornecedor.place(relx=0.27, rely=0.18, height=20)
        self.et_tel_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 10))
        self.et_tel_fornecedor.place(relx=0.27, rely=0.24, width=150, height=20)

        self.lbl_logr_fornecedor = Label(self.frameCadTelaFornecedor, text='Logradouro: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_logr_fornecedor.place(relx=0.45, rely=0.03, height=20)
        self.et_logr_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 10))
        self.et_logr_fornecedor.place(relx=0.45, rely=0.09, width=455, height=20)

        self.lbl_num_fornecedor = Label(self.frameCadTelaFornecedor, text='Número: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_num_fornecedor.place(relx=0.91, rely=0.03, height=20)
        self.et_num_fornecedor = Entry(self.frameCadTelaFornecedor)
        self.et_num_fornecedor.place(relx=0.91, rely=0.09, width=70, height=20)

        self.lbl_cep_fornecedor = Label(self.frameCadTelaFornecedor, text='Cep: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cep_fornecedor.place(relx=0.45, rely=0.18, height=20)
        self.et_cep_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 10))
        self.et_cep_fornecedor.place(relx=0.45, rely=0.24, width=80, height=20)

        self.lbl_cidade_fornecedor = Label(self.frameCadTelaFornecedor, text='Cidade: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cidade_fornecedor.place(relx=0.54, rely=0.18, height=20)
        self.et_cidade_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 10))
        self.et_cidade_fornecedor.place(relx=0.54, rely=0.24, width=220, height=20)

        self.lbl_estado_fornecedor = Label(self.frameCadTelaFornecedor, text='Estado: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_estado_fornecedor.place(relx=0.77, rely=0.18, height=20)
        self.et_estado_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 10))
        self.et_estado_fornecedor.place(relx=0.77, rely=0.24, width=210, height=20)

        self.lbl_qtd_fornecida_fornecedor = Label(self.frameCadTelaFornecedor, text='Qtd Fornecida: ', font=('Roboto', 12, 'bold'),bg='#d9d9d9')
        self.lbl_qtd_fornecida_fornecedor.place(relx=0.45, rely=0.33, height=20)
        self.et_qtd_fornecida_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 10))
        self.et_qtd_fornecida_fornecedor.place(relx=0.45, rely=0.39, relwidth=0.06, height=20)

        self.lbl_data_fornecimento = Label(self.frameCadTelaFornecedor, text='Data do Fornecimento: ', font=('Roboto', 12, 'bold'),bg='#d9d9d9')
        self.lbl_data_fornecimento.place(relx=0.02, rely=0.33, height=20)
        self.et_data_fornecimento = Entry(self.frameCadTelaFornecedor, font=('Roboto', 10))
        self.et_data_fornecimento.place(relx=0.02, rely=0.39, relwidth=0.07, width=100, height=20)

        self.btn_calendario = Button(self.frameCadTelaFornecedor, text='Selecionar Data', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.btn_calendario.place(relx=0.24, rely=0.34, width=180, height=40)

        self.img_consultar = PhotoImage(file="imagens/consultar.png")
        self.btn_consultar = Button(self.frameCadTelaFornecedor, image=self.img_consultar, bg="#d9d9d9")
        self.btn_consultar.place(relx=0.45, rely=0.65, relwidth=0.1, height=40)

        self.et_consultar = Entry(self.frameCadTelaFornecedor, font=('Roboto', 16))
        self.et_consultar.place(relx=0.56, rely=0.65, width=422, height=40)
        
        self.img_salvar = PhotoImage(file="imagens/adicionar.png")
        self.btn_salvar = Button(self.frameCadTelaFornecedor, image=self.img_salvar, bg='#d9d9d9')
        self.btn_salvar.place(relx=0.02, rely=0.65, relwidth=0.09, height=40)

        self.img_listar = PhotoImage(file="imagens/listar.png")
        self.btn_listar = Button(self.frameCadTelaFornecedor, image=self.img_listar, bg='#d9d9d9')
        self.btn_listar.place(relx=0.12, rely=0.65, relwidth=0.09, height=40)

        self.img_alterar = PhotoImage(file="imagens/editar.png")
        self.btn_alterar = Button(self.frameCadTelaFornecedor, image=self.img_alterar, bg='#d9d9d9')
        self.btn_alterar.place(relx=0.22, rely=0.65, relwidth=0.09, height=40)

        self.img_excluir = PhotoImage(file="imagens/excluir.png")
        self.btn_excluir = Button(self.frameCadTelaFornecedor, image=self.img_excluir, bg='#d9d9d9')
        self.btn_excluir.place(relx=0.32, rely=0.65, relwidth=0.095, height=40)

        self.listaForne = ttk.Treeview(self.frameResTelaFornecedor, height=3, columns=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 
        'Col8', 'Col9', 'Col10', 'Col11', 'Col12'), show='headings')
        self.listaForne.heading("#0", text='')
        self.listaForne.heading('#1', text='CNPJ')
        self.listaForne.heading('#2', text='Fornecedor')
        self.listaForne.heading('#3', text='Email')
        self.listaForne.heading('#4', text='Telefone')
        self.listaForne.heading('#5', text='Logradouro')
        self.listaForne.heading('#6', text='Número')
        self.listaForne.heading('#7', text='Cep')
        self.listaForne.heading('#8', text='Cidade')
        self.listaForne.heading('#9', text='Estado')
        self.listaForne.heading('#10', text='Qtd')
        self.listaForne.heading('#11', text='Data')

        self.listaForne.column('#0', width=1, anchor='center')
        self.listaForne.column('#1', width=50, anchor='center')
        self.listaForne.column('#2', width=200, anchor='center')
        self.listaForne.column('#3', width=250)
        self.listaForne.column('#4', width=150)
        self.listaForne.column('#5', width=350)
        self.listaForne.column('#6', width=80)
        self.listaForne.column('#7', width=80)
        self.listaForne.column('#8', width=200)
        self.listaForne.column('#9', width=200)
        self.listaForne.column('#10', width=80)

        self.listaForne.place(relx=0.01, rely=0.03, relwidth=0.93, relheight=0.9)

        self.scrollListaForne = Scrollbar(self.frameResTelaFornecedor, orient='vertical')

        self.listaForne.configure(yscrollcommand=self.scrollListaForne.set)
        self.scrollListaForne.place(relx=0.97, rely=0.03, relwidth= 0.02, relheight=0.9)

        self.scrollHor = Scrollbar(self.frameResTelaFornecedor, orient='horizontal')
        self.listaForne.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.01, rely=0.94, relwidth=0.1, relheight=0.05)

    # CONFIGURAÇÕES DA TELA SERVIÇO
    def widgets_servico(self):
        self.img_crud()
        self.frameCadTelaServico = Frame(self.frameMenu_right, bd = 1, bg = '#d9d9d9')
        self.frameCadTelaServico.place(relx=0, rely=0., relwidth=1, relheight=0.48)

        self.frameResTelaServico = Frame(self.frameMenu_right, bd = 1, bg = '#d9d9d9')
        self.frameResTelaServico.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

        self.lbl_cod_servico = Label(self.frameCadTelaServico, text="Código: ", font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_cod_servico.place(relx=0.04, rely=0.05, height=20)
        self.et_cod_servico = Entry(self.frameCadTelaServico)
        self.et_cod_servico.place(relx=0.04, rely=0.12, width=80, height=20)

        self.lbl_desc_servico = Label(self.frameCadTelaServico, text='Descrição: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_desc_servico.place(relx=0.04, rely=0.22, height=20)
        self.et_desc_servico = Entry(self.frameCadTelaServico)
        self.et_desc_servico.place(relx=0.04, rely=0.29, width=250, height=20)

        self.lbl_tipo_servico = Label(self.frameCadTelaServico, text='Tipo: ', font=('Roboto', 12, 'bold'),bg='#d9d9d9')
        self.lbl_tipo_servico.place(relx=0.04, rely=0.4, height=20)
        self.et_tipo_servico = Entry(self.frameCadTelaServico)
        self.et_tipo_servico.place(relx=0.04, rely=0.47, width=100, height=20)

        self.lbl_preco_servico = Label(self.frameCadTelaServico, text='Preço: ', font=('Roboto', 12, 'bold'), bg='#d9d9d9')
        self.lbl_preco_servico.place(relx=0.04, rely=0.57, height=20)
        self.et_preco_servico = Entry(self.frameCadTelaServico)
        self.et_preco_servico.place(relx=0.04, rely=0.63, width=80, height=20)

        self.btn_salvar = Button(self.frameCadTelaServico, image=self.imgSalvar, font=('Roboto', 12, 'bold'), bg='#d9d9d9', command=self.inserir_servico)
        self.btn_salvar.place(relx=0.04, rely=0.75, relwidth=0.12, height=50)

        self.btn_listar = Button(self.frameCadTelaServico, image=self.imgListar, font=('Roboto', 12, 'bold'), bg='#d9d9d9', command=self.exibir_servico)
        self.btn_listar.place(relx=0.18, rely=0.75, relwidth=0.12, height=50)

        self.btn_alterar = Button(self.frameCadTelaServico, image=self.imgAlterar, font=('Roboto', 12, 'bold'), bg='#d9d9d9', command=self.editar_servico)
        self.btn_alterar.place(relx=0.32, rely=0.75, relwidth=0.12, height=50)

        self.btn_excluir = Button(self.frameCadTelaServico, image=self.imgExcluir, font=('Roboto', 12, 'bold'), bg='#d9d9d9', command=self.deletar_servico)
        self.btn_excluir.place(relx=0.46, rely=0.75, relwidth=0.12, height=50)

        self.listaServico = ttk.Treeview(self.frameResTelaServico, height=3, columns=('Col1', 'Col2', 'Col3', 'Col4'), show='headings')

        self.listaServico.heading("#0", text='')
        self.listaServico.heading('#1', text='Código')
        self.listaServico.heading('#2', text='Descrição')
        self.listaServico.heading('#3', text='Preço')
        self.listaServico.heading('#4', text='Tipo')

        self.listaServico.column('#0', width=1, anchor='center')
        self.listaServico.column('#1', width=50, anchor='center')
        self.listaServico.column('#2', width=300, anchor='center')
        self.listaServico.column('#3', width=80, anchor='center')
        self.listaServico.column('#4', width=100, anchor='center')

        self.listaServico.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.85)
        self.listaServico.bind("<Double-1>", self.duplo_clique_servico)

    # CONFIGURAÇÕES DA TELA DE ORDEM DE SERVIÇO
    def widgets_os(self):
        pass

MenuTela()