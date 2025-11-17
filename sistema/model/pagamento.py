class Pagamento:
    def __init__(self, contrato_id, valor):
        self._id = contrato_id + 'pagamento'
        self._contrato_id = contrato_id
        self._valor = valor
        self._status = 'pendente'  # pendente, aprovado, recusado, estornado
        self._metodo = 'cartao'  # cartao, dinheiro, pix
    
    def get_id(self):
        return self._id
    
    def get_contrato_id(self):
        return self._contrato_id
    
    def get_valor(self):
        return self._valor
    
    def get_status(self):
        return self._status
    
    def get_metodo(self):
        return self._metodo
    
    def set_status(self, novo_status):
        self._status = novo_status
    
    def set_metodo(self, novo_metodo):
        self._metodo = novo_metodo
    
    def aprovar(self):
        self._status = 'aprovado'
    
    def recusar(self):
        self._status = 'recusado'
    
    def estornar(self):
        self._status = 'estornado'
    
    def to_dict(self):
        return {
            'id': self._id,
            'contrato_id': self._contrato_id,
            'valor': self._valor,
            'status': self._status,
            'metodo': self._metodo
        }
    
    @classmethod
    def from_dict(cls, data):
        pagamento = cls(
            contrato_id=data['contrato_id'],
            valor=data['valor']
        )
        pagamento._status = data['status']
        pagamento._metodo = data.get('metodo', 'cartao')
        return pagamento