import hashlib
import uuid

class Usuario:
    def __init__(self, nome, cpf, email, senha, tipo):
        self._id = str(uuid.uuid4())[:8]
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._senha_hash = self._criptografar_senha(senha)
        self._tipo = tipo  # 'cliente' ou 'prestador'
        self._biometria_hash = None
    
    def _criptografar_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_cpf(self):
        return self._cpf
    
    def get_tipo(self):
        return self._tipo
    
    def get_email(self):
        return self._email
    
    def autenticar_senha(self, senha):
        return self._senha_hash == self._criptografar_senha(senha)
    
    def autenticar_biometria(self, biometria_hash):
        return self._biometria_hash == biometria_hash
    
    def set_nome(self, novo_nome):
        self._nome = novo_nome
    
    def set_senha(self, nova_senha):
        self._senha_hash = self._criptografar_senha(nova_senha)
    
    def set_biometria_hash(self, biometria_hash):
        self._biometria_hash = biometria_hash
    
    def to_dict(self):
        return {
            'id': self._id,
            'nome': self._nome,
            'cpf': self._cpf,
            'email': self._email,
            'senha_hash': self._senha_hash,
            'tipo': self._tipo,
            'biometria_hash': self._biometria_hash
        }
    
    @classmethod
    def from_dict(cls, data):
        usuario = cls(
            nome=data['nome'],
            cpf=data['cpf'],
            email=data['email'],
            senha="temp",  # Senha temporária, será sobrescrita
            tipo=data['tipo']
        )
        usuario._senha_hash = data['senha_hash']
        usuario._biometria_hash = data.get('biometria_hash')
        usuario._id = data['id']
        return usuario