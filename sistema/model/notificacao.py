import time

class Notificacao:
    def __init__(self, usuario_id, titulo, mensagem, tipo='info'):
        self.__id = f"{usuario_id}_{titulo}_{time.time()}"
        self.__usuario_id = usuario_id
        self.__titulo = titulo
        self.__mensagem = mensagem
        self.__tipo = tipo
        self.__lida = False
    
    def get_id(self):
        return self.__id
    
    def get_usuario_id(self):
        return self.__usuario_id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_mensagem(self):
        return self.__mensagem
    
    def get_tipo(self):
        return self.__tipo
    
    def get_lida(self):
        return self.__lida
    
    def marcar_como_lida(self):
        self.__lida = True
    
    def to_dict(self):
        return {
            'id': self.__id,
            'usuario_id': self.__usuario_id,
            'titulo': self.__titulo,
            'mensagem': self.__mensagem,
            'tipo': self.__tipo,
            'lida': self.__lida
        }
    
    @classmethod
    def from_dict(cls, data):
        notificacao = cls(
            usuario_id=data['usuario_id'],
            titulo=data['titulo'],
            mensagem=data['mensagem'],
            tipo=data['tipo']
        )
        notificacao.__lida = data['lida']
        notificacao.__id = data['id']
        return notificacao