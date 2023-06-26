from tkinter import *
from tkinter import messagebox
from modulos.categoriaproduto import CategoriaProduto
from modulos.cliente import Cliente
from modulos.servico import Servico
from modulos.fornecedor import Fornecedor

class Funcionalidades:
    categoria = CategoriaProduto()
    cliente = Cliente()
    servico = Servico()
    fornecedor = Fornecedor()
    
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
    
    def limpa_usuario(self):
        self.et_nova_senha.delete(0, END)
        self.et_confir_senha.delete(0, END)
        
#CRUD de Categoria

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
        
        
#CRUD do Cliente 
    def  inserir_cliente(self):
        self.cpf = self.et_cpf_cliente.get() 
        self.nome = self.et_nome_cliente.get()
        self.email = self.et_email_cliente.get() 
        self.telefone = self.et_tel_cliente.get()   
        self.logradouro = self.et_logr_cliente.get()
        self.numero = self.et_num_cliente.get()
        self.cep = self.et_cep_cliente.get()       
        self.cidade = self.et_cidade_cliente.get()
        self.estado = self.et_estado_cliente.get()

        self.cliente.cadastrarCliente(self.cpf,self.nome,self.email,
                                      self.telefone,self.logradouro,self.numero,
                                      self.cep,self.cidade,self.estado)    
        self.limpa_cliente()
    
    def lista_cliente(self):
        self.listaCliente.delete(*self.listaCliente.get_children())
        self.lista = self.cliente.listarCliente()
        for i in self.lista:
            self.listaCliente.insert('',END, values=i)
  
            
    def alterar_cliente(self):
        self.cod = self.et_cod_cliente.get()
        self.cpf = self.et_cpf_cliente.get()
        self.nome = self.et_nome_cliente.get()
        self.email = self.et_email_cliente.get()
        self.telefone = self.et_tel_cliente.get()
        self.logradouro = self.et_logr_cliente.get()
        self.numero = self.et_num_cliente.get()
        self.cep = self.et_cep_cliente.get()
        self.cidade = self.et_cidade_cliente.get()
        self.estado = self.et_estado_cliente.get()
        self.cliente.alterarCliente(self.cod,self.cpf,self.nome,self.email,self.telefone,
                                    self.logradouro,self.numero,self.cep,self.cidade,
                                    self.estado)       
        self.lista_cliente()
    
    def excluir_cliente(self):
        self.codigo = self.et_cod_cliente.get()
        self.cliente.deletarCliente(self.codigo)
        self.limpa_cliente()
        self.lista_cliente()
        

    def duplo_clique_cliente(self, event):
        self.limpa_cliente()
        self.listaCliente.selection()
        for i in self.listaCliente.selection():
            col1, col2, col3, col4,col5, col6, col7, col8, col9,col10 = self.listaCliente.item(i, 'values')
            self.et_cod_cliente.insert(END,col1)
            self.et_cpf_cliente.insert(END, col2)
            self.et_nome_cliente.insert(END, col3) 
            self.et_email_cliente.insert(END, col4)
            self.et_tel_cliente.insert(END, col5)
            self.et_logr_cliente.insert(END, col6)
            self.et_num_cliente.insert(END, col7)
            self.et_cep_cliente.insert(END, col8)
            self.et_cidade_cliente.insert(END, col9)
            self.et_estado_cliente.insert(END, col10)
    
    def limpa_cliente(self):
        self.et_cod_cliente.delete(0,END)
        self.et_cpf_cliente.delete(0,END)
        self.et_nome_cliente.delete(0,END)
        self.et_email_cliente.delete(0,END)
        self.et_tel_cliente.delete(0,END)
        self.et_logr_cliente.delete(0,END)
        self.et_num_cliente.delete(0,END)
        self.et_cep_cliente.delete(0,END)
        self.et_cidade_cliente.delete(0,END)
        self.et_estado_cliente.delete(0,END)


#CRUD do Fornecedor
    def inserir_fornecedor(self):
        self.cnpj = self.et_cnpj_fornecedor.get()
        self.nome = self.et_nome_fornecedor.get()
        self.email = self.et_email_fornecedor.get()
        self.telefone = self.et_tel_fornecedor.get()
        self.logradouro = self.et_logr_fornecedor.get()
        self.numero = self.et_num_fornecedor.get()
        self.cep = self.et_cep_fornecedor.get()
        self.cidade = self.et_cidade_fornecedor.get()
        self.estado = self.et_estado_fornecedor.get()
        #self.qtd = self.et_qtd_fornecida_fornecedor.get()
       # self.data = self.et_data_fornecimento.get()
        
        self.fornecedor.cadastrarFornecedor(self.cnpj,self.nome,
                                             self.email, self.telefone, 
                                             self.logradouro, self.numero, 
                                             self.cep,self.cidade, 
                                             self.estado)
        self.limpa_fornecedor()
                
    def lista_fornecedor(self):
        self.listaFornecedor.delete(*self.listaFornecedor.get_children())
        self.lista = self.fornecedor.listarFornecedor()
        for i in self.lista:
            self.listaFornecedor.insert('',END, values=i)
            
    def pesquisar_fornecedor(self):
        pass
    
    def alterar_fornecedor(self):
        self.cod = self.et_cod_fornecedor.get()
        self.cnpj = self.et_cnpj_fornecedor.get()
        self.nome = self.et_nome_fornececdor.get()
        self.email = self.et_email_fornecedor.get()
        self.telefone = self.et_tel_fornecedor.get()
        self.logradouro = self.et_logr_fornecedor.get()
        self.numero = self.et_num_fornecedor.get()
        self.cep = self.et_cep_fornecedor.get()
        self.cidade = self.et_cidade_fornecedor.get()
        self.estado = self.et_estado_fornecedor.get()
        #self.qtd = self.et_qtd_fornecida_fornecedor.get()
        #self.data = self.et_data_fornecimento.get()
        
        self.fornecedor.alterarFornecedor(self.cod,self.cnpj,self.nome,
                                             self.email, self.telefone, 
                                             self.logradouro, self.numero, 
                                             self.cep,self.cidade, 
                                             self.estado)
        self.lista_fornecedor()
    
    def excluir_fornecedor(self):
        self.cod = self.et_cod_fornecedor.get()
        self.fornecedor.excluirFornecedor(self.cod)
        self.limpa_fornecedor()
        self.lista_fornecedor()
        
    def duplo_clique_for(self):
        self.limpa_fornecedor()
        self.listaFornecedor.selection()
        for i in self.listaFornecedor.selection():
         col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = self.listaFornecedor.item(i, 'values')
         self.et_cod_fornecedor.insert(END,col1)
         self.et_cnpj_fornecedor.insert(END,col2)
         self.et_nome_fornececdor.insert(END,col3)
         self.et_email_fornecedor.insert(END,col4)
         self.et_tel_fornecedor.insert(END,col5)
         self.et_logr_fornecedor.insert(END,col6)
         self.et_num_fornecedor.insert(END,col7)
         self.et_cep_fornecedor.insert(END,col8)
         self.et_cidade_fornecedor.insert(END,col9)
         self.et_estado_fornecedor.insert(END,col10)
        # self.et_qtd_fornecida_fornecedor.insert(END,col11)
         #self.et_data_fornecimento.insert(END,col12)
    
    def limpa_fornecedor(self):
        self.et_cod_fornecedor.delete(0,END)
        self.et_cnpj_fornecedor.delete(0,END)
        self.et_nome_fornececdor.delete(0,END)
        self.et_email_fornecedor.delete(0,END)
        self.et_tel_fornecedor.delete(0,END)
        self.et_logr_fornecedor.delete(0,END)
        self.et_num_fornecedor.delete(0,END)
        self.et_cep_fornecedor.delete(0,END)
        self.et_cidade_fornecedor.delete(0,END)
        self.et_estado_fornecedor.delete(0,END)
        #self.et_qtd_fornecida_fornecedor.delete(0,END)
       # self.et_data_fornecimento.delete(0,END)
           
#CRUD de 
