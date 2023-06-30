from tkinter import *
from tkinter import messagebox
from modulos.categoriaproduto import CategoriaProduto
from modulos.cliente import Cliente
from modulos.servico import Servico
from modulos.usuario import Usuario
from modulos.fornecedor import Fornecedor
from modulos.produto import Produto

class Funcionalidades:

    # OBJETOS DAS CLASSES 
    categoria = CategoriaProduto()
    cliente = Cliente()
    servico = Servico()
    usuario = Usuario()
    fornecedor = Fornecedor()
    produto = Produto()
    
    # FUNÇÔES DOS BOTÕES DA TELA DE USUÁRIO
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
        if self.desc == '':
            messagebox.showwarning('Alerta', 'Insira da descrição da categoria')
        else:
            self.categoria.cadastrarCategoria(self.desc)
            messagebox.showinfo('Info', 'Categoria de produto cadastrada com sucesso!')
        self.limpa_categoria()

    def exibir_categoria(self):
        self.listaCategoria.delete(*self.listaCategoria.get_children())
        self.exibir = self.categoria.listarCategoria()
        if len(self.exibir) == 0:
            messagebox.showinfo('Informação', 'Não há categorias cadastradas')
        else:
            for i in self.exibir:
                self.listaCategoria.insert('',END, values=i)  
    

    def editar_categoria(self):
        self.cod = self.et_cod_categoria.get()
        self.desc = self.et_desc_categoria.get()
        if self.desc == '':
            messagebox.showwarning('Alerta', 'Insira da descrição da categoria')
        else:
            self.categoria.alterarCategoria(self.cod, self.desc)
            messagebox.showinfo('Info', 'Categoria alterada com sucesso!')
            self.limpa_categoria()
        self.exibir_categoria()

    def excluir_categoria(self):
        self.cod = self.et_cod_categoria.get()
        self.categoria.deletarCategoria(self.cod)
        messagebox.showinfo('Info', 'Categoria excluída com sucesso!')
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
        
    def exibir_categ_prod(self):
        self.res = self.categoria.listarCategoria()
        return self.res
    
    def inserir_produto(self):
        self.desc_produto = self.et_desc_produto.get()
        self.mod_produto = self.et_mode_produto.get()
        self.preco_compra = self.et_preco_comp_produto.get()
        self.preco_venda = self.et_preco_ven_produto.get()
        self.qtd_produto = self.et_qtd_produto.get()
        self.cat = self.et_categoria.get()
        self.cod_cat = [self.cat]
        self.produto.cadastrarProduto(self.desc_produto, self.mod_produto, self.preco_compra, self.preco_venda, self.qtd_produto, self.cod_cat[0][1])
        messagebox.showinfo('Informação', 'Produto cadastrado com sucesso!')
        print(self.cod_cat[0][1])
        '''for c in range(0, 2):
            self.grava = {'Codigo': self.res[c][0]}
            print(self.grava)'''


    def exibir_produto(self):
        self.listaProd.delete(*self.listaProd.get_children())
        self.exibirProd = self.produto.listarProduto()
        if len(self.exibirProd) == 0:
            messagebox.showinfo('Informação', 'Não há produtos cadastrados')
        else:
            for i in self.exibirProd:
                self.listaProd.insert('',END, values=i)  
    

    def editar_produto(self):
        self.desc_produto = self.et_desc_produto.get()
        self.mod_produto = self.et_mode_produto.get()
        self.preco_compra = self.et_preco_comp_produto.get()
        self.preco_venda = self.et_preco_ven_produto.get()
        self.qtd_produto = self.et_qtd_produto.get()
        self.cat = self.et_categoria.get()
        self.cod_cat = [self.cat]
        messagebox.showinfo('Informação', 'Produto alterado com sucesso!')

    def excluir_produto(self):
        self.cod_prod = self.et_cod_produto.get()
        self.produto.deletarProduto(self.cod_prod)
        self.exibir_produto()
        self.limpa_produto()
        messagebox.showinfo('Info', 'Produto excluído com sucesso!')

    def duplo_clique_prod(self, event):
        self.limpa_produto()
        self.listaProd.selection()
        for i in self.listaProd.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.listaProd.item(i, 'values')
            self.et_cod_produto.insert(END, col1)
            self.et_desc_produto.insert(END, col2)
            self.et_mode_produto.insert(END, col3)
            self.et_preco_comp_produto.insert(END, col4)
            self.et_preco_ven_produto.insert(END, col5)
            self.et_qtd_produto.insert(END, col6)
            self.et_categoria.set(col7)
            

    def limpa_produto(self):
        self.et_cod_produto.delete(0, END)
        self.et_desc_produto.delete(0, END) 
        self.et_mode_produto.delete(0, END)
        self.et_preco_comp_produto.delete(0, END)
        self.et_preco_ven_produto.delete(0, END)
        self.et_qtd_produto.delete(0, END)


#CRUD do Cliente
    def inserir_cliente(self):
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
        for n in self.lista:
            self.listaCliente.insert('',END, values=n)

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
        #self.data = self.et_data_fornecimento.get()
        
        self.fornecedor.cadastrarFornecedor(self.cnpj,self.nome,
                                             self.email, self.telefone, 
                                             self.logradouro, self.numero, 
                                             self.cep,self.cidade, 
                                             self.estado)
        self.limpa_fornecedor()
                
    def lista_fornecedor(self):
        self.listaForne.delete(*self.listaForne.get_children())
        self.listaf = self.fornecedor.listarFornecedor()
        for i in self.listaf:
            self.listaForne.insert('',END, values = i)
            
    def pesquisar_fornecedor(self):
        self.nome = self.et_nome_fornecedor.get()
        self.fornecedor.consultarFornecedor(self.nome)
        self.lista_fornecedor()
        pass
    
    def alterar_fornecedor(self):
        self.cod = self.et_cod_fornecedor.get()
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
        
    def duplo_clique_for(self, event):
        self.limpa_fornecedor()
        self.listaForne.selection()
        for i in self.listaForne.selection():
         col1, col2, col3, col4, col5, col6, col7, col8, col9, col10= self.listaForne.item(i, 'values')
         self.et_cod_fornecedor.insert(END,col1)
         self.et_cnpj_fornecedor.insert(END,col2)
         self.et_nome_fornecedor.insert(END,col3)
         self.et_email_fornecedor.insert(END,col4)
         self.et_tel_fornecedor.insert(END,col5)
         self.et_logr_fornecedor.insert(END,col6)
         self.et_num_fornecedor.insert(END,col7)
         self.et_cep_fornecedor.insert(END,col8)
         self.et_cidade_fornecedor.insert(END,col9)
         self.et_estado_fornecedor.insert(END,col10)
         #self.et_qtd_fornecida_fornecedor.insert(END,col11)
         #self.et_data_fornecimento.insert(END,col12)
    
    def limpa_fornecedor(self):
        self.et_cod_fornecedor.delete(0,END)
        self.et_cnpj_fornecedor.delete(0,END)
        self.et_nome_fornecedor.delete(0,END)
        self.et_email_fornecedor.delete(0,END)
        self.et_tel_fornecedor.delete(0,END)
        self.et_logr_fornecedor.delete(0,END)
        self.et_num_fornecedor.delete(0,END)
        self.et_cep_fornecedor.delete(0,END)
        self.et_cidade_fornecedor.delete(0,END)
        self.et_estado_fornecedor.delete(0,END)
        #self.et_qtd_fornecida_fornecedor.delete(0,END)
        #self.et_data_fornecimento.delete(0,END)
       
       
# FUNÇÕES DOS BOTÕES DA TELA DE SERVIÇO
    def inserir_servico(self):
        self.cod_servico = self.et_cod_servico.get()
        self.desc_servico = self.et_desc_servico.get()
        self.preco_servico = self.et_preco_servico.get()
        self.tipo_servico = self.et_tipo_servico.get()
        
        self.servico.cadastrarServico(self.cod_servico, self.desc_servico, self.preco_servico, self.tipo_servico)
        self.limpa_servico()

    def exibir_servico(self):
        self.listaServico.delete(*self.listaServico.get_children())
        self.exibir_serv = self.servico.listarServicos()
        for s in self.exibir_serv:
            self.listaServico.insert('',END, values=s)

    def editar_servico(self):
        self.cod_servico = self.et_cod_servico.get()
        self.desc_servico = self.et_desc_servico.get()
        self.preco_servico = self.et_preco_servico.get()
        self.tipo_servico = self.et_tipo_servico.get()
        self.servico.alterarServico(self.cod_servico, self.desc_servico, self.preco_servico, self.tipo_servico)
        self.limpa_servico()
        self.exibir_servico()

    def deletar_servico(self):
        self.cod_servico = self.et_cod_servico.get()
        self.servico.excluirServico(self.cod_servico)
        self.limpa_servico()
        self.exibir_servico()

    def duplo_clique_servico(self, event):
        self.limpa_servico()
        self.listaServico.selection()
        for i in self.listaServico.selection():
            col1, col2, col3, col4 = self.listaServico.item(i, 'values')
            self.et_cod_servico.insert(END, col1)
            self.et_desc_servico.insert(END, col2) 
            self.et_preco_servico.insert(END, col3)
            self.et_tipo_servico.insert(END, col4)
    
    def limpa_servico(self):
        self.et_cod_servico.delete(0, END)
        self.et_desc_servico.delete(0, END)
        self.et_preco_servico.delete(0, END)
        self.et_tipo_servico.delete(0, END)
