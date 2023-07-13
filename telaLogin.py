from tkinter import *
from telaMudaSenha import MudarSenhaTela


appLogin = Tk()

class LoginTela:

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
        self.titulo_login.place(relx=0.4, rely=0.12)
        self.titulo_login.configure(background='#585858',font=("Roboto", 24,"bold"))

    def widgets_tela_login(self):
        # Criação dos widgets (rótulos, campos de entrada e botão)
        self.lbl_usuario = Label(self.appLogin, text="Usuário:",fg='#FFF')
        self.lbl_usuario.place(relx=0.3, rely=0.31)
        self.lbl_usuario.configure(background='#585858',font=("Roboto", 12))
        self.et_usuario = Entry(appLogin, font=('Roboto', 12))
        self.et_usuario.place(relx=0.43, rely=0.32, width=120)

        self.lbl_senha = Label(self.appLogin, text="Senha:",fg='#FFF')
        self.lbl_senha.place(relx=0.32, rely=0.45)
        self.lbl_senha.configure(background='#585858',font=("Roboto", 12))
        self.et_senha = Entry(self.appLogin, font=('Roboto', 12), show="*")  
        self.et_senha.place(relx=0.43, rely=0.46, width=120)

        self.img_logar = PhotoImage(file="imagens/logar.png")
        self.btn_login = Button(self.appLogin, image=self.img_logar,bg="#FFF")
        self.btn_login.place(relx=0.44, rely=0.59, width=90, height=50)

        self.img_mudar_senha = PhotoImage(file="imagens/alterar_senha.png")
        self.btn_alterarsenha = Button(self.appLogin, bd=0, image=self.img_mudar_senha, bg='#FFF', fg='#FFF', command=MudarSenhaTela)
        self.btn_alterarsenha.place(relx=0.44, rely=0.8, width=90, height=50)

LoginTela()
   



