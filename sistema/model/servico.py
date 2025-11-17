class Servico:
    def __init__(self, prestador_id, titulo, descricao, valor):
        self._id = titulo + prestador_id
        self._prestador_id = prestador_id
        self._titulo = titulo
        self._descricao = descricao
        self._valor = valor
        self._ativo = True
    
    def get_id(self):
        return self._id
    
    def get_prestador_id(self):
        return self._prestador_id
    
    def get_titulo(self):
        return self._titulo
    
    def get_descricao(self):
        return self._descricao
    
    def get_valor(self):
        return self._valor
    
    def get_ativo(self):
        return self._ativo
    
    def set_titulo(self, novoTitulo):
        self._titulo = novoTitulo
    
    def set_descricao(self, novaDescricao):
        self._descricao = novaDescricao
    
    def set_valor(self, novoValor):
        self._valor = novoValor
    
    def desativar(self):
        self._ativo = False
    
    def ativar(self):
        self._ativo = True
    
    def to_dict(self):
        return {
            'id': self._id,
            'prestador_id': self._prestador_id,
            'titulo': self._titulo,
            'descricao': self._descricao,
            'valor': self._valor,
            'ativo': self._ativo
        }
    
    @classmethod
    def from_dict(cls, data):
        servico = cls(
            prestador_id=data['prestador_id'],
            titulo=data['titulo'],
            descricao=data['descricao'],
            valor=data['valor']
        )
        servico._ativo = data['ativo']
        return servico