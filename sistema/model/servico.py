class Servico:
    def __init__(self, prestador_id, titulo, descricao, valor):
        self.__id = titulo + prestador_id
        self.__prestador_id = prestador_id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__valor = valor
        self.__ativo = True
    
    def get_id(self):
        return self.__id
    
    def get_prestador_id(self):
        return self.__prestador_id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_descricao(self):
        return self.__descricao
    
    def get_valor(self):
        return self.__valor
    
    def get_ativo(self):
        return self.__ativo
    
    def set_titulo(self, novoTitulo):
        self.__titulo = novoTitulo
    
    def set_descricao(self, novaDescricao):
        self.__descricao = novaDescricao
    
    def set_valor(self, novoValor):
        self.__valor = novoValor
    
    def desativar(self):
        self.__ativo = False
    
    def ativar(self):
        self.__ativo = True
    
    def to_dict(self):
        return {
            'id': self.__id,
            'prestador_id': self.__prestador_id,
            'titulo': self.__titulo,
            'descricao': self.__descricao,
            'valor': self.__valor,
            'ativo': self.__ativo
        }
    
    @classmethod
    def from_dict(cls, data):
        servico = cls(
            prestador_id=data['prestador_id'],
            titulo=data['titulo'],
            descricao=data['descricao'],
            valor=data['valor']
        )
        servico.__ativo = data['ativo']
        servico.__id = data['id']
        return servico