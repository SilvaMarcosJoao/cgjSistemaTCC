from tkinter import *
from telaMudaSenha import MudarSenhaTela
from tkinter import messagebox
from telaMenu import MenuTela
from modulos.usuario import Usuario

appLogin = Tk()

class LoginTela():
    usuario = Usuario()
    def __init__(self) -> None:
        self.appLogin = appLogin
        self.config_tela_login()
        self.widgets_tela_login()
        self.appLogin.mainloop()
        
    def config_tela_login(self) -> None:
        self.appLogin.title('Sistema de Gerenciamento (SGZurc)') 
        self.appLogin.configure(bg='#585858')
        self.larTela = 600
        self.altTela = 350

        self.lMonitor = self.appLogin.winfo_screenwidth()
        self.aMonitor = self.appLogin.winfo_screenheight()
        self.posX = (self.lMonitor / 2) - (self.larTela / 2)
        self.posY = (self.aMonitor / 2) - (self.altTela / 2)
        self.appLogin.geometry("%dx%d+%d+%d" % (self.larTela, self.altTela, self.posX, self.posY))
        self.appLogin.minsize(width=600, height=350)
        self.appLogin.resizable(False, False)
        
        self.titulo_login = Label(self.appLogin, text="SGZurc",fg='#FFF')
        self.titulo_login.place(relx=0.4, rely=0.1)
        self.titulo_login.configure(background='#585858',font=("Roboto", 24,"bold"))

    def widgets_tela_login(self):
        # Criação dos widgets (rótulos, campos de entrada e botão)
        self.lbl_usuario = Label(self.appLogin, text="Usuário:",fg='#FFF')
        self.lbl_usuario.place(relx=0.3, rely=0.3)
        self.lbl_usuario.configure(background='#585858',font=("Roboto", 12, 'bold'))
        self.et_usuario = Entry(appLogin, font=('Roboto', 12))
        self.et_usuario.place(relx=0.42, rely=0.3, width=120)

        self.lbl_senha = Label(self.appLogin, text="Senha:",fg='#FFF')
        self.lbl_senha.place(relx=0.32, rely=0.4)
        self.lbl_senha.configure(background='#585858',font=("Roboto", 12, 'bold'))
        self.et_senha = Entry(self.appLogin, font=('Roboto', 12), show="*")  
        self.et_senha.place(relx=0.42, rely=0.4, width=120)

        self.img_logar = PhotoImage(file="imagens/logar.png")
        self.btn_login = Button(self.appLogin, image=self.img_logar,bg="#FFF", command=self.efetuarLogin)
        self.btn_login.place(relx=0.44, rely=0.59, width=90, height=50)

        self.img_mudar_senha = PhotoImage(file="imagens/alterar_senha.png")
        self.btn_alterarsenha = Button(self.appLogin, bd=0, image=self.img_mudar_senha, bg='#FFF', fg='#FFF', command=MudarSenhaTela)
        self.btn_alterarsenha.place(relx=0.44, rely=0.8, width=90, height=50)
    
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
                    
                    MenuTela()
                    self.appLogin.destroy()
                else:
                    print(self.resUser[0])
                    messagebox.showwarning('Atenção', 'Usuário ou senha inválidos!')
                    self.limpa_usuario()
        except:
            messagebox.showerror('Erro', 'Houve um erro, não foi possível efetuar login')
        
        
    def limpa_usuario(self):
        self.et_usuario.delete(0,END)
        self.et_senha.delete(0,END)
    
LoginTela()
   



