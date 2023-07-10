from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from modulos.usuario import Usuario
from modulos.funcionalidades import Funcionalidades
from modulos.validacoes import Validadores
from telaFornecimento import FornecimentoTela
from telaCliente import TelaCliente
from telaProduto import TelaProduto


appMenu = Tk()

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
        self.imgConsultar = PhotoImage(file='imagens/consultar.png')

    def mudaCorBtnMenu(self):
        self.btn_ger_venda.config(bg='#6E6E6E')
        self.btn_ger_categoria.config(bg='#6E6E6E')
        self.btn_ger_fornecedor.config(bg='#6E6E6E')
        self.btn_ger_produto.config(bg='#6E6E6E')
        self.btn_ger_usuario.config(bg='#6E6E6E')
        self.btn_ger_cliente.config(bg='#6E6E6E')
        self.btn_inicio.config(bg='#6E6E6E')
        self.btn_ger_servico.config(bg='#6E6E6E')
        self.btn_ger_os.config(bg='#6E6E6E')

    def indicate(self, btn, page):
        self.mudaCorBtnMenu()
        btn.config(bg='#FFF')
        self.delete_page()
        page()

    def delete_page(self):
        for f in self.frameMenu_right.winfo_children():
            f.destroy()

    def validaEntradas(self):
        self.impCod = (self.appMenu.register(self.limitar_cod), "%P")
        self.tamCod = (self.appMenu.register(self.limitar_tam_cod), "%P")
        self.valString = (self.appMenu.register(self.validarString), "%P")
        self.valInt = (self.appMenu.register(self.validaInt), "%P")
        self.valDec = (self.appMenu.register(self.validaDecim), "%P")
        self.validadorSenha = (self.appMenu.register(self.validarSenha), "%P")
        


    def inserirDatave(self):
        dataIniv = self.calendarioObj.get_date()
        self.calendarioObj.destroy()
        self.et_data_venda.delete(0,END)
        self.et_data_venda.insert(END, dataIniv)
        self.calData.destroy()

    def calendariove(self):
        self.calendarioObj = Calendar(self.frameMenu_right, fg='gray75', bg='blue', font=('Arial', 9, 'bold'), locale='pt_br')
        self.calendarioObj.place(relx=0.5, rely=0.1)
        self.calData = Button(self.frameMenu_right, text='Inserir Data', command=self.inserirDatave)
        self.calData.place(relx=0.5, rely=0.45, width=100, height=25)
            
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
        self.frameMenu_left = Frame(self.appMenu, bd=1, bg='#FFF')
        self.frameMenu_left.place(relx=0, rely=0, relwidth=0.15, relheight=1)

        self.frameMenu_right = Frame(self.appMenu, bd=1, bg='#505050')
        self.frameMenu_right.place(relx=0.15, rely=0, relwidth=0.85, relheight=1)

    # FRAME DE EXIBIÇÃO DAS TELAS
    def widgets_menu_left(self) -> None:
        self.img_inicio = PhotoImage(file='./imagens/inicio.png', width=60)
        self.btn_inicio = Button(self.frameMenu_left, image=self.img_inicio, text='Início',relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#6E6E6E',command=lambda: self.indicate(self.btn_inicio, self.widgets_inicio))
        self.btn_inicio.place(relx=0.08, rely=0.05, width=150, height=50)

        self.img_ger_usu = PhotoImage(file='./imagens/usuario.png')
        self.btn_ger_usuario = Button(self.frameMenu_left, image=self.img_ger_usu, text=' Usuário', relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#6E6E6E',command=lambda: self.indicate(self.btn_ger_usuario, self.widgets_usuario))
        self.btn_ger_usuario.place(relx=0.08, rely=0.14, width=150, height=50)

        self.img_ger_cli = PhotoImage(file='./imagens/cliente.png')
        self.btn_ger_cliente = Button(self.frameMenu_left, image=self.img_ger_cli,text=' Cliente', relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#6E6E6E', command=lambda: self.indicate(self.btn_ger_cliente, self.widgets_cliente))
        self.btn_ger_cliente.place(relx=0.08, rely=0.23, width=150, height=50)

        self.img_ger_cat = PhotoImage(file='./imagens/categoria.png')
        self.btn_ger_categoria = Button(self.frameMenu_left, image=self.img_ger_cat, text='Categoria', relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#6E6E6E', command=lambda:self.indicate(self.btn_ger_categoria, self.widgets_categoria) )
        self.btn_ger_categoria.place(relx=0.08, rely=0.32, width=150, height=50)

        self.img_ger_produto = PhotoImage(file='./imagens/produto.png')
        self.btn_ger_produto = Button(self.frameMenu_left, image=self.img_ger_produto, text=' Produto', relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#6E6E6E', command=lambda: self.indicate(self.btn_ger_produto, self.widgets_produto))
        self.btn_ger_produto.place(relx=0.08, rely=0.41, width=150, height=50)
        
        self.img_ger_forn = PhotoImage(file='./imagens/fornecedor.png')
        self.btn_ger_fornecedor = Button(self.frameMenu_left, image=self.img_ger_forn, text=' Fornecedor', relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#6E6E6E', command=lambda: self.indicate(self.btn_ger_fornecedor, self.widgets_fornecedor))
        self.btn_ger_fornecedor.place(relx=0.08, rely=0.5, width=150, height=50)

        self.img_ger_serv = PhotoImage(file='./imagens/servico.png')
        self.btn_ger_servico = Button(self.frameMenu_left, image=self.img_ger_serv, text=' Serviço', relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#6E6E6E', command=lambda: self.indicate(self.btn_ger_servico, self.widgets_servico))
        self.btn_ger_servico.place(relx=0.08, rely=0.59, width=150, height=50)

        self.img_os = PhotoImage(file='./imagens/OS.png')
        self.btn_ger_os = Button(self.frameMenu_left, image=self.img_os, text='Ordem de Serviço', relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#6E6E6E', command=lambda: self.indicate(self.btn_ger_os, self.widgets_os))
        self.btn_ger_os.place(relx=0.08, rely=0.68, width=150, height=50)

        self.img_ger_vend = PhotoImage(file='./imagens/venda.png')
        self.btn_ger_venda = Button(self.frameMenu_left, image=self.img_ger_vend, text=' Venda', relief='groove',font=('Roboto', 7, 'bold'), compound='left', anchor='center', bg='#6E6E6E', command=lambda: self.indicate(self.btn_ger_venda, self.widgets_venda))
        self.btn_ger_venda.place(relx=0.08, rely=0.77, width=150, height=50)

        self.img_ger_sair = PhotoImage(file='./imagens/sair.png')
        self.btn_sair = Button(self.frameMenu_left, image=self.img_ger_sair, text='Finalizar', relief='groove', font=('Roboto', 7, 'bold'), compound='left', anchor='center',bg='#6E6E6E', command=self.appMenu.destroy)
        self.btn_sair.place(relx=0.08, rely=0.86, width=150, height=50)

    # CONFIGURAÇÕES DA TELA INICIO
    def widgets_inicio(self) -> None:
        self.lbl_titulo_inicio = Label(self.frameMenu_right, text='SGZurc', bg='#505050', font=('Roboto', 40, 'bold'))
        self.lbl_titulo_inicio.place(relx=0.4, rely=0.2)

        self.lbl_subtitulo_inicio = Label(self.frameMenu_right, text='Sistema de Gerenciamento', bg='#505050', font=('Roboto', 28, 'bold'))
        self.lbl_subtitulo_inicio.place(relx=0.26, rely=0.4)

    # CONFIGURAÇÕES DA TELA USUÁRIO
    def widgets_usuario(self) -> None:
        self.validaEntradas()
        self.usuario_frame = Frame(self.frameMenu_right)
        self.usuario_frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.8)
        
        lbl_titulo_usuario = Label(self.usuario_frame, text='USUÁRIO', font=('Roboto', 15))
        lbl_titulo_usuario.place(relx=0.025, rely=0.01)

        self.lbl_nova_senha = Label(self.usuario_frame, text='Nova Senha:',font=('Roboto', 10, 'bold'))
        self.lbl_nova_senha.place(relx=0.2, rely=0.2)
        self.et_nova_senha = Entry(self.usuario_frame, font=('Roboto', 9), show='*', validate='key', validatecommand=self.validadorSenha)
        self.et_nova_senha.place(relx=0.42, rely=0.2, width=150, height=20)

        self.lbl_confir_senha = Label(self.usuario_frame, text='Confirmar Senha:', font=('Roboto', 10, 'bold'))
        self.lbl_confir_senha.place(relx=0.19, rely=0.25)
        self.et_confir_senha = Entry(self.usuario_frame, font=('Roboto', 9), show ='*', validate='key', validatecommand=self.validadorSenha)
        self.et_confir_senha.place(relx=0.42, rely =0.25, width=150, height=20)

        self.btn_alterar_senha = Button(self.usuario_frame, text='Alterar', font=('Roboto', 10, 'bold'), fg='#FFF',bg='#505050', command=self.mudar_senha)
        self.btn_alterar_senha.place(relx=0.4, rely=0.4, width=100, height=40)
    
    # CONFIGURAÇÕES DA TELA CLIENTE         
    def widgets_cliente(self) -> None:
        self.validaEntradas()
        self.img_crud()
        self.frameCadTelaCliente = Frame(self.frameMenu_right, bd=1,bg='#d9d9d9')
        self.frameCadTelaCliente.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        lbl_titulo_cliente = Label(self.frameCadTelaCliente, text='CLIENTE', font=('Roboto', 15), bg='#d9d9d9')
        lbl_titulo_cliente.place(relx=0.025, rely=0.01)
         
        self.lbl_cod_cliente = Label(self.frameCadTelaCliente, text='Código:', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cod_cliente.place(relx=0.025, rely=0.1, height=20)
        self.et_cod_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9), bg='#FFF', state='disabled')
        self.et_cod_cliente.place(relx=0.09, rely=0.1, width=50, height=20)
        
        self.lbl_cpf_cliente = Label(self.frameCadTelaCliente, text='CPF:',  font=('Roboto', 9, 'bold'), bg='#d9d9d9')    
        self.lbl_cpf_cliente.place(relx=0.025, rely=0.15, height=20)
        self.et_cpf_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9),bg= '#FFF')
        self.et_cpf_cliente.place(relx=0.09, rely=0.15, width=220, height=20)
        
        self.lbl_nome_cliente = Label(self.frameCadTelaCliente, text='Nome: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_nome_cliente.place(relx=0.025, rely=0.2, height=20)
        self.et_nome_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9), validate='key', validatecommand=self.valString, bg='#FFF')
        self.et_nome_cliente.place(relx=0.09, rely=0.2, width=220, height=20)

        self.lbl_email_cliente = Label(self.frameCadTelaCliente, text='E-mail: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_email_cliente.place(relx=0.025, rely=0.25, height=20)
        self.et_email_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9), bg='#FFF')
        self.et_email_cliente.place(relx=0.09, rely=0.25, width=220, height=20)

        self.lbl_tel_cliente = Label(self.frameCadTelaCliente, text='Telefone: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_tel_cliente.place(relx=0.025, rely=0.3,  height=20)
        self.et_tel_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9), bg='#FFF')
        self.et_tel_cliente.place(relx=0.09, rely=0.3, width=220, height=20)

        self.lbl_logr_cliente = Label(self.frameCadTelaCliente, text='Endereço: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_logr_cliente.place(relx=0.34, rely=0.1, height=20)
        self.et_logr_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9), validate='key', validatecommand=self.valString, bg='#FFF')
        self.et_logr_cliente.place(relx=0.405, rely=0.1, width=220, height=20)

        self.lbl_num_cliente = Label(self.frameCadTelaCliente, text='Número: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_num_cliente.place(relx=0.35, rely=0.15, height=20)
        self.et_num_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9), bg='#FFF', validate='key', validatecommand=self.valInt)
        self.et_num_cliente.place(relx=0.405, rely=0.15, width=60, height=20)

        self.lbl_cep_cliente = Label(self.frameCadTelaCliente, text='Cep: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cep_cliente.place(relx=0.49, rely=0.15, height=20)
        self.et_cep_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9), bg='#FFF')
        self.et_cep_cliente.place(relx=0.525, rely=0.15, width=100, height=20)

        self.lbl_cidade_cliente = Label(self.frameCadTelaCliente, text='Cidade: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cidade_cliente.place(relx=0.355, rely=0.2, height=20)
        self.et_cidade_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9), validate='key', validatecommand=self.valString, bg='#FFF')
        self.et_cidade_cliente.place(relx=0.405, rely=0.2, width=220, height=20)

        self.lbl_estado_cliente = Label(self.frameCadTelaCliente, text='Estado: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_estado_cliente.place(relx=0.355, rely=0.25, height=20)
        self.et_estado_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9), validate='key', validatecommand=self.valString, bg='#FFF')
        self.et_estado_cliente.place(relx=0.405, rely=0.25, width=220, height=20)
        
        self.btn_consultar = Button(self.frameCadTelaCliente, text=' Consultar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.buscar_cliente)
        self.btn_consultar.place(relx=0.88, rely=0.065, relwidth=0.09, height=40)
        self.lbl_pes = Label(self.frameCadTelaCliente, text='Buscar Cliente: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_pes.place(relx=0.73, rely=0.065)
        self.et_consultar_cliente = Entry(self.frameCadTelaCliente, font=('Roboto', 9), bg='#FFF')
        self.et_consultar_cliente.place(relx=0.73, rely=0.1, width=130, height=20)
        
        self.btn_salvar = Button(self.frameCadTelaCliente, command=self.inserir_cliente, text=' Salvar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_salvar.place(relx=0.88, rely=0.145, relwidth=0.09, height=40)
        
        self.btn_listar = Button(self.frameCadTelaCliente, command=self.lista_cliente,  text=' Listar', relief='groove',font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_listar.place(relx=0.88, rely=0.225, relwidth=0.09, height=40)

        self.btn_alterar = Button(self.frameCadTelaCliente, command=self.alterar_cliente, text=' Alterar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_alterar.place(relx=0.88, rely=0.305, relwidth=0.09, height=40)

        self.btn_excluir = Button(self.frameCadTelaCliente, command=self.excluir_cliente, text=' Excluir', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_excluir.place(relx=0.88, rely=0.385, relwidth=0.09, height=40)
    
        self.listaCliente = ttk.Treeview(self.frameCadTelaCliente, height=3 ,columns=('Col1','Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7',
                                                                                      'Col8', 'Col9','Col10'), show = 'headings')
        self.listaCliente.heading("#0", text='')
        self.listaCliente.heading("#1", text='Código')
        self.listaCliente.heading('#2', text='CPF')
        self.listaCliente.heading('#3', text='Nome')
        self.listaCliente.heading('#4', text='Email')
        self.listaCliente.heading('#5', text='Telefone')
        self.listaCliente.heading('#6', text='Endereço')
        self.listaCliente.heading('#7', text='Número')
        self.listaCliente.heading('#8', text='Cep')
        self.listaCliente.heading('#9', text='Cidade')
        self.listaCliente.heading('#10', text='Estado')

        self.listaCliente.column('#0', width=1, anchor='center')
        self.listaCliente.column('#1', width=60, anchor='center')
        self.listaCliente.column('#2', width=120, anchor='center')
        self.listaCliente.column('#3', width=240, anchor='center')
        self.listaCliente.column('#4', width=160, anchor='center')
        self.listaCliente.column('#5', width=160, anchor='center')
        self.listaCliente.column('#6', width=250, anchor='center')
        self.listaCliente.column('#7', width=80, anchor='center')
        self.listaCliente.column('#8', width=100, anchor='center')
        self.listaCliente.column('#9', width=80, anchor='center')
        self.listaCliente.column('#10', width=80, anchor='center')

        self.listaCliente.place(relx=0.02, rely=0.47, relwidth=0.95, relheight=0.49)
        
        self.scrollLista = Scrollbar(self.frameCadTelaCliente, orient='vertical', command=self.listaCliente.yview)
        self.listaCliente.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.975, rely=0.47, relwidth= 0.02, relheight=0.48)

        self.scrollHor = Scrollbar(self.frameCadTelaCliente, orient='horizontal', command=self.listaCliente.xview)
        self.listaCliente.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.02, rely=0.96, relwidth=0.075, relheight=0.035)
        self.listaCliente.bind("<Double-1>", self.duplo_clique_cliente)

    # CONFIGURAÇÕES DA TELA CATEGORIA
    def widgets_categoria(self) -> None:
        self.validaEntradas()
        self.img_crud()
        self.categoria_frame = Frame(self.frameMenu_right, bd=1,bg='#d9d9d9')
        self.categoria_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        lbl_titulo_categoria = Label(self.categoria_frame, text='CATEGORIA', font=('Roboto', 15), bg='#d9d9d9')
        lbl_titulo_categoria.place(relx=0.025, rely=0.01)

        self.lbl_cod_categoria = Label(self.categoria_frame, text='Código:', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cod_categoria.place(relx=0.25, rely=0.1, height=20)
        self.et_cod_categoria = Entry(self.categoria_frame, font=('Roboto', 9), state='disabled', validate='key', validatecommand=self.impCod, bg='#FFF')
        self.et_cod_categoria.config(state='disabled')
        self.et_cod_categoria.place(relx=0.30, rely=0.1, width=50, height=20)

        self.lbl_desc_categoria = Label(self.categoria_frame, text='Descrição da Categoria: ', font=('Roboto', 9, 'bold') , bg='#d9d9d9')
        self.lbl_desc_categoria.place(relx=0.25, rely=0.15, height=20)
        self.et_desc_categoria = Entry(self.categoria_frame, font=('Roboto', 9), validate='key', validatecommand=self.valString, bg='#FFF')
        self.et_desc_categoria.place(relx=0.40, rely=0.15, width=171, height=20)

        self.btn_salvar_categoria = Button(self.categoria_frame, text=' Salvar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.inserir_categoria)
        self.btn_salvar_categoria.place(relx=0.84, rely=0.1, relwidth=0.1, height=40)

        self.btn_lista_categoria = Button(self.categoria_frame,  text=' Listar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.exibir_categoria)
        self.btn_lista_categoria.place(relx=0.84, rely=0.18, relwidth=0.1, height=40)

        self.btn_alterar_categoria = Button(self.categoria_frame,  text=' Alterar', relief='groove',  font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.editar_categoria)
        self.btn_alterar_categoria.place(relx=0.84, rely=0.26, relwidth=0.1, height=40)

        self.btn_excluir_categoria = Button(self.categoria_frame,  text=' Excluir', relief='groove',font=('Roboto',10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.excluir_categoria)
        self.btn_excluir_categoria.place(relx=0.84, rely=0.34, relwidth=0.1, height=40)

        self.listaCategoria = ttk.Treeview(self.categoria_frame, height=3, columns=('Col1', 'Col2'))

        self.listaCategoria.heading('#0', text='')
        self.listaCategoria.heading('#1', text='Código Categoria')
        self.listaCategoria.heading('#2', text='Descrição da Categoria')

        self.listaCategoria.column('#0', width=1)
        self.listaCategoria.column('#1', width=120, minwidth=100, stretch=NO, anchor='center')
        self.listaCategoria.column('#2', width=290, minwidth=290, stretch=NO, anchor='center')
        self.listaCategoria.place(relx=0.26, rely=0.48, relwidth=0.45, relheight=0.5)

        self.scrollListaCat = Scrollbar(self.categoria_frame, orient='vertical', command=self.listaCategoria.yview)
        self.listaCategoria.configure(yscrollcommand=self.scrollListaCat.set)
        self.scrollListaCat.place(relx=0.72, rely=0.48, relwidth= 0.02, relheight=0.5)
        self.listaCategoria.bind("<Double-1>", self.duplo_clique_cat)

    # CONFIGURAÇÕES DA TELA PRODUTO
    def widgets_produto(self):
        self.validaEntradas()
        self.img_crud()
        self.produto_frame = Frame(self.frameMenu_right, bg='#d9d9d9')
        self.produto_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        lbl_titulo_prod = Label(self.produto_frame, text='PRODUTO', font=('Roboto', 15), bg='#d9d9d9')
        lbl_titulo_prod.place(relx=0.02, rely=0.01)
        
        self.lbl_cod_produto = Label(self.produto_frame, text='Código: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cod_produto.place(relx=0.02, rely=0.1)
        self.et_cod_produto = Entry(self.produto_frame, font=('Roboto', 9), state='disabled')
        self.et_cod_produto.place(relx=0.09, rely=0.1, width=50, height=20)
        
        self.lbl_mode_produto = Label(self.produto_frame, text='Modelo: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_mode_produto.place(relx=0.02, rely=0.15)
        self.et_mode_produto = Entry(self.produto_frame, font=('Roboto', 9))
        self.et_mode_produto.place(relx=0.09, rely=0.15, width=150, height=20)
        
        self.lbl_desc_produto = Label(self.produto_frame, text='Descrição: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_desc_produto.place(relx=0.02, rely=0.2)
        self.et_desc_produto = Entry(self.produto_frame, font=('Roboto', 10))
        self.et_desc_produto.place(relx=0.09, rely=0.2, width=150, height=20)

        self.lbl_preco_comp_produto = Label(self.produto_frame, text='Preço Compra: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_preco_comp_produto.place(relx=0.02, rely=0.25)
        self.et_preco_comp_produto = Entry(self.produto_frame,font=('Roboto', 9))
        self.et_preco_comp_produto.place(relx=0.115, rely=0.25, width=125, height=20)

        self.lbl_preco_ven_produto = Label(self.produto_frame, text='Preço Venda: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_preco_ven_produto.place(relx=0.35, rely=0.1)
        self.et_preco_ven_produto = Entry(self.produto_frame, font=('Roboto', 9))
        self.et_preco_ven_produto.place(relx=0.435, rely=0.1, width=125, height=20)

        self.lbl_qtd_produto = Label(self.produto_frame, text='Qtd: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_qtd_produto.place(relx=0.15, rely=0.1)
        self.et_qtd_produto = Entry(self.produto_frame, font=('Roboto', 10))
        self.et_qtd_produto.place(relx=0.18, rely=0.1, width=63, height=20)

        self.lbl_cat_produto = Label(self.produto_frame, text='Categoria: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cat_produto.place(relx=0.35, rely=0.15)
        self.et_categoria = StringVar(self.produto_frame)
        self.et_categoria.set('')
        self.lista = self.exibir_categ_prod()
        self.popupMenu = OptionMenu(self.produto_frame, self.et_categoria, *self.lista)
        self.popupMenu.place(relx=0.435, rely=0.15, width=126, height=22)
        
        self.btn_fornecimento = Button(self.produto_frame, text='Selecionar Fornecedor', font=('Roboto', 9, 'bold'), bg='#d9d9d9', command=FornecimentoTela)
        self.btn_fornecimento.place(relx=0.35, rely=0.2, width=206, height=23)

        self.lbl_consulta_produto = Label(self.produto_frame, text='Buscar Produto: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_consulta_produto.place(relx=0.72, rely=0.07)
        self.et_consulta_produto = Entry(self.produto_frame, font=('Roboto', 9), bg='#FFF')
        self.et_consulta_produto.place(relx=0.72, rely=0.11, width=130, height=20)
        self.btn_consulta_produto = Button(self.produto_frame, text=' Consultar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.consu_produto)
        self.btn_consulta_produto.place(relx=0.87, rely=0.075, relwidth=0.1, height=40)

        self.btn_salvar_produto = Button(self.produto_frame, text=' Salvar', relief='groove',font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.inserir_produto)
        self.btn_salvar_produto.place(relx=0.87, rely=0.155, relwidth=0.1, height=40)

        self.btn_lista_produto = Button(self.produto_frame,   text=' Listar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.exibir_produto)
        self.btn_lista_produto.place(relx=0.87, rely=0.235, relwidth=0.1, height=40)

        self.btn_alterar_produto = Button(self.produto_frame, text=' Alterar', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.editar_produto)
        self.btn_alterar_produto.place(relx=0.87, rely=0.315, relwidth=0.1, height=40)

        self.btn_excluir_produto = Button(self.produto_frame,  text=' Excluir', relief='groove', font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.excluir_produto)
        self.btn_excluir_produto.place(relx=0.87, rely=0.395, relwidth=0.1, height=40)

        self.listaProd = ttk.Treeview(self.produto_frame, height=3, columns=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7'), show='headings')
        
        self.listaProd.heading("#0", text='')
        self.listaProd.heading("#1", text='Código')
        self.listaProd.heading('#2', text='Descrição')
        self.listaProd.heading('#3', text='Modelo')
        self.listaProd.heading('#4', text='Preço Compra')
        self.listaProd.heading('#5', text='Preço Venda')
        self.listaProd.heading('#6', text='Qtd')
        self.listaProd.heading('#7', text='Categoria')

        self.listaProd.column('#0', width=1, anchor='center')
        self.listaProd.column('#1', width=50, anchor='center')
        self.listaProd.column('#2', width=200, anchor='center')
        self.listaProd.column('#3', width=180, anchor='center')
        self.listaProd.column('#4', width=60, anchor='center')
        self.listaProd.column('#5', width=60, anchor='center')
        self.listaProd.column('#6', width=50, anchor='center')
        self.listaProd.column('#7', width=100, anchor='center')
        
        self.et_preco_comp_produto.getdouble(s=0)

        self.listaProd.place(relx=0.02, rely=0.48, relwidth=0.95, relheight=0.48)

        self.scrollListaProd = Scrollbar(self.produto_frame, orient='vertical', command=self.listaProd.yview)

        self.listaProd.configure(yscrollcommand=self.scrollListaProd.set)
        self.scrollListaProd.place(relx=0.975, rely=0.48, relwidth= 0.02, relheight=0.48)

        self.scrollHor = Scrollbar(self.produto_frame, orient='horizontal')
        self.listaProd.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.02, rely=0.965, relwidth=0.1, relheight=0.03)
        self.listaProd.bind("<Double-1>", self.duplo_clique_prod)
        
    # CONFIGURAÇÕES DA TELA FORNECEDOR
    def widgets_fornecedor(self) -> None:
        self.validaEntradas()
        self.img_crud()
        self.frameCadTelaFornecedor = Frame(self.frameMenu_right, bd=1, bg='#d9d9d9')
        self.frameCadTelaFornecedor.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        lbl_titulo_fornecedor = Label(self.frameCadTelaFornecedor, text='FORNECEDOR', font=('Roboto', 15), bg='#d9d9d9')
        lbl_titulo_fornecedor.place(relx=0.025, rely=0.01)

        self.lbl_cod_fornecedor = Label(self.frameCadTelaFornecedor, text='Código:', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cod_fornecedor.place(relx=0.02, rely=0.1, height=20)
        self.et_cod_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9), validate='key', validatecommand=self.impCod)
        self.et_cod_fornecedor.place(relx=0.09, rely=0.1, width=50, height=20)

        self.lbl_cnpj_fornecedor = Label(self.frameCadTelaFornecedor, text='CNPJ/CPF: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cnpj_fornecedor.place(relx=0.02, rely=0.15, height=20)
        self.et_cnpj_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9))
        self.et_cnpj_fornecedor.place(relx=0.09, rely=0.15, width=220, height=20)

        self.lbl_nome_fornecedor = Label(self.frameCadTelaFornecedor, text='Nome: ', font=('Roboto', 9, 'bold'),bg='#d9d9d9')
        self.lbl_nome_fornecedor.place(relx=0.02, rely=0.2, height=20)
        self.et_nome_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9), validate='key', validatecommand=self.valString)
        self.et_nome_fornecedor.place(relx=0.09, rely=0.2, width=220, height=20)

        self.lbl_email_fornecedor = Label(self.frameCadTelaFornecedor, text='E-mail: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_email_fornecedor.place(relx=0.02, rely=0.25, height=20)
        self.et_email_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9))
        self.et_email_fornecedor.place(relx=0.09, rely=0.25, width=220, height=20)

        self.lbl_tel_fornecedor = Label(self.frameCadTelaFornecedor, text='Telefone: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_tel_fornecedor.place(relx=0.02, rely=0.3, height=20)
        self.et_tel_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9))
        self.et_tel_fornecedor.place(relx=0.09, rely=0.3, width=220, height=20)

        self.lbl_logr_fornecedor = Label(self.frameCadTelaFornecedor, text='Endereço: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_logr_fornecedor.place(relx=0.02, rely=0.35, height=20)
        self.et_logr_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9), validate='key', validatecommand=self.valString)
        self.et_logr_fornecedor.place(relx=0.09, rely=0.35, width=220, height=20)

        self.lbl_num_fornecedor = Label(self.frameCadTelaFornecedor, text='Número: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_num_fornecedor.place(relx=0.35, rely=0.1, height=20)
        self.et_num_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9), validate='key', validatecommand=self.valInt)
        self.et_num_fornecedor.place(relx=0.405, rely=0.1, width=60, height=20)

        self.lbl_cep_fornecedor = Label(self.frameCadTelaFornecedor, text='Cep: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cep_fornecedor.place(relx=0.49, rely=0.1, height=20)
        self.et_cep_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9))
        self.et_cep_fornecedor.place(relx=0.522, rely=0.1, width=107, height=20)

        self.lbl_cidade_fornecedor = Label(self.frameCadTelaFornecedor, text='Cidade: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cidade_fornecedor.place(relx=0.35, rely=0.15, height=20)
        self.et_cidade_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9), validate='key', validatecommand=self.valString)
        self.et_cidade_fornecedor.place(relx=0.405, rely=0.15, width=220, height=20)

        self.lbl_estado_fornecedor = Label(self.frameCadTelaFornecedor, text='Estado: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_estado_fornecedor.place(relx=0.35, rely=0.2, height=20)
        self.et_estado_fornecedor = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9), validate='key', validatecommand=self.valString)
        self.et_estado_fornecedor.place(relx=0.405, rely=0.2, width=220, height=20)
        
        self.btn_consultar = Button(self.frameCadTelaFornecedor, command=self.pesquisar_fornecedor,text="Consultar",font=('Roboto', 10,'bold'),  bg="#f3f3f3")
        self.btn_consultar.place(relx=0.88, rely=0.075, relwidth=0.09, height=40)

        self.lbl_pes_forn = Label(self.frameCadTelaFornecedor, text='Buscar Fornecedor: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_pes_forn.place(relx=0.73, rely=0.065)
        self.et_consultar_forne = Entry(self.frameCadTelaFornecedor, font=('Roboto', 9))
        self.et_consultar_forne.place(relx=0.73, rely=0.105, width=130, height=20)
        
        self.btn_salvar = Button(self.frameCadTelaFornecedor, command= self.inserir_fornecedor,text="Salvar",font=('Roboto', 10,'bold'), bg='#f3f3f3')
        self.btn_salvar.place(relx=0.88, rely=0.155, relwidth=0.09, height=40)

        self.btn_listar = Button(self.frameCadTelaFornecedor, command= self.lista_fornecedor,text="Listar",font=('Roboto', 10,'bold'), bg='#f3f3f3')
        self.btn_listar.place(relx=0.88, rely=0.235, relwidth=0.09, height=40)

        self.btn_alterar = Button(self.frameCadTelaFornecedor, command= self.alterar_fornecedor,text="Alterar",font=('Roboto', 10,'bold'), bg='#f3f3f3')
        self.btn_alterar.place(relx=0.88, rely=0.315, relwidth=0.09, height=40)

        self.btn_excluir = Button(self.frameCadTelaFornecedor, command=self.excluir_fornecedor,text="Excluir",font=('Roboto', 10,'bold'), bg='#f3f3f3')
        self.btn_excluir.place(relx=0.88, rely=0.395, relwidth=0.09, height=40)

        self.listaForne = ttk.Treeview(self.frameCadTelaFornecedor, height=3, columns=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 
                                                                                        'Col8', 'Col9', 'Col10'), show='headings')
        self.listaForne.heading("#0", text='')
        self.listaForne.heading("#1", text='Código')
        self.listaForne.heading('#2', text='CNPJ')
        self.listaForne.heading('#3', text='Nome')
        self.listaForne.heading('#4', text='Email')
        self.listaForne.heading('#5', text='Telefone')
        self.listaForne.heading('#6', text='Endereço')
        self.listaForne.heading('#7', text='Número')
        self.listaForne.heading('#8', text='Cep')
        self.listaForne.heading('#9', text='Cidade')
        self.listaForne.heading('#10', text='Estado')

        self.listaForne.column('#0', width=1, anchor='center')
        self.listaForne.column('#1', width=60, anchor='center')
        self.listaForne.column('#2', width=80, anchor='center')
        self.listaForne.column('#3', width=230, anchor='center')
        self.listaForne.column('#4', width=180, anchor='center')
        self.listaForne.column('#5', width=130, anchor='center')
        self.listaForne.column('#6', width=220, anchor='center')
        self.listaForne.column('#7', width=60, anchor='center')
        self.listaForne.column('#8', width=80, anchor='center')
        self.listaForne.column('#9', width=150, anchor='center')
        self.listaForne.column('#10', width=150, anchor='center')

        self.listaForne.place(relx=0.02, rely=0.48, relwidth=0.95, relheight=0.49)
        

        self.scrollListaForne = Scrollbar(self.frameCadTelaFornecedor, orient='vertical', command=self.listaForne.yview)
        self.listaForne.configure(yscrollcommand=self.scrollListaForne.set)
        self.scrollListaForne.place(relx=0.975, rely=0.48, relwidth= 0.02, relheight=0.48)
        

        self.scrollHor = Scrollbar(self.frameCadTelaFornecedor, orient='horizontal', command=self.listaForne.xview)
        self.listaForne.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.02, rely=0.97, relwidth=0.08, relheight=0.03)
        self.listaForne.bind("<Double-1>", self.duplo_clique_for)

    # CONFIGURAÇÕES DA TELA SERVIÇO
    def widgets_servico(self):
        self.validaEntradas()
        self.img_crud()
        self.frameCadTelaServico = Frame(self.frameMenu_right, bd=1, bg = '#d9d9d9')
        self.frameCadTelaServico.place(relx=0.12, rely=0.025, relwidth=0.75, relheight=0.95)
        
        lbl_titulo_servico = Label(self.frameCadTelaServico, text='SERVIÇO', font=('Roboto', 15), bg='#d9d9d9')
        lbl_titulo_servico.place(relx=0.025, rely=0.01)

        self.lbl_cod_servico = Label(self.frameCadTelaServico, text="Código: ", font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cod_servico.place(relx=0.2, rely=0.05, height=20)
        self.et_cod_servico = Entry(self.frameCadTelaServico, validate='key', state='disabled')
        self.et_cod_servico.place(relx=0.29, rely=0.05, width=55, height=20)
        
        self.lbl_preco_servico = Label(self.frameCadTelaServico, text='Preço: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_preco_servico.place(relx=0.2, rely=0.1, height=20)
        self.et_preco_servico = Entry(self.frameCadTelaServico)
        self.et_preco_servico.place(relx=0.29, rely=0.1, width=80, height=20)
        
        self.lbl_tipo_servico = Label(self.frameCadTelaServico, text='Tipo: ', font=('Roboto', 9, 'bold'),bg='#d9d9d9')
        self.lbl_tipo_servico.place(relx=0.2, rely=0.15, height=20)
        self.et_tipo_servico = Entry(self.frameCadTelaServico, validate='key', validatecommand=self.valString)
        self.et_tipo_servico.place(relx=0.29, rely=0.15, width=150, height=20) 
        
        self.lbl_desc_servico = Label(self.frameCadTelaServico, text='Descrição: ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_desc_servico.place(relx=0.2, rely=0.2, height=20)
        self.et_desc_servico = Entry(self.frameCadTelaServico)
        self.et_desc_servico.place(relx=0.29, rely=0.2, width=150, height=20)
        
        self.btn_salvar_serv = Button(self.frameCadTelaServico, text=' Salvar', relief='groove',  font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.inserir_servico)
        self.btn_salvar_serv.place(relx=0.72, rely=0.05, relwidth=0.12, height=40)

        self.btn_listar_serv = Button(self.frameCadTelaServico, text=' Listar', relief='groove',  font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.exibir_servico)
        self.btn_listar_serv.place(relx=0.72, rely=0.13, relwidth=0.12, height=40)

        self.btn_alterar_serv = Button(self.frameCadTelaServico, text=' Alterar', relief='groove',  font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.editar_servico)
        self.btn_alterar_serv.place(relx=0.72, rely=0.21, relwidth=0.12, height=40)

        self.btn_excluir_serv = Button(self.frameCadTelaServico, text=' Excluir', relief='groove',  font=('Roboto', 10, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.deletar_servico)
        self.btn_excluir_serv.place(relx=0.72, rely=0.29, relwidth=0.12, height=40)

        self.listaServico = ttk.Treeview(self.frameCadTelaServico, height=3, columns=('Col1', 'Col2', 'Col3', 'Col4'), show='headings')

        self.listaServico.heading("#0", text='')
        self.listaServico.heading('#1', text='Código')
        self.listaServico.heading('#2', text='Descrição')
        self.listaServico.heading('#3', text='Preço')
        self.listaServico.heading('#4', text='Tipo')

        self.listaServico.column('#0', width=1, anchor='center')
        self.listaServico.column('#1', width=60, anchor='center')
        self.listaServico.column('#2', width=240, anchor='center')
        self.listaServico.column('#3', width=80, anchor='center')
        self.listaServico.column('#4', width=100, anchor='center')

        self.listaServico.place(relx=0.2, rely=0.45, relwidth=0.65, relheight=0.45)
        
        self.scrollListaServico = Scrollbar(self.frameCadTelaServico, orient='vertical', command=self.listaServico.yview)
        self.listaServico.configure(yscrollcommand=self.scrollListaServico.set)
        self.scrollListaServico.place(relx=0.86, rely=0.45, relwidth= 0.02, relheight=0.45)

        self.scrollHor = Scrollbar(self.frameCadTelaServico, orient='horizontal', command=self.listaServico.xview)
        self.listaServico.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.2, rely=0.9, relwidth=0.08, relheight=0.03)
        
        self.listaServico.bind("<Double-1>", self.duplo_clique_servico)

    # CONFIGURAÇÕES DA TELA DE ORDEM DE SERVIÇO
    def widgets_os(self):
        self.validaEntradas()
        self.img_crud()
        self.frameCadOs = Frame(self.frameMenu_right, bd=1,bg='#d9d9d9')
        self.frameCadOs.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        lbl_titulo_os = Label(self.frameCadOs, text='ORDEM DE SERVIÇO', font=('Roboto', 12), bg='#d9d9d9')
        lbl_titulo_os.place(relx=0.01, rely=0.01)

        self.lbl_cod_os = Label(self.frameCadOs, text='Código:', font=('Roboto', 9, 'bold'), bg= '#D9D9D9')
        self.lbl_cod_os.place(relx=0.03, rely=0.05, height=20)
        self.et_cod_os = Entry(self.frameCadOs, font=('Roboto', 9), validate='key', validatecommand=self.impCod, bg='#FFF')
        self.et_cod_os.place(relx=0.09, rely=0.05, width=50, height=20)

        self.lbl_modelo_os = Label(self.frameCadOs, text='Modelo:', font=('Roboto', 9, 'bold'), bg= '#d9d9d9')
        self.lbl_modelo_os.place(relx=0.03, rely=0.1, height=20)
        self.et_modelo_os = Entry(self.frameCadOs, font=('Roboto', 9), bg='#FFF')
        self.et_modelo_os.place(relx=0.09, rely=0.1, width=220, height=20)

        self.lbl_data_exec_servico = Label(self.frameCadOs, text='Data:', font=('Roboto', 9, 'bold'), bg= '#D9D9D9')
        self.lbl_data_exec_servico.place(relx=0.03, rely=0.15, height=20)
        self.et_data_exec_servico = Entry(self.frameCadOs, font=('Roboto', 9), bg='#FFF')
        self.et_data_exec_servico.place(relx=0.09, rely=0.15, width=220, height=20)

        self.lbl_valor_total_os = Label(self.frameCadOs, text='Total R$:', font=('Roboto', 9, 'bold'), bg= '#D9D9D9')
        self.lbl_valor_total_os.place(relx=0.03, rely=0.20, height=20)
        self.et_valor_total_os = Entry(self.frameCadOs, font=('Roboto', 9),  bg='#FFF')
        self.et_valor_total_os.place(relx=0.09, rely=0.20, width=220, height=20)

        self.lbl_defeito = Label(self.frameCadOs, text='Defeito:',  font=('Roboto', 9, 'bold'), bg='#D9D9D9')    
        self.lbl_defeito.place(relx=0.38, rely=0.1, height=20)
        self.et_defeito = Entry(self.frameCadOs, font=('Roboto', 9),bg= '#FFF')
        self.txt_defeito = Text(self.frameCadOs, font=('Roboto', 9),bg= '#FFF')
        self.txt_defeito.place(relx=0.44, rely=0.1, width=220, height=120)

        self.lbl_situacao = Label(self.frameCadOs, text='Situação:',  font=('Roboto', 9, 'bold'), bg='#D9D9D9')    
        self.lbl_situacao.place(relx=0.58, rely=0.04, height=20)
        
        #Option Menu
        # vai armazenar a informação escolhida
        self.et_situacao = StringVar(self.frameCadOs)
        # outra variavel do tipo tupla, que vamos definir as opções que o usuário pode escolher
    
        self.listaSituacao = ('Concluído', 'Em aberto')
        #definindo uma opção padrão que sempre vai aparecer
        self.et_situacao.set('')

        #Variavel do option menu
        self.popupSituacao = OptionMenu(self.frameCadOs, self.et_situacao, *self.listaSituacao)
        self.popupSituacao.place(relx=0.64, rely=0.04, width=100, height=22)
        
        #Botão da listagem de serviços
        self.lbl_servico_os = Label(self.frameCadOs, text='Serviço:',  font=('Roboto', 9, 'bold'), bg='#D9D9D9')
        self.lbl_servico_os.place(relx=0.38, rely=0.04, height=20)
        
        #Option Menu
        # vai armazenar a informação escolhida
        self.et_servico_os = StringVar(self.frameCadOs)
    
        #definindo uma opção padrão que sempre vai aparecer
        self.et_servico_os.set('')
        
        self.listas = self.exibir_serv_os()

        #Variavel do option menu
        self.popupServicos = OptionMenu(self.frameCadOs, self.et_servico_os, *self.listas)
        self.popupServicos.place(relx=0.44, rely=0.04, width=100, height=22)
        
        
         #Botões do CRUD da Ordem de Serviço
        self.btn_salvar_os = Button(self.frameCadOs, text=' Salvar', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.inserir_Os)
        self.btn_salvar_os.place(relx=0.84, rely=0.05, relwidth=0.12, height=40)

        self.btn_listar_os = Button(self.frameCadOs, text=' Listar', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.lista_Os)
        self.btn_listar_os.place(relx=0.84, rely=0.14, relwidth=0.12, height=40)

        self.btn_alterar_os = Button(self.frameCadOs, text=' Alterar', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_alterar_os.place(relx=0.84, rely=0.23, relwidth=0.12, height=40)

        self.btn_excluir_os = Button(self.frameCadOs, text=' Excluir', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command=self.excluir_Os)
        self.btn_excluir_os.place(relx=0.84, rely=0.32, relwidth=0.12, height=40)

         #Botões para adicionar os componenetes da Ordem de Serviço
        self.lbl_procuraprodt_os = Label(self.frameCadOs,text= 'Produto:',font=('Roboto', 9, 'bold'), bg='#d9d9d9' )
        self.lbl_procuraprodt_os.place(relx=0.03, rely=0.25)

        self.et_procurarprodt_os = Entry(self.frameCadOs)
        self.et_procurarprodt_os.place(relx=0.09,rely=0.25, width=220, height=20)

        self.btn_procurarprodt_os = Button(self.frameCadOs, text='Procurar' ,relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_procurarprodt_os.place(relx=0.35, rely=0.25, width=62, height=20)

        self.lbl_procurarclie_os = Label(self.frameCadOs, text='Cliente:', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_procurarclie_os.place(relx=0.03, rely=0.3)

        self.et_procurarclien_os = Entry(self.frameCadOs)
        self.et_procurarclien_os.place(relx=0.09, rely=0.3, width=220, height=20)

        self.btn_procurarclien_os = Button(self.frameCadOs, text='Procurar' ,relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_procurarclien_os.place(relx=0.35, rely=0.3, width=62, height=20)


        self.btn_removprodt_os = Button(self.frameCadOs, text=' Remover Produto', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_removprodt_os.place(relx=0.7, rely=0.05, relwidth=0.12, height=40)

        self.btn_addprodt_os = Button(self.frameCadOs, text=' Adicionar Produto', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_addprodt_os.place(relx=0.7, rely=0.14, relwidth=0.12, height=40)

        self.btn_addcliente_os = Button(self.frameCadOs, text=' Adicionar Cliente', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_addcliente_os.place(relx=0.7, rely=0.23, relwidth=0.12, height=40)

        self.btn_removclien_os = Button(self.frameCadOs, text='Remover Cliente', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_removclien_os.place(relx=0.7, rely=0.32, relwidth=0.12, height=40)
        
        
        self.listaOS = ttk.Treeview(self.frameCadOs, height= 3, columns=('col1','col2','col3','col4','col5','col6','col7','col8'), show='headings')
        
        self.listaOS.heading('#0', text='')
        self.listaOS.heading('#1', text='Ordem de Serviço')
        self.listaOS.heading('#2', text='Cliente')
        self.listaOS.heading('#3', text='Serviços')
        self.listaOS.heading('#4', text='Materiais')
        self.listaOS.heading('#5', text='Preço Unit')
        self.listaOS.heading('#6', text='Quantidade')
        self.listaOS.heading('#7', text='Preço')
        self.listaOS.heading('#8', text='Situação')


        self.listaOS.column('#0', width=1, anchor='center')
        self.listaOS.column('#1', width=5, anchor='center')
        self.listaOS.column('#2', width=180, anchor='center')
        self.listaOS.column('#3', width=180, anchor='center')
        self.listaOS.column('#4', width=180, anchor='center')
        self.listaOS.column('#5', width=80, anchor='center')
        self.listaOS.column('#6', width=5, anchor='center')
        self.listaOS.column('#7', width=80, anchor='center')
        self.listaOS.column('#8', width=80, anchor='center')


        self.listaOS.place(relx=0.05, rely=0.45, relwidth=0.9, relheight=0.5)
        
        self.scrollListaOS = Scrollbar(self.frameCadOs, orient='vertical',  command=self.listaOS.yview)
        self.scrollListaOS.config(command=self.frameCadOs.winfo_y)
        self.listaOS.configure(yscrollcommand=self.scrollListaOS.set)
        self.scrollListaOS.place(relx=0.955, rely=0.45, relwidth= 0.02, relheight=0.5)

        self.scrollHor = Scrollbar(self.frameCadOs, orient='horizontal', command=self.listaOS.xview)
        self.listaOS.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.05, rely=0.955, relwidth=0.08, relheight=0.03)

    def widgets_venda(self):
        self.validaEntradas()
        self.img_crud()
        self.frameCadTelaVenda = Frame(self.frameMenu_right, bd=1,background='#d9d9d9')
        self.frameCadTelaVenda.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        lbl_titulo_venda = Label(self.frameCadTelaVenda, text='VENDA', font=('Roboto', 15), bg='#d9d9d9')
        lbl_titulo_venda.place(relx=0.025, rely=0.01)

        self.lbl_cod_venda = Label(self.frameCadTelaVenda, text="Código: ", font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_cod_venda.place(relx=0.05, rely=0.05, height=20)
        self.et_cod_venda = Entry(self.frameCadTelaVenda, validate='key', validatecommand=self.tamCod)
        self.et_cod_venda.place(relx=0.11, rely=0.05, width=55, height=20)

        self.lbl_data_venda = Label(self.frameCadTelaVenda, text='Data : ', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_data_venda.place(relx=0.405, rely=0.05, height=20)
        self.et_data_venda = Entry(self.frameCadTelaVenda)
        self.et_data_venda.place(relx=0.445, rely=0.05, width=60, height=20)
        self.btn_calendario = Button(self.frameCadTelaVenda, text='Inserir', font=('Roboto', 9, 'bold'), bg='#d9d9d9', command=self.calendariove)
        self.btn_calendario.place(relx=0.51, rely=0.05, width=62, height=20)

        #self.lbl_qtdprodt_venda = Label(self.frameCadTelaVenda, text="Qtd", font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        #self.lbl_qtdprodt_venda.place(relx=0.1, rely=0.4, height=20)
        #self.et_qtdprodt_venda = Entry(self.frameCadTelaVenda)
        #self.et_qtdprodt_venda.place(relx=0.16, rely=0.4, width=55, height=20)



        #Botões do CRUD da venda
        self.btn_salvar_venda = Button(self.frameCadTelaVenda, text=' Salvar', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_salvar_venda.place(relx=0.84, rely=0.05, relwidth=0.12, height=40)

        self.btn_listar_venda = Button(self.frameCadTelaVenda, text=' Listar', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_listar_venda.place(relx=0.84, rely=0.14, relwidth=0.12, height=40)

        self.btn_alterar_venda = Button(self.frameCadTelaVenda, text=' Alterar', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_alterar_venda.place(relx=0.84, rely=0.23, relwidth=0.12, height=40)

        self.btn_excluir_venda = Button(self.frameCadTelaVenda, text=' Excluir', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_excluir_venda.place(relx=0.84, rely=0.32, relwidth=0.12, height=40)



         #Botões para adicionar os componenetes da venda

        self.lbl_procuraprodt_venda = Label(self.frameCadTelaVenda,text= 'Produto:',font=('Roboto', 9, 'bold'), bg='#d9d9d9' )
        self.lbl_procuraprodt_venda.place(relx=0.05, rely=0.1)

        self.btn_procurarprodt_venda = Button(self.frameCadTelaVenda, text='Procurar' ,relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3', command= TelaProduto)
        self.btn_procurarprodt_venda.place(relx=0.11, rely=0.1, width=62, height=20)

        self.lbl_procurarclie_venda = Label(self.frameCadTelaVenda, text='Cliente:', font=('Roboto', 9, 'bold'), bg='#d9d9d9')
        self.lbl_procurarclie_venda.place(relx=0.05, rely=0.15)

        self.btn_procurarclien_venda = Button(self.frameCadTelaVenda, text='Procurar' ,relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3',  command= TelaCliente)
        self.btn_procurarclien_venda.place(relx=0.11, rely=0.15, width=62, height=20)

        self.btn_removprodt_venda = Button(self.frameCadTelaVenda, text=' Remover Produto', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_removprodt_venda.place(relx=0.6, rely=0.05, relwidth=0.12, height=40)

        self.btn_addprodt_venda = Button(self.frameCadTelaVenda, text=' Adicionar Produto', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_addprodt_venda.place(relx=0.6, rely=0.14, relwidth=0.12, height=40)

        self.btn_addcliente_venda = Button(self.frameCadTelaVenda, text=' Adicionar Cliente', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_addcliente_venda.place(relx=0.6, rely=0.23, relwidth=0.12, height=40)

        self.btn_removclien_venda = Button(self.frameCadTelaVenda, text='Remover Cliente', relief='groove', font=('Roboto', 9, 'bold'), compound='left', anchor='center', bg='#f3f3f3')
        self.btn_removclien_venda.place(relx=0.6, rely=0.32, relwidth=0.12, height=40)


        self.listaVenda = ttk.Treeview(self.frameCadTelaVenda, height= 3, columns=('col1','col2','col3','col4','col5'), show='headings')
        
        self.listaVenda.heading('#0', text='')
        self.listaVenda.heading('#1', text='Cliente')
        self.listaVenda.heading('#2', text='Produtos')
        self.listaVenda.heading('#3', text='Preço Unit')
        self.listaVenda.heading('#4', text='Quantidade')
        self.listaVenda.heading('#5', text='Preço')

        self.listaVenda.column('#0', width=1, anchor='center')
        self.listaVenda.column('#1', width=180, anchor='center')
        self.listaVenda.column('#2', width=180, anchor='center')
        self.listaVenda.column('#3', width=80, anchor='center')
        self.listaVenda.column('#4', width=5, anchor='center')
        self.listaVenda.column('#5', width=80, anchor='center')

        self.listaVenda.place(relx=0.05, rely=0.45, relwidth=0.9, relheight=0.5)

        self.scrollListaVenda = Scrollbar(self.frameCadTelaVenda, orient='vertical',  command=self.listaVenda.yview)
        self.scrollListaVenda.config(command=self.frameCadTelaVenda.winfo_y)
        self.listaVenda.configure(yscrollcommand=self.scrollListaVenda.set)
        self.scrollListaVenda.place(relx=0.955, rely=0.45, relwidth= 0.02, relheight=0.5)

        self.scrollHor = Scrollbar(self.frameCadTelaVenda, orient='horizontal', command=self.listaVenda.xview)
        self.listaVenda.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.05, rely=0.955, relwidth=0.08, relheight=0.03)

        
        self.listaVenda = ttk.Treeview(self.frameCadTelaVenda, height= 3, columns=('col1','col2','col3','col4','col5','col6'), show='headings')
        
        self.listaVenda.heading('#0', text='')
        self.listaVenda.heading('#1', text='Venda')
        self.listaVenda.heading('#2', text='Cliente')
        self.listaVenda.heading('#3', text='Materiais')
        self.listaVenda.heading('#4', text='Preço Unit')
        self.listaVenda.heading('#5', text='Quantidade')
        self.listaVenda.heading('#6', text='Preço')


        self.listaVenda.column('#0', width=1, anchor='center')
        self.listaVenda.column('#1', width=5, anchor='center')
        self.listaVenda.column('#2', width=180, anchor='center')
        self.listaVenda.column('#3', width=180, anchor='center')
        self.listaVenda.column('#4', width=80, anchor='center')
        self.listaVenda.column('#5', width=5, anchor='center')
        self.listaVenda.column('#6', width=80, anchor='center')


        self.listaVenda.place(relx=0.05, rely=0.99, relwidth=0.9, relheight=0.5)

MenuTela()