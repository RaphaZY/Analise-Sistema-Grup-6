class Contrato:
    def __init__(self, cliente_id, prestador_id, servico_titulo, valor):
        self._id = cliente_id + prestador_id + servico_titulo
        self._cliente_id = cliente_id
        self._prestador_id = prestador_id
        self._servico_titulo = servico_titulo
        self._valor = valor
        self._status = "solicitado"  # solicitado, aceito, concluido, cancelado
    
    def get_id(self):
        return self._id
    
    def get_cliente_id(self):
        return self._cliente_id
    
    def get_prestador_id(self):
        return self._prestador_id
    
    def get_servico_titulo(self):
        return self._servico_titulo
    
    def get_valor(self):
        return self._valor
    
    def get_status(self):
        return self._status
    
    def set_status(self, novo_status):
        self._status = novo_status
    
    def aceitar(self):
        if self._status == "solicitado":
            self._status = "aceito"
            return True
        return False
    
    def concluir(self):
        if self._status == "aceito":
            self._status = "concluido"
            return True
        return False
    
    def cancelar(self):
        if self._status in ["solicitado", "aceito"]:
            self._status = "cancelado"
            return True
        return False
    
    def recusar(self):
        if self._status == "solicitado":
            self._status = "cancelado"  # Usamos cancelado para recusado também
            return True
        return False
    
    def to_dict(self):
        return {
            'id': self._id,
            'cliente_id': self._cliente_id,
            'prestador_id': self._prestador_id,
            'servico_titulo': self._servico_titulo,
            'valor': self._valor,
            'status': self._status
        }
    
    @classmethod
    def from_dict(cls, data):
        contrato = cls(
            cliente_id=data['cliente_id'],
            prestador_id=data['prestador_id'],
            servico_titulo=data['servico_titulo'],
            valor=data['valor']
        )
        contrato._status = data['status']
        return contrato