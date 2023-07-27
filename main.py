from mods import *
import classesfuncoes
from PIL import Image, ImageTk
appLogin = CTk()

class LoginTela(classesfuncoes.Funcionalidades):
    
    def __init__(self) -> None:
        self.appLogin = appLogin
        self.config_tela_login()
        self.widgets_tela_login()
        self.img_procurar = CTkImage(dark_image=Image.open('.\\imagens\\procurar.png'), size=(40, 40))
        self.appLogin.mainloop()
        
    def config_tela_login(self) -> None:
        self.appLogin.title('Sistema de Gerenciamento (SGZurc) - Login') 
        self.appLogin.configure(fg_color='#585858')
        self.larTela = 600
        self.altTela = 350

        self.lMonitor = self.appLogin.winfo_screenwidth()
        self.aMonitor = self.appLogin.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.larTela / 2)
        self.posY = (self.aMonitor / 2) - (self.altTela / 2)
        self.appLogin.geometry("%dx%d+%d+%d" % (self.larTela, self.altTela, self.posX, self.posY))
        self.appLogin.minsize(width=600, height=350)
        self.appLogin.resizable(False, False)
        
        self.titulo_login = CTkLabel(self.appLogin, text="SGZurc", fg_color="#585858",text_color="#FFF")
        self.titulo_login.place(relx=0.41, rely=0.1)
        self.titulo_login.configure(bg_color='#FFF',font=("Roboto", 24,"bold"))

    def widgets_tela_login(self):
        # Criação dos widgets (rótulos, campos de entrada e botão)
        self.lbl_usuario = CTkLabel(self.appLogin, text="Usuário:",text_color="#FFF")
        self.lbl_usuario.place(relx=0.345, rely=0.3)
        self.lbl_usuario.configure(bg_color='#585858',font=("Roboto", 12, 'bold'))
        self.et_usuario = CTkEntry(appLogin, font=('Roboto', 12), width=120, placeholder_text='Digite seu usuário')
        self.et_usuario.place(relx=0.44, rely=0.3)

        self.lbl_senha = CTkLabel(self.appLogin, text="Senha:",text_color="#FFF")
        self.lbl_senha.place(relx=0.345, rely=0.4)
        self.lbl_senha.configure(bg_color='#585858',font=("Roboto", 12, 'bold'))
        self.et_senha = CTkEntry(self.appLogin, font=('Roboto', 12), show="*", width=120, placeholder_text='Digite sua senha')  
        self.et_senha.place(relx=0.44, rely=0.4)

        
        self.btn_login = CTkButton(self.appLogin, text="Entrar", 
                    text_color="#000", 
                    font=('Roboto', 14, 'bold'), 
                    fg_color="#d9d9d9", 
                    border_color="#FFF", 
                    hover_color="#ccc",
                    width=80, height=50, command=self.telaMenu)
        self.btn_login.place(relx=0.43, rely=0.59)

        
        self.btn_alterarsenha = CTkButton(self.appLogin, text="Alterar Senha", 
                                          text_color="#000", 
                                          font=('Roboto', 14, 'bold'), 
                                          fg_color="#d9d9d9", 
                                          border_color="#FFF", 
                                          hover_color="#ccc", 
                                          width=180, 
                                          height=50,
                                          command=self.telamudaSenha)
        self.btn_alterarsenha.place(relx=0.34, rely=0.78)
    
    def efetuarLogin(self) -> None:
        """
        Captura o usuario e senha digitada nos campos de login, envia
        para a função da classe usuário verificar esses dados e autorizar
        o login.
        :param : não tem parâmetro.
        :return: não tem retorno.
        """
        self.captusuario = self.et_usuario.get().strip()
        self.captsenha = self.et_senha.get().strip()
        self.resUser = self.usuario.logar()
        try:
            if len(self.captusuario) == 0 and len(self.captsenha) == 0:
                messagebox.showwarning('Alerta', 'Preencha os campos para logar')
            elif len(self.captusuario) < 2 or len(self.captusuario) > 20:
                messagebox.showwarning('Alerta', 'O usuário não atende aos requisitos')
            elif len(self.captsenha) != 8:
                messagebox.showwarning('Alerta', 'A senha não atende aos requisitos')
            else:
                if self.resUser[0][0] == self.captusuario and self.resUser[0][1] == self.captsenha:
                    self.limpa_usuario()
            
                    self.appLogin.destroy()
                    
                else:
                    print(self.resUser[0])
                    messagebox.showwarning('Atenção', 'Usuário ou senha inválidos!')
                    self.limpa_usuario()
        except Exception as e:
            messagebox.showerror('Erro', 'Houve um erro, não foi possível efetuar login')
            print(e)
        
        
    def limpa_usuario(self):
        self.et_usuario.delete(0,END)
        self.et_senha.delete(0,END)


    # VISUAL DA TELA DE ALTERAR SENHA
    def telamudaSenha(self):
        self.mudasenhatela = CTkToplevel()
        self.mudasenhatela.title("Sistema de Gerenciamento (SGZurc) - Alterar Senha")
        self.mudasenhatela.configure(fg_color='#505050')
        self.largTela = 600
        self.alturTela = 350
        self.lMonitor = self.mudasenhatela.winfo_screenwidth()
        self.aMonitor = self.mudasenhatela.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.largTela / 2)
        self.posY = (self.aMonitor / 2) - (self.alturTela / 2)
        self.mudasenhatela.geometry("%dx%d+%d+%d" % (self.largTela, self.alturTela, self.posX, self.posY))
        self.mudasenhatela.focus_force()
        self.mudasenhatela.grab_set()
        self.mudasenhatela.resizable(False, False)

        self.titulo_login_senha = CTkLabel(self.mudasenhatela, text="SGZurc",text_color='#FFF')
        self.titulo_login_senha.place(relx=0.42, rely=0.1)
        self.titulo_login_senha.configure(font=("Roboto", 24,"bold"))

        self.nova_senha = CTkLabel(self.mudasenhatela, text="Nova senha:", font=('Roboto', 12, 'bold'), text_color='#FFF')
        self.nova_senha.place(relx=0.32, rely=0.3)
        self.et_nova_senha = CTkEntry(self.mudasenhatela, font=('Roboto', 12), show='*', width=120, placeholder_text='Digite nova senha')
        self.et_nova_senha.place(relx=0.46, rely=0.3)

        self.confirmar_senha = CTkLabel(self.mudasenhatela, text="Confirmar senha:",text_color='#FFF')
        self.confirmar_senha.place(relx=0.265, rely=0.4)
        self.et_confir_senha = CTkEntry(self.mudasenhatela, font=('Roboto', 12), show='*', width=120, placeholder_text='Confirmar senha') 
        self.et_confir_senha.place(relx=0.46, rely=0.4)

        self.btn_alterar = CTkButton(self.mudasenhatela, text="Alterar", 
                                        text_color="#000", 
                                        font=('Roboto', 14, 'bold'), 
                                        fg_color="#d9d9d9", 
                                        border_color="#FFF", 
                                        hover_color="#ccc", 
                                        width=180, 
                                        height=50,
                                        command=self.mudar_senha)
        self.btn_alterar.place(relx=0.35, rely=0.59)


    def mudaCorBtnMenu(self):
        self.btn_ger_venda.configure(fg_color='#6E6E6E')
        self.btn_ger_categoria.configure(fg_color='#6E6E6E')
        self.btn_ger_fornecedor.configure(fg_color='#6E6E6E')
        self.btn_ger_produto.configure(fg_color='#6E6E6E')
        self.btn_ger_usuario.configure(fg_color='#6E6E6E')
        self.btn_ger_cliente.configure(fg_color='#6E6E6E')
        self.btn_ger_fornecimento.configure(fg_color='#6E6E6E')
        self.btn_ger_relatorio.configure(fg_color='#6E6E6E')
        self.btn_inicio.configure(fg_color='#6E6E6E')

    def indicate(self, btn, page):
        self.mudaCorBtnMenu()
        btn.configure(fg_color='#FFF')
        self.delete_page()
        page()

    def delete_page(self):
        for f in self.frameMenu_right.winfo_children():
            f.destroy()

    def inserirDatave(self):
        dataIniv = self.calendarioObj.get_date()
        self.calendarioObj.destroy()
        self.et_data_venda.delete(0,END)
        self.et_data_venda.insert(END, dataIniv)
        self.calData.destroy()

    def calendariove(self):
        self.calendarioObj = Calendar(self.frameMenu_right, fg='gray75', bg='blue', font=('Arial', 9, 'bold'), locale='pt_br')
        self.calendarioObj.place(relx=0.5, rely=0.1)
        self.calData = CTkButton(self.frameMenu_right, 
                        text='Inserir Data', 
                        command=self.inserirDatave, 
                        width=100, height=25,
                        text_color='#fff',
                        hover_color='#333',
                        font=('Roboto', 12, 'bold'), 
                        compound='left', 
                        anchor='center', 
                        fg_color='#505050')
        self.calData.place(relx=0.5, rely=0.42)

    def inserirDataFornecimento(self):
        data = self.calendarioFor.get_date()
        self.calendarioFor.destroy()
        self.et_data_fornecimento.delete(0,END)
        self.et_data_fornecimento.insert(END, data)
        self.callen.destroy()


    def calendario(self):
        self.calendarioFor = Calendar(self.fornecimento_frame, bg_color='gray75', font=('Arial', 12, 'bold'), locale='pt_br')
        self.calendarioFor.place(relx=0.5, rely=0.1)
        self.callen = CTkButton(self.frameMenu_right, 
                        text='Inserir Data', 
                        command=self.inserirDataFornecimento, 
                        width=100, height=25,
                        text_color='#fff',
                        hover_color='#333',
                        font=('Roboto', 12, 'bold'), 
                        compound='left', 
                        anchor='center', 
                        fg_color='#505050', 
                        )
        self.callen.place(relx=0.5, rely=0.56)

    

    # VISUAL DA TELA MENU PRINCIPAL
    def telaMenu(self):
        self.appMenu = CTkToplevel()
        self.appMenu.title('Sistema de Gerenciamento (SGZurc) - Menu Inicial')
        #self.appMenu.iconbitmap('./imagens/icone.ico')
        self.largTela = 1200
        self.alturTela = 600
        self.lMonitor = self.appMenu.winfo_screenwidth()
        self.aMonitor = self.appMenu.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.largTela / 2)
        self.posY = (self.aMonitor / 2) - (self.alturTela / 2)
        self.appMenu.geometry("%dx%d+%d+%d" % (self.largTela, self.alturTela, self.posX, self.posY))
        self.appMenu.resizable(False, False)
        self.appMenu.configure(bg='#FFF')
        self.appMenu.focus_force()
        self.appMenu.grab_set()
        self.frame_menu()
        self.widgets_menu_left()
        self.widgets_inicio()
        

    # FRAME DO MENU PRINCIPAL LATERAL
    def frame_menu(self) -> None:
        self.frameMenu_left = CTkFrame(self.appMenu, fg_color='#fff')
        self.frameMenu_left.place(relx=0, rely=0, relwidth=0.15, relheight=1)

        self.frameMenu_right = CTkFrame(self.appMenu, fg_color='#505050')
        self.frameMenu_right.place(relx=0.15, rely=0, relwidth=0.85, relheight=1)
    

    # FRAME DE EXIBIÇÃO DAS TELAS
    def widgets_menu_left(self) -> None:
        self.img_inicio = CTkImage(dark_image=Image.open('.\\imagens\\inicio.png'), size=(40, 40))
        self.btn_inicio = CTkButton(master=self.frameMenu_left, 
                    image=self.img_inicio,         
                    text='Início', 
                    font=('Roboto', 10, 'bold'), 
                    compound='left', 
                    anchor='center', 
                    fg_color='#6E6E6E',
                    text_color='#000',
                    hover_color='#FFF',
                    command=lambda: self.indicate(self.btn_inicio, self.widgets_inicio),
                    width=150, height=50)
        self.btn_inicio.place(relx=0.08, rely=0.01)
        
        self.img_ger_usu = CTkImage(dark_image=Image.open('.\\imagens\\usuario.png'), size=(40, 40))
        self.btn_ger_usuario = CTkButton(self.frameMenu_left, 
                    image=self.img_ger_usu,
                    text=' Usuário', 
                    font=('Roboto', 10, 'bold'), 
                    compound='left', 
                    anchor='center', 
                    fg_color='#6E6E6E',
                    text_color='#000',
                    hover_color='#FFF',
                    command=lambda: self.indicate(self.btn_ger_usuario, self.widgets_usuario),
                    width=150, height=50)
        self.btn_ger_usuario.place(relx=0.08, rely=0.61)

        self.img_ger_cli = CTkImage(dark_image=Image.open('.\\imagens\\cliente.png'), size=(40, 40))
        self.btn_ger_cliente = CTkButton(self.frameMenu_left,
                    image=self.img_ger_cli, 
                    text=' Cliente', 
                    font=('Roboto', 10, 'bold'), 
                    compound='left', 
                    anchor='center', 
                    fg_color='#6E6E6E', 
                    text_color='#000',
                    hover_color='#FFF',
                    command=lambda: self.indicate(self.btn_ger_cliente, self.widgets_cliente),
                    width=150, height=50)
        self.btn_ger_cliente.place(relx=0.08, rely=0.21)

        self.img_ger_cat = CTkImage(dark_image=Image.open('.\\imagens\\categoria.png'), size=(40, 40))
        self.btn_ger_categoria = CTkButton(self.frameMenu_left, 
                    image=self.img_ger_cat,
                    text='Categoria', 
                    font=('Roboto', 10, 'bold'), 
                    compound='left', 
                    anchor='center', 
                    fg_color='#6E6E6E', 
                    text_color='#000',
                    hover_color='#FFF',
                    command=lambda:self.indicate(self.btn_ger_categoria, self.widgets_categoria),
                    width=150, height=50)
        self.btn_ger_categoria.place(relx=0.08, rely=0.11)

        self.img_ger_produto = CTkImage(dark_image=Image.open('.\\imagens\\produto.png'), size=(40, 40))
        self.btn_ger_produto = CTkButton(self.frameMenu_left, 
                    image=self.img_ger_produto,
                    text=' Produto', 
                    font=('Roboto', 10, 'bold'), 
                    compound='left', 
                    anchor='center', 
                    fg_color='#6E6E6E', 
                    text_color='#000',
                    hover_color='#FFF',
                    command=lambda: self.indicate(self.btn_ger_produto, self.widgets_produto),
                    width=150, height=50)
        self.btn_ger_produto.place(relx=0.08, rely=0.51)
        
        
        self.img_ger_forn = CTkImage(dark_image=Image.open('.\\imagens\\fornecedor.png'), size=(40, 40))
        self.btn_ger_fornecedor = CTkButton(self.frameMenu_left, 
                    image=self.img_ger_forn,
                    text=' Fornecedor', 
                    font=('Roboto', 10, 'bold'), 
                    compound='left', 
                    anchor='center', 
                    fg_color='#6E6E6E', 
                    text_color='#000',
                    hover_color='#FFF',
                    command=lambda: self.indicate(self.btn_ger_fornecedor, self.widgets_fornecedor),
                    width=150, height=50)
        self.btn_ger_fornecedor.place(relx=0.08, rely=0.31)

        self.img_ger_vend = CTkImage(dark_image=Image.open('.\\imagens\\venda.png'), size=(40, 40))
        self.btn_ger_venda = CTkButton(self.frameMenu_left, 
                    image=self.img_ger_vend,
                    text=' Venda', 
                    font=('Roboto', 10, 'bold'), 
                    compound='left', 
                    anchor='center', 
                    fg_color='#6E6E6E', 
                    text_color='#000',
                    hover_color='#FFF',
                    command=lambda: self.indicate(self.btn_ger_venda, self.widgets_venda), 
                    width=150, height=50)
        self.btn_ger_venda.place(relx=0.08, rely=0.71)

        self.img_ger_sair = CTkImage(dark_image=Image.open('.\\imagens\\sair.png'), size=(40, 40))
        self.btn_sair = CTkButton(self.frameMenu_left,
                    image=self.img_ger_sair,  
                    text='Finalizar', 
                    font=('Roboto', 10, 'bold'), 
                    compound='left', 
                    anchor='center',
                    fg_color='#6E6E6E',
                    text_color='#000', 
                    hover_color='#FFF',
                    command=self.finalizar,
                    width=150, height=50)
        self.btn_sair.place(relx=0.08, rely=0.91)

        self.img_ger_fornecimen = CTkImage(dark_image=Image.open('.\\imagens\\fornecimento.png'), size=(40, 40))
        self.btn_ger_fornecimento = CTkButton(self.frameMenu_left, 
                    image=self.img_ger_fornecimen,
                    text=' Fornecimento', 
                    font=('Roboto', 10, 'bold'), 
                    compound='left', 
                    anchor='center', 
                    fg_color='#6E6E6E', 
                    text_color='#000',
                    hover_color='#FFF',
                    command=lambda: self.indicate(self.btn_ger_fornecimento, self.widgets_fornecimento),
                    width=150, height=50)
        self.btn_ger_fornecimento.place(relx=0.08, rely=0.41)

        self.img_ger_relatorio = CTkImage(dark_image=Image.open('.\\imagens\\dashboard.png'), size=(40, 40))
        self.btn_ger_relatorio = CTkButton(self.frameMenu_left,  
                    image=self.img_ger_relatorio,
                    text='Relatório', 
                    font=('Roboto', 10, 'bold'), 
                    compound='left', 
                    anchor='center', 
                    fg_color='#6E6E6E', 
                    text_color='#000',
                    hover_color='#FFF',
                    command=lambda: self.indicate(self.btn_ger_relatorio, self.widgets_relatorio),
                    width=150, height=50)
        self.btn_ger_relatorio.place(relx=0.08, rely=0.81)

    # CONFIGURAÇÕES DA TELA INICIO
    def widgets_inicio(self) -> None:
        self.frame_inicio = CTkFrame(self.frameMenu_right, fg_color='#fff')
        self.frame_inicio.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.95)

        self.imgTitulo = CTkImage(dark_image=Image.open('.\\imagens\\logo.jpg'), size=(250, 250))
        self.lblImagem = CTkLabel(self.frame_inicio, text='', image=self.imgTitulo)
        self.lblImagem.place(relx=0.38, rely=0.2)

        self.lbl_subtitulo_inicio = CTkLabel(self.frame_inicio, 
                    text='Sistema de Gerenciamento', 
                    text_color='#000', 
                    font=('Roboto', 28, 'bold'))
        self.lbl_subtitulo_inicio.place(relx=0.32, rely=0.7)
    
    # CONFIGURAÇÕES DA TELA USUÁRIO
    def widgets_usuario(self) -> None:

        self.usuario_frame = CTkFrame(self.frameMenu_right, fg_color='#fff')
        self.usuario_frame.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)
        
        lbl_titulo_usuario = CTkLabel(self.usuario_frame, text_color='#505050',text='USUÁRIO', font=('Roboto', 15))
        lbl_titulo_usuario.place(relx=0.025, rely=0.01)

        self.lbl_nova_senha = CTkLabel(self.usuario_frame,text_color='#505050',
                    text='Nova Senha:',
                    font=('Roboto', 12, 'bold'))
        self.lbl_nova_senha.place(relx=0.23, rely=0.2)
        self.et_nova_senha = CTkEntry(self.usuario_frame, font=('Roboto', 12), show='*', width=150, height=30, placeholder_text='Digite nova senha')
        self.et_nova_senha.focus()
        self.et_nova_senha.place(relx=0.45, rely=0.2)

        self.lbl_confir_senha = CTkLabel(self.usuario_frame, text_color='#505050',
                    text='Confirmar Senha:', font=('Roboto', 12, 'bold'))
        self.lbl_confir_senha.place(relx=0.23, rely=0.34)
        self.et_confir_senha = CTkEntry(self.usuario_frame, font=('Roboto', 12), show ='*', width=150, height=30, placeholder_text='Confirmar senha')
        self.et_confir_senha.place(relx=0.45, rely =0.34)

        self.btn_alterar_senha = CTkButton(self.usuario_frame, text="Alterar", 
                                          text_color="#fff", 
                                          font=('Roboto', 14, 'bold'), 
                                          fg_color="#505050", 
                                          border_color="#FFF", 
                                          hover_color="#777", 
                                          width=70, 
                                          height=30,
                                          command=self.mudar_senha)
        self.btn_alterar_senha.place(relx=0.45, rely=0.55)


    # CONFIGURAÇÕES DA TELA CLIENTE         
    def widgets_cliente(self) -> None:
        
        self.frameCadTelaCliente = CTkFrame(self.frameMenu_right, fg_color='#fff')
        self.frameCadTelaCliente.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        lbl_titulo_cliente = CTkLabel(self.frameCadTelaCliente, 
                                text_color='#505050', text='GERENCIAR CLIENTE', font=('Roboto', 15))
        lbl_titulo_cliente.place(relx=0.42, rely=0.01)
         
        #self.lbl_cod_cliente = CTkLabel(self.frameCadTelaCliente, text='Código:', font=('Roboto', 12, 'bold'), height=20)
        #self.lbl_cod_cliente.place(relx=0.025, rely=0.1)
        self.et_cod_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), state='disabled', width=50, height=30)
        self.et_cod_cliente.place(relx=0.08, rely=0.1)
        self.et_cod_cliente.place_forget()
        self.et_cod_cliente.focus_displayof()
        
        self.lbl_cpf_cliente = CTkLabel(self.frameCadTelaCliente, text_color='#505050',text='CPF*:', font=('Roboto', 12, 'bold'), height=20)    
        self.lbl_cpf_cliente.place(relx=0.025, rely=0.11)
        self.et_cpf_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), width=220, height=30, placeholder_text='CPF')
        self.et_cpf_cliente.focus()
        self.et_cpf_cliente.place(relx=0.08, rely=0.1)
        
        self.lbl_nome_cliente = CTkLabel(self.frameCadTelaCliente,text_color='#505050', text='Nome*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_nome_cliente.place(relx=0.025, rely=0.18)
        self.et_nome_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), width=220, height=30, placeholder_text='Nome completo')
        self.et_nome_cliente.place(relx=0.08, rely=0.17)

        self.lbl_email_cliente = CTkLabel(self.frameCadTelaCliente,text_color='#505050', text='E-mail*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_email_cliente.place(relx=0.025, rely=0.25)
        self.et_email_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), width=220, height=30, placeholder_text='E-mail')
        self.et_email_cliente.place(relx=0.08, rely=0.24)

        self.lbl_tel_cliente = CTkLabel(self.frameCadTelaCliente,text_color='#505050', text='Fone*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_tel_cliente.place(relx=0.025, rely=0.32)
        self.et_tel_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), width=220, height=30, placeholder_text='Telefone')
        self.et_tel_cliente.place(relx=0.08, rely=0.31)

        self.lbl_logr_cliente = CTkLabel(self.frameCadTelaCliente,text_color='#505050', text='Endereço*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_logr_cliente.place(relx=0.34, rely=0.11)
        self.et_logr_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), width=220, height=30, placeholder_text='Endereço')
        self.et_logr_cliente.place(relx=0.415, rely=0.1)

        self.lbl_num_cliente = CTkLabel(self.frameCadTelaCliente,text_color='#505050', text='Número*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_num_cliente.place(relx=0.35, rely=0.18)
        self.et_num_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), width=60, height=30, placeholder_text='Número')
        self.et_num_cliente.place(relx=0.415, rely=0.17)

        self.lbl_cep_cliente = CTkLabel(self.frameCadTelaCliente,text_color='#505050', text='CEP: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_cep_cliente.place(relx=0.5, rely=0.18)
        self.et_cep_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), width=100, height=30, placeholder_text='CEP')
        self.et_cep_cliente.place(relx=0.535, rely=0.17)

        self.lbl_cidade_cliente = CTkLabel(self.frameCadTelaCliente,text_color='#505050', text='Cidade*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_cidade_cliente.place(relx=0.355, rely=0.25)
        self.et_cidade_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), width=220, height=30, placeholder_text='Cidade')
        self.et_cidade_cliente.place(relx=0.415, rely=0.24)

        self.lbl_estado_cliente = CTkLabel(self.frameCadTelaCliente,text_color='#505050', text='Estado*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_estado_cliente.place(relx=0.355, rely=0.32)
        self.et_estado_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), width=220, height=30, placeholder_text='Estado')
        self.et_estado_cliente.place(relx=0.415, rely=0.31)
        
        self.btn_consultar = CTkButton(self.frameCadTelaCliente, 
                image=self.img_procurar, 
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                fg_color='#505050', 
                border_width=2,
                command=self.buscar_cliente)
        self.btn_consultar.place(relx=0.92, rely=0.1, relwidth=0.05, relheight=0.055)

        self.lbl_pes = CTkLabel(self.frameCadTelaCliente,text_color='#505050', text='Buscar Nome: ', font=('Roboto', 12, 'bold'))
        self.lbl_pes.place(relx=0.78, rely=0.065)
        self.et_consultar_cliente = CTkEntry(self.frameCadTelaCliente, font=('Roboto', 12), width=130, height=30, placeholder_text='Buscar')
        self.et_consultar_cliente.place(relx=0.78, rely=0.1)
        
        self.btn_salvar = CTkButton(self.frameCadTelaCliente,  
                text=' Salvar', 
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                border_width=2,
                height=40,
                command=self.inserir_cliente)
        self.btn_salvar.place(relx=0.88, rely=0.165, relwidth=0.09)
        

        self.btn_alterar = CTkButton(self.frameCadTelaCliente,  
                text=' Alterar',  
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                border_width=2,
                height=40,
                command=self.alterar_cliente)
        self.btn_alterar.place(relx=0.88, rely=0.245, relwidth=0.09)
        

        self.btn_excluir = CTkButton(self.frameCadTelaCliente,  
                text=' Excluir',  
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                border_width=2,
                height=40,
                command=self.deletar_cliente)
        self.btn_excluir.place(relx=0.88, rely=0.325, relwidth=0.09)
    
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
        self.listaCliente.heading('#8', text='CEP')
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
        
        self.scrollLista = CTkScrollbar(self.frameCadTelaCliente, orientation='vertical', command=self.listaCliente.yview)
        self.listaCliente.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.97, rely=0.475, relwidth= 0.02, relheight=0.48)

        self.scrollHor = CTkScrollbar(self.frameCadTelaCliente, orientation='horizontal', command=self.listaCliente.xview)
        self.listaCliente.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.02, rely=0.96, relwidth=0.075, relheight=0.035)
        self.listaCliente.bind("<Double-1>", self.duplo_clique_cliente)
        self.lista_cliente()


     # CONFIGURAÇÕES DA TELA CATEGORIA
    def widgets_categoria(self) -> None:
        
        self.categoria_frame = CTkFrame(self.frameMenu_right, fg_color='#fff')
        self.categoria_frame.place(relx=0.13, rely=0.08, relwidth=0.75, relheight=0.85)
        
        lbl_titulo_categoria = CTkLabel(self.categoria_frame, text_color='#505050',text='GERENCIAR CATEGORIA', font=('Roboto', 15))
        lbl_titulo_categoria.place(relx=0.38, rely=0.01)

        #self.lbl_cod_categoria = CTkLabel(self.categoria_frame, text='Código:', font=('Roboto', 12, 'bold'), height=20)
        #self.lbl_cod_categoria.place(relx=0.27, rely=0.11)
        self.et_cod_categoria = CTkEntry(self.categoria_frame, font=('Roboto', 12), state='disabled', width=50, height=30)
        self.et_cod_categoria.configure(state='disabled')
        self.et_cod_categoria.place(relx=0.34, rely=0.1)
        self.et_cod_categoria.focus_displayof()
        self.et_cod_categoria.place_forget()
        

        self.lbl_desc_categoria = CTkLabel(self.categoria_frame,text_color='#505050', text='Descrição da Categoria*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_desc_categoria.place(relx=0.27, rely=0.16)
        self.et_desc_categoria = CTkEntry(self.categoria_frame, font=('Roboto', 12), width=171, height=30, placeholder_text='Descrição')
        self.et_desc_categoria.focus()
        self.et_desc_categoria.place(relx=0.48, rely=0.15)

        self.btn_salvar_categoria = CTkButton(self.categoria_frame, 
                text=' Salvar', 
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.inserir_categoria)
        self.btn_salvar_categoria.place(relx=0.84, rely=0.1, relwidth=0.1)
        

        self.btn_lista_categoria = CTkButton(self.categoria_frame,  
                text=' Listar', 
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.exibir_categoria)
        self.btn_lista_categoria.place(relx=0.84, rely=0.19, relwidth=0.1)

        self.btn_alterar_categoria = CTkButton(self.categoria_frame,  
                text=' Alterar',  
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050',
                height=40,
                command=self.editar_categoria)
        self.btn_alterar_categoria.place(relx=0.84, rely=0.28, relwidth=0.1)

        self.btn_excluir_categoria = CTkButton(self.categoria_frame,  
                text=' Excluir',
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.deletar_categoria)
        self.btn_excluir_categoria.place(relx=0.84, rely=0.37, relwidth=0.1)

        self.listaCategoria = ttk.Treeview(self.categoria_frame, height=3, columns=('Col1', 'Col2'), show='headings')

        self.listaCategoria.heading('#0', text='')
        self.listaCategoria.heading('#1', text='Código')
        self.listaCategoria.heading('#2', text='Descrição da Categoria')

        self.listaCategoria.column('#0', width=1)
        self.listaCategoria.column('#1', width=70, minwidth=70, stretch=NO, anchor='center')
        self.listaCategoria.column('#2', width=270, minwidth=270, stretch=NO, anchor='center')
        self.listaCategoria.place(relx=0.26, rely=0.43, relwidth=0.45, relheight=0.5)

        self.scrollListaCat = CTkScrollbar(self.categoria_frame, orientation='vertical', command=self.listaCategoria.yview)
        self.listaCategoria.configure(yscrollcommand=self.scrollListaCat.set)
        self.scrollListaCat.place(relx=0.71, rely=0.43, relwidth= 0.02, relheight=0.5)
        self.listaCategoria.bind("<Double-1>", self.duplo_clique_cat)
        self.exibir_categoria()

    # CONFIGURAÇÕES DA TELA PRODUTO
    def widgets_produto(self):
        self.produto_frame = CTkFrame(self.frameMenu_right, fg_color='#fff')
        self.produto_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        lbl_titulo_prod = CTkLabel(self.produto_frame,text_color='#505050', text='GERENCIAR PRODUTO', font=('Roboto', 15))
        lbl_titulo_prod.place(relx=0.4, rely=0.01)
        
        #self.lbl_cod_produto = CTkLabel(self.produto_frame, text='Código: ', font=('Roboto', 12, 'bold'))
        #self.lbl_cod_produto.place(relx=0.02, rely=0.1)
        self.et_cod_produto = CTkEntry(self.produto_frame, font=('Roboto', 12), state='disabled', width=50, height=30)
        self.et_cod_produto.place(relx=0.1, rely=0.1)
        self.et_cod_produto.place_forget()
        self.et_cod_produto.focus_displayof()
        
        self.lbl_mode_produto = CTkLabel(self.produto_frame,text_color='#505050', text='Modelo*: ', font=('Roboto', 12, 'bold'))
        self.lbl_mode_produto.place(relx=0.02, rely=0.17)
        self.et_mode_produto = CTkEntry(self.produto_frame, font=('Roboto', 12), width=150, height=30, placeholder_text='Modelo do produto')
        self.et_mode_produto.place(relx=0.1, rely=0.17)
        
        self.lbl_desc_produto = CTkLabel(self.produto_frame, text_color='#505050',text='Descrição*: ', font=('Roboto', 12, 'bold'))
        self.lbl_desc_produto.place(relx=0.02, rely=0.1)
        self.et_desc_produto = CTkEntry(self.produto_frame, font=('Roboto', 12), width=150, height=30, placeholder_text='Descrição do produto')
        self.et_desc_produto.focus()
        self.et_desc_produto.place(relx=0.1, rely=0.1)

        self.lbl_preco_comp_produto = CTkLabel(self.produto_frame,text_color='#505050', text='Preço Compra*: ', font=('Roboto', 12, 'bold'))
        self.lbl_preco_comp_produto.place(relx=0.02, rely=0.24)
        self.et_preco_comp_produto = CTkEntry(self.produto_frame,font=('Roboto', 12), width=125, height=30, placeholder_text='Preço de compra')
        self.et_preco_comp_produto.place(relx=0.125, rely=0.24)
        

        self.lbl_preco_ven_produto = CTkLabel(self.produto_frame,text_color='#505050', text='Preço Venda*: ', font=('Roboto', 12, 'bold'))
        self.lbl_preco_ven_produto.place(relx=0.34, rely=0.1)
        self.et_preco_ven_produto = CTkEntry(self.produto_frame, font=('Roboto', 12), width=125, height=30, placeholder_text='Preço de venda')
        self.et_preco_ven_produto.place(relx=0.435, rely=0.1)

        #self.lbl_qtd_produto = CTkLabel(self.produto_frame, text='Qtd: ', font=('Roboto', 12, 'bold'))
        #self.lbl_qtd_produto.place(relx=0.16, rely=0.1)
        self.et_qtd_produto = CTkEntry(self.produto_frame, font=('Roboto', 12), state='readonly', width=63, height=30)
        self.et_qtd_produto.place(relx=0.19, rely=0.1)
        self.et_qtd_produto.place_forget()
        self.et_qtd_produto.focus_displayof()

        self.lbl_cat_produto = CTkLabel(self.produto_frame,text_color='#505050', text='Categoria*: ', font=('Roboto', 12, 'bold'))
        self.lbl_cat_produto.place(relx=0.34, rely=0.16)
        self.et_categoria = StringVar(self.produto_frame)
        self.et_categoria.set('')
        self.lista = self.exibir_categ_prod()
        if len(self.lista) == 0:
            self.lista = " "
        self.popupMenu = OptionMenu(self.produto_frame, self.et_categoria, *self.lista)
        self.popupMenu.place(relx=0.435, rely=0.17, width=126, height=22)

        self.lbl_consulta_produto = CTkLabel(self.produto_frame,text_color='#505050', text='Buscar Descrição: ', font=('Roboto', 12, 'bold'))
        self.lbl_consulta_produto.place(relx=0.78, rely=0.06)
        self.et_consulta_produto = CTkEntry(self.produto_frame, font=('Roboto', 12),  width=130, height=30, placeholder_text='Buscar')
        self.et_consulta_produto.place(relx=0.78, rely=0.1)
        
        self.btn_consulta_produto = CTkButton(self.produto_frame, 
                image=self.img_procurar,
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.consu_produto)
        self.btn_consulta_produto.place(relx=0.92, rely=0.1, relwidth=0.05, relheight=0.055)

        self.btn_salvar_produto = CTkButton(self.produto_frame, 
                text=' Salvar', 
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.inserir_produto)
        self.btn_salvar_produto.place(relx=0.88, rely=0.165, relwidth=0.09)

        self.btn_alterar_produto = CTkButton(self.produto_frame, 
                text=' Alterar',
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.editar_produto)
        self.btn_alterar_produto.place(relx=0.88, rely=0.245, relwidth=0.09)

        self.btn_excluir_produto = CTkButton(self.produto_frame,  
                text=' Excluir', 
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.deletar_produto)
        self.btn_excluir_produto.place(relx=0.88, rely=0.325, relwidth=0.09)

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

        self.scrollListaProd = CTkScrollbar(self.produto_frame, orientation='vertical', command=self.listaProd.yview)

        self.listaProd.configure(yscrollcommand=self.scrollListaProd.set)
        self.scrollListaProd.place(relx=0.975, rely=0.48, relwidth= 0.02, relheight=0.48)

        self.scrollHor = CTkScrollbar(self.produto_frame, orientation='horizontal')
        self.listaProd.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.02, rely=0.965, relwidth=0.1, relheight=0.03)
        self.listaProd.bind("<Double-1>", self.duplo_clique_prod)
        self.exibir_produto()

    # CONFIGURAÇÕES DA TELA FORNECEDOR
    def widgets_fornecedor(self) -> None:
        self.frameCadTelaFornecedor = CTkFrame(self.frameMenu_right, fg_color='#fff')
        self.frameCadTelaFornecedor.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
        
        lbl_titulo_fornecedor = CTkLabel(self.frameCadTelaFornecedor,text_color='#505050', text='GERENCIAR FORNECEDOR', font=('Roboto', 15))
        lbl_titulo_fornecedor.place(relx=0.39, rely=0.01)

        #self.lbl_cod_fornecedor = CTkLabel(self.frameCadTelaFornecedor, text='Código:', font=('Roboto', 12, 'bold'), height=20)
        #self.lbl_cod_fornecedor.place(relx=0.02, rely=0.1)
        self.et_cod_fornecedor = CTkEntry(self.frameCadTelaFornecedor, font=('Roboto', 12), state='disabled', width=50, height=30)
        self.et_cod_fornecedor.place(relx=0.1, rely=0.1)
        self.et_cod_fornecedor.place_forget()
        self.et_cod_fornecedor.focus_displayof()

        self.lbl_cnpj_fornecedor = CTkLabel(self.frameCadTelaFornecedor,text_color='#505050', text='CNPJ/CPF*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_cnpj_fornecedor.place(relx=0.02, rely=0.11)
        self.et_cnpj_fornecedor = CTkEntry(self.frameCadTelaFornecedor,text_color='#505050', font=('Roboto', 12), width=220, height=30, placeholder_text='CNPJ')
        self.et_cnpj_fornecedor.focus()
        self.et_cnpj_fornecedor.place(relx=0.1, rely=0.1)

        self.lbl_nome_fornecedor = CTkLabel(self.frameCadTelaFornecedor,text_color='#505050', text='Nome*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_nome_fornecedor.place(relx=0.02, rely=0.18)
        self.et_nome_fornecedor = CTkEntry(self.frameCadTelaFornecedor, font=('Roboto', 12), width=220, height=30, placeholder_text='Nome completo')
        self.et_nome_fornecedor.place(relx=0.1, rely=0.17)

        self.lbl_email_fornecedor = CTkLabel(self.frameCadTelaFornecedor,text_color='#505050', text='E-mail*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_email_fornecedor.place(relx=0.02, rely=0.25)
        self.et_email_fornecedor = CTkEntry(self.frameCadTelaFornecedor, font=('Roboto', 12), width=220, height=30, placeholder_text='E-mail')
        self.et_email_fornecedor.place(relx=0.1, rely=0.24)

        self.lbl_tel_fornecedor = CTkLabel(self.frameCadTelaFornecedor,text_color='#505050', text='Telefone*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_tel_fornecedor.place(relx=0.02, rely=0.32)
        self.et_tel_fornecedor = CTkEntry(self.frameCadTelaFornecedor, font=('Roboto', 12), width=220, height=30, placeholder_text='Telefone')
        self.et_tel_fornecedor.place(relx=0.1, rely=0.31)

        self.lbl_logr_fornecedor = CTkLabel(self.frameCadTelaFornecedor,text_color='#505050', text='Endereço*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_logr_fornecedor.place(relx=0.34, rely=0.1)
        self.et_logr_fornecedor = CTkEntry(self.frameCadTelaFornecedor, font=('Roboto', 12), width=220, height=30, placeholder_text='Endereço')
        self.et_logr_fornecedor.place(relx=0.415, rely=0.1)

        self.lbl_num_fornecedor = CTkLabel(self.frameCadTelaFornecedor,text_color='#505050', text='Número*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_num_fornecedor.place(relx=0.35, rely=0.18)
        self.et_num_fornecedor = CTkEntry(self.frameCadTelaFornecedor, font=('Roboto', 12), width=60, height=30, placeholder_text='Número')
        self.et_num_fornecedor.place(relx=0.415, rely=0.17)

        self.lbl_cep_fornecedor = CTkLabel(self.frameCadTelaFornecedor,text_color='#505050', text='CEP*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_cep_fornecedor.place(relx=0.49, rely=0.18)
        self.et_cep_fornecedor = CTkEntry(self.frameCadTelaFornecedor, font=('Roboto', 12), width=107, height=30, placeholder_text='CEP')
        self.et_cep_fornecedor.place(relx=0.532, rely=0.17)

        self.lbl_cidade_fornecedor = CTkLabel(self.frameCadTelaFornecedor,text_color='#505050', text='Cidade*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_cidade_fornecedor.place(relx=0.35, rely=0.25)
        self.et_cidade_fornecedor = CTkEntry(self.frameCadTelaFornecedor, font=('Roboto', 12),width=220, height=30, placeholder_text='Cidade')
        self.et_cidade_fornecedor.place(relx=0.415, rely=0.24)

        self.lbl_estado_fornecedor = CTkLabel(self.frameCadTelaFornecedor, text_color='#505050',text='Estado*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_estado_fornecedor.place(relx=0.35, rely=0.32)
        self.et_estado_fornecedor = CTkEntry(self.frameCadTelaFornecedor, font=('Roboto', 12), width=220, height=30, placeholder_text='Estado')
        self.et_estado_fornecedor.place(relx=0.415, rely=0.31)
        
        self.btn_consultar = CTkButton(self.frameCadTelaFornecedor,
                image=self.img_procurar,
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.pesquisar_fornecedor)
        self.btn_consultar.place(relx=0.92, rely=0.1, relwidth=0.05, relheight=0.055)

        self.lbl_pes_forn = CTkLabel(self.frameCadTelaFornecedor,text_color='#505050', text='Buscar Nome: ', font=('Roboto', 12, 'bold'))
        self.lbl_pes_forn.place(relx=0.78, rely=0.065)
        self.et_consultar_forne = CTkEntry(self.frameCadTelaFornecedor, font=('Roboto', 12), width=130, height=30, placeholder_text='Buscar')
        self.et_consultar_forne.place(relx=0.78, rely=0.10)

        self.btn_salvar = CTkButton(self.frameCadTelaFornecedor, 
                text='Salvar',
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.inserir_fornecedor)
        self.btn_salvar.place(relx=0.88, rely=0.165, relwidth=0.09)

        self.btn_alterar = CTkButton(self.frameCadTelaFornecedor,
                text="Alterar",
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.alterar_fornecedor)
        self.btn_alterar.place(relx=0.88, rely=0.245, relwidth=0.09)

        self.btn_excluir = CTkButton(self.frameCadTelaFornecedor,
                text="Excluir",
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.excluir_fornecedor)
        self.btn_excluir.place(relx=0.88, rely=0.325, relwidth=0.09)

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
        self.listaForne.heading('#8', text='CEP')
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
        
        self.scrollListaForne = CTkScrollbar(self.frameCadTelaFornecedor, orientation='vertical', command=self.listaForne.yview)
        self.listaForne.configure(yscrollcommand=self.scrollListaForne.set)
        self.scrollListaForne.place(relx=0.97, rely=0.48, relwidth= 0.02, relheight=0.49)
        
        self.scrollHor = CTkScrollbar(self.frameCadTelaFornecedor, orientation='horizontal', command=self.listaForne.xview)
        self.listaForne.configure(xscrollcommand=self.scrollHor.set)
        self.scrollHor.place(relx=0.02, rely=0.97, relwidth=0.08, relheight=0.03)
        self.listaForne.bind("<Double-1>", self.duplo_clique_for)
        self.lista_fornecedor()

    def widgets_fornecimento(self):
        
        self.fornecimento_frame = CTkFrame(self.frameMenu_right, fg_color='#fff')
        self.fornecimento_frame.place(relx=0.12, rely=0.12, relwidth=0.75, relheight=0.75)

        lbl_titulo_fornecimento = CTkLabel(self.fornecimento_frame,text_color='#505050', text='VISUALIZAR FORNECIMENTO', font=('Roboto', 15))
        lbl_titulo_fornecimento.place(relx=0.35, rely=0.01)

        self.lbl_produto = CTkLabel(self.fornecimento_frame,text_color='#505050', text='Produto*: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_produto.place(relx=0.02, rely=0.1)
        self.dadosRecebidosProduto = list(self.fornecimentoProduto())

        self.comboxProduto = ttk.Combobox(self.fornecimento_frame, values=self.dadosRecebidosProduto, width=40, height=22)
        self.comboxProduto.place(relx=0.13, rely=0.1)
        
        self.lbl_fornecedor_fornecimento = CTkLabel(self.fornecimento_frame,text_color='#505050', text='Fornecedor*: ', font=('Roboto', 12, 'bold'), height=25)
        self.lbl_fornecedor_fornecimento.place(relx=0.02, rely=0.18)
        self.dadosRecebidosFornecedor = self.fornecimentoFornecedor()
        self.comboxFornecedor = ttk.Combobox(self.fornecimento_frame, values=self.dadosRecebidosFornecedor, width=40, height=25)
        self.comboxFornecedor.place(relx=0.13, rely=0.18)

        self.lbl_data_fornecimento = CTkLabel(self.fornecimento_frame, text_color='#505050',text='Data Forneci*.: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_data_fornecimento.place(relx=0.02, rely=0.27)
        self.et_data_fornecimento = CTkEntry(self.fornecimento_frame, width=80, height=22, placeholder_text='Data')
        self.et_data_fornecimento.place(relx=0.16, rely=0.27)
        self.btn_calendario = CTkButton(self.fornecimento_frame, 
                text='Inserir', 
                text_color='#fff',
                font=('Roboto', 12, 'bold'),
                fg_color='#505050', 
                width=65, 
                height=22, 
                hover_color='#333',
                command=self.calendario)
        self.btn_calendario.place(relx=0.27, rely=0.27)

        self.qtd_fornecida = CTkLabel(self.fornecimento_frame,text_color='#505050', text='Qtd Fornecida*: ', font=('Roboto', 12, 'bold'), height=20)
        self.qtd_fornecida.place(relx=0.02, rely=0.35)
        self.et_qtd_fornecida = CTkEntry(self.fornecimento_frame, width=62, height=20, placeholder_text='Qtd')
        self.et_qtd_fornecida.place(relx=0.16, rely=0.35) 

        self.btn_salvarFornecimento = CTkButton(self.fornecimento_frame,
                text="Salvar",
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.inserir_fornecimento)
        self.btn_salvarFornecimento.place(relx=0.88, rely=0.18, relwidth=0.09)

        self.btn_listarFornecimento = CTkButton(self.fornecimento_frame, 
                text="Listar",
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                fg_color='#505050', 
                height=40,
                command=self.exibir_fornecimento)
        self.btn_listarFornecimento.place(relx=0.88, rely=0.29, relwidth=0.09)
        
        self.btn_buscarFornecimento = CTkButton(self.fornecimento_frame, 
                image=self.img_procurar,
                text_color='#fff',
                hover_color='#333',
                font=('Roboto', 12, 'bold'),   
                fg_color='#505050', 
                command=self.buscar_fornecimento)
        self.btn_buscarFornecimento.place(relx=0.91, rely=0.1, relwidth=0.06, relheight=0.065)
        self.lbl_buscarForn = CTkLabel(self.fornecimento_frame,text_color='#505050', text='Buscar Fornecedor: ', font=('Roboto', 12, 'bold'), height=20)
        self.lbl_buscarForn.place(relx=0.735, rely=0.06)
        self.et_consu_forneci = CTkEntry(self.fornecimento_frame,width=130, height=26, placeholder_text='Buscar')
        self.et_consu_forneci.place(relx=0.735, rely=0.1)

        self.listaFornecimento = ttk.Treeview(self.fornecimento_frame, height=3 ,columns=('Col1','Col2', 'Col3', 'Col4'),show = 'headings')
        self.listaFornecimento.heading("#0", text='')
        self.listaFornecimento.heading("#1", text='Produto')
        self.listaFornecimento.heading('#2', text='Fornecedor')
        self.listaFornecimento.heading('#3', text='Data Fornecimento')
        self.listaFornecimento.heading('#4', text='Qtd Fornecida') 

        self.listaFornecimento.column('#0', width=1, anchor='center')
        self.listaFornecimento.column('#1', width=120, anchor='center')
        self.listaFornecimento.column('#2', width=120, anchor='center')
        self.listaFornecimento.column('#3', width=80, anchor='center')
        self.listaFornecimento.column('#4', width=80, anchor='center')

        self.listaFornecimento.place(relx=0.025, rely=0.46, relwidth=0.95, relheight=0.5)
        self.listaFornecimento.bind("<Double-1>", self.duplo_clique_fornecimento)

        self.scrollListaFornecimento = CTkScrollbar(self.fornecimento_frame, orientation='vertical', command=self.listaFornecimento.yview)
        self.listaFornecimento.configure(yscrollcommand=self.scrollListaFornecimento.set)
        self.scrollListaFornecimento.place(relx=0.975, rely=0.46, relwidth= 0.02, relheight=0.5)
        self.exibir_fornecimento()
    def widgets_venda(self):

        self.frameCadTelaVenda = CTkFrame(self.frameMenu_right, fg_color='#fff')
        self.frameCadTelaVenda.place(relx=0.12, rely=0.025, relwidth=0.75, relheight=0.95)
        
        lbl_titulo_venda = CTkLabel(self.frameCadTelaVenda,text_color='#505050', text='GERENCIAR VENDA', font=('Roboto', 15))
        lbl_titulo_venda.place(relx=0.4, rely=0.01)

        self.lbl_nome_clien_venda = CTkLabel(self.frameCadTelaVenda,text_color='#505050', text="Cliente*: ", font=('Roboto', 12, 'bold'))
        self.lbl_nome_clien_venda.place(relx=0.025, rely=0.09) 
        self.cliRecebidos = self.clienteVenda()
        self.comboxClien_venda = ttk.Combobox(self.frameCadTelaVenda, values=self.cliRecebidos)
        self.comboxClien_venda.place(relx=0.1, rely=0.1, width=300, height=20)

        self.lbl_data_venda = CTkLabel(self.frameCadTelaVenda, text_color='#505050',
                text='Data Venda*: ', 
                font=('Roboto', 12, 'bold'), height=20)
        self.lbl_data_venda.place(relx=0.025, rely=0.16)
        self.et_data_venda = CTkEntry(self.frameCadTelaVenda, width=75, height=20, placeholder_text='Data')
        self.et_data_venda.place(relx=0.14, rely=0.16)

        self.btn_calendario = CTkButton(self.frameCadTelaVenda,
                text='Selecionar', 
                font=('Roboto', 12, 'bold'), 
                width=65, 
                height=22,
                text_color='#fff',
                hover_color='#333',
                fg_color='#505050', 
                command=self.calendariove)
        self.btn_calendario.place(relx=0.24, rely=0.16)

        self.lbl_exibi_total = CTkLabel(self.frameCadTelaVenda, font=('Roboto', 12, 'bold'))
        self.lbl_exibi_total.place(relx=0.5, rely=0.93)
        
        
        self.btn_salvar_venda = CTkButton(self.frameCadTelaVenda,text='Registrar \nVenda',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center',
                text_color='#fff',
                hover_color='#333',
                fg_color='#505050',
                height=50,
                command=self.inserir_venda)
        self.btn_salvar_venda.place(relx=0.89, rely=0.1, relwidth=0.09)


        # VISUAL DO CARRINHO
        self.cabecalhoAdd = LabelFrame(self.frameCadTelaVenda, text='Carrinho', font=('Roboto', 14), bg='#fff')
        self.cabecalhoAdd.place(relx=0.02, rely=0.25, relwidth=0.96, relheight=0.73)

        self.lbl_prodt_venda = CTkLabel(self.cabecalhoAdd, text_color='#505050',text="Produto*: ", font=('Roboto', 12, 'bold'))
        self.lbl_prodt_venda.place(relx=0.025, rely=0.09) 
        self.prodRecebidos = self.produtosVenda()
        self.comboxaddItens = ttk.Combobox(self.cabecalhoAdd, values=self.prodRecebidos)
        self.comboxaddItens.place(relx=0.11, rely=0.1, width=300, height=20)

        self.lbl_qtd_venda = CTkLabel(self.cabecalhoAdd,text_color='#505050', text="Qtd*: ", font=('Roboto', 12, 'bold'))
        self.lbl_qtd_venda.place(relx=0.025, rely=0.19) 
        self.et_qtd_venda = CTkEntry(self.cabecalhoAdd, height=20, font=('Roboto', 12), width=70)
        self.et_qtd_venda.place(relx=0.07, rely=0.2) 

        self.btn_add_prod = CTkButton(self.cabecalhoAdd, 
                text='Adicionar',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center', 
                height=20, 
                text_color='#fff',
                hover_color='#333',
                fg_color='#505050',
                command=self.adicionaItens_venda)
        self.btn_add_prod.place(relx=0.855, rely=0.4, relwidth=0.12)

        self.btn_remov_prod = CTkButton(self.cabecalhoAdd, 
                text='Remover',
                font=('Roboto', 12, 'bold'), 
                compound='left', 
                anchor='center',  
                height=20,
                text_color='#fff',
                hover_color='#333',
                fg_color='#505050',
                command=self.remover_produto_venda)
        self.btn_remov_prod.place(relx=0.855, rely=0.48, relwidth=0.12)

        self.listaAddItens = ttk.Treeview(self.cabecalhoAdd, height=3, columns=('Col1', 'Col2', 'Col3', 'col4', 'col5'), show='headings')
        
        self.listaAddItens.heading("#0", text='')
        self.listaAddItens.heading('#1', text='Cód produto')
        self.listaAddItens.heading('#2', text='Descrição')
        self.listaAddItens.heading('#3', text='Modelo')
        self.listaAddItens.heading('#4', text='Valor Unitário')
        self.listaAddItens.heading('#5', text='Quantidade')
        
        self.listaAddItens.column('#0', width=1, anchor='center')
        self.listaAddItens.column('#1', width=50, anchor='center')
        self.listaAddItens.column('#2', width=50, anchor='center')
        self.listaAddItens.column('#3', width=50, anchor='center')
        self.listaAddItens.column('#4', width=50, anchor='center')
        self.listaAddItens.column('#5', width=50, anchor='center')
        
        self.listaAddItens.place(relx=0.02, rely=0.4, relwidth=0.8, relheight=0.45)

        self.scrollListaHistTela = CTkScrollbar(self.cabecalhoAdd, orientation='vertical', command=self.listaAddItens.yview)

        self.listaAddItens.configure(yscrollcommand=self.scrollListaHistTela.set)
        self.scrollListaHistTela.place(relx=0.82, rely=0.4, relwidth= 0.02, relheight=0.45)

        self.lbl_totalGeral = CTkLabel(self.frameCadTelaVenda, text='TOTAL DA COMPRA R$: ', font=('Roboto', 12, 'bold'))
        self.lbl_totalGeral.place(relx=0.04, rely=0.905)
        
        self.tot = DoubleVar()
        self.lbl_exibGeral = CTkLabel(self.frameCadTelaVenda, textvariable=self.tot, font=('Roboto', 12, 'bold'))
        self.lbl_exibGeral.place(relx=0.25, rely=0.905)
        

    def widgets_relatorio(self) ->None: 
        self.relatorio_frame = CTkFrame(self.frameMenu_right, fg_color='#fff')
        self.relatorio_frame.place(relx=0.12, rely=0.12, relwidth=0.75, relheight=0.75)
        
        lbl_titulo_relatorio = CTkLabel(self.relatorio_frame,text_color='#505050', text='VISUALIZAR VENDAS', font=('Roboto', 15))
        lbl_titulo_relatorio.place(relx=0.4, rely=0.01)
        
        self.lbl_consultar = CTkLabel(self.relatorio_frame,text_color='#505050', text='Código:', font=('Roboto', 12,'bold'))
        self.lbl_consultar.place(relx=0.4, rely=0.150)
        self.et_consultar = CTkEntry(self.relatorio_frame, font=('Roboto', 14), width=60, height=26, placeholder_text='Cód')
        self.et_consultar.place(relx=0.4, rely=0.20)

        self.btn_consultar = CTkButton(self.relatorio_frame,text='Buscar',
                command=self.consultarVenda, 
                image=self.img_procurar,
                font=('Roboto', 10,'bold'), 
                fg_color='#505050')
        self.btn_consultar.place(relx=0.49, rely=0.2, relwidth=0.07, relheight=0.06)
        
        self.btn_listar = CTkButton(self.relatorio_frame, 
                text='Listar', 
                text_color='#fff',
                font=('Roboto', 12,'bold'),
                height=40,
                fg_color='#505050', 
                hover_color='#333',
                command=self.listarVenda)
        self.btn_listar.place(relx= 0.87, rely=0.2, relwidth=0.1)
        
        self.btn_gerarPDF = CTkButton(self.relatorio_frame, 
                text='Gerar PDF',
                text_color='#fff', 
                font=('Roboto', 12,'bold'), 
                height=40, 
                fg_color='#505050',
                hover_color='#333',
                command=self.gerarRelPDF)
        self.btn_gerarPDF.place(relx= 0.87, rely= 0.3, relwidth=0.1)
        
        
        self.listaRelatorio = ttk.Treeview(self.relatorio_frame, height= 3, columns= ('Col1', 'Col2', 'Col3', 'Col4', 'Col5'), show= 'headings')
        self.listaRelatorio.heading("#0", text='')
        self.listaRelatorio.heading("#1", text='Código da Venda')
        self.listaRelatorio.heading("#2", text='Cliente')
        self.listaRelatorio.heading("#3", text='CPF')
        self.listaRelatorio.heading("#4", text='Valor')
        self.listaRelatorio.heading("#5", text='Data da Venda')
        
        self.listaRelatorio.column("#0", width=1, minwidth=1 ,anchor='center')
        self.listaRelatorio.column("#1", width=70, minwidth=80 ,anchor='center')
        self.listaRelatorio.column("#2", width=240, minwidth=90 ,anchor='center')
        self.listaRelatorio.column("#3", width=100, minwidth=90 ,anchor='center')
        self.listaRelatorio.column("#4", width=90, minwidth=90 ,anchor='center')
        self.listaRelatorio.column("#5", width=80, minwidth=90 ,anchor='center')
        
        self.listaRelatorio.place(relx=0.025, rely=0.46, relwidth=0.95, relheight=0.5)
        
        self.scrolllistaRelatorio = CTkScrollbar(self.relatorio_frame, orientation='vertical', command=self.listaRelatorio.yview)
        self.listaRelatorio.configure(yscrollcommand= self.scrolllistaRelatorio.set)
        self.scrolllistaRelatorio.place(relx=0.975, rely=0.46, relwidth= 0.02, relheight=0.5)
        self.listarVenda()

LoginTela()
   
