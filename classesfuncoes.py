from mods import *

class BancoDados:
    # CONSTRUTOR
    def __init__(self) -> None:
        # ATRIBUTOS
        self.__nome = 'zurcBanco.db'
        self.conexao = None
        self.cursor = None

    # MÉTODOS DE CONEXÃO E DESCONEXÃO DA CLASSE BANCO DADOS
    def conectar(self) -> None:
        """
        """
        try:
            self.conexao = sqlite3.connect(self.__nome)
            self.cursor = self.conexao.cursor()
        except Exception as error:
            print(f'Houve um erro: {error}')

    def desconectar(self) -> None:
        """
        """
        try:
            self.conexao.close()
        except Exception as erro:
            print(f'Erro ao desconectar-se: {erro}')

    def tabelaCategoria(self):
        self.conectar()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS "categoria_produto" (
	    "cod_categoria_produto"	INTEGER NOT NULL UNIQUE,
	    "desc_categoria_produto"  TEXT(15) NOT NULL,
	    PRIMARY KEY("cod_categoria_produto" AUTOINCREMENT));""")
        self.conexao.commit()
        self.desconectar()
    
    def tabelaProduto(self):
        self.conectar()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS "produto" (
	    "cod_produto"	INTEGER NOT NULL UNIQUE,
	    "desc_produto"	TEXT(25) NOT NULL,
	    "modelo_produto"	TEXT(15) NOT NULL,
	    "preco_compra_produto"	REAL NOT NULL,
	    "preco_venda_produto"	REAL NOT NULL,
	    "qtd_estoque"	INTEGER DEFAULT 0,
	    "cod_categoria_produto"	INTEGER NOT NULL,
	    FOREIGN KEY("cod_categoria_produto") REFERENCES "categoria_produto",
	    PRIMARY KEY("cod_produto" AUTOINCREMENT));""")
        self.conexao.commit()
        self.desconectar()

    def tabelaUsuario(self):
        self.conectar()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS "usuario" (
	    "cod_usuario"	INTEGER NOT NULL UNIQUE,
	    "nome"	TEXT(20) NOT NULL,
	    "usuario"	TEXT(15) NOT NULL,
	    "senha"	TEXT(8) NOT NULL UNIQUE,
	    PRIMARY KEY("cod_usuario" AUTOINCREMENT));""")
        self.conexao.commit()
        self.desconectar()

    def tabelaFornecedor(self):
        self.conectar()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS "fornecedor" (
	    "cod_fornecedor"	INTEGER NOT NULL UNIQUE,
	    "cnpj_cpf"	TEXT(14) NOT NULL UNIQUE,
	    "nome_fornecedor"	TEXT(25) NOT NULL,
	    "email"	TEXT(35) NOT NULL UNIQUE,
	    "telefone"	TEXT(14) NOT NULL,
	    "logradouro"	TEXT(40) NOT NULL,
	    "numero"	INTEGER NOT NULL,
	    "cep"	INTEGER(8),
	    "cidade"	TEXT(40) NOT NULL,
	    "estado"	TEXT(40) NOT NULL,
	    PRIMARY KEY("cod_fornecedor" AUTOINCREMENT)); """)
        self.conexao.commit()
        self.desconectar()
    
    def tabelaFornecimento(self):
        self.conectar()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS "fornecimento" (
	    "cod_produto"	INTEGER NOT NULL,
	    "cod_fornecedor"	INTEGER NOT NULL,
	    "data_fornecimento"	TEXT(10),
	    "qtd_fornecida"	INTEGER NOT NULL,
	    FOREIGN KEY("cod_produto") REFERENCES "produto"("cod_produto"),
	    FOREIGN KEY("cod_fornecedor") REFERENCES "fornecimento"("cod_fornecedor"));""")
        self.conexao.commit()
        self.desconectar()

    def tabelaCliente(self):
        self.conectar()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS "cliente" (
	    "cod_cliente"	INTEGER NOT NULL UNIQUE,
	    "cpf"	TEXT(14) UNIQUE,
	    "nome_cliente"	TEXT(20) NOT NULL,
	    "email"	TEXT(35) UNIQUE,
	    "telefone"	TEXT(14) NOT NULL UNIQUE,
	    "logradouro"	TEXT(40) NOT NULL,
	    "numero"	INTEGER NOT NULL,
	    "cep"	INTEGER(8) UNIQUE,
	    "cidade"	TEXT(40) NOT NULL,
	    "estado"	TEXT(40) NOT NULL,
	    PRIMARY KEY("cod_cliente" AUTOINCREMENT));""")
        self.conexao.commit()
        self.desconectar()

    def tabelaVenda(self):
        self.conectar()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS "venda" (
	    "cod_venda"	INTEGER NOT NULL UNIQUE,
	    "cod_cliente"	INTEGER NOT NULL,
	    "valor_total"	REAL NOT NULL,
	    "data_venda"	TEXT(10) NOT NULL,
	    PRIMARY KEY("cod_venda" AUTOINCREMENT),
	    FOREIGN KEY("cod_cliente") REFERENCES "cliente");""")
        self.conexao.commit()
        self.desconectar()

    def tabelaItensVenda(self):
        self.conectar()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS "itens_venda" (
	    "cod_venda"	INTEGER NOT NULL UNIQUE,
	    "cod_produto"	INTEGER NOT NULL,
	    "qtd"	INTEGER NOT NULL,
	    "valor"	INTEGER NOT NULL,
	    FOREIGN KEY("cod_venda") REFERENCES "venda",
	    FOREIGN KEY("cod_produto") REFERENCES "produto"); """)
        self.conexao.commit()
        self.desconectar()



import sqlite3
banco = BancoDados()
banco.tabelaUsuario()
banco.tabelaCategoria()
banco.tabelaProduto()
banco.tabelaFornecedor()
banco.tabelaFornecimento()
banco.tabelaCliente()
banco.tabelaVenda()
banco.tabelaItensVenda()

class CategoriaProduto:
    banco = BancoDados()
    # CONSTRUTOR
    def __init__(self, cod_categoria_produto: int=None, desc_categoria_produto:str=None) -> None:
        # ATRIBUTOS
        self.__cod_categoria_produto = cod_categoria_produto
        self.__desc_categoria_produto=desc_categoria_produto
        
    # GETTERS E SETTERS
    def get_cod_categoria_produto(self) -> int:
        return self.__cod_categoria_produto
    
    def set_cod_categoria_produto(self, cod: int) -> None:
        self.__cod_categoria_produto = cod
    
    def get_desc_categoria_produto(self) -> str:
        return self.__desc_categoria_produto

    def set_desc_categoria_produto(self, desc_categoria_produto) -> None:
        self.__desc_categoria_produto = desc_categoria_produto

    # MÉTODOS DE CRUD DA CLASSE CATEGORIA PRODUTO
    def cadastrarCategoria(self, desc_categoria:str) -> None:
        """
        Cadastra a categoria dos produtos.
        :param: desc_categoria. 
        :return: Não há retorno. 
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO categoria_produto (desc_categoria_produto) 
        VALUES ('{desc_categoria}')""")
        self.banco.conexao.commit()
        self.banco.desconectar()
        
    def alterarCategoria(self, cod_categoria_produto:int, desc_categoria:str) -> None:
        """
        Altera a descrição de uma categoria.
        :param: cod_categoria_produto do tipo inteiro e desc_categoria do tipo string.
        :return: Não tem retorno
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""UPDATE categoria_produto SET desc_categoria_produto = ('{desc_categoria}')
                                WHERE cod_categoria_produto = ('{cod_categoria_produto}') """) 
        self.banco.conexao.commit()
        self.banco.desconectar()

    def listarCategoria(self) -> list:
        """
        Exibe as categorias cadastradas.
        :param: não há parâmetros.
        :return: retorna uma lista com as categorias.
        """
        self.banco.conectar()
        categoria = self.banco.cursor.execute(f"""SELECT * FROM categoria_produto """).fetchall()     
        self.banco.desconectar()
        return categoria
    
    def excluirCategoria(self, cod_categoria_produto:int) -> None:
        """
        Deleta uma categoria.
        :param: cód_categoria_produto do tipo inteiro.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""DELETE FROM categoria_produto
                                WHERE cod_categoria_produto = '{cod_categoria_produto}' """)
        self.banco.conexao.commit()
        self.banco.desconectar()

    def buscaQtdCodigoCategoria(self) -> int:
        self.banco.conectar()
        self.qtdcRegis = self.banco.cursor.execute(f""" SELECT count(cod_categoria_produto)  from categoria_produto""").fetchall()

        return self.qtdcRegis
    
    def codigoCategoria(self) -> int:
        self.banco.conectar()
        self.codigo = self.banco.cursor.execute(f""" SELECT cod_categoria_produto  from categoria_produto""").fetchall()
        return self.codigo
    

class Produto:
    banco = BancoDados()
    # CONSTRUTOR
    def __init__(self,cod_produto: int=None, desc_produto: str=None, modelo_produto:str=None ,preco_compra_produto:float=None, preco_venda_produto: float=None, qtd : int=None, categoria_produto :int=None):
        # ATRIBUTOS
        self.__cod_produto=cod_produto
        self.__desc_produto=desc_produto
        self.__modelo_produto=modelo_produto
        self.__preco_compra_produto=preco_compra_produto
        self.__preco_venda_produto=preco_venda_produto
        self.__qtd =qtd 
        self.__categoria_produto=categoria_produto

    # GETTERS E SETTERS
    def get_cod_produto(self) -> int:
        return self.__cod_produto

    def get_desc_produto(self) -> str:
        return self.__desc_produto

    def get_modelo_produto(self) -> str:
        return self.__modelo_produto

    def get_preco_compra_produto(self) -> float:
        return self.__preco_compra_produto

    def get_preco_venda_produto(self) -> float:
        return self.__preco_venda_produto

    def get_qtd(self) -> int:
        return self.__qtd

    def get_cod_categoria_produto(self) -> int:
        return self.__categoria_produto

    def set_cod_produto(self, cod_produto:int) -> None:
        self.__cod_produto = cod_produto

    def set_desc_produto(self, desc_produto:str) -> None:
        self.__desc_produto = desc_produto

    def set_modelo_produto(self, modelo_produto:str) -> None:
        self.__modelo_produto = modelo_produto

    def set_preco_compra_produto(self, preco_compra_produto:float) -> None:
        self.__preco_compra_produto = preco_compra_produto

    def set_preco_venda_produto(self, preco_venda_produto:float) -> None:
        self.__preco_venda_produto = preco_venda_produto

    def set_qtd(self, qtd:int) -> None:
        self.__qtd = qtd

    def set_cod_categoria_produto(self, cod_categoria_produto:int) -> None:
        self.__cod_produto = cod_categoria_produto


    # MÉTODOS DE CRUD DA CLASSE PRODUTO
    def cadastrarProduto(self, desc_produto:str, mod_produto:str, preco_compra:float, preco_venda:float, cod_categoria:int) -> None:
        """
        Realiza o cadastro de produto.
        :param: desc_produto, mod_produto, preco_compra, preco_venda e cod_categoria.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO produto (desc_produto, modelo_produto,
                          preco_compra_produto, preco_venda_produto, cod_categoria_produto) 
                           VALUES ('{desc_produto}','{mod_produto}',
                           '{preco_compra}','{preco_venda}','{cod_categoria}') """)
        self.banco.conexao.commit()
        self.banco.desconectar()
       
    def alterarProduto(self, cod_produto:int, desc_produto:str, modelo_produto:str, preco_compra_produto:float, preco_venda_produto:float) -> None:
        """
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""UPDATE produto
                                SET desc_produto =('{desc_produto}'),
                                modelo_produto =('{modelo_produto}'),
                                preco_compra_produto =('{preco_compra_produto}'),
                                preco_venda_produto =('{preco_venda_produto}')
                                WHERE cod_produto =('{cod_produto}')""")
        self.banco.conexao.commit()
        self.banco.desconectar()
   
    def listarProdutos(self) -> list:
        """
        Exibe um lista com todos os produtos cadastrados.
        :param: Não tem parâmetro.
        :return: Retorna uma lista com os produtos.
        """
        self.banco.conectar()
        self.produtos = self.banco.cursor.execute("""SELECT cod_produto, desc_produto, modelo_produto, preco_compra_produto,
                                      preco_venda_produto, qtd_estoque, categoria_produto.desc_categoria_produto 
                                      FROM categoria_produto, produto 
                                      WHERE produto.cod_categoria_produto = categoria_produto.cod_categoria_produto""").fetchall()
        self.banco.desconectar()
        return self.produtos
        
    def consultarProduto(self, desc_produto:str) -> list: 
        """
        """
        self.banco.conectar()
        produto = self.banco.cursor.execute(f"""SELECT cod_produto, desc_produto, modelo_produto,
                          preco_compra_produto, preco_venda_produto, qtd_estoque, categoria_produto.desc_categoria_produto 
                          FROM categoria_produto, produto
                            WHERE produto.cod_categoria_produto = categoria_produto.cod_categoria_produto and desc_produto like '{desc_produto[0]}%'""").fetchall()
        self.banco.desconectar()  
        return produto

    def excluirProduto(self, cod_produto:int) -> None:
        """
        Exclui um produto específico.
        :param: cod_produto.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""DELETE FROM produto
                                WHERE cod_produto='{cod_produto}'""")
        self.banco.conexao.commit()
        self.banco.desconectar()

    # MÉTODOS ASSOCIAS A VENDA
    def atualizaEstoqueProd(self, cod_produto:int, qtd:int) -> None:
        """
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""UPDATE produto SET qtd_estoque = qtd_estoque + '{qtd}' 
                    WHERE cod_produto = {cod_produto}""")
        self.banco.conexao.commit()
        self.banco.desconectar()
        
    def abatEstoqueProd(self, cod_produto: int, qtd:int) -> None:
        """ 
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""UPDATE produto SET qtd_estoque=qtd_estoque - '{qtd}'
                                  WHERE cod_produto = {cod_produto}""")
        self.banco.conexao.commit()
        self.banco.desconectar()

    def consultaProdutoVenda(self) -> list:
        """
        """
        self.banco.conectar()
        self.produto = self.banco.cursor.execute(f"""SELECT cod_produto, desc_produto,
                                         modelo_produto, preco_venda_produto FROM produto 
                                         """).fetchall()   
        self.banco.desconectar()
        return self.produto
    
    



class Fornecedor:
    banco = BancoDados()
    # CONSTRUTOR
    def __init__(self,cod_fornecedor:int=None, cpnj_cpf:str=None, nome_fornecedor:str=None, 
                 email:str=None, telefone:str=None, logradouro:str=None, numero:int=None, cep:int=None,
                 cidade:str=None, estado:str=None) -> None:
        # ATRIBUTOS
        self.__cod_fornecedor = cod_fornecedor
        self.__cnpj_cpf = cpnj_cpf
        self.__nome_fornecedor = nome_fornecedor
        self.__email = email
        self.__telefone = telefone
        self.__logradouro = logradouro
        self.__numero = numero
        self.__cep = cep
        self.__cidade = cidade
        self.__estado = estado

    # GETTERS E SETTERS
    def get_cod_fornecedor(self) -> int:
        return self.__cod_fornecedor

    def set_cod_fornecedor(self, cod_fornecedor:int) -> None:
        self.__cod_fornecedor = cod_fornecedor
    
    def get_cpnj_cpf(self) -> str:
        return self.__cnpj_cpf

    def set_cnpj_cpf(self, cnpj_cpf:str) -> None:
        self.__cnpj_cpf = cnpj_cpf

    def get_nome_fornecedor(self) -> str:
        return self.__nome_fornecedor

    def set_nome_fornecedor(self, nome_fornecedor:str) -> None:
        self.__nome_fornecedor = nome_fornecedor

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email:str) -> None:
        self.__email = email

    def get_telefone(self) -> str:
        return self.__telefone

    def set_telefone(self, telefone:str) -> None:
        self.__telefone = telefone

    def get_logradouro(self) -> str:
        return self.__logradouro

    def set_logradouro(self, logradouro:str) -> None:
        self.__logradouro = logradouro

    def get_numero(self) -> int:
        return self.__numero

    def set_numero(self, numero:int) -> None:
        self.__numero = numero

    def get_cep(self) -> int:
        return self.__cep

    def set_cep(self, cep:int) -> None:
        self.__cep = cep

    def get_cidade(self) -> str:
        return self.__cidade

    def set_cidade(self, cidade:str) -> None:
        self.__cidade = cidade

    def get_estado(self) -> str:
        return self.__estado

    def set_estado(self, estado:str) -> None:
        self.__estado = estado

    # MÉTODOS DE CRUD DA CLASSE FORNECEDOR
    def cadastrarFornecedor(self, cnpj:str, nome_fornecedor:str, email:str, telefone:str, logradouro:str, numero:int, cep:int, cidade:str, estado:str) -> None:
        """
        Cadastra um fornecedor.
        :param: cnpj, nome_fornecedor, email, telefone, logradouro, numero, cep, cidade e estado.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f""" INSERT INTO fornecedor (cnpj_cpf, 
                                 nome_fornecedor, email, telefone, logradouro, 
                                 numero, cep, cidade, estado)
                                 VALUES ('{cnpj}', '{nome_fornecedor}', '{email}', '{telefone}', '{logradouro}', '{numero}', '{cep}', 
                                 '{cidade}', '{estado}')""")
        self.banco.conexao.commit()
        self.banco.desconectar()

    def listarFornecedor(self) -> list:
        """
        Retorna uma lista com fornecedores.
        :param: Não tem parâmetro.
        :return: retorna uma lista com dados.
        """
        self.banco.conectar()
        fornecedores=self.banco.cursor.execute(f"""SELECT * FROM fornecedor""").fetchall()   
        self.banco.desconectar()
        return fornecedores

    def consultarFornecedor(self, nome_fornecedor:str) -> list:
        """
        Exibe os dados de um fornecedor específico.
        :param: nome_fornecedor.
        :return: retorna uma lista com os dados do fornecedor.
        """
        self.banco.conectar()
        forn = self.banco.cursor.execute(f"""SELECT cod_fornecedor, cnpj_cpf, nome_fornecedor,
                                    email, telefone, logradouro, numero, 
                                    cep, cidade, estado FROM fornecedor 
                                    WHERE nome_fornecedor like '{nome_fornecedor[0]}%' """).fetchall()
        self.banco.desconectar()
        return forn

    def alterarFornecedor(self,cod_fornecedor:int, cnpj:str, nome_fornecedor:str, email:str, telefone:str, logradouro:str, numero:int, cep:int, cidade:str, estado:str) -> None:
        """
        Altera os dados de um fornecedor específico.
        :param: cod_fornecedor, cnpj, nome_fornecedor, email, telefone, logradouro, numero, cep, cidade e estado.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""UPDATE fornecedor 
        SET cnpj_cpf = '{cnpj}',
        nome_fornecedor = '{nome_fornecedor}',
        email = '{email}',
        telefone = '{telefone}',
        logradouro = '{logradouro}',
        numero = '{numero}',
        cep = '{cep}',
        cidade = '{cidade}',
        estado = '{estado}'
        WHERE cod_fornecedor = '{cod_fornecedor}' """)
        self.banco.conexao.commit()
        self.banco.desconectar()

    def excluirFornecedor(self, cod_fornecedor:int) -> None:
        """
        Exclui um fornecedor específico.
        :param: cod_fornecedor.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""DELETE FROM fornecedor 
                                 WHERE cod_fornecedor = {cod_fornecedor}""")
        self.banco.conexao.commit()
        self.banco.desconectar()


class Fornecimento:
    banco = BancoDados()
    # CONSTRUTOR
    def __init__(self, cod_fornecedor=None, cod_produto=None, qtd_fornecida=None, data_fornecimento=None) -> None:
        # ATRIBUTOS
        self.__cod_fornecedor= cod_fornecedor
        self.__cod_produto = cod_produto
        self.__qtd_fornecida = qtd_fornecida
        self.__data_fornecimento = data_fornecimento

    # GETTERS E SETTERS
    def get_cod_fornecedor(self) -> int:
        return self.__cod_fornecedor 

    def set_cnpj(self, cod_fornecedor) -> None:
        self.__cod_fornecedor = cod_fornecedor

    def get_cod_produto(self) -> int:
        return self.__cod_produto
    
    def set_cod_produto(self, cod_produto) -> None:
        self.__cod_produto = cod_produto

    def get_qtd_fornecida(self) -> int:
        return self.__qtd_fornecida

    def set_qtd_fornecida(self, qtd_fornecida: int) -> None:
        self.__qtd_fornecida = qtd_fornecida

    def get_data_fornecimento(self) -> str:
        return self.__data_fornecimento

    def set_data_fornecimento(self, data_fornecimento: str) -> None:
        self.__data_fornecimento = data_fornecimento

    # MÉTODOS DE CRUD DA CLASSE FORNECIMENTO
    def cadastrarFornecimento(self, cod_produto:int, cod_fornecedor:int, data:str, qtd:int) -> None:
        """
        Insere os dados na tabela fornecimento.
        :param: cod_produto, cod_fornecedor, data e qtd.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO fornecimento (cod_produto, cod_fornecedor, data_fornecimento, qtd_fornecida)
                                  VALUES ('{cod_produto}', '{cod_fornecedor}', '{data}', '{qtd}')""")
        self.banco.conexao.commit()
        self.banco.desconectar()
    
    def listarFornecimentos(self) -> list:
        """
        Exibe a lista de fornecedores e os produtos fornecidos por eles.
        :param: Não há parâmetro.
        :return: retorna uma lista com dados.
        """
        self.banco.conectar()
        self.forneci = list(self.banco.cursor.execute(f""" SELECT produto.desc_produto, fornecedor.nome_fornecedor, data_fornecimento, qtd_fornecida 
                                                 FROM produto, fornecedor, fornecimento
                                                 WHERE fornecimento.cod_produto = produto.cod_produto and 
                                                 fornecimento.cod_fornecedor = fornecedor.cod_fornecedor""").fetchall())
        self.banco.conexao.commit()
        self.banco.desconectar()
        return self.forneci
    
    def alterar_fornecimento(self, cod_produto:int, cod_fornecedor:int) -> None:
        """
        """
        self.banco.conectar()
        self.banco.cursor.execute(f""" UPDATE fornecimento SET qtd_fornecida, data_fornecimento
                                  WHERE cod_produto = '{cod_produto}' and cod_fornecedor = '{cod_fornecedor}' """)
        self.banco.conexao.commit()
        self.banco.desconectar()

class Cliente:
    banco = BancoDados()
    # CONSTRUTOR
    def __init__(self, cod_cliente:int=None, cpf:str=None, nome_cliente:str=None, email:str=None ,telefone:str=None, logradouro:str=None, numero:int=None, cep:int=None, cidade:str=None, estado:str=None):
        # ATRIBUTOS
        self._cod_cliente=cod_cliente
        self.__nome_cliente=nome_cliente
        self.__logradouro=logradouro
        self.__cpf=cpf
        self.__telefone=telefone
        self.__email=email
        self.__numero=numero
        self.__cep=cep
        self.__cidade=cidade
        self.__estado=estado

    # GETTERS E SETTERS
    def get_cod_cliente(self) -> int:
        return self.__cod_cliente
    
    def get_nome_cliente(self) -> str:
        return self.__nome_cliente

    def get_logradouro(self) -> str:
        return self.__logradouro

    def get_cpf(self) -> str:
        return self.__cpf

    def get_telefone(self) -> str:
        return self.__telefone

    def get_email(self) -> str:
        return self.__email

    def get_numero(self) -> int:
        return self.__numero

    def get_cep(self) -> int:
        return self.__cep

    def get_cidade(self) -> str:
        return self.__cidade

    def get_estado(self) -> str:
        return self.__estado
    
    def set_cod_cliente(self, cod:int )-> None:
        self.__cod_cliente = cod

    def set_nome_cliente(self, nome_cliente:str) -> None:
        self.__nome_cliente = nome_cliente

    def set_logradouro(self, logradouro:str) -> None:
        self.__logradouro = logradouro

    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def set_telefone(self, telefone:str) -> None:
        self.__telefone = telefone

    def set_email(self, email:str) -> None:
        self.__email = email

    def set_numero(self, numero:int) -> None:
        self.__numero = numero

    def set_cep(self, cep:int) -> None:
        self.__cep = cep

    def set_cidade(self, cidade:str) -> None:
        self.__cidade = cidade

    def set_estado(self, estado:str) -> None:
        self.__estado = estado

    # MÉTODOS DE CRUD DA CLASSE CLIENTE
    def cadastrarCliente(self, cpf:str, nome_cliente:str, email:str, telefone:str, logradouro:str, numero:int, cep:int, cidade:str, estado:str) -> None:
        """
        Efetua o cadastro dos clientes.
        :param: .
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO cliente (cpf, nome_cliente, email,
                          telefone, logradouro, numero, cep, cidade, estado) 
                          values('{cpf }','{nome_cliente }','{email }','{telefone }',
                          '{logradouro }','{numero }','{cep }','{cidade }',
                          '{estado }')""")
        self.banco.conexao.commit()
        self.banco.desconectar()
        
    def alterarCliente(self, cod_cliente:int, cpf:str, nome_cliente:str, email:str, telefone:str, logradouro:str, numero:int, cep:int, cidade:str, estado:str) -> None:
        """
        Altera os dados de um cliente.
        :param:cod_cliente, cpf, nome_cliente, email, telefone, logradouro, numero, cep, cidade e estado.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""UPDATE cliente
                                SET cpf = ('{cpf }'), 
                                nome_cliente = ('{nome_cliente }') ,
                                email = ('{email }'),
                                telefone = ('{telefone }'),
                                logradouro = ('{logradouro }'),
                                numero = ('{numero }'),
                                cep = ('{cep }'), 
                                cidade= ('{cidade }'), 
                                estado = ('{estado }')
                                WHERE cod_cliente='{cod_cliente}'""")
        self.banco.conexao.commit()
        self.banco.desconectar()
        
    def listarClientes(self) -> list:
        """
        Exibe uma lista de clientes.
        :param: Não tem parâmetro.
        :return: retorna uma lista com clientes.
        """
        self.banco.conectar()
        clientes=self.banco.cursor.execute(f"""SELECT * FROM cliente""").fetchall()   
        self.banco.desconectar()
        return clientes 
    
    def consultarCliente(self, nome:str) -> list:
        """
        Exibe um cliente especifico.
        :param: nome.
        :param: retorna uma lista com os dados do cliente.
        """
        self.banco.conectar()
        cli = self.banco.cursor.execute(f"""SELECT cod_cliente, cpf, nome_cliente, email,
                          telefone, logradouro, numero, cep, cidade, estado FROM Cliente
                         WHERE nome_cliente like '{nome[0]}%' """).fetchall()              
        self.banco.desconectar()    
        return cli
    
    def excluirCliente(self, cod_cliente:int) -> None:
        """
        Deleta um cliente especifica.
        :param: cod_cliente.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""DELETE FROM cliente
                                WHERE cod_cliente='{cod_cliente}'""")
        self.banco.conexao.commit()
        self.banco.desconectar()

    
    #MÉTODOS PERSONALIZADOS para telaCliente

    def listaperCliente(self) -> list:
        """
        """
        self.banco.conectar()
        cliente = self.banco.cursor.execute(f"""SELECT cod_cliente, cpf, nome_cliente FROM cliente""").fetchall()   
        self.banco.desconectar()
        return cliente
    
    def consultaperCliente(self, nome:str) -> list:
        """
        """
        self.banco.conectar()
        clis = self.banco.cursor.execute(f"""SELECT cod_cliente, cpf, nome_cliente FROM cliente
                         WHERE nome_cliente like '{nome[0]}%' """).fetchall()
        self.banco.desconectar()    
        return clis


class Venda:
    banco = BancoDados()    
    # CONSTRUTOR
    def __int__(self, cod_venda:int=None, cod_cliente:int=None, valor_total:float=None, data_venda:str=None) -> None:
        # ATRIBUTOS
        self.__cod_venda = cod_venda
        self.__cod_cliente = cod_cliente
        self.__valor_total = valor_total
        self.__data_venda = data_venda

    # GETTERS E SETTERS
    def get_cod_venda(self) -> int:
        return self.__cod_venda
    
    def set_cod_venda(self, cod_venda) -> None:
        self.__cod_venda = cod_venda

    def get_cliente_venda(self) -> int:
        return self.__cod_cliente
    
    def set_cliente_venda(self, cod_cliente) -> None:
        self.__cod_cliente = cod_cliente
        
    def get_valor_total(self) -> float:
        return self.__valor_total
    
    def set_valor_total(self, valor_total:float) -> None:
        self.__valor_total = valor_total

    def get_data_venda(self) -> str:
        self.__data_venda
    
    def set_data_venda(self,data: str) -> None:
        self.__data_venda = data 

    # MÉTODOS DE CRUD DA CLASSE VENDA
    def cadastrarVenda(self, cod_cliente:int, valor_total:float, data_venda:str) -> None:
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO Venda(cod_cliente,
                             valor_total, data_venda)
                             VALUES ('{cod_cliente}',
                             '{valor_total}','{data_venda}')""")
        self.banco.conexao.commit()
        self.banco.desconectar()
        
    def listarVendas(self) -> list:
        """
        """
        self.banco.conectar()
        self.vendas = self.banco.cursor.execute(f"""SELECT cod_venda, cliente.nome_cliente,
                                        cliente.cpf, valor_total, data_venda
                                      FROM venda, cliente
                                      WHERE venda.cod_cliente = cliente.cod_cliente""").fetchall()
        self.banco.desconectar()
        return self.vendas
    
    def consultarVenda(self, cod_venda:int):
        """
        """
        self.banco.conectar()
        self.vend = self.banco.cursor.execute(f"""SELECT cod_venda, cliente.nome_cliente,
                                    cliente.cpf, valor_total, data_venda
                                    FROM cliente, venda
                                    WHERE venda.cod_cliente = cliente.cod_cliente 
                                     and cod_venda ='{cod_venda}'""").fetchall()
        self.banco.desconectar()
        return self.vend
    
    def resCodVenda(self):
        self.banco.conectar()
        self.cods = self.banco.cursor.execute(f"""SELECT cod_venda FROM venda 
                                            WHERE cod_venda = (SELECT MAX(cod_venda) FROM venda) """).fetchall()
        return self.cods


class ItensVenda:
    banco = BancoDados()
    # CONSTRUTOR
    def __init__(self, cod_produto = None, qtd = None, cod_venda = None, valor = None) -> None:
        # ATRIBUTOS
        self.__cod_produto = cod_produto
        self.__qtd = qtd
        self.__cod_venda = cod_venda
        self.__valor = valor
        self.itens = []

    # GETTERS E SETTERS
    def get_cod_produto(self) -> int:
        return self.__cod_produto
    
    def set_cod_produto(self, cod_prod:int) -> None:
        self.__cod_produto = cod_prod

    def get_qtd(self) -> int:
        return self.__qtd
    
    def set_qtd(self, qtdItem) -> None:
        self.__qtd = qtdItem

    def get_cod_venda(self) -> int:
        return self.__cod_venda

    def set_cod_venda(self, cod_venda:int) -> None:
        self.__cod_venda = cod_venda
    
    def get_valor(self) -> float:
        return self.__valor
    
    def set_valor(self, valorcompra:float) -> None:
        self.__valor = valorcompra

    # MÉTODOS DE CRUD DA CLASSE ITENS VENDA
    def cadastrarItens(self, cod_venda:int, cod_produto:int, qtd:int, valorCompra:float) -> None:
        self.banco.conectar()
        self.banco.cursor.execute(f""" INSERT INTO itens_venda (cod_venda, cod_produto, qtd, valor)
                                    VALUES('{cod_venda}', '{cod_produto}', '{qtd}', '{valorCompra}' ) """)
        self.banco.conexao.commit()
        self.banco.desconectar()

    
class Usuario:
    banco = BancoDados()
    #CONSTRUTOR
    def __init__(self):
        # ATRIBUTOS
        self.__cod_usuario = None
        self.__usuario = None
        self.__nome = None
        self.__senha = None

    # GETTERS E SETTERS
    def get_cod_usuario(self) -> int:
        return self.__cod_usuario
    
    def get_usuario(self) -> str:
        return self.__usuario
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_senha(self) -> str:
        return self.__senha
    
    def set_cod_usuario(self, cod_usuario:int) -> None:
        self.__cod_usuario = cod_usuario
        
    def set_usuario(self, usuario:str) -> None:
        self.__usuario = usuario
        
    def set_nome(self, nome:str) -> None:
        self.__nome = nome
    
    def set_senha(self, senha:str) -> None:
        self.__senha = senha

    # MÉTODOS DE CRUD DA CLASSE USUÁRIO
    def logar(self) -> list:
        """
        Exibe  o usuário e senha. 
        :param: Não tem parâmetro.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.res = self.banco.cursor.execute(f""" SELECT usuario, senha FROM usuario""").fetchall()
        return self.res
    
    def alterar_senha(self, senha:str) -> None:
        """
        Altera a senha do usuário do sistema.
        :param: senha, digitada pelo usuário.
        :return: não há retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f""" UPDATE usuario SET senha= '{senha}' WHERE cod_usuario = 1 """)
        self.banco.conexao.commit()

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
            self.exibir_categoria()

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
                    self.et_cod_categoria.configure(state='normal') 
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
        
        self.opList = []
        for row in self.categoria.listarCategoria():
            self.opList.append(list(row))
        return self.opList
            

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
                self.exibir_produto()
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
                self.et_cod_produto.configure(state='normal')
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
                self.exibir_produto()
            else:
                messagebox.showwarning('Alerta','Nenhum produto encontrado, não foi possível excluir')
        except Exception as erro:
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
                self.lista_cliente()         
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
                    self.et_cod_cliente.configure(state='normal')
                    self.listaCliente.insert('',END, values=n)
        except Exception as erro:
            messagebox.showerror('Erro', 'Erro ao listar clientes')
            print(erro)
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
            elif len(self.cnpj) != 14:
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
                self.lista_fornecedor()
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
                self.et_cod_fornecedor.configure(state='normal')
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
                self.exibir_fornecimento()
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
        if len(self.et_qtd_venda.get()) == 0 or len(self.comboxaddItens.get()) == 0:
            messagebox.showwarning('Alerta', 'Preencha os campos do carrinho!')
        else:
            self.produtoadd = [self.comboxaddItens.get()]
        
            self.lista = []
        
            self.produtosBanco = self.produtosVenda()
            for v in self.produtosBanco:
                if int(self.produtoadd[0][0]) == v[0]:
                    self.lista.append(list(v))
            self.tot.set(0)
            for l in self.lista:
                l.append(int(self.et_qtd_venda.get()))
                l.append(l[3] * l[4])
            
            for i in self.lista:
                self.listaAddItens.insert('', END, values=i)
                self.itensVenda.itens.append(i)

            c = 0 
            self.tot.set(0) 
            for it in self.itensVenda.itens:
                c +=it[5]
                self.tot.set(c)
            
        
    def remover_produto_venda(self):
        """ 
        Remove os itens do carrinho
        :param: Não tem parâmetros.
        :return: Não tem retorno.
        """
        c = float(self.restot.get())
        
        itemSelecionado = self.listaAddItens.selection()
        for i in self.listaAddItens.selection():
            valores = self.listaAddItens.item(itemSelecionado, 'values')
            self.listaAddItens.delete(i)
            c-= float(valores[5])
            self.tot.set(c)
            self.itensVenda.itens.pop(itemSelecionado)
        c = 0 
        

 
    def limpaItens(self):
        """
        Limpa os campos da tela venda.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
        """
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
        self.data = self.et_data_venda.get()
        if len(self.clienteadd) == 0 or len(self.data) == 0:
            messagebox.showwarning('Alerta','Preencha todos campos')
        else:
            self.client = self.cliente.listarClientes()
            for c in self.client:
                if c[0] == int(self.clienteadd[0][0:2]):
                    self.cod_cli = c[0]
    
            self.listaItens = self.itensVenda.itens
            soma = 0.0
            for i in self.listaItens:
                soma += float(i[5])
                
            self.venda.cadastrarVenda(self.cod_cli, soma, self.data)
            
            self.pro = self.produto.listarProdutos()
            self.codigoVenda = self.venda.resCodVenda()
            for item in self.listaItens:
                self.itensVenda.cadastrarItens(self.codigoVenda[0][0], item[0], item[4], item[5]) 
                for p in self.pro:
                    if item[0] == p[0]:
                        if int(item[4]) > p[5]:
                            messagebox.showwarning('Atenção', 'Você não pode vender mais do que tem em estoque!')
                        else:  
                            self.produto.abatEstoqueProd(item[0], int(item[4]))
                            messagebox.showinfo('Sistema', 'Venda Realizada!')
            print(self.pro) 

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
        """
        Exibe todas as vendas realizadas.
        :param: Não tem parâmetro.
        :return: Não tem retorno.
        """
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
        self.canv.drawString(6, 710, f'Código venda')
        
        self.canv.setFont('Helvetica', 15)
        self.canv.drawString(160, 710, f'Cliente')

        self.canv.setFont('Helvetica', 15)
        self.canv.drawString(310, 710, f'CPF')

        self.canv.setFont('Helvetica', 15)
        self.canv.drawString(390, 710, f'Valor total')

        self.canv.setFont('Helvetica', 15)
        self.canv.drawString(490, 710, f'Data da Venda')
        self.canv.rect(4, 750, 591, 250, fill=False, stroke=True)

        #Organizando os valores do cliente na tela
        self.vendas = list(self.venda.listarVendas())
        self.x = 20
        self.y = 700
        self.ylinhavertical = 730
        for venda in self.vendas:
            
            self.y = self.y - 30

            
            self.canv.drawString(40,self.y, f'{venda[0]}')
            self.canv.drawString(120,self.y, f'{venda[1]}')
            self.canv.drawString(280,self.y, f'{venda[2]}')
            self.canv.drawString(400,self.y, f'{venda[3]:.2f}')
            self.canv.drawString(505,self.y, f'{venda[4]}')

        self.canv.showPage()
        self.canv.save()
        messagebox.showinfo('Sistema', 'PDF Gerado com Sucesso!')
