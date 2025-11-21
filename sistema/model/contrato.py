class Contrato:
    def __init__(self, cliente_id, prestador_id, servico_titulo, valor):
        self.__id = cliente_id + prestador_id + servico_titulo
        self.__cliente_id = cliente_id
        self.__prestador_id = prestador_id
        self.__servico_titulo = servico_titulo
        self.__valor = valor
        self.__status = "solicitado"  # solicitado, aceito, concluido, cancelado
    
    def get_id(self):
        return self.__id
    
    def get_cliente_id(self):
        return self.__cliente_id
    
    def get_prestador_id(self):
        return self.__prestador_id
    
    def get_servico_titulo(self):
        return self.__servico_titulo
    
    def get_valor(self):
        return self.__valor
    
    def get_status(self):
        return self.__status
    
    def set_status(self, novo_status):
        self.__status = novo_status
    
    def aceitar(self):
        if self.__status == "solicitado":
            self.__status = "aceito"
            return True
        return False
    
    def concluir(self):
        if self.__status == "aceito":
            self.__status = "concluido"
            return True
        return False
    
    def cancelar(self):
        if self.__status in ["solicitado", "aceito"]:
            self.__status = "cancelado"
            return True
        return False
    
    def recusar(self):
        if self.__status == "solicitado":
            self.__status = "cancelado"  # Usamos cancelado para recusado também
            return True
        return False
    
    def to_dict(self):
        return {
            'id': self.__id,
            'cliente_id': self.__cliente_id,
            'prestador_id': self.__prestador_id,
            'servico_titulo': self.__servico_titulo,
            'valor': self.__valor,
            'status': self.__status
        }
    
    @classmethod
    def from_dict(cls, data):
        contrato = cls(
            cliente_id=data['cliente_id'],
            prestador_id=data['prestador_id'],
            servico_titulo=data['servico_titulo'],
            valor=data['valor']
        )
        contrato.__status = data['status']
        contrato.__id = data['id']
        return contrato