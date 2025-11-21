import hashlib
import uuid

class Usuario:
    def __init__(self, nome, cpf, email, senha):
        self.__id = str(uuid.uuid4())[:8]
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__senha_hash = self.__criptografar_senha(senha)
        self.__biometria_hash = None
    
    def __criptografar_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_email(self):
        return self.__email
    
    def get_biometria_hash(self):
        return self.__biometria_hash
    
    def autenticar_senha(self, senha):
        return self.__senha_hash == self.__criptografar_senha(senha)
    
    def autenticar_biometria(self, biometria_hash):
        return self.__biometria_hash == biometria_hash
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def set_senha(self, nova_senha):
        self.__senha_hash = self.__criptografar_senha(nova_senha)
    
    def set_biometria_hash(self, biometria_hash):
        self.__biometria_hash = biometria_hash
    
    def to_dict(self):
        return {
            'id': self.__id,
            'nome': self.__nome,
            'cpf': self.__cpf,
            'email': self.__email,
            'senha_hash': self.__senha_hash,
            'biometria_hash': self.__biometria_hash
        }
    
    @classmethod
    def from_dict(cls, data):
        usuario = cls(
            nome=data['nome'],
            cpf=data['cpf'],
            email=data['email'],
            senha="temp"
        )
        usuario.__senha_hash = data['senha_hash']
        usuario.__biometria_hash = data.get('biometria_hash')
        usuario.__id = data['id']
        return usuario