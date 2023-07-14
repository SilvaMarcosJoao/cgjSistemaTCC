from tkinter import *
from tkinter import messagebox
from modulos.categoriaproduto import CategoriaProduto
from modulos.cliente import Cliente
from modulos.usuario import Usuario
from modulos.fornecedor import Fornecedor
from modulos.fornecimento import Fornecimento
from modulos.venda import Venda
from modulos.produto import Produto


class Funcionalidades:

    # OBJETOS DAS CLASSES 
    categoria = CategoriaProduto()
    cliente = Cliente()
    usuario = Usuario()
    fornecedor = Fornecedor()
    fornecimento = Fornecimento()
    produto = Produto()
    venda = Venda()

    
    # FUNÇÔES DOS BOTÕES DA TELA DE USUÁRIO
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
            elif self.captusuario != '' or self.captsenha != '':
                 messagebox.showwarning('Atenção', 'Usuário ou senha inválidos!')
            else:
                if self.resUser[0] == self.captusuario and self.resUser[1] == self.captsenha:
                   messagebox.showwarning('Atenção', 'Usuário ou senha inválidos!') 
                else:
                    messagebox.showwarning('Atenção', 'Usuário ou senha inválidos!')
        except:
            messagebox.showerror('Erro', 'Houve um erro, não foi possível efetuar login')

    
    def mudar_senha(self) -> None:
        """
        Captura a senha digitada pelo usuário, verifica e envia a
        função de alterar senha da classe usuário.
        :param : não tem parâmetro.
        :return: não tem retorno.
        """
        self.senha = self.et_nova_senha.get().strip()
        self.usuario.set_senha(self.et_confir_senha.get().strip())
        if self.senha == '' or self.usuario.get_senha() == '':
            messagebox.showwarning('Alerta', 'Preencha os campos')
        elif len(self.senha) != 8 or len(self.usuario.get_senha()) != 8:
            messagebox.showwarning('Alerta', 'A senha deve conter 8 caracteres')
        elif self.senha != self.usuario.get_senha():
            messagebox.showwarning('Alerta', 'Senhas diferentes')     
        else:
            self.usuario.alterar_senha(self.usuario.get_senha())
            messagebox.showinfo('Sistema', 'Senha alterada com sucesso!')
            self.limpa_usuario()   
    
    def limpa_usuario(self):
        """
        Realiza a limpeza dos campos da tela usuário.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
        """
        self.et_nova_senha.delete(0, END)
        self.et_confir_senha.delete(0, END)

        
    # FUNÇÕES DOS BOTÕES DA TELA CATEGORIA DE PRODUTO
    def inserir_categoria(self):
        """
        Captura os dados do campo descrição da tela categoria, verifica 
        e envia para a função de cadastro da classe Categoria_produto.
        :param: Não tem parâmetro.
        :param: Não tem retorno.
        """
        self.categoria.set_desc_categoria_produto(self.et_desc_categoria.get().strip())
        if self.categoria.get_desc_categoria_produto() == '':
            messagebox.showwarning('Alerta', 'Insira da descrição da categoria')
        else:
            self.categoria.cadastrarCategoria(self.categoria.get_desc_categoria_produto())
            messagebox.showinfo('Info', 'Categoria de produto cadastrada com sucesso!')
            self.limpa_categoria()

    def exibir_categoria(self):
        """
        """
        self.listaCategoria.delete(*self.listaCategoria.get_children())
        self.exibir = self.categoria.listarCategoria()
        try:
            if len(self.exibir) == 0:
                messagebox.showinfo('Informação', 'Não há categoria cadastrada!')
            else:
                for i in self.exibir:
                    self.et_cod_categoria.config(state='normal') 
                    self.listaCategoria.insert('',END, values=i) 
        except:
            messagebox.showerror('Erro', 'Houve um erro na listagem de categoria')

    def editar_categoria(self):
        """
        """
        self.cod = self.et_cod_categoria.get().strip()
        self.categoria.set_desc_categoria_produto(self.et_desc_categoria.get().strip())
        try:
            if self.categoria.get_desc_categoria_produto() == '':
                messagebox.showwarning('Alerta', 'Exiba as categorias para editar e selecione')
            elif len(self.categoria.get_desc_categoria_produto()) > 15:
                messagebox.showwarning('Alerta','Preencha a descrição de categoria corretamente!')
            else:
                self.categoria.alterarCategoria(self.cod, self.categoria.get_desc_categoria_produto())
                messagebox.showinfo('Info', 'Categoria alterada com sucesso!')
                self.limpa_categoria()
                self.exibir_categoria() 
        except:
            messagebox.showerror('Erro', 'Houve um erro nas alterações')

    def excluir_categoria(self):
        """

        """
        self.cod = self.et_cod_categoria.get().strip()
        if len(self.cod) == 0:
            messagebox.showwarning('Erro', 'Não foi possível deletar a categoria, \nselecione-a antes de excluir.')
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
        Realiza a limpeza dos campos da tela categoria.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
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
        self.cat = self.et_categoria.get().strip()
        self.cod_cat = [self.cat]
        try:
            if self.desc_produto == '' or self.mod_produto == '' or self.preco_compra == '' or self.preco_venda == '' or self.cod_cat == '':
                messagebox.showwarning('Alerta', 'Por favor, preencha os campos')
            elif len(self.desc_produto) < 3 or len(self.desc_produto) > 25:
                    messagebox.showwarning('Alerta', 'Descrição inválida, \nquantidade de caracteres não atende aos requisitos')
            elif len(self.mod_produto) > 15:
                messagebox.showwarning('Alerta', 'Modelo inválido, preencha corretamente!')
            else:
                self.produto.cadastrarProduto(self.desc_produto, self.mod_produto, self.preco_compra, self.preco_venda, self.cod_cat[0][1])
                self.limpa_produto()
                messagebox.showinfo('Informação', 'Produto cadastrado com sucesso!')  
        except Exception as erro:
            messagebox.showerror('Erro', 'Não foi possível cadastrar o produto')
            print(erro)

    def exibir_produto(self):
        """
        """
        self.listaProd.delete(*self.listaProd.get_children())
        self.exibirProd = self.produto.listarProduto()
        if len(self.exibirProd) == 0:
            messagebox.showinfo('Informação', 'Não há produtos cadastrados.')
        else:
            for i in self.exibirProd:
                self.et_cod_produto.config(state='normal')
                self.listaProd.insert('',END, values=i) 
            
    def consu_produto(self):
        """
        """
        self.listaProd.delete(*self.listaProd.get_children())
        self.prod = self.et_consulta_produto.get()
        if len(self.prod) == 0:
            messagebox.showwarning('Alerta', 'Preencha o campo de consulta.')
        else:
            self.resProd = self.produto.consultarProduto(self.prod)
            if len(self.resProd) == 0:
                messagebox.showinfo('Informação', 'Nenhum produto encontrado.')
            else:
                for v in self.resProd:
                    self.listaProd.insert('',END, values=v)
                self.limpa_produto()

    def editar_produto(self):
        """
        """
        self.cod_produto = self.et_cod_produto.get().strip()
        self.desc_produto = self.et_desc_produto.get().strip()
        self.mod_produto = self.et_mode_produto.get().strip()
        self.preco_compra = self.et_preco_comp_produto.get().strip()
        self.preco_venda = self.et_preco_ven_produto.get().strip()
        self.cat = self.et_categoria.get().strip()
        self.cod_categoria = [self.cat]
        print(self.cat)
        try:
            if self.cod_produto == '' or self.desc_produto == '' or self.mod_produto == '' or self.preco_compra == '' or self.preco_venda == '' or self.cod_categoria == '':
                messagebox.showwarning('Alerta', 'Por favor, Selecione um produto para alterar')
            elif len(self.desc_produto) < 3 or len(self.desc_produto) > 25:
                    messagebox.showwarning('Alerta', 'Descrição inválida, \nquantidade de caracteres não atende aos requisitos')
            elif len(self.mod_produto) > 15:
                messagebox.showwarning('Alerta', 'Modelo inválido, preencha corretamente!')
            else:
                self.produto.alterarProduto(self.cod_produto, self.desc_produto, 
                                            self.mod_produto, self.preco_compra, 
                                            self.preco_venda)
                
                self.limpa_produto()
                messagebox.showinfo('Informação', 'Produto alterado com sucesso!')
                self.exibir_produto()
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
        except Exception as erro:
            messagebox.showerror('Erro', 'Houve um erro ao excluir o produto')
            print(erro)

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
        Realiza a limpeza dos campos da tela produto.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
        """
        self.et_cod_produto.delete(0, END)
        self.et_desc_produto.delete(0, END) 
        self.et_mode_produto.delete(0, END)
        self.et_preco_comp_produto.delete(0, END)
        self.et_preco_ven_produto.delete(0, END)
        self.et_qtd_produto.delete(0, END)
        

    def listaper_produto(self):
        """
        """
        self.listaProdTela.delete(*self.listaProdTela.get_children())
        self.listaPr = self.produto.listaperProduto()
        if len(self.listaPr) == 0:
            messagebox.showinfo('Informação', 'Não há produtos cadastrados.')
        else:
            for i in self.listaPr:
                self.listaProdTela.insert('',END, values=i) 


    def consuper_produto(self):
        """
        """
        self.listaProdTela.delete(*self.listaProdTela.get_children())
        self.prod = self.et_consulta_produto.get()
        if len(self.prod) == 0:
            messagebox.showwarning('Alerta', 'Preencha o campo de consulta.')
        else:
            self.resProd = self.produto.consultaperProduto(self.prod)
            if len(self.resProd) == 0:
                messagebox.showinfo('Informação', 'Nenhum produto encontrado.')
            else:
                for v in self.resProd:
                    self.listaProdtela.insert('',END, values=v)
                

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
        try:
            if len(self.lista) == 0:
                messagebox.showinfo('Informação', 'Não há clientes cadastrados.')
            else:
                for n in self.lista:
                    self.et_cod_cliente.config(state='normal')
                    self.listaCliente.insert('',END, values=n)
        except:
            messagebox.showerror('Erro', 'Erro ao listar clientes')

    def buscar_cliente(self):
        """
        """
        self.listaCliente.delete(*self.listaCliente.get_children())
        self.cli = self.et_consultar_cliente.get()
        try:
            if len(self.cli) == 0:
                messagebox.showwarning('Alerta', 'Preencha o campo de consulta.')
            else:
                self.resCli = self.cliente.consultarCliente(self.cli)
                if len(self.resCli) == 0:
                    messagebox.showinfo('Informação', 'Nenhum cliente encontrado.')
                else:
                    for v in self.resCli:
                        self.listaCliente.insert('',END, values=v)
        except:
            messagebox.showerror('Erro', 'Erro a buscar cliente')
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
                self.lista_cliente()
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
        Realiza a limpeza dos campos da tela cliente.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
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
    
    #Métodos de busca e listagem personalizados para telaCliente
    def listaper_cliente(self):
        """
        """
        self.listaClienteTela.delete(*self.listaClienteTela.get_children())
        self.listaP = self.cliente.listaperCliente()
        if len(self.listaP) == 0:
            messagebox.showinfo('Informação', 'Não há clientes cadastrados.')
        else:
            for n in self.listaP:
                self.listaClienteTela.insert('',END, values=n)

    def buscaper_cliente(self):
        """
        """
        self.listaClienteTela.delete(*self.listaClienteTela.get_children())
        self.cli = self.et_consultar_cliente.get()
        if len(self.cli) == 0:
            messagebox.showwarning('Alerta', 'Preencha o campo de consulta.')
        else:
            self.resCli = self.cliente.consultaperCliente(self.cli)
            if len(self.resCli) == 0:
                messagebox.showinfo('Informação', 'Nenhum cliente encontrado.')
            else:
                for v in self.resCli:
                    self.listaClienteTela.insert('',END, values=v)
        


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
                self.et_cod_fornecedor.config(state='normal')
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
            messagebox.showerror('Erro', 'Não foi possível deletar o fornecedor.')

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
        Realiza a limpeza dos campos da tela fornecedor.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
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
       

    # FUNÇÕES DOS BOTÕES DA TELA FORNECIMENTO
    def fornecimentoProduto(self):
        """
        """
        self.dadosProd = self.produto.listarProduto()
        self.exibirProdutos = []
        for i in range(0, len(self.dadosProd)):
            self.exibirProdutos.append(self.dadosProd[i][1:3])
        return self.exibirProdutos
    
    def fornecimentoFornecedor(self):
        """
        """
        self.dadosForn = self.fornecedor.listarFornecedor()
        self.exibirDados = []
        for c in range(0, len(self.dadosForn)):
            self.exibirDados.append(self.dadosForn[c][2])
        return self.exibirDados

    def inserir_fornecimento(self):
        """
        """
        self.cod_prod = None
        self.cnpj_forn = None
        self.resProduto = self.comboxProduto.get()
        self.fornecimentoProduto()

        for v in self.dadosProd:
            if self.resProduto in v:
                self.cod_prod = v[0]

        self.resFornecedor = self.comboxFornecedor.get()
        self.fornecimentoFornecedor()
        for i in self.dadosForn:
            if self.resFornecedor in i:
                self.cod_fornece = i[0]
        
        self.qtdfornecida = self.et_qtd_fornecida.get()
        self.data = self.et_data_fornecimento.get()
        
        self.fornecimento.cadastrar_fornecimento(self.cod_prod, self.cod_fornece, self.data, self.qtdfornecida)
        self.produto.atualizaEstoqueProd(self.cod_prod, self.qtdfornecida)
        self.limpa_fornecimento()

    def exibir_fornecimento(self):
        """
        """
        self.listaFornecimento.delete(*self.listaFornecimento.get_children())
        self.resultadoForn = self.fornecimento.listar_fornecimento()
        try:
            if len(self.resultadoForn) == 0:
                messagebox.showwarning('Alerta', 'Não fornecimento registrado')
            else:
                for r in self.resultadoForn:
                    self.listaFornecimento.insert('', END,values=r)
        except:
            messagebox.showerror('Erro', 'Houve um erro, não foi possível exibir a lista de fornecimento')

    def editar_fornecimento(self):
        """
        """
        self.alt_cod_fornece = None
        try:
            self.resForn = self.comboxFornecedor.get().strip()
            self.fornecimentoFornecedor()
            for i in self.dadosForn:
                if self.resForn in i:
                    self.alt_cod_fornece = i[0]
                self.fornecimento.set_cod_produto(self.alt_cod_fornece)
                self.fornecimento.set_qtd_fornecida(self.et_qtd_fornecida.get().strip())
                if len(self.fornecimento.get_cod_fornecedor()) == 0 and len(self.fornecimento.get_qtd_fornecida()) == 0:
                    messagebox.showwarning('Alerta', 'Selecione, para alterar')
                else:
                    self.fornecimento.alterar_fornecimento(self.fornecimento.get_cod_fornecedor(), self.fornecimento.get_qtd_fornecida)
        except:
            messagebox.showerror('Erro', 'Erro na alteração.')
        
    def duplo_clique_fornecimento(self, event):
        """
        """
        self.limpa_fornecimento()
        self.listaFornecimento.selection()
        for c in self.listaFornecimento.selection():
            col1, col2, col3, col4 = self.listaFornecimento.item(c, 'values')
            self.comboxProduto.insert(END, col1)
            self.comboxFornecedor.insert(END, col2)
            self.et_data_fornecimento.insert(END, col3)
            self.et_qtd_fornecida.insert(END, col4)

    def limpa_fornecimento(self):
        """
        Realiza a limpeza dos campos da subtela fornecimento.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
        """
        self.comboxProduto.delete(0, END)
        self.comboxFornecedor.delete(0, END)
        self.et_qtd_fornecida.delete(0, END)
        self.et_data_fornecimento.delete(0, END)



    #CRUD da venda
    #métodos para adicionar cliente e produto a venda
    def produtosVenda(self):
        self.prodVenda = self.produto.listarProduto()
        self.exibirProdutos = []
        for i in range(0, len(self.prodVenda)):
            self.exibirProdutos.append(self.prodVenda[i][1:3])
        return self.exibirProdutos
        
    def clienteVenda(self):
        self.cliVenda = self.cliente.listarCliente() 
        self.exibirDados = []
        for c in range(0, len(self.cliVenda)):
            self.exibirDados.append(self.cliVenda[c][0:3])
        return self.exibirDados
        
        
    def adiciona_venda(self):
        """
        """
        self.cod_prod = None
        self.cod_cliente = None
        self.resProduto = self.produtosVenda()
        self.inserir


        self.resCliente = self.comboxCliente.get()
        self.clienteVenda()
        for i in self.cliVenda:
            if self.resCliente in i:
                self.cod_cliente = i[1]
                self.self.listaVenda.insert('', END, values=self.resCliente)


    def remover_produto_venda(self, produto):
        self.produtos.remove(produto)
    
    def inserir_venda(self):
        """
        """
        pass 
    
    def calcular_total(self):
        """
        """
        pass
    
    def consultarVenda(self):
        self.listaHistTela.delete(*self.listaHistTela.get_children())
        self.codv = self.et_consulta_venda.get()
        if len(self.codv) == 0:
            messagebox.showwarning('Alerta', 'Preencha o campo de consulta.')
        else:
            self.resVen = self.venda.consultarVenda(self.codv)
            if len(self.resVen) == 0:
                messagebox.showinfo('Informação', 'Nenhuma venda encontrada.')
            else:
                for v in self.resVen:
                    self.listaHistTela.insert('',END, values=v)
    
    
    def listarVenda(self):
        self.listaHistTela.delete(*self.listaHistTela.get_children())
        self.listav = self.venda.listarVendas()
        if len(self.listav) == 0:
            messagebox.showinfo('Informação', 'Não há vendas cadastrados.')
        else:
            for i in self.listav:
                self.et_cod_venda.config(state='normal')
                self.listaHistTela.insert('',END, values = i)   


    def listar_vendas_por_dia(self, data):
        vendas_dia = []
        for venda in self.vendas:
            if venda[1].date() == data.date():
                vendas_dia.append(venda)
        return vendas_dia
    
    def listar_vendas_por_mes(self, mes, ano):
        vendas_mes = []
        for venda in self.vendas:
            if venda[1].month == mes and venda[1].year == ano:
                vendas_mes.append(venda)
        return vendas_mes


    def adicionar(self):
        self.cod_prod = self.et_cod_produto
        self.qtd = self.qtd_venda
