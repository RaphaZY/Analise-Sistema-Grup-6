import time

class Notificacao:
    def __init__(self, usuario_id, titulo, mensagem, tipo='info'):
        self._id = f"{usuario_id}_{titulo}_{time.time()}"
        self._usuario_id = usuario_id
        self._titulo = titulo
        self._mensagem = mensagem
        self._tipo = tipo
        self._lida = False
    
    def get_id(self):
        return self._id
    
    def get_usuario_id(self):
        return self._usuario_id
    
    def get_titulo(self):
        return self._titulo
    
    def get_mensagem(self):
        return self._mensagem
    
    def get_tipo(self):
        return self._tipo
    
    def get_lida(self):
        return self._lida
    
    def marcar_como_lida(self):
        self._lida = True
    
    def to_dict(self):
        return {
            'id': self._id,
            'usuario_id': self._usuario_id,
            'titulo': self._titulo,
            'mensagem': self._mensagem,
            'tipo': self._tipo,
            'lida': self._lida
        }
    
    @classmethod
    def from_dict(cls, data):
        notificacao = cls(
            usuario_id=data['usuario_id'],
            titulo=data['titulo'],
            mensagem=data['mensagem'],
            tipo=data['tipo']
        )
        notificacao._lida = data['lida']
        notificacao._id = data['id']
        return notificacao