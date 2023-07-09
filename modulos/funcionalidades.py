from tkinter import *
from tkinter import messagebox
from modulos.categoriaproduto import CategoriaProduto
from modulos.cliente import Cliente
from modulos.servico import Servico
from modulos.ordemservico import OS
from modulos.usuario import Usuario
from modulos.fornecedor import Fornecedor
from modulos.fornecimento import Fornecimento
from modulos.produto import Produto

class Funcionalidades:

    # OBJETOS DAS CLASSES 
    categoria = CategoriaProduto()
    cliente = Cliente()
    servico = Servico()
    usuario = Usuario()
    fornecedor = Fornecedor()
    fornecimento = Fornecimento()
    produto = Produto()
    os = OS()

    
    # FUNÇÔES DOS BOTÕES DA TELA DE USUÁRIO
    def mudar_senha(self) -> None:
        """
        """
        self.senha = self.et_nova_senha.get().strip()
        self.conf = self.et_confir_senha.get().strip()
        if self.senha == '' or self.conf == '':
            messagebox.showwarning('Alerta', 'Preencha os campos')
        elif len(self.senha) != 8 or len(self.conf) != 8:
            messagebox.showwarning('Alerta', 'A senha deve conter 8 caracteres')
        elif self.senha != self.conf:
            messagebox.showwarning('Alerta', 'Senhas diferentes')     
        else:
            self.usuario.alterar_senha(self.senha)
            messagebox.showinfo('Sistema', 'Senha alterada com sucesso!')
            self.limpa_usuario()     
    
    def limpa_usuario(self):
        """
        """
        self.et_nova_senha.delete(0, END)
        self.et_confir_senha.delete(0, END)
        
    # FUNÇÕES DOS BOTÕES DA TELA CATEGORIA DE PRODUTO
    def inserir_categoria(self):
        """
        """
        self.desc = self.et_desc_categoria.get().strip()
        if self.desc == '':
            messagebox.showwarning('Alerta', 'Insira da descrição da categoria')
        else:
            self.categoria.cadastrarCategoria(self.desc)
            messagebox.showinfo('Info', 'Categoria de produto cadastrada com sucesso!')
            self.limpa_categoria()

    def exibir_categoria(self):
        """
        """
        self.listaCategoria.delete(*self.listaCategoria.get_children())
        self.exibir = self.categoria.listarCategoria()
        if len(self.exibir) == 0:
            messagebox.showinfo('Informação', 'Não há categoria cadastrada!')
        else:
            for i in self.exibir:
                self.et_cod_categoria.config(state='normal') 
                self.listaCategoria.insert('',END, values=i) 

    def editar_categoria(self):
        """
        """
        self.cod = self.et_cod_categoria.get().strip()
        self.desc = self.et_desc_categoria.get().strip()
        if self.desc == '':
            messagebox.showwarning('Alerta', 'Exiba as categorias para editar e selecione')
        elif len(self.desc) > 15:
            messagebox.showwarning('Alerta','Preencha a descrição de categoria corretamente!')
        else:
            self.categoria.alterarCategoria(self.cod, self.desc)
            messagebox.showinfo('Info', 'Categoria alterada com sucesso!')
            self.limpa_categoria()
            self.exibir_categoria()

    def excluir_categoria(self):
        """
        """
        self.cod = self.et_cod_categoria.get().strip()
        if len(self.cod) == 0:
            messagebox.showerror('Erro', 'Não foi possível deletar a categoria')
        else:
            self.categoria.deletarCategoria(self.cod)
            messagebox.showinfo('Info', 'Categoria excluída com sucesso!')
            self.limpa_categoria()
            self.exibir_categoria()

    def duplo_clique_cat(self, event):
        """
        """
        self.limpa_categoria()
        self.listaCategoria.selection()
        for i in self.listaCategoria.selection():
            col1, col2 = self.listaCategoria.item(i, 'values')
            self.et_cod_categoria.insert(END, col1)
            self.et_desc_categoria.insert(END, col2) 
             
    def limpa_categoria(self):
        """
        """
        self.et_cod_categoria.delete(0, END)
        self.et_desc_categoria.delete(0, END)
        
    def exibir_categ_prod(self):
        """
        """
        self.res = self.categoria.listarCategoria()
        return self.res
    

    # FUNÇÕES DOS BOTÕES DA TELA DE PRODUTO
    def inserir_produto(self):
        """
        """
        self.desc_produto = self.et_desc_produto.get().strip()
        self.mod_produto = self.et_mode_produto.get().strip()
        self.preco_compra = self.et_preco_comp_produto.get().strip()
        self.preco_venda = self.et_preco_ven_produto.get().strip()
        self.qtd_produto = self.et_qtd_produto.get().strip()
        self.cat = self.et_categoria.get().strip()
        self.cod_cat = [self.cat].strip()
        try:
            if self.desc_produto == '' or self.mod_produto == '' or self.preco_compra == '' or self.preco_venda == '' or self.qtd_produto == '' or self.cod_cat == '':
                messagebox.showwarning('Alerta', 'Por favor, preencha os campos')
            elif len(self.desc_produto) < 3 or len(self.desc_produto) > 25:
                    messagebox.showwarning('Alerta', 'Descrição inválida, \nquantidade de caracteres não atende aos requisitos')
            elif len(self.mod_produto) > 15:
                messagebox.showwarning('Alerta', 'Modelo inválido, preencha corretamente!')
            else:
                self.produto.cadastrarProduto(self.desc_produto, self.mod_produto, self.preco_compra, self.preco_venda, self.qtd_produto, self.cod_cat[0][1])
                self.limpa_produto()
                messagebox.showinfo('Informação', 'Produto cadastrado com sucesso!')  
        except:
            messagebox.showerror('Erro', 'Não foi possível cadastrar o produto')
            
    def exibir_produto(self):
        """
        """
        self.listaProd.delete(*self.listaProd.get_children())
        self.exibirProd = self.produto.listarProduto()
        for e in self.exibirProd:
            self.et_cod_produto.config(state='normal')
            self.listaProd.insert('',END, values=e) 
            
            
    def consu_produto(self):
        pass

    def editar_produto(self):
        """
        """
        self.cod_produto = self.et_cod_produto.get().strip()
        self.desc_produto = self.et_desc_produto.get().strip()
        self.mod_produto = self.et_mode_produto.get().strip()
        self.preco_compra = self.et_preco_comp_produto.get().strip()
        self.preco_venda = self.et_preco_ven_produto.get().strip()
        self.qtd_produto = self.et_qtd_produto.get().strip()
        self.cat = self.et_categoria.get().strip()
        self.cod_cat = [self.cat]
        try:
            if self.desc_produto == '' or self.mod_produto == '' or self.preco_compra == '' or self.preco_venda == '' or self.qtd_produto == '' or self.cod_cat == '':
                messagebox.showwarning('Alerta', 'Por favor, Selecione um produto para alterar')
            elif len(self.desc_produto) < 3 or len(self.desc_produto) > 25:
                    messagebox.showwarning('Alerta', 'Descrição inválida, \nquantidade de caracteres não atende aos requisitos')
            elif len(self.mod_produto) > 15:
                messagebox.showwarning('Alerta', 'Modelo inválido, preencha corretamente!')
            else:
                self.produto.alterarProduto(self.cod_produto, self.desc_produto, self.mod_produto, self.preco_compra, self.preco_venda, self.qtd_produto, self.cod_cat[0][1])
                self.limpa_produto()
                messagebox.showinfo('Informação', 'Produto alterado com sucesso!')
        except Exception as error:
            print(f'Erro', 'Não foi possível alterar o produto:' )
            print(error)
        

    def excluir_produto(self):
        """
        """
        self.cod_prod = self.et_cod_produto.get().strip()
        try:
            if len(self.cod_prod) != 0:
                self.produto.deletarProduto(self.cod_prod)
                self.exibir_produto()
                self.limpa_produto()
                messagebox.showinfo('Info', 'Produto deletado com sucesso!')
            else:
                messagebox.showwarning('Alerta','Nenhum produto encontrado, não foi possível excluir')
        except:
            messagebox.showerror('Erro', 'Houve um erro ao excluir o produto')
    def duplo_clique_prod(self, event):
        """
        """
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
        """
        """
        self.et_cod_produto.delete(0, END)
        self.et_desc_produto.delete(0, END) 
        self.et_mode_produto.delete(0, END)
        self.et_preco_comp_produto.delete(0, END)
        self.et_preco_ven_produto.delete(0, END)
        self.et_qtd_produto.delete(0, END)

    # FUNÇÕES DOS BOTÕES DA TELA DE CLIENTE
    def inserir_cliente(self):
        """
        """
        self.cpf = self.et_cpf_cliente.get().strip()
        self.nome = self.et_nome_cliente.get().strip()
        self.email = self.et_email_cliente.get().strip() 
        self.telefone = self.et_tel_cliente.get().strip()   
        self.logradouro = self.et_logr_cliente.get().strip()
        self.numero = self.et_num_cliente.get().strip()
        self.cep = self.et_cep_cliente.get().strip()       
        self.cidade = self.et_cidade_cliente.get().strip()
        self.estado = self.et_estado_cliente.get().strip()

        try:
            if self.nome == '' or self.email == '' or self.telefone == '' or self.logradouro == '' or self.numero == '' or self.cidade == '' or self.estado == '':
                messagebox.showwarning('Alerta', 'Preencha os campos!')
            elif len(self.cpf) != 11:
                messagebox.showwarning('Alerta', 'CPF Inválido')
            elif len(self.nome) <= 3 or len(self.nome) > 20:
                messagebox.showwarning('Alerta', 'Por favor, Insira um nome válido!')
                if self.nome == '':
                    messagebox.showwarning('Alerta', 'Preencha o campo nome!')
            elif len(self.email) > 35 or '@' not in self.email:
                messagebox.showwarning('Alerta', 'Preencha o Email corretamente!')
            elif len(self.telefone ) < 9 or len(self.telefone) > 14:
                messagebox.showwarning('Alerta', 'Por favor, Insira um telefone válido!')
            elif len(self.logradouro) > 40:
                messagebox.showwarning('Alerta','Digite um endereço válido!')
            elif len(self.cidade) <= 3 or len(self.cidade) > 40:
                messagebox.showwarning('Alerta', 'Preencha o campo de cidade corretamente!')
            elif len(self.estado) < 3 or len(self.estado) > 40:
                messagebox.showwarning('Alerta', 'Preencha o campo de estado corretamente!')
            else:
                messagebox.showinfo('Sistema', 'Cliente cadastrado com sucesso!')
                self.cliente.cadastrarCliente(self.cpf,self.nome,self.email,
                                      self.telefone,self.logradouro,self.numero,
                                      self.cep,self.cidade,self.estado)    
                self.limpa_cliente()
        except:
            messagebox.showerror('Erro', 'Houve um erro inesperado!')  

    def lista_cliente(self):
        """
        """
        self.listaCliente.delete(*self.listaCliente.get_children())
        self.lista = self.cliente.listarCliente()
        if len(self.lista) == 0:
            messagebox.showinfo('Informação', 'Não há clientes cadastrados.')
        else:
            for n in self.lista:
                self.et_cod_cliente.config(state='normal')
                self.listaCliente.insert('',END, values=n)

    def buscar_cliente(self):
        """
        """
        self.listaCliente.delete(*self.listaCliente.get_children())
        self.cli = self.et_consultar_cliente.get()
        if len(self.cli) == 0:
            messagebox.showwarning('Alerta', 'Preencha o campo de consulta.')
        else:
            self.resCli = self.cliente.consultarCliente(self.cli)
            if len(self.resCli) == 0:
                messagebox.showinfo('Informação', 'Nenhum cliente encontrado.')
            else:
                for v in self.resCli:
                    self.listaCliente.insert('',END, values=v)
        self.limpa_cliente()

    def alterar_cliente(self):
        """
        """
        self.cod = self.et_cod_cliente.get().strip()
        self.cpf = self.et_cpf_cliente.get().strip()
        self.nome = self.et_nome_cliente.get().strip()
        self.email = self.et_email_cliente.get().strip()
        self.telefone = self.et_tel_cliente.get().strip()
        self.logradouro = self.et_logr_cliente.get().strip()
        self.numero = self.et_num_cliente.get().strip()
        self.cep = self.et_cep_cliente.get().strip()
        self.cidade = self.et_cidade_cliente.get().strip()
        self.estado = self.et_estado_cliente.get().strip()
        try:
            if self.nome == '' or self.email == '' or self.telefone == '' or self.logradouro == '' or self.numero == '' or self.cidade == '' or self.estado == '':
                messagebox.showwarning('Alerta', 'Nenhum Cliente encontrado, liste e selecione para alterar')
            elif len(self.cpf) != 11:
                messagebox.showwarning('Alerta', 'CPF inválido, não foi possível alterar')
            elif len(self.nome) <= 3 or len(self.nome) > 20:
                messagebox.showwarning('Alerta', 'Por favor, Insira um nome válido!')
                if self.nome == '':
                    messagebox.showwarning('Alerta', 'Preencha o campo nome!')
            elif len(self.email) > 35 or '@' not in self.email:
                messagebox.showwarning('Alerta', 'Preencha o Email corretamente!')
            elif len(self.telefone ) < 9 or len(self.telefone) > 14:
                messagebox.showwarning('Alerta', 'Por favor, Insira um telefone válido!')
            elif len(self.logradouro) > 40:
                messagebox.showwarning('Alerta','Digite um endereço válido!')
            elif len(self.cidade) <= 3 or len(self.cidade) > 40:
                messagebox.showwarning('Alerta', 'Preencha o campo de cidade corretamente!')
            elif len(self.estado) < 3 or len(self.estado) > 40:
                messagebox.showwarning('Alerta', 'Preencha o campo de estado corretamente!')
            else:
                self.cliente.alterarCliente(self.cod, self.cpf,self.nome,self.email,
                                      self.telefone,self.logradouro,self.numero,
                                      self.cep,self.cidade,self.estado)    
                messagebox.showinfo('Sistema', 'Dados Alterados com sucesso!')
                self.limpa_cliente()
        except:
            messagebox.showerror('Erro', 'Houve um erro inesperado!') 
            
    def excluir_cliente(self):
        """
        """
        self.codigo = self.et_cod_cliente.get()
        try:
            if len(self.codigo) == 0:
                messagebox.showwarning('Alerta', 'Cliente não encontrado, impossível deletar')
            else:
                self.cliente.deletarCliente(self.codigo)
                messagebox.showinfo('Sistema', 'Cliente deletado com sucesso!')
                self.limpa_cliente()
                self.lista_cliente()
        except:
            messagebox.showerror('Erro', 'Não foi possível deletar o cliente')

    def duplo_clique_cliente(self, event):
        """
        """
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
        """
        """
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
        self.et_consultar_cliente.delete(0, END)


    # FUNÇÕES DOS BOTÕES DA TELA FORNECEDOR
    def inserir_fornecedor(self):
        """
        """
        self.cnpj = self.et_cnpj_fornecedor.get().strip()
        self.nome = self.et_nome_fornecedor.get().strip()
        self.email = self.et_email_fornecedor.get().strip()
        self.telefone = self.et_tel_fornecedor.get().strip()
        self.logradouro = self.et_logr_fornecedor.get().strip()
        self.numero = self.et_num_fornecedor.get().strip()
        self.cep = self.et_cep_fornecedor.get().strip()
        self.cidade = self.et_cidade_fornecedor.get().strip()
        self.estado = self.et_estado_fornecedor.get().strip()
        
        try:
            
            if self.nome == '' or self.email == '' or self.telefone == '' or self.logradouro == '' or self.numero == '' or self.cidade == '' or self.estado == '':
                messagebox.showwarning('Alerta', 'Preencha os campos!')
            elif len(self.cnpj) != 11:
                messagebox.showwarning('Alerta', 'CPF/CNPJ Inválido')
            elif len(self.nome) <= 3 or len(self.nome) > 20:
                messagebox.showwarning('Alerta', 'Por favor, Insira um nome válido!')
                if self.nome == '':
                    messagebox.showwarning('Alerta', 'Preencha o campo nome!')
            elif len(self.email) > 35 or '@' not in self.email:
                messagebox.showwarning('Alerta', 'Preencha o Email corretamente!')
            elif len(self.telefone ) < 9 or len(self.telefone) > 14:
                messagebox.showwarning('Alerta', 'Por favor, Insira um telefone válido!')
            elif len(self.logradouro) > 40:
                messagebox.showwarning('Alerta','Digite um endereço válido!')
            elif len(self.cidade) <= 3 or len(self.cidade) > 40:
                messagebox.showwarning('Alerta', 'Preencha o campo de cidade corretamente!')
            elif len(self.estado) < 3 or len(self.estado) > 40:
                messagebox.showwarning('Alerta', 'Preencha o campo de estado corretamente!')
            else:
                messagebox.showinfo('Sistema', 'Fornecedor cadastrado com sucesso!')
                self.fornecedor.cadastrarFornecedor(self.cnpj,self.nome,
                                             self.email, self.telefone, 
                                             self.logradouro, self.numero, 
                                             self.cep,self.cidade, 
                                             self.estado)
                self.limpa_fornecedor()
                
        except:
            messagebox.showerror('Erro', 'Houve um erro inesperado!')
                
    def lista_fornecedor(self):
        """
        """
        self.listaForne.delete(*self.listaForne.get_children())
        self.listaf = self.fornecedor.listarFornecedor()
        if len(self.listaf) == 0:
            messagebox.showinfo('Informação', 'Não há fornecedores cadastrados.')
        else:
            for i in self.listaf:
                self.listaForne.insert('',END, values = i)
            
    def pesquisar_fornecedor(self):
        """
        """
        self.listaForne.delete(*self.listaForne.get_children())
        self.forne = self.et_consultar_forne.get()
        if len(self.forne) == 0:
            messagebox.showwarning('Alerta', 'Preencha o campo de consulta.')
        else:
            self.resForne = self.fornecedor.consultarFornecedor(self.forne)
            if len(self.resForne) ==0:
                messagebox.showinfo("Informação", "Nenhum Fornecedor encontrado.")
            else:
                for r in self.resForne:
                    self.listaForne.insert('', END, values=r)
        self.limpa_fornecedor()
        
    def alterar_fornecedor(self):
        """
        """
        self.cod = self.et_cod_fornecedor.get().strip()
        self.cnpj = self.et_cnpj_fornecedor.get().strip()
        self.nome = self.et_nome_fornecedor.get().strip()
        self.email = self.et_email_fornecedor.get().strip()
        self.telefone = self.et_tel_fornecedor.get().strip()
        self.logradouro = self.et_logr_fornecedor.get().strip()
        self.numero = self.et_num_fornecedor.get().strip()
        self.cep = self.et_cep_fornecedor.get().strip()
        self.cidade = self.et_cidade_fornecedor.get().strip()
        self.estado = self.et_estado_fornecedor.get().strip()
        try:
            
            if self.nome == '' or self.email == '' or self.telefone == '' or self.logradouro == '' or self.numero == '' or self.cidade == '' or self.estado == '':
                messagebox.showwarning('Alerta', 'Preencha os campos!')
            elif len(self.cnpj) != 11:
                messagebox.showwarning('Alerta', 'CPF Inválido')
            elif len(self.nome) <= 3 or len(self.nome) > 20:
                messagebox.showwarning('Alerta', 'Por favor, Insira um nome válido!')
                if self.nome == '':
                    messagebox.showwarning('Alerta', 'Preencha o campo nome!')
            elif len(self.email) > 35 or '@' not in self.email:
                messagebox.showwarning('Alerta', 'Preencha o Email corretamente!')
            elif len(self.telefone ) < 9 or len(self.telefone) > 14:
                messagebox.showwarning('Alerta', 'Por favor, Insira um telefone válido!')
            elif len(self.logradouro) > 40:
                messagebox.showwarning('Alerta','Digite um endereço válido!')
            elif len(self.cidade) <= 3 or len(self.cidade) > 40:
                messagebox.showwarning('Alerta', 'Preencha o campo de cidade corretamente!')
            elif len(self.estado) < 3 or len(self.estado) > 40:
                messagebox.showwarning('Alerta', 'Preencha o campo de estado corretamente!')
            else:
                self.fornecedor.alterarFornecedor(self.cod,self.cnpj,self.nome,
                                             self.email, self.telefone, 
                                             self.logradouro, self.numero, 
                                             self.cep,self.cidade, 
                                             self.estado)
                messagebox.showinfo('Sistema', 'Dados alterados com sucesso.')
                self.lista_fornecedor()
        except:
            messagebox.showerror('Sistema', 'Houve um erro inesperado.')
    
    def excluir_fornecedor(self):
        """
        """
        self.cod = self.et_cod_fornecedor.get()
        try:
            if len(self.cod) == 0:
                messagebox.showwarning('Alerta', 'Fornecedor não encontrado, impossível deletar.')
            else:
                self.fornecedor.excluirFornecedor(self.cod)
                messagebox.showinfo('Sistema', 'Fornecedor deletado com sucesso')
                self.limpa_fornecedor()
                self.lista_fornecedor()
        except:
            messagebox.showerror('Erro', 'Não foi possível deletar o fornecedor.'
                                 )
    def duplo_clique_for(self, event):
        """
        """
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
    
    def limpa_fornecedor(self):
        """
        """
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
       
    def inserir_fornecimento(self):
        """
        """
        self.res = self.fornecedor.listarFornecedor()
        self.cod_prod_obt = self.et_cod_produto.get()
        self.qtd_fornecimento = self.et_qtd_fornecida.get()
        self.data = self.et_data_fornecimento.get()
        print(self.res)
        #self.fornecimento.cadastrar_fornecimento(self.cnpj_obt, self.cod_prod_obt, self.data, self.qtd_fornecimento)


    # FUNÇÕES DOS BOTÕES DA TELA DE SERVIÇO
    def inserir_servico(self):
        """
        """
        self.cod_servico = self.et_cod_servico.get().strip()
        self.desc_servico = self.et_desc_servico.get().strip()
        self.preco_servico = self.et_preco_servico.get().strip()
        self.tipo_servico = self.et_tipo_servico.get().strip()
        try:
            if self.cod_servico == '' or self.desc_servico == '' or self.preco_servico == '' or self.tipo_servico == '':
                messagebox.showwarning('Alerta', 'Por favor, preencha os campos')
            elif len(self.cod_servico) > 5:
                messagebox.showwarning('Alerta', 'Insira um código válido!')
            elif len(self.desc_servico) < 4 or len(self.desc_servico) > 40:
                messagebox.showwarning('Alerta', 'Preencha uma descrição válida')
            elif len(self.tipo_servico) < 4 or len(self.tipo_servico) > 25:
                messagebox.showwarning('Alerta', 'Prencha um tipo válido')
            else:
                self.servico.cadastrarServico(self.cod_servico, self.desc_servico, self.preco_servico, self.tipo_servico)
                self.limpa_servico()
                messagebox.showinfo('Info', 'Serviço cadastrado com sucesso!')
        except:
            messagebox.showerror('Erro', 'Não foi possível concluir o cadastro de serviço')
        

    def exibir_servico(self):
        """
        """
        self.listaServico.delete(*self.listaServico.get_children())
        self.exibir_serv = self.servico.listarServicos()
        if len(self.exibir_serv) == 0:
            messagebox.showinfo('Informação', 'Não há servico cadastrado')
        else:
            for s in self.exibir_serv:
                self.et_cod_servico.config(state='normal')
                self.listaServico.insert('',END, values=s)

    def editar_servico(self):
        """
        """
        self.cod_servico = self.et_cod_servico.get().strip()
        self.desc_servico = self.et_desc_servico.get().strip()
        self.preco_servico = self.et_preco_servico.get().strip()
        self.tipo_servico = self.et_tipo_servico.get().strip()
        try:
            if self.cod_servico == '' or self.desc_servico == '' or self.preco_servico == '' or self.tipo_servico == '':
                messagebox.showwarning('Alerta', 'Selecione um serviço, para alterá-lo')
            elif len(self.cod_servico) > 5:
                messagebox.showwarning('Alerta', 'Insira um código válido!')
            elif len(self.desc_servico) < 4 or len(self.desc_servico) > 40:
                messagebox.showwarning('Alerta', 'Preencha uma descrição válida')
            elif len(self.tipo_servico) < 4 or len(self.tipo_servico) > 25:
                messagebox.showwarning('Alerta', 'Prencha um tipo válido')
            else:
                self.servico.alterarServico(self.cod_servico, self.desc_servico, self.preco_servico, self.tipo_servico)
                messagebox.showinfo('Info', 'Serviço alterado com sucesso!')
                self.limpa_servico()
                self.exibir_servico()
        except:
            messagebox.showerror('Erro', 'Erro ao tentar salvar as alterações')
        

    def deletar_servico(self):
        """
        """
        self.cod_servico = self.et_cod_servico.get().strip()
        try:
            if len(self.cod_servico) == 0:
                messagebox.showwarning('Alerta', 'Não foi possível deletar, serviço não encontrado')
            else:
                messagebox.showinfo('Info', 'Serviço deletado com sucesso!')
                self.servico.excluirServico(self.cod_servico)
                self.limpa_servico()
                self.exibir_servico()
        except:
            messagebox.showerror('Erro', 'Erro ao tentar deletar o serviço')

    def duplo_clique_servico(self, event):
        """
        """
        self.limpa_servico()
        self.listaServico.selection()
        for i in self.listaServico.selection():
            col1, col2, col3, col4 = self.listaServico.item(i, 'values')
            self.et_cod_servico.insert(END, col1)
            self.et_desc_servico.insert(END, col2) 
            self.et_preco_servico.insert(END, col3)
            self.et_tipo_servico.insert(END, col4)
    
    def limpa_servico(self):
        """
        """
        self.et_cod_servico.delete(0, END)
        self.et_desc_servico.delete(0, END)
        self.et_preco_servico.delete(0, END)
        self.et_tipo_servico.delete(0, END)


    #CRUD da venda
    def pegar_produto(self):
        """
        """
        pass
    
    def pegar_cliente(self):
        """
        """
        pass
    
    def inserir_venda(self):
        """
        """
        pass
    
    def duplo_clique(self):
        """
        """
        pass
    
    def excluir_venda(self):
        """
        """
        pass
    
    def calcular_total(self):
        """
        """
        pass
    
#CRUD da Ordem de Serviço
    def inserir_Os(self):
        
        self.cod_os = self.et_cod_os.get()
        self.modelo = self.et_modelo_os.get()
        self.data = self.et_data_exec_servico.get()
        self.valorttl = self.et_valor_total_os.get()
        self.defeito = self.et_defeito.get()
        self.situacao = self.et_situacao.get()
        self.os.registrarOS(self.cod_os, self.modelo, 
                            self.data, self.valorttl,
                            self.defeito, self.situacao)

    def excluir_Os(self):
        """
        """
        self.cod = self.et_cod_os.get()
        try:
            if len(self.cod) == 0:
                messagebox.showerror("Alerta", "OS não encontrada, impossível deletar.")
            else:
                self.os.deletarOS(self.cod)
                messagebox.showinfo('Sistema, OS deletada com sucesso.')
                self.limpa_Os()
                self.lista_Os()
        except: 
            messagebox.showerror('Erro', 'Não foi possível deletar a OS.')
            
    def lista_Os(self):
        """
        """
        self.listaOS.delete(*self.listaOS.get_children())
        self.listarOs = self.os.listarOS()
        if len(self.listarOs) == 0:
            messagebox.showinfo('Informação', 'Não há Ordens de Serviço cadastradas.')
        else:
            for s in self.listarOs:
                self.et_cod_os.config(state='normal')
                self.listaOS.insert('',END, values=s)    

    def limpa_Os(self):
        """
        """
        self.et_cod_os.delete(0, END)
        self.et_modelo_os.delete(0, END)
        self.et_data_exec_servico.delete(0,END)
        self.et_valor_total_os.delete(0, END)
        self.et_defeito.delete(0, END)
        self.et_situacao.delete(0, END)
    
 
    def duplo_cliqueOs(self, event):
        """
        """
        self.limpa_Os()
        self.listaOS.selection()
        for i in self.listaOS.selection():
            col1,col2,col3,col4,col5,col6= self.listaOs.item(i, 'values')
            self.et_cod_os.delete(END, col1)
            self.et_modelo_os.delete(END, col2)
            self.et_data_exec_servico.delete(END, col3)
            self.et_valor_total_os.delete(END, col4)
            self.et_defeito.delete(END, col5)
            self.et_situacao.delete(END, col6)
        

                
                
    def calcular_totalOS(self):
        """
        """
        pass
    
    def pegar_material(self):
        """
        """
        pass
    
    def pegar_clienteOs(self):
        """
        """
        pass
    
    def exibir_serv_os(self):
        """
        """
        self.ser = self.servico.listarServicos()
        return self.ser