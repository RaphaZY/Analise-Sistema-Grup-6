import time

class Avaliacao:
    def __init__(self, contrato_id, avaliador_id, avaliado_id, nota, comentario=''):
        self._id = f"{contrato_id}_avaliacao_{time.time()}"
        self._contrato_id = contrato_id
        self._avaliador_id = avaliador_id
        self._avaliado_id = avaliado_id
        self._nota = max(1, min(5, nota))  # Nota entre 1-5
        self._comentario = comentario
    
    def get_id(self):
        return self._id
    
    def get_contrato_id(self):
        return self._contrato_id
    
    def get_avaliador_id(self):
        return self._avaliador_id
    
    def get_avaliado_id(self):
        return self._avaliado_id
    
    def get_nota(self):
        return self._nota
    
    def get_comentario(self):
        return self._comentario
    
    def set_nota(self, nova_nota):
        self._nota = max(1, min(5, nova_nota))
    
    def set_comentario(self, novo_comentario):
        self._comentario = novo_comentario
    
    def to_dict(self):
        return {
            'id': self._id,
            'contrato_id': self._contrato_id,
            'avaliador_id': self._avaliador_id,
            'avaliado_id': self._avaliado_id,
            'nota': self._nota,
            'comentario': self._comentario
        }
    
    @classmethod
    def from_dict(cls, data):
        avaliacao = cls(
            contrato_id=data['contrato_id'],
            avaliador_id=data['avaliador_id'],
            avaliado_id=data['avaliado_id'],
            nota=data['nota'],
            comentario=data['comentario']
        )
        avaliacao._id = data['id']
        return avaliacao