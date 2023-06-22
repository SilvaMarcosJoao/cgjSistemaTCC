from tkinter import *
from tkinter import messagebox
from modulos.categoriaproduto import CategoriaProduto

class Funcionalidades:
    categoria = CategoriaProduto()
    def __init__(self):
        self.caractere = None
        self.numInt = None

    def valida_string(self,texto: str) -> str:
        '''
        Esta função recebe um parâmetro qualquer para ser validado
        se é ou não uma String
        :param texto: recebe uma cadeia de caractere
        :return v: retorna a string após ser validada
        '''
        try:
            self.caractere = str(input(texto)).strip()
        except (ValueError, TypeError, FloatingPointError):
            print('\033[1;31mErro, valor digitado não é compatível com um texto\033[m')

        else:
            return self.caractere

    def valida_int(self, valor: int) -> int:
        '''
            Esta função recebe um parâmetro qualquer para ser validado
            se é ou não um valor inteiro
            :param valor: recebe um valor
            :return v: retorna o valor validado
            '''
        while True:
            try:
                self.numInt = int(input(valor))
            except ValueError:
                print('\033[1;31mValor inválido\033[m')
            except TypeError:
                print('\033[1;31mTipo de valor errado\033[m')
            else:
                return self.numInt
            
    def mudar_senha(self) -> None:
        if self.et_nova_senha.get() == '' or self.et_confir_senha.get() == '':
            messagebox.showwarning('Alerta', 'Preencha os campos')
        elif len(self.et_nova_senha.get()) != 8 or len(self.et_confir_senha.get()) != 8:
            messagebox.showwarning('Alerta', 'A senha deve conter 8 caracteres')
        elif self.et_nova_senha.get() != self.et_confir_senha.get():
            messagebox.showinfo('Alerta', 'Senhas diferentes')     
        else:
            self.senha = self.et_nova_senha.get()
            self.conf = self.et_confir_senha.get()
            self.usuario.alterar_senha(self.senha)
            self.msg_avi = 'Senha alterada com sucesso!'
            messagebox.showinfo('Aviso', self.msg_avi)
            self.limpa_usuario()     
    
    
    def inserir_categoria(self):
        self.desc = self.et_desc_categoria.get()
        self.categoria.cadastrarCategoria(self.desc)
        self.limpa_categoria()

    def exibir_categoria(self):
        self.listaCategoria.delete(*self.listaCategoria.get_children())
        self.exibir = self.categoria.listarCategoria()
        for i in self.exibir:
            self.listaCategoria.insert('',END, values=i)

    def editar_categoria(self):
        self.cod = self.et_cod_categoria.get()
        self.desc = self.et_desc_categoria.get()
        self.categoria.alterarCategoria(self.cod, self.desc)
        self.limpa_categoria()
        self.exibir_categoria()

    def excluir_categoria(self):
        self.cod = self.et_cod_categoria.get()
        self.categoria.deletarCategoria(self.cod)
        self.limpa_categoria()
        self.exibir_categoria()

    def duplo_clique_cat(self, event):
        self.limpa_categoria()
        self.listaCategoria.selection()
        for i in self.listaCategoria.selection():
            col1, col2 = self.listaCategoria.item(i, 'values')
            self.et_cod_categoria.insert(END, col1)
            self.et_desc_categoria.insert(END, col2) 
             
    def limpa_categoria(self):
        self.et_cod_categoria.delete(0, END)
        self.et_desc_categoria.delete(0, END)















    def limpa_usuario(self):
        self.et_nova_senha.delete(0, END)
        self.et_confir_senha.delete(0, END)

    

    


