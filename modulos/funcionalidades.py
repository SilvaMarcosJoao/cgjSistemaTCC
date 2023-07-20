from tkinter import *
from tkinter import messagebox
from modulos.categoriaproduto import CategoriaProduto
from modulos.cliente import Cliente
from modulos.usuario import Usuario
from modulos.fornecedor import Fornecedor
from modulos.fornecimento import Fornecimento
from modulos.venda import Venda
from modulos.produto import Produto
from modulos.itensvenda import ItensVenda
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser


class Funcionalidades():

    # OBJETOS DAS CLASSES 
    categoria = CategoriaProduto()
    cliente = Cliente()
    usuario = Usuario()
    fornecedor = Fornecedor()
    fornecimento = Fornecimento()
    produto = Produto()
    venda = Venda()
    itensVenda = ItensVenda()
    
    # FUNÇÔES DOS BOTÕES DA TELA DE USUÁRIO
    def finalizar(self) -> None:
        self.appMenu.destroy()

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
        Exibe na tela as categorias retornadas pelo método listarCategoria da classe Categoria_Produto
        :param: Não tem parâmetro.
        :return: Não tem retorno.
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

    def deletar_categoria(self):
        """

        """
        self.cod = self.et_cod_categoria.get().strip()
        if len(self.cod) == 0:
            messagebox.showwarning('Erro', 'Não foi possível deletar a categoria, \nselecione-a antes de excluir.')
        else:
            self.categoria.excluirCategoria(self.cod)
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
        self.codCat = []
        self.codCat.append(self.cat)
        self.codBanco = self.categoria.codigoCategoria()
        self.codigoCatego = None
        for c in self.codBanco:
            print(int(self.codCat[0][1]))
            if c[0] == int(self.codCat[0][1]):
                 self.codigoCatego = c[0]
            elif self.codCat[0][1:3].isnumeric():
                if c[0] == int(self.codCat[0][1:3]):
                    self.codigoCatego = c[0]
        try:
            if self.desc_produto == '' or self.mod_produto == '' or self.preco_compra == '' or self.preco_venda == '' or self.codigoCatego == 0:
                messagebox.showwarning('Alerta', 'Por favor, preencha os campos')
            elif len(self.desc_produto) < 3 or len(self.desc_produto) > 25:
                    messagebox.showwarning('Alerta', 'Descrição inválida, \nquantidade de caracteres não atende aos requisitos')
            elif len(self.mod_produto) > 15:
                messagebox.showwarning('Alerta', 'Modelo inválido, preencha corretamente!')
            else:
                self.produto.cadastrarProduto(self.desc_produto, self.mod_produto, self.preco_compra, self.preco_venda, self.codigoCatego)
                self.limpa_produto()
                messagebox.showinfo('Sistema', 'Produto cadastrado com sucesso!')  
                
        except Exception as erro:
            messagebox.showerror('Erro', 'Não foi possível cadastrar o produto')

    def exibir_produto(self):
        """
        Exibe os dados retornado pelo método listarProdutos da classe Produto.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
        """
        self.listaProd.delete(*self.listaProd.get_children())
        self.exibirProd = self.produto.listarProdutos()
        if len(self.exibirProd) == 0:
            messagebox.showinfo('Sistema', 'Não há produtos cadastrados.')
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
                messagebox.showinfo('Sistema', 'Nenhum produto encontrado.')
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
        
    def deletar_produto(self):
        """
        """
        self.cod_prod = self.et_cod_produto.get().strip()
        try:
            if len(self.cod_prod) != 0:
                self.produto.excluirProduto(self.cod_prod)
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
        except Exception as errou:
            messagebox.showerror('Erro', 'Houve um erro inesperado!')  
            print(errou)
        self.limpa_cliente()

    def lista_cliente(self):
        """
        Exibe a lista de cliente retornada pelo método listarClientes da classe Cliente.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
        """
        self.listaCliente.delete(*self.listaCliente.get_children())
        self.lista = self.cliente.listarClientes()
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
            
    def deletar_cliente(self):
        """
        """
        self.codigo = self.et_cod_cliente.get()
        try:
            if len(self.codigo) == 0:
                messagebox.showwarning('Alerta', 'Cliente não encontrado, impossível deletar')
            else:
                self.cliente.excluirCliente(self.codigo)
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
        self.dadosProd = self.produto.listarProdutos()
        self.exibirProdutos = []
        for i in range(0, len(self.dadosProd)):
            self.exibirProdutos.append(self.dadosProd[i][0:3])
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
        try:
            self.resProduto = self.comboxProduto.get()
            self.resFornecedor = self.comboxFornecedor.get()
            self.qtdfornecida = int(self.et_qtd_fornecida.get())
            self.data = self.et_data_fornecimento.get()
            if len(self.resProduto) == 0 or len(self.resFornecedor) == 0 or self.qtdfornecida == 0 or len(self.data) == 0:
                messagebox.showwarning('Alerta','Por favor, preencha as informações')
            elif type(self.qtdfornecida) != int:
                messagebox.showwarning('Alerta','Por favor, insira um quantidade válida')
            else:
                self.fornecimentoProduto()
                for v in self.dadosProd:   
                    if int(self.resProduto[0]) in v:
                        self.cod_prod = v[0]

                self.fornecimentoFornecedor()
                for i in self.dadosForn:
                    if self.resFornecedor in i:
                        self.cod_fornece = i[0]
        
                self.fornecimento.cadastrarFornecimento(self.cod_prod, self.cod_fornece, self.data, self.qtdfornecida)
                self.produto.atualizaEstoqueProd(self.cod_prod, self.qtdfornecida)
                messagebox.showinfo('Sistema', 'Fornecimento Realizado!')
        except Exception as err: 
            messagebox.showerror('Erro', 'Erro no fornecimento')
            print(err)
        self.limpa_fornecimento()

    def exibir_fornecimento(self):
        """
        Exibe os dados retornados pela função de consulta da classe fornecimento.
        :param: Não ná parâmetro.
        :return: Não há retorno.
        """
        self.listaFornecimento.delete(*self.listaFornecimento.get_children())
        self.resultadoForn = self.fornecimento.listarFornecimentos()
        try:
            if len(self.resultadoForn) == 0:
                messagebox.showwarning('Alerta', 'Não fornecimento registrado')
            else:
                for r in self.resultadoForn:
                    self.listaFornecimento.insert('', END,values=r)
        except:
            messagebox.showerror('Erro', 'Houve um erro, não foi possível exibir a lista de fornecimento')

 
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
        self.prodVenda = self.produto.consultaProdutoVenda()
        self.exibirProdutos = []

        for i in range(0, len(self.prodVenda)):
            self.exibirProdutos.append(self.prodVenda[i])
        return self.prodVenda
        
        
    def clienteVenda(self):
        self.cliVenda = self.cliente.listarClientes() 
        self.exibirDados = []
        for c in range(0, len(self.cliVenda)):
            self.exibirDados.append(self.cliVenda[c][0:3])
        return self.exibirDados
        
    def adicionaItens_venda(self):
        self.produtoadd = [self.comboxaddItens.get()]
        
        self.lista = []
        
        self.produtosBanco = self.produtosVenda()
        for v in self.produtosBanco:
            if int(self.produtoadd[0][0]) == v[0]:
                self.lista.append(list(v))

        for l in self.lista:
            l.append(int(self.et_qtd_venda.get()))
            l.append(l[3] * l[4])
        for i in self.lista:
            self.listaAddItens.insert('', END, values=i)
            self.itensVenda.itens.append(i)
        
        #print(self.itensVenda.itens)
            

    def remover_produto_venda(self):
        """
        Remove os itens do carrinho
        :param: Não tem parâmetros.
        :return: Não tem retorno.
        """
        self.listaAddItens.selection()
        for i in self.listaAddItens.selection():
            self.listaAddItens.delete(i)
        

    def limpaItens(self):
        self.comboxaddItens.delete(0, END)
        self.et_qtd_venda.delete(0, END)
        self.et_data_venda.delete(0, END)
        self.comboxClien_venda.delete(0, END)


    def inserir_venda(self):
        """
        Captura os dados selecionados, e envia para o método de cadastro 
        da classe Venda.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
        """
        self.valortotal = ''
        self.clienteadd = [self.comboxClien_venda.get()]
        self.client = self.cliente.listarClientes()
        for c in self.client:
            if c[0] == int(self.clienteadd[0][0:2]):
                self.cod_cli = c[0]
    
        self.listaItens = self.itensVenda.itens
        soma = 0.0
        for i in self.listaItens:
            soma += float(i[5])
        self.data = self.et_data_venda.get()
        self.venda.cadastrarVenda(self.cod_cli, soma, self.data)
        #self.lbl_exibGeral.insert('', END, values=soma)
        self.pro = self.produto.listarProdutos()
        self.codigoVenda = self.venda.resCodVenda()
        for item in self.listaItens:
            self.itensVenda.cadastrarItens(self.codigoVenda[0][0], item[0], item[4], item[5]) 
            if item[0] == self.pro[0][0]:
                if int(item[4]) > self.pro[0][5]:
                    messagebox.showwarning('Atenção', 'Você não pode vender mais do que tem em estoque!')
                else:  
                    self.produto.abatEstoqueProd(item[0], int(item[4]))
                    messagebox.showinfo('Sistema', 'Venda Realizada!')
                    self.limpaItens()

    def consultarVenda(self):
        self.listaRelatorio.delete(*self.listaRelatorio.get_children())
        self.codv = self.et_consultar.get()
        if len(self.codv) == 0:
            messagebox.showwarning('Alerta', 'Preencha o campo de consulta.')
        else:
            self.resVen = self.venda.consultarVenda(self.codv)
            if len(self.resVen) == 0:
                messagebox.showinfo('Informação', 'Nenhuma venda encontrada.')
            else:
                for v in self.resVen:
                    self.listaRelatorio.insert('',END, values=v)
        self.et_consultar.delete(0, END)
    
    
    def listarVenda(self):
        self.listaRelatorio.delete(*self.listaRelatorio.get_children())
        self.listav = self.venda.listarVendas()
        if len(self.listav) == 0:
            messagebox.showinfo('Informação', 'Não há vendas cadastrados.')
        else:
            for i in self.listav:
                self.listaRelatorio.insert('',END, values=i)   

    def gerarRelPDF(self):
        # Criando arquivo pdf do relatório
        self.canv = canvas.Canvas('./relatorios/RelatorioVendasGeral.pdf')
        

        self.canv.setFont('Helvetica-Bold', 20)
        #desenhar uma string na tela
        self.canv.drawString(200, 790, 'Relatório de Vendas')

        self.canv.setFont('Helvetica', 15)
        self.canv.drawString(6, 700, f'Código venda')

        self.canv.setFont('Helvetica', 15)
        self.canv.drawString(160, 700, f'Cliente')

        self.canv.setFont('Helvetica', 15)
        self.canv.drawString(310, 700, f'CPF')

        self.canv.setFont('Helvetica', 15)
        self.canv.drawString(390, 700, f'Valor total')

        self.canv.setFont('Helvetica', 15)
        self.canv.drawString(490, 700, f'Data da Venda')
        self.canv.rect(4, 750, 591, 250, fill=False, stroke=True)

        #Organizando os valores do cliente na tela
        self.vendas = list(self.venda.listarVendas())
        self.x = 20
        self.y = 700
        self.ylinhavertical = 540
        for venda in self.vendas:
            self.ylinhavertical-= 55
            self.y = self.y  - 80
            
            self.canv.drawString(40,self.y, f'{venda[0]}')
            self.canv.drawString(110,self.y, f'{venda[1]}')
            self.canv.drawString(280,self.y, f'{venda[2]}')
            self.canv.drawString(400,self.y, f'{venda[3]}')
            self.canv.drawString(505,self.y, f'{venda[4]}')
            self.canv.rect(4, self.ylinhavertical, 591, 250, fill=False, stroke=True)
            



        #criar linha e ou espaçamento na tela 20 é a esquerda começando 550 abaixo da última informação o outro
        # 550 seria o comprimento do retangulo e o 5 é a grossura da linha 
        '''self.canv.rect(20, 720, 550, 250, fill=False, stroke=True)
        self.canv.rect(20, 220, 0, 500, fill=False, stroke=True)
        self.canv.rect(148, 220, 0, 500, fill=False, stroke=True)
        self.canv.rect(340, 220, 0, 500, fill=False, stroke=True)
        self.canv.rect(440, 220, 0, 500, fill=False, stroke=True)
        self.canv.rect(570, 220, 0, 500, fill=False, stroke=True)
        self.canv.rect(20, 190, 550, 0, fill=False, stroke=True)
        self.canv.rect(20, 250, 550, 0, fill=False, stroke=True)
        self.canv.rect(20, 310, 550, 0, fill=False, stroke=True)
        self.canv.rect(20, 370, 550, 0, fill=False, stroke=True)
        self.canv.rect(20, 430, 550, 0, fill=False, stroke=True)
        self.canv.rect(20, 490, 550, 0, fill=False, stroke=True)
        self.canv.rect(20, 550, 550, 0, fill=False, stroke=True)
        self.canv.rect(20, 610, 550, 0, fill=False, stroke=True)
        self.canv.rect(20, 670, 550, 0, fill=False, stroke=True)'''

        self.canv.showPage()
        self.canv.save()
        messagebox.showinfo('Sistema', 'PDF Gerado com Sucesso!')
