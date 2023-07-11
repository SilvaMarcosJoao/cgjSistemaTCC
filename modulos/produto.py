from modulos.dbsqlite import BancoDados

banco = BancoDados()


class Produto:
    def __init__(self,cod_produto: int=None, desc_produto: str=None, modelo_produto:str=None ,preco_compra_produto:float=None, preco_venda_produto: float=None, qtd : int=None, categoria_produto :int=None):

        self.__cod_produto=cod_produto
        self.__desc_produto=desc_produto
        self.__modelo_produto=modelo_produto
        self.__preco_compra_produto=preco_compra_produto
        self.__preco_venda_produto=preco_venda_produto
        self.__qtd =qtd 
        self.__categoria_produto=categoria_produto

    # Getters e Setters
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


    #cadastra os produtos 
    def cadastrarProduto(self, desc_produto:str, mod_produto:str, preco_compra:float, preco_venda:float, qtd:int, cod_categoria:int) -> None:
        banco.conectar()
        banco.cursor.execute(f"""INSERT INTO produto (desc_produto, modelo_produto,
                          preco_compra_produto, preco_venda_produto, qtd_estoque, cod_categoria_produto) 
                           VALUES ('{desc_produto}','{mod_produto}',
                           '{preco_compra}','{preco_venda}','{qtd}','{cod_categoria}') """)
        banco.conexao.commit()
        banco.desconectar()
    
    #Atualizar produto    
    def alterarProduto(self, cod_produto:int, desc_produto:str, modelo_produto:str, preco_compra_produto:float, preco_venda_produto:float, qtd:int) -> None:
        banco.conectar()
        banco.cursor.execute(f"""UPDATE produto
                                SET desc_produto =('{desc_produto}'),
                                modelo_produto =('{modelo_produto}'),
                                preco_compra_produto =('{preco_compra_produto}'),
                                preco_venda_produto =('{preco_venda_produto}'),
                                qtd_estoque =('{qtd}') 
                                WHERE cod_produto =('{cod_produto}')""")
        banco.conexao.commit()
        banco.desconectar()
   
               
    #mostra todos os produtos
    def listarProduto(self) -> list:
        banco.conectar()
        produtos=banco.cursor.execute("""SELECT cod_produto, desc_produto, modelo_produto, preco_compra_produto,
                                      preco_venda_produto, qtd_estoque, categoria_produto.desc_categoria_produto 
                                      FROM categoria_produto, produto 
                                      WHERE produto.cod_categoria_produto = categoria_produto.cod_categoria_produto""").fetchall()
        banco.desconectar()
        return produtos
        
    #procura um produto   
    def consultarProduto(self, desc_produto:str) -> list: 
        banco.conectar()
        produto = banco.cursor.execute(f"""SELECT cod_produto, desc_produto, modelo_produto,
                          preco_compra_produto, preco_venda_produto, qtd_estoque , categoria_produto.desc_categoria_produto 
                          FROM categoria_produto, produto
                            WHERE produto.cod_categoria_produto = categoria_produto.cod_categoria_produto and desc_produto like '{desc_produto[0]}%'""").fetchall()
        banco.desconectar()  
        return produto
    '''
    def consultaProdutoFornecimento(self) -> list:
        banco.conectar()
        listaPdt = banco.cursor.execute(f"""SELECT cod_produto, desc_produto, preco_venda from produto """).fetchall()
        banco.desconectar()
        return listaPdt'''

    #apaga produtos
    def deletarProduto(self, cod_produto:int) -> None:
        banco.conectar()
        banco.cursor.execute(f"""DELETE FROM produto
                                WHERE cod_produto='{cod_produto}'""")
        banco.conexao.commit()
        banco.desconectar()


# Métodos personalizados para telaCliente

    def listaperProduto(self):
        banco.conectar()
        produtos=banco.cursor.execute(f"""SELECT cod_produto, desc_produto, modelo_produto,
                                      preco_venda_produto, qtd_estoque
                                      FROM PRODUTO """).fetchall()
        banco.desconectar()                              
        return produtos
        

    def consultaperProduto(self, desc_produto: str) -> list:
        banco.conectar()
        produto=banco.cursor.execute(f"""SELECT cod_produto, desc_produto,
                                         modelo_produto, preco_venda_produto,qtd_estoque FROM PRODUTO 
                                           WHERE desc_produto like '{desc_produto[0]}%'""").fetchall()   
        banco.desconectar()
        return produto