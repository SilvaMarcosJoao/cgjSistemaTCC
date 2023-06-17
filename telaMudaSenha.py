from tkinter import *
from tkinter import messagebox
from modulos.usuario import Usuario

objUsuario = Usuario()

class MudarSenhaTela:

    def __init__(self) -> None:
        self.mudasenhatela = Toplevel()
        self.config_tela_muda_senha()
        self.widgets_tela_muda_senha()

    # Criação da janela principal

    def config_tela_muda_senha(self) -> None:
        self.mudasenhatela.title("Sistema de Gerenciamento (SGZurc)")
        self.mudasenhatela.configure(background='#585858')
        
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

    # Criação dos widgets (rótulos, campos de entrada e botão)
    def widgets_tela_muda_senha(self) -> None:

        self.titulo_login = Label(self.mudasenhatela, text="SGZurc",fg='#FFFFFF')
        self.titulo_login.place(relx=0.47, rely=0.15)
        self.titulo_login.configure(background='#585858',font=("Roboto", 15,"bold"))

        self.nova_senha = Label(self.mudasenhatela, text="Nova senha:",fg='#FFFFFF')
        self.nova_senha.place(relx=0.26, rely=0.31)
        self.nova_senha.configure(background='#585858',font=("Roboto", 12))
        self.et_nova_senha = Entry(self.mudasenhatela, font=('Roboto', 12), show='*')
        self.et_nova_senha.place(relx=0.44, rely=0.32, width=120)

        self.confirmar_senha = Label(self.mudasenhatela, text="Confirmar senha:",fg='#FFFFFF')
        self.confirmar_senha.place(relx=0.19, rely=0.45)
        self.confirmar_senha.configure(background='#585858',font=("Roboto", 12))
        self.et_conf_senha = Entry(self.mudasenhatela, font=('Roboto', 12), show='*')  
        self.et_conf_senha.place(relx=0.44, rely=0.46, width=120)

        self.btn_alterar = Button(self.mudasenhatela, text="Alterar", bg="#FFFFFF", fg="#151515", command=self.inter_muda_senha)
        self.btn_alterar.place(relx=0.45, rely=0.59, width=90, height=50)
    

    def inter_muda_senha(self) -> None:
        self.senha = self.et_nova_senha.get()
        self.repete_senha = self.et_conf_senha.get()
        try:
            objUsuario.alterar_senha(self.senha, self.repete_senha)

        except:
            self.msg_erro = 'Erro, por favor corrija!'
            messagebox.showerror('Erro',self.msg_erro)
        else:
            self.msg_avi = 'Senha alterada com sucesso!'
            messagebox.showinfo('Aviso', self.msg_avi)









