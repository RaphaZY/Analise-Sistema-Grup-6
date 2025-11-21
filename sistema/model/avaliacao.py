import time

class Avaliacao:
    def __init__(self, contrato_id, avaliador_id, avaliado_id, nota, comentario=''):
        self.__id = f"{contrato_id}_avaliacao_{time.time()}"
        self.__contrato_id = contrato_id
        self.__avaliador_id = avaliador_id
        self.__avaliado_id = avaliado_id
        self.__nota = max(1, min(5, nota))  # Nota entre 1-5
        self.__comentario = comentario
    
    def get_id(self):
        return self.__id
    
    def get_contrato_id(self):
        return self.__contrato_id
    
    def get_avaliador_id(self):
        return self.__avaliador_id
    
    def get_avaliado_id(self):
        return self.__avaliado_id
    
    def get_nota(self):
        return self.__nota
    
    def get_comentario(self):
        return self.__comentario
    
    def set_nota(self, nova_nota):
        self.__nota = max(1, min(5, nova_nota))
    
    def set_comentario(self, novo_comentario):
        self.__comentario = novo_comentario
    
    def to_dict(self):
        return {
            'id': self.__id,
            'contrato_id': self.__contrato_id,
            'avaliador_id': self.__avaliador_id,
            'avaliado_id': self.__avaliado_id,
            'nota': self.__nota,
            'comentario': self.__comentario
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
        avaliacao.__id = data['id']
        return avaliacao