class Pagamento:
    def __init__(self, contrato_id, valor):
        self.__id = contrato_id + 'pagamento'
        self.__contrato_id = contrato_id
        self.__valor = valor
        self.__status = 'pendente'  # pendente, aprovado, recusado, estornado
        self.__metodo = 'cartao'  # cartao, dinheiro, pix
    
    def get_id(self):
        return self.__id
    
    def get_contrato_id(self):
        return self.__contrato_id
    
    def get_valor(self):
        return self.__valor
    
    def get_status(self):
        return self.__status
    
    def get_metodo(self):
        return self.__metodo
    
    def set_status(self, novo_status):
        self.__status = novo_status
    
    def set_metodo(self, novo_metodo):
        self.__metodo = novo_metodo
    
    def aprovar(self):
        self.__status = 'aprovado'
    
    def recusar(self):
        self.__status = 'recusado'
    
    def estornar(self):
        self.__status = 'estornado'
    
    def to_dict(self):
        return {
            'id': self.__id,
            'contrato_id': self.__contrato_id,
            'valor': self.__valor,
            'status': self.__status,
            'metodo': self.__metodo
        }
    
    @classmethod
    def from_dict(cls, data):
        pagamento = cls(
            contrato_id=data['contrato_id'],
            valor=data['valor']
        )
        pagamento.__status = data['status']
        pagamento.__metodo = data.get('metodo', 'cartao')
        pagamento.__id = data['id']
        return pagamento