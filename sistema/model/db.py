import os

class Database:
    def __init__(self, diretorio='sistema/data/'):
        self.diretorio = diretorio
        self.arquivos = {
            'usuarios': 'usuarios.txt',
            'servicos': 'servicos.txt', 
            'contratos': 'contratos.txt',
            'notificacoes': 'notificacoes.txt',
            'avaliacoes': 'avaliacoes.txt',
            'pagamentos': 'pagamentos.txt'
        }
        self.dados = {
            'usuarios': [],
            'servicos': [],
            'contratos': [],
            'notificacoes': [],
            'avaliacoes': [],
            'pagamentos': []
        }
        # Criar diretório se não existir
        os.makedirs(self.diretorio, exist_ok=True)
        self.carregar()
    
    def carregar(self):
        """Carrega dados dos arquivos TXT"""
        for tabela, arquivo in self.arquivos.items():
            caminho_arquivo = os.path.join(self.diretorio, arquivo)
            try:
                if os.path.exists(caminho_arquivo):
                    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                        linhas = f.readlines()
                        # Pular cabeçalho se existir
                        start_index = 1 if linhas and ';' in linhas[0] else 0
                        for linha in linhas[start_index:]:
                            linha = linha.strip()
                            if linha:
                                campos = linha.split(';')
                                if tabela == 'usuarios':
                                    if len(campos) >= 6:  # Agora são 6 campos sem o tipo
                                        item = {
                                            'id': campos[0],
                                            'nome': campos[1],
                                            'cpf': campos[2],
                                            'email': campos[3],
                                            'senha_hash': campos[4],
                                            'biometria_hash': campos[5] if len(campos) > 5 else None
                                        }
                                        self.dados[tabela].append(item)
                                elif tabela == 'servicos':
                                    if len(campos) >= 6:
                                        item = {
                                            'id': campos[0],
                                            'prestador_id': campos[1],
                                            'titulo': campos[2],
                                            'descricao': campos[3],
                                            'valor': float(campos[4]),
                                            'ativo': campos[5].lower() == 'true'
                                        }
                                        self.dados[tabela].append(item)
                                elif tabela == 'contratos':
                                    if len(campos) >= 6:
                                        item = {
                                            'id': campos[0],
                                            'cliente_id': campos[1],
                                            'prestador_id': campos[2],
                                            'servico_titulo': campos[3],
                                            'valor': float(campos[4]),
                                            'status': campos[5]
                                        }
                                        self.dados[tabela].append(item)
                                elif tabela == 'notificacoes':
                                    if len(campos) >= 6:
                                        item = {
                                            'id': campos[0],
                                            'usuario_id': campos[1],
                                            'titulo': campos[2],
                                            'mensagem': campos[3],
                                            'tipo': campos[4],
                                            'lida': campos[5].lower() == 'true'
                                        }
                                        self.dados[tabela].append(item)
                                elif tabela == 'avaliacoes':
                                    if len(campos) >= 6:
                                        item = {
                                            'id': campos[0],
                                            'contrato_id': campos[1],
                                            'avaliador_id': campos[2],
                                            'avaliado_id': campos[3],
                                            'nota': int(campos[4]),
                                            'comentario': campos[5] if len(campos) > 5 else ''
                                        }
                                        self.dados[tabela].append(item)
                                elif tabela == 'pagamentos':
                                    if len(campos) >= 5:
                                        item = {
                                            'id': campos[0],
                                            'contrato_id': campos[1],
                                            'valor': float(campos[2]),
                                            'status': campos[3],
                                            'metodo': campos[4] if len(campos) > 4 else 'cartao'
                                        }
                                        self.dados[tabela].append(item)
            except Exception as e:
                print(f"Erro ao carregar {tabela}: {e}")
                self.dados[tabela] = []
    
    def salvar(self):
        """Salva dados nos arquivos TXT"""
        for tabela, arquivo in self.arquivos.items():
            caminho_arquivo = os.path.join(self.diretorio, arquivo)
            try:
                with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                    # Escrever cabeçalho
                    if tabela == 'usuarios':
                        f.write("id;nome;cpf;email;senha_hash;biometria_hash\n")  # Removido tipo
                        for item in self.dados[tabela]:
                            linha = f"{item['id']};{item['nome']};{item['cpf']};{item['email']};{item['senha_hash']};{item.get('biometria_hash', '')}"
                            f.write(linha + '\n')
                    
                    elif tabela == 'servicos':
                        f.write("id;prestador_id;titulo;descricao;valor;ativo\n")
                        for item in self.dados[tabela]:
                            linha = f"{item['id']};{item['prestador_id']};{item['titulo']};{item['descricao']};{item['valor']};{item['ativo']}"
                            f.write(linha + '\n')
                    
                    elif tabela == 'contratos':
                        f.write("id;cliente_id;prestador_id;servico_titulo;valor;status\n")
                        for item in self.dados[tabela]:
                            linha = f"{item['id']};{item['cliente_id']};{item['prestador_id']};{item['servico_titulo']};{item['valor']};{item['status']}"
                            f.write(linha + '\n')
                    
                    elif tabela == 'notificacoes':
                        f.write("id;usuario_id;titulo;mensagem;tipo;lida\n")
                        for item in self.dados[tabela]:
                            linha = f"{item['id']};{item['usuario_id']};{item['titulo']};{item['mensagem']};{item['tipo']};{item['lida']}"
                            f.write(linha + '\n')
                    
                    elif tabela == 'avaliacoes':
                        f.write("id;contrato_id;avaliador_id;avaliado_id;nota;comentario\n")
                        for item in self.dados[tabela]:
                            linha = f"{item['id']};{item['contrato_id']};{item['avaliador_id']};{item['avaliado_id']};{item['nota']};{item.get('comentario', '')}"
                            f.write(linha + '\n')
                    
                    elif tabela == 'pagamentos':
                        f.write("id;contrato_id;valor;status;metodo\n")
                        for item in self.dados[tabela]:
                            linha = f"{item['id']};{item['contrato_id']};{item['valor']};{item['status']};{item.get('metodo', 'cartao')}"
                            f.write(linha + '\n')
                            
            except Exception as e:
                print(f"Erro ao salvar {tabela}: {e}")
    
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