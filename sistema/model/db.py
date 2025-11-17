import json

class Database:
    def __init__(self, arquivo='sistema/db.txt'):
        self.arquivo = arquivo
        self.dados = {
            'usuarios': [],
            'servicos': [],
            'contratos': [],
            'notificacoes': [],
            'avaliacoes': [],
            'pagamentos': []
        }
        self.carregar()
    
    def carregar(self):
        try:
            with open(self.arquivo, 'r') as f:
                dados_carregados = json.load(f)
                # Garante que todas as tabelas existam
                for tabela in self.dados.keys():
                    if tabela in dados_carregados:
                        self.dados[tabela] = dados_carregados[tabela]
        except:
            # Se der erro, mantém a estrutura padrão
            pass
    
    def salvar(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.dados, f, indent=2)
    
    def inserir(self, tabela, obj):
        if tabela not in self.dados:
            self.dados[tabela] = []
        self.dados[tabela].append(obj.to_dict())
        self.salvar()
    
    def buscar(self, tabela, campo, valor):
        if tabela not in self.dados:
            return []
        return [item for item in self.dados[tabela] if item.get(campo) == valor]
    
    def buscar_todos(self, tabela):
        if tabela not in self.dados:
            return []
        return self.dados[tabela]
    
    def atualizar(self, tabela, obj_id, novos_dados):
        if tabela not in self.dados:
            return False
        for item in self.dados[tabela]:
            if item.get('id') == obj_id:
                item.update(novos_dados)
                self.salvar()
                return True
        return False
    
    def remover(self, tabela, obj_id):
        if tabela not in self.dados:
            return False
        for i, item in enumerate(self.dados[tabela]):
            if item.get('id') == obj_id:
                del self.dados[tabela][i]
                self.salvar()
                return True
        return False