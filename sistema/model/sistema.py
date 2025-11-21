from model.db import Database
from model.usuario import Usuario
from model.servico import Servico
from model.contrato import Contrato
from model.notificacao import Notificacao
from model.avaliacao import Avaliacao
from model.pagamento import Pagamento
import hashlib
import os

class Sistema:
    def __init__(self):
        self.__db = Database()
        self.__usuario_logado = None
        self.__tipo_sessao = None  # 'cliente' ou 'prestador'
    
    def pausar(self):
        input("\nPressione Enter para continuar...")
    
    def inicializar_dados(self):
        """Inicializa dados padrão se não existirem usuários no sistema"""
        usuarios = self.__db.buscar_todos('usuarios')
        if not usuarios:
            print("Criando dados iniciais...")
            
            # Prestadores
            prestador1 = Usuario("João Silva", "12345678901", "joao@email.com", "123")
            dados_biometricos1 = f"12345678901_João Silva_biometria_facial"
            biometria_hash1 = hashlib.sha256(dados_biometricos1.encode()).hexdigest()
            prestador1.set_biometria_hash(biometria_hash1)
            self.__db.inserir('usuarios', prestador1)
            
            prestador2 = Usuario("Maria Santos", "98765432100", "maria@email.com", "123")
            dados_biometricos2 = f"98765432100_Maria Santos_biometria_facial"
            biometria_hash2 = hashlib.sha256(dados_biometricos2.encode()).hexdigest()
            prestador2.set_biometria_hash(biometria_hash2)
            self.__db.inserir('usuarios', prestador2)
            
            # Serviços
            servico1 = Servico(prestador1.get_id(), "Encanador Residencial", "Conserto de vazamentos e instalações", 150.0)
            self.__db.inserir('servicos', servico1)
            
            servico2 = Servico(prestador2.get_id(), "Eletricista", "Instalações elétricas e reparos", 200.0)
            self.__db.inserir('servicos', servico2)
            
            servico3 = Servico(prestador1.get_id(), "Pintura Residencial", "Pintura interna e externa", 800.0)
            self.__db.inserir('servicos', servico3)
            
            # Clientes
            cliente1 = Usuario("Carlos Oliveira", "11122233344", "carlos@email.com", "123")
            dados_biometricos3 = f"11122233344_Carlos Oliveira_biometria_facial"
            biometria_hash3 = hashlib.sha256(dados_biometricos3.encode()).hexdigest()
            cliente1.set_biometria_hash(biometria_hash3)
            self.__db.inserir('usuarios', cliente1)
            
            cliente2 = Usuario("Ana Costa", "55566677788", "ana@email.com", "123")
            dados_biometricos4 = f"55566677788_Ana Costa_biometria_facial"
            biometria_hash4 = hashlib.sha256(dados_biometricos4.encode()).hexdigest()
            cliente2.set_biometria_hash(biometria_hash4)
            self.__db.inserir('usuarios', cliente2)
            
            cliente3 = Usuario("Raphael", "12345678910", "rapha@email.com", "123")
            dados_biometricos5 = f"12345678910_Raphael_biometria_facial"
            biometria_hash5 = hashlib.sha256(dados_biometricos5.encode()).hexdigest()
            cliente3.set_biometria_hash(biometria_hash5)
            self.__db.inserir('usuarios', cliente3)
            
            print("Dados iniciais criados!")
            self.pausar()
    
    def menu_principal(self):
        while True:
            print("\n=== SISTEMA DE SERVIÇOS ===")
            if not self.__usuario_logado:
                print("1. Cadastrar")
                print("2. Login com CPF/Senha")
                print("3. Login com Biometria")
                print("4. Sair")
                
                opcao = input("Escolha: ")
                
                if opcao == '1': 
                    self.cadastrar_usuario()
                elif opcao == '2': 
                    self.login_cpf_senha()
                elif opcao == '3': 
                    self.login_biometria()
                elif opcao == '4': 
                    break
            else:
                print(f"Bem-vindo, {self.__usuario_logado.get_nome()}! ({self.__tipo_sessao})")
                if self.__tipo_sessao == 'cliente':
                    print("1. Buscar serviços")
                    print("2. Meus contratos")
                    print("3. Minhas avaliações")
                    print("4. Meus pagamentos")
                else:  # prestador
                    print("1. Meus serviços")
                    print("2. Solicitações de serviço")
                    print("3. Minhas avaliações")
                    print("4. Meus pagamentos")
                print("5. Notificações")
                print("6. Editar perfil")
                print("7. Reconfigurar Biometria")
                print("8. Trocar Tipo de Acesso")
                print("9. Logout")
                
                opcao = input("Escolha: ")
                
                if opcao == '1': 
                    if self.__tipo_sessao == 'cliente': 
                        self.buscar_servicos()
                    else: 
                        self.meus_servicos()
                elif opcao == '2':
                    if self.__tipo_sessao == 'cliente': 
                        self.meus_contratos()
                    else: 
                        self.solicitacoes_servico()
                elif opcao == '3': 
                    self.minhas_avaliacoes()
                elif opcao == '4': 
                    self.meus_pagamentos()
                elif opcao == '5': 
                    self.ver_notificacoes()
                elif opcao == '6': 
                    self.editar_perfil()
                elif opcao == '7': 
                    self.configurar_biometria()
                elif opcao == '8': 
                    self.trocar_tipo_acesso()
                elif opcao == '9': 
                    self.__usuario_logado = None
                    self.__tipo_sessao = None
    
    def cadastrar_usuario(self):
        print("\n--- CADASTRO ---")
        nome = input("Nome: ")
        cpf = input("CPF (apenas números): ")
        email = input("Email: ")
        senha = input("Senha: ")
        
        # Verificar se CPF já existe
        if any(u['cpf'] == cpf for u in self.__db.buscar_todos('usuarios')):
            print("CPF já cadastrado!")
            self.pausar()
            return
        
        # Verificar se email já existe
        if any(u['email'] == email for u in self.__db.buscar_todos('usuarios')):
            print("Email já cadastrado!")
            self.pausar()
            return
        
        # Simular cadastro de biometria facial
        print("\n--- CADASTRO DE BIOMETRIA FACIAL ---")
        print("Por favor, posicione seu rosto frente à câmera...")
        print("(Simulando captura de biometria facial)")
        
        # Gerar dados biométricos simulados baseados no CPF + Nome
        dados_biometricos = f"{cpf}_{nome}_biometria_facial"
        biometria_hash = hashlib.sha256(dados_biometricos.encode()).hexdigest()
        
        print("✓ Biometria facial cadastrada com sucesso!")
        
        # Criar usuário
        usuario = Usuario(nome, cpf, email, senha)
        usuario.set_biometria_hash(biometria_hash)
        
        self.__db.inserir('usuarios', usuario)
        
        # Notificação de boas-vindas
        notificacao = Notificacao(
            usuario.get_id(),
            "Bem-vindo!",
            f"Olá {nome}, seja bem-vindo ao nosso sistema de serviços! Sua biometria facial foi cadastrada com sucesso."
        )
        self.__db.inserir('notificacoes', notificacao)
        
        print("\nCadastrado com sucesso!")
        print("Sua biometria facial foi registrada e pode ser usada para login.")
        self.pausar()
    
    def escolher_tipo_acesso(self):
        """Permite ao usuário escolher entre cliente e prestador"""
        print("\n--- ESCOLHA O TIPO DE ACESSO ---")
        print("1. Cliente")
        print("2. Prestador")
        
        while True:
            opcao = input("Escolha (1 ou 2): ")
            if opcao == '1':
                return 'cliente'
            elif opcao == '2':
                return 'prestador'
            else:
                print("Opção inválida! Escolha 1 para Cliente ou 2 para Prestador.")
    
    def login_cpf_senha(self):
        print("\n--- LOGIN COM CPF E SENHA ---")
        cpf = input("CPF: ")
        senha = input("Senha: ")
        
        usuarios = [Usuario.from_dict(u) for u in self.__db.buscar_todos('usuarios')]
        for usuario in usuarios:
            if usuario.get_cpf() == cpf and usuario.autenticar_senha(senha):
                self.__usuario_logado = usuario
                self.__tipo_sessao = self.escolher_tipo_acesso()
                
                # Notificação de login
                notificacao = Notificacao(
                    usuario.get_id(),
                    "Login realizado",
                    f"Login realizado com sucesso como {self.__tipo_sessao}."
                )
                self.__db.inserir('notificacoes', notificacao)
                
                print(f"Login realizado como {self.__tipo_sessao}!")
                self.pausar()
                return
        
        print("CPF ou senha incorretos!")
        self.pausar()
    
    def login_biometria(self):
        print("\n--- LOGIN COM BIOMETRIA ---")
        cpf = input("CPF: ")
        
        usuarios = [Usuario.from_dict(u) for u in self.__db.buscar_todos('usuarios')]
        for usuario in usuarios:
            if usuario.get_cpf() == cpf:
                if usuario.get_biometria_hash() is None:
                    print("Biometria não configurada para este usuário.")
                    self.pausar()
                    return
                
                # Simular leitura de biometria
                print("\nPor favor, posicione seu rosto frente à câmera...")
                print("(Simulando verificação de biometria facial)")
                
                # Gerar os mesmos dados biométricos que foram cadastrados
                dados_biometricos = f"{usuario.get_cpf()}_{usuario.get_nome()}_biometria_facial"
                biometria_hash = hashlib.sha256(dados_biometricos.encode()).hexdigest()
                
                if usuario.autenticar_biometria(biometria_hash):
                    self.__usuario_logado = usuario
                    self.__tipo_sessao = self.escolher_tipo_acesso()
                    
                    # Notificação de login
                    notificacao = Notificacao(
                        usuario.get_id(),
                        "Login por biometria",
                        f"Login realizado com sucesso usando biometria facial como {self.__tipo_sessao}."
                    )
                    self.__db.inserir('notificacoes', notificacao)
                    
                    print(f"✓ Biometria reconhecida! Login realizado como {self.__tipo_sessao}!")
                    self.pausar()
                    return
                else:
                    print("✗ Biometria não reconhecida!")
                    self.pausar()
                    return
        
        print("CPF não encontrado!")
        self.pausar()
    
    def trocar_tipo_acesso(self):
        """Permite ao usuário trocar entre cliente e prestador sem fazer logout"""
        print("\n--- TROCAR TIPO DE ACESSO ---")
        novo_tipo = self.escolher_tipo_acesso()
        self.__tipo_sessao = novo_tipo
        print(f"Tipo de acesso alterado para: {novo_tipo}")
        self.pausar()

    def configurar_biometria(self):
        print("\n--- RECONFIGURAR BIOMETRIA FACIAL ---")
        
        # Simular leitura de biometria
        print("Por favor, posicione seu rosto frente à câmera...")
        print("(Simulando captura de biometria facial)")
        
        # Gerar novos dados biométricos
        dados_biometricos = f"{self.__usuario_logado.get_cpf()}_{self.__usuario_logado.get_nome()}_biometria_facial_nova"
        biometria_hash = hashlib.sha256(dados_biometricos.encode()).hexdigest()
        
        # Configurar biometria para o usuário usando o setter
        self.__usuario_logado.set_biometria_hash(biometria_hash)
        
        # Atualizar no banco
        for i, usuario_dict in enumerate(self.__db.dados['usuarios']):
            if usuario_dict['id'] == self.__usuario_logado.get_id():
                self.__db.dados['usuarios'][i] = self.__usuario_logado.to_dict()
                self.__db.salvar()
                break
        
        # Notificação
        notificacao = Notificacao(
            self.__usuario_logado.get_id(),
            "Biometria reconfigurada",
            "Sua biometria facial foi reconfigurada com sucesso."
        )
        self.__db.inserir('notificacoes', notificacao)
        
        print("✓ Biometria reconfigurada com sucesso!")
        self.pausar()

    def buscar_servicos(self):
        print("\n--- SERVIÇOS DISPONÍVEIS ---")
        servicos = [Servico.from_dict(s) for s in self.__db.buscar_todos('servicos')]
        servicos_ativos = [s for s in servicos if s.get_ativo()]
        
        if not servicos_ativos:
            print("Nenhum serviço disponível!")
            self.pausar()
            return
            
        for i, servico in enumerate(servicos_ativos, 1):
            prestador_dict = next((u for u in self.__db.buscar_todos('usuarios') 
                           if u['id'] == servico.get_prestador_id()), None)
            if prestador_dict:
                prestador = Usuario.from_dict(prestador_dict)
                
                # Calcular avaliação média do prestador
                avaliacoes = [Avaliacao.from_dict(a) for a in self.__db.buscar_todos('avaliacoes')]
                avaliacoes_prestador = [a for a in avaliacoes if a.get_avaliado_id() == prestador.get_id()]
                media = sum(a.get_nota() for a in avaliacoes_prestador) / len(avaliacoes_prestador) if avaliacoes_prestador else 5.0
                
                print(f"{i}. {servico.get_titulo()} - R$ {servico.get_valor()}")
                print(f"   Por: {prestador.get_nome()} ⭐ {media:.1f}")
                print(f"   {servico.get_descricao()}")
        
        opcao = input("\nEscolha o serviço (0 para voltar): ")
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao > 0 and opcao <= len(servicos_ativos):
                servico_escolhido = servicos_ativos[opcao-1]
                self.solicitar_servico(servico_escolhido)
    
    
    def solicitar_servico(self, servico):
        print(f"\n--- SOLICITAR SERVIÇO: {servico.get_titulo()} ---")
        print(f"Valor: R$ {servico.get_valor()}")
        confirmar = input("Confirmar solicitação? (s/n): ")
        
        if confirmar.lower() == 's':
            contrato = Contrato(
                self.__usuario_logado.get_id(),
                servico.get_prestador_id(),
                servico.get_titulo(),
                servico.get_valor()
            )
            self.__db.inserir('contratos', contrato)
            
            # Criar pagamento
            pagamento = Pagamento(contrato.get_id(), servico.get_valor())
            self.__db.inserir('pagamentos', pagamento)
            
            # Notificar prestador
            notificacao = Notificacao(
                servico.get_prestador_id(),
                "Nova solicitação de serviço",
                f"Você recebeu uma nova solicitação para: {servico.get_titulo()}"
            )
            self.__db.inserir('notificacoes', notificacao)
            
            # Notificar cliente
            notificacao_cliente = Notificacao(
                self.__usuario_logado.get_id(),
                "Serviço solicitado",
                f"Sua solicitação para {servico.get_titulo()} foi enviada ao prestador."
            )
            self.__db.inserir('notificacoes', notificacao_cliente)
            
            print("Serviço solicitado com sucesso!")
        else:
            print("Solicitação cancelada.")
    
    def meus_contratos(self):
        print("\n--- MEUS CONTRATOS ---")
        contratos = [Contrato.from_dict(c) for c in self.__db.buscar_todos('contratos')]
        meus_contratos = [c for c in contratos if c.get_cliente_id() == self.__usuario_logado.get_id()]
        
        if not meus_contratos:
            print("Nenhum contrato encontrado!")
            self.pausar()
            return
            
        for i, contrato in enumerate(meus_contratos, 1):
            print(f"{i}. {contrato.get_servico_titulo()} - Status: {contrato.get_status()}")
        
        opcao = input("\nEscolha contrato para detalhes (0 para voltar): ")
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao > 0 and opcao <= len(meus_contratos):
                self.detalhes_contrato_cliente(meus_contratos[opcao-1])
        self.pausar()
    
    def detalhes_contrato_cliente(self, contrato):
        print(f"\n--- DETALHES DO CONTRATO ---")
        print(f"Serviço: {contrato.get_servico_titulo()}")
        print(f"Status: {contrato.get_status()}")
        print(f"Valor: R$ {contrato.get_valor()}")
        
        # Informações do pagamento
        pagamentos = [Pagamento.from_dict(p) for p in self.__db.buscar_todos('pagamentos')]
        pagamento_contrato = next((p for p in pagamentos if p.get_contrato_id() == contrato.get_id()), None)
        if pagamento_contrato:
            print(f"Pagamento: {pagamento_contrato.get_status()}")
        
        # Ações disponíveis
        if contrato.get_status() == "concluido":
            print("\n1. Avaliar serviço")
            print("2. Voltar")
            opcao = input("Escolha: ")
            if opcao == '1':
                self.avaliar_servico(contrato)
    
    def avaliar_servico(self, contrato):
        print(f"\n--- AVALIAR SERVIÇO: {contrato.get_servico_titulo()} ---")
        nota = int(input("Nota (1-5): "))
        comentario = input("Comentário (opcional): ")
        
        # Encontrar prestador
        prestador_dict = next((u for u in self.__db.buscar_todos('usuarios') 
                       if u['id'] == contrato.get_prestador_id()), None)
        
        if prestador_dict:
            avaliacao = Avaliacao(
                contrato.get_id(),
                self.__usuario_logado.get_id(),
                contrato.get_prestador_id(),
                nota,
                comentario
            )
            self.__db.inserir('avaliacoes', avaliacao)
            
            # Notificar prestador
            notificacao = Notificacao(
                contrato.get_prestador_id(),
                "Nova avaliação",
                f"Você recebeu uma avaliação de {nota} estrelas para o serviço {contrato.get_servico_titulo()}"
            )
            self.__db.inserir('notificacoes', notificacao)
            
            print("Avaliação registrada com sucesso!")
        self.pausar()
    
    def minhas_avaliacoes(self):
        print("\n--- MINHAS AVALIAÇÕES ---")
        avaliacoes = [Avaliacao.from_dict(a) for a in self.__db.buscar_todos('avaliacoes')]
        
        if self.__tipo_sessao == 'cliente':
            minhas_avaliacoes = [a for a in avaliacoes if a.get_avaliador_id() == self.__usuario_logado.get_id()]
            print("Avaliações que você fez:")
        else:
            minhas_avaliacoes = [a for a in avaliacoes if a.get_avaliado_id() == self.__usuario_logado.get_id()]
            print("Avaliações que você recebeu:")
        
        if not minhas_avaliacoes:
            print("Nenhuma avaliação encontrada!")
            self.pausar()
            return
        
        for i, avaliacao in enumerate(minhas_avaliacoes, 1):
            usuario_dict = next((u for u in self.__db.buscar_todos('usuarios') 
                        if u['id'] == (avaliacao.get_avaliador_id() if self.__tipo_sessao == 'prestador' else avaliacao.get_avaliado_id())), None)
            nome_usuario = usuario_dict['nome'] if usuario_dict else "Usuário"
            
            if self.__tipo_sessao == 'cliente':
                print(f"{i}. ⭐ {avaliacao.get_nota()}/5 - Para: {nome_usuario}")
            else:
                print(f"{i}. ⭐ {avaliacao.get_nota()}/5 - De: {nome_usuario}")
            
            if avaliacao.get_comentario():
                print(f"   Comentário: {avaliacao.get_comentario()}")
        self.pausar()
    
    def meus_pagamentos(self):
        print("\n--- MEUS PAGAMENTOS ---")
        pagamentos = [Pagamento.from_dict(p) for p in self.__db.buscar_todos('pagamentos')]
        contratos = [Contrato.from_dict(c) for c in self.__db.buscar_todos('contratos')]
        
        if self.__tipo_sessao == 'cliente':
            meus_contratos = [c for c in contratos if c.get_cliente_id() == self.__usuario_logado.get_id()]
        else:
            meus_contratos = [c for c in contratos if c.get_prestador_id() == self.__usuario_logado.get_id()]
        
        meus_pagamentos = []
        for contrato in meus_contratos:
            pagamento_contrato = next((p for p in pagamentos if p.get_contrato_id() == contrato.get_id()), None)
            if pagamento_contrato:
                meus_pagamentos.append((contrato, pagamento_contrato))
        
        if not meus_pagamentos:
            print("Nenhum pagamento encontrado!")
            self.pausar()
            return
        
        for i, (contrato, pagamento) in enumerate(meus_pagamentos, 1):
            print(f"{i}. {contrato.get_servico_titulo()} - R$ {pagamento.get_valor()} - Status: {pagamento.get_status()}")
        self.pausar()
    
    def ver_notificacoes(self):
        print("\n--- NOTIFICAÇÕES ---")
        notificacoes = [Notificacao.from_dict(n) for n in self.__db.buscar_todos('notificacoes')]
        minhas_notificacoes = [n for n in notificacoes if n.get_usuario_id() == self.__usuario_logado.get_id()]
        
        nao_lidas = [n for n in minhas_notificacoes if not n.get_lida()]
        lidas = [n for n in minhas_notificacoes if n.get_lida()]
        
        if nao_lidas:
            print("Não lidas:")
            for i, notificacao in enumerate(nao_lidas, 1):
                print(f"{i}. 📢 {notificacao.get_titulo()}")
                print(f"   {notificacao.get_mensagem()}")
        
        if lidas:
            print("\nLidas:")
            for i, notificacao in enumerate(lidas, len(nao_lidas)+1):
                print(f"{i}. ✓ {notificacao.get_titulo()}")
                print(f"   {notificacao.get_mensagem()}")
        
        if not minhas_notificacoes:
            print("Nenhuma notificação!")
            self.pausar()
            return
        
        opcao = input("\n1. Marcar todas como lidas\n2. Voltar\nEscolha: ")
        if opcao == '1':
            for notificacao in nao_lidas:
                notificacao.marcar_como_lida()
                self.__db.atualizar('notificacoes', notificacao.get_id(), notificacao.to_dict())
            print("Notificações marcadas como lidas!")
        self.pausar()
    
    def meus_servicos(self):
        print("\n--- MEUS SERVIÇOS ---")
        servicos = [Servico.from_dict(s) for s in self.__db.buscar_todos('servicos')]
        meus_servicos = [s for s in servicos if s.get_prestador_id() == self.__usuario_logado.get_id()]
        
        if not meus_servicos:
            print("Nenhum serviço cadastrado!")
        else:
            for i, servico in enumerate(meus_servicos, 1):
                status = "Ativo" if servico.get_ativo() else "Inativo"
                print(f"{i}. {servico.get_titulo()} - R$ {servico.get_valor()} - {status}")
        
        print("\n1. Cadastrar novo serviço")
        print("2. Editar serviço")
        print("3. Ativar/Desativar serviço")
        opcao = input("Escolha: ")
        
        if opcao == '1':
            self.cadastrar_servico()
        elif opcao == '2':
            if meus_servicos:
                num = input("Número do serviço para editar: ")
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= len(meus_servicos):
                        self.editar_servico(meus_servicos[num-1])
        elif opcao == '3':
            if meus_servicos:
                num = input("Número do serviço para ativar/desativar: ")
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= len(meus_servicos):
                        servico = meus_servicos[num-1]
                        if servico.get_ativo():
                            servico.desativar()
                            print("Serviço desativado!")
                        else:
                            servico.ativar()
                            print("Serviço ativado!")
                        self.__db.atualizar('servicos', servico.get_id(), servico.to_dict())
        self.pausar()
    
    def cadastrar_servico(self):
        print("\n--- NOVO SERVIÇO ---")
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        valor = float(input("Valor: R$ "))
        
        servico = Servico(self.__usuario_logado.get_id(), titulo, descricao, valor)
        self.__db.inserir('servicos', servico)
        print("Serviço cadastrado!")
    
    def editar_servico(self, servico):
        print(f"\n--- EDITAR SERVIÇO: {servico.get_titulo()} ---")
        novoTitulo = input(f"Novo título ({servico.get_titulo()}): ") or servico.get_titulo()
        novaDescricao = input(f"Nova descrição ({servico.get_descricao()}): ") or servico.get_descricao()
        novoValor = input(f"Novo valor ({servico.get_valor()}): ")
        
        servico.set_titulo(novoTitulo)
        servico.set_descricao(novaDescricao)
        if novoValor:
            servico.set_valor(float(novoValor))
        
        self.__db.atualizar('servicos', servico.get_id(), servico.to_dict())
        print("Serviço atualizado!")
    
    def solicitacoes_servico(self):
        print("\n--- SOLICITAÇÕES ---")
        contratos = [Contrato.from_dict(c) for c in self.__db.buscar_todos('contratos')]
        solicitacoes = [c for c in contratos if c.get_prestador_id() == self.__usuario_logado.get_id()]
        
        if not solicitacoes:
            print("Nenhuma solicitação encontrada!")
            self.pausar()
            return
            
        for i, contrato in enumerate(solicitacoes, 1):
            cliente_dict = next((u for u in self.__db.buscar_todos('usuarios') 
                         if u['id'] == contrato.get_cliente_id()), None)
            nome_cliente = cliente_dict['nome'] if cliente_dict else "Cliente"
            print(f"{i}. {contrato.get_servico_titulo()} - Cliente: {nome_cliente} - Status: {contrato.get_status()}")
        
        num = input("\nNúmero para gerenciar (0 para voltar): ")
        if num.isdigit():
            num = int(num)
            if num > 0 and num <= len(solicitacoes):
                self.detalhes_contrato_prestador(solicitacoes[num-1])
        self.pausar()
    
    def detalhes_contrato_prestador(self, contrato):
        print(f"\n--- DETALHES DO CONTRATO ---")
        print(f"Serviço: {contrato.get_servico_titulo()}")
        print(f"Status: {contrato.get_status()}")
        print(f"Valor: R$ {contrato.get_valor()}")
        
        cliente_dict = next((u for u in self.__db.buscar_todos('usuarios') 
                     if u['id'] == contrato.get_cliente_id()), None)
        if cliente_dict:
            cliente = Usuario.from_dict(cliente_dict)
            print(f"Cliente: {cliente.get_nome()}")
        
        # Ações disponíveis
        if contrato.get_status() == "solicitado":
            print("\n1. Aceitar contrato")
            print("2. Recusar contrato")
        elif contrato.get_status() == "aceito":
            print("\n1. Marcar como concluído")
        elif contrato.get_status() == "concluido":
            print("\nContrato concluído - Aguardando avaliação do cliente")
        
        opcao = input("Escolha: ")
        
        if contrato.get_status() == "solicitado":
            if opcao == '1':
                contrato.aceitar()
                
                # Atualizar pagamento
                pagamentos = [Pagamento.from_dict(p) for p in self.__db.buscar_todos('pagamentos')]
                pagamento_contrato = next((p for p in pagamentos if p.get_contrato_id() == contrato.get_id()), None)
                if pagamento_contrato:
                    pagamento_contrato.set_status('aprovado')
                    self.__db.atualizar('pagamentos', pagamento_contrato.get_id(), pagamento_contrato.to_dict())
                
                # Notificar cliente
                notificacao = Notificacao(
                    contrato.get_cliente_id(),
                    "Serviço aceito",
                    f"O prestador aceitou seu serviço: {contrato.get_servico_titulo()}"
                )
                self.__db.inserir('notificacoes', notificacao)
                
                print("Contrato aceito!")
            elif opcao == '2':
                contrato.recusar()
                
                # Atualizar pagamento
                pagamentos = [Pagamento.from_dict(p) for p in self.__db.buscar_todos('pagamentos')]
                pagamento_contrato = next((p for p in pagamentos if p.get_contrato_id() == contrato.get_id()), None)
                if pagamento_contrato:
                    pagamento_contrato.set_status('recusado')
                    self.__db.atualizar('pagamentos', pagamento_contrato.get_id(), pagamento_contrato.to_dict())
                
                print("Contrato recusado!")
        
        elif contrato.get_status() == "aceito" and opcao == '1':
            contrato.concluir()
            
            # Notificar cliente
            notificacao = Notificacao(
                contrato.get_cliente_id(),
                "Serviço concluído",
                f"O serviço {contrato.get_servico_titulo()} foi concluído. Por favor, avalie o serviço."
            )
            self.__db.inserir('notificacoes', notificacao)
            
            print("Serviço marcado como concluído!")
        
        self.__db.atualizar('contratos', contrato.get_id(), contrato.to_dict())
        self.pausar()
    
    def editar_perfil(self):
        print("\n--- EDITAR PERFIL ---")
        print(f"Nome atual: {self.__usuario_logado.get_nome()}")
        print(f"Email atual: {self.__usuario_logado.get_email()}")
        print(f"CPF atual: {self.__usuario_logado.get_cpf()}")
        
        novo_nome = input("Novo nome (deixe em branco para manter): ")
        nova_senha = input("Nova senha (deixe em branco para manter): ")
        
        if novo_nome:
            self.__usuario_logado.set_nome(novo_nome)
        if nova_senha:
            self.__usuario_logado.set_senha(nova_senha)
        
        # Atualizar no banco
        for i, usuario_dict in enumerate(self.__db.dados['usuarios']):
            if usuario_dict['id'] == self.__usuario_logado.get_id():
                self.__db.dados['usuarios'][i] = self.__usuario_logado.to_dict()
                self.__db.salvar()
                break
        
        print("Perfil atualizado com sucesso!")
        self.pausar()