import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class SistemaIngressos:
    def __init__(self, root):
        self.root = root
        self.root.title("EasyTickets - Sistema de Ingressos")
        self.root.geometry("1000x700")
        self.root.configure(bg="#F5F5F5")
        
        # Arquivos para salvar os dados
        self.arquivo_eventos = "eventos.json"
        self.arquivo_usuarios = "usuarios.json"
        self.arquivo_compras = "compras.json"
        self.usuario_logado = None
        
        # Carregar dados
        self.eventos = self.carregar_eventos()
        self.usuarios = self.carregar_usuarios()
        
        # Cores do tema (EasyTickets)
        self.cor_primaria = "#FF6B35"
        self.cor_secundaria = "#004E89"
        self.cor_sucesso = "#06A77D"
        self.cor_fundo = "#F5F5F5"
        self.cor_card = "#FFFFFF"
        self.cor_texto = "#333333"
        self.cor_texto_claro = "#666666"
        
        # Criar tela de login inicial
        self.tela_login()
    
    def carregar_eventos(self):
        """Carrega eventos do arquivo JSON"""
        if os.path.exists(self.arquivo_eventos):
            try:
                with open(self.arquivo_eventos, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def salvar_eventos(self):
        """Salva eventos no arquivo JSON"""
        try:
            with open(self.arquivo_eventos, 'w', encoding='utf-8') as f:
                json.dump(self.eventos, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {str(e)}")
            return False
    
    def carregar_usuarios(self):
        """Carrega usuários do arquivo JSON"""
        if os.path.exists(self.arquivo_usuarios):
            try:
                with open(self.arquivo_usuarios, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def salvar_usuarios(self):
        """Salva usuários no arquivo JSON"""
        try:
            with open(self.arquivo_usuarios, 'w', encoding='utf-8') as f:
                json.dump(self.usuarios, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {str(e)}")
            return False
    
    def carregar_compras(self):
        """Carrega compras do arquivo JSON"""
        if os.path.exists(self.arquivo_compras):
            try:
                with open(self.arquivo_compras, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def salvar_compras(self, compras):
        """Salva compras no arquivo JSON"""
        try:
            with open(self.arquivo_compras, 'w', encoding='utf-8') as f:
                json.dump(compras, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {str(e)}")
            return False
    
    def limpar_tela(self):
        """Limpa todos os widgets da tela"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def criar_botao_estilizado(self, parent, texto, comando, cor_bg, largura=25, altura=2):
        """Cria botão estilizado"""
        btn = tk.Button(
            parent,
            text=texto,
            font=("Segoe UI", 11, "bold"),
            width=largura,
            height=altura,
            command=comando,
            bg=cor_bg,
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            activebackground=self.escurecer_cor(cor_bg),
            activeforeground="white"
        )
        return btn
    
    def escurecer_cor(self, cor):
        """Escurece uma cor hexadecimal"""
        # Simplificado - retorna uma cor mais escura
        cores_escuras = {
            "#FF6B35": "#E55A2B",
            "#004E89": "#003D6B",
            "#06A77D": "#058A6A",
            "#757575": "#616161"
        }
        return cores_escuras.get(cor, "#333333")
    
    def criar_card(self, parent, padding=20):
        """Cria um frame com estilo de card"""
        card = tk.Frame(
            parent,
            bg=self.cor_card,
            relief=tk.FLAT,
            bd=0
        )
        # Simular sombra com bordas
        return card
    
    def tela_login(self):
        """Tela de login"""
        self.limpar_tela()
        self.root.configure(bg=self.cor_fundo)
        
        # Frame central
        frame_central = tk.Frame(self.root, bg=self.cor_fundo)
        frame_central.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Card de login
        card_login = self.criar_card(frame_central, padding=40)
        card_login.pack(padx=30, pady=30)
        
        # Logo/Título
        frame_titulo = tk.Frame(card_login, bg=self.cor_card, pady=30)
        frame_titulo.pack()
        
        titulo = tk.Label(
            frame_titulo,
            text="🎫 Sistema de Ingressos",
            font=("Segoe UI", 28, "bold"),
            bg=self.cor_card,
            fg=self.cor_primaria
        )
        titulo.pack()
        
        subtitulo = tk.Label(
            frame_titulo,
            text="Faça login para continuar",
            font=("Segoe UI", 12),
            bg=self.cor_card,
            fg=self.cor_texto_claro
        )
        subtitulo.pack(pady=(10, 0))
        
        # Frame de campos
        frame_campos = tk.Frame(card_login, bg=self.cor_card, padx=50, pady=30)
        frame_campos.pack()
        
        # Email
        tk.Label(
            frame_campos,
            text="Email:",
            font=("Segoe UI", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        entry_email = tk.Entry(
            frame_campos,
            width=35,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_email.grid(row=1, column=0, pady=(0, 15), ipady=8)
        
        # Senha
        tk.Label(
            frame_campos,
            text="Senha:",
            font=("Segoe UI", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=2, column=0, sticky="w", pady=(0, 5))
        
        entry_senha = tk.Entry(
            frame_campos,
            width=35,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9",
            show="●"
        )
        entry_senha.grid(row=3, column=0, pady=(0, 20), ipady=8)
        
        # Frame de botões
        frame_botoes = tk.Frame(card_login, bg=self.cor_card, pady=20)
        frame_botoes.pack()
        
        def fazer_login():
            email = entry_email.get().strip()
            senha = entry_senha.get().strip()
            
            if not email or not senha:
                messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
                return
            
            # Verificar credenciais
            usuario_encontrado = None
            for usuario in self.usuarios:
                if usuario['email'] == email and usuario['senha'] == senha:
                    usuario_encontrado = usuario
                    break
            
            if usuario_encontrado:
                self.usuario_logado = usuario_encontrado
                messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario_encontrado['nome']}!")
                self.criar_menu_principal()
            else:
                messagebox.showerror("Erro", "Email ou senha incorretos!")
        
        btn_login = self.criar_botao_estilizado(
            frame_botoes,
            "Entrar",
            fazer_login,
            self.cor_primaria,
            largura=30
        )
        btn_login.pack(pady=5)
        
        btn_registro = tk.Button(
            frame_botoes,
            text="Não tem conta? Criar conta",
            font=("Segoe UI", 10),
            bg=self.cor_card,
            fg=self.cor_secundaria,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.tela_registro,
            activebackground=self.cor_card,
            activeforeground=self.cor_secundaria
        )
        btn_registro.pack(pady=10)
    
    def tela_registro(self):
        """Tela de registro de novo usuário"""
        self.limpar_tela()
        self.root.configure(bg=self.cor_fundo)
        
        # Frame central
        frame_central = tk.Frame(self.root, bg=self.cor_fundo)
        frame_central.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Card de registro
        card_registro = self.criar_card(frame_central, padding=40)
        card_registro.pack(padx=30, pady=30)
        
        # Título
        frame_titulo = tk.Frame(card_registro, bg=self.cor_card, pady=20)
        frame_titulo.pack()
        
        titulo = tk.Label(
            frame_titulo,
            text="Criar Nova Conta",
            font=("Segoe UI", 24, "bold"),
            bg=self.cor_card,
            fg=self.cor_primaria
        )
        titulo.pack()
        
        # Frame de campos
        frame_campos = tk.Frame(card_registro, bg=self.cor_card, padx=50, pady=20)
        frame_campos.pack()
        
        # Nome
        tk.Label(
            frame_campos,
            text="Nome Completo:",
            font=("Segoe UI", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        entry_nome = tk.Entry(
            frame_campos,
            width=35,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_nome.grid(row=1, column=0, pady=(0, 10), ipady=8)
        
        # Email
        tk.Label(
            frame_campos,
            text="Email:",
            font=("Segoe UI", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=2, column=0, sticky="w", pady=(0, 5))
        
        entry_email = tk.Entry(
            frame_campos,
            width=35,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_email.grid(row=3, column=0, pady=(0, 10), ipady=8)
        
        # Senha
        tk.Label(
            frame_campos,
            text="Senha:",
            font=("Segoe UI", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=4, column=0, sticky="w", pady=(0, 5))
        
        entry_senha = tk.Entry(
            frame_campos,
            width=35,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9",
            show="●"
        )
        entry_senha.grid(row=5, column=0, pady=(0, 20), ipady=8)
        
        # Frame de botões
        frame_botoes = tk.Frame(card_registro, bg=self.cor_card, pady=20)
        frame_botoes.pack()
        
        def criar_conta():
            nome = entry_nome.get().strip()
            email = entry_email.get().strip()
            senha = entry_senha.get().strip()
            
            if not nome or not email or not senha:
                messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
                return
            
            if len(senha) < 4:
                messagebox.showwarning("Atenção", "A senha deve ter pelo menos 4 caracteres!")
                return
            
            # Verificar se email já existe
            for usuario in self.usuarios:
                if usuario['email'] == email:
                    messagebox.showerror("Erro", "Este email já está cadastrado!")
                    return
            
            # Criar novo usuário
            novo_usuario = {
                "id": len(self.usuarios) + 1,
                "nome": nome,
                "email": email,
                "senha": senha
            }
            
            self.usuarios.append(novo_usuario)
            
            if self.salvar_usuarios():
                messagebox.showinfo("Sucesso", "Conta criada com sucesso! Faça login para continuar.")
                self.tela_login()
        
        btn_criar = self.criar_botao_estilizado(
            frame_botoes,
            "Criar Conta",
            criar_conta,
            self.cor_sucesso,
            largura=30
        )
        btn_criar.pack(pady=5)
        
        btn_voltar = tk.Button(
            frame_botoes,
            text="Voltar ao Login",
            font=("Segoe UI", 10),
            bg=self.cor_card,
            fg=self.cor_texto_claro,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.tela_login,
            activebackground=self.cor_card,
            activeforeground=self.cor_secundaria
        )
        btn_voltar.pack(pady=10)
    
    def criar_menu_principal(self):
        """Cria o menu principal do sistema"""
        self.limpar_tela()
        self.root.configure(bg=self.cor_fundo)
        
        # Header
        frame_header = tk.Frame(self.root, bg=self.cor_primaria, height=80)
        frame_header.pack(fill=tk.X)
        frame_header.pack_propagate(False)
        
        frame_header_content = tk.Frame(frame_header, bg=self.cor_primaria)
        frame_header_content.pack(fill=tk.BOTH, expand=True, padx=30, pady=15)
        
        titulo = tk.Label(
            frame_header_content,
            text="🎫 Sistema de Ingressos",
            font=("Segoe UI", 20, "bold"),
            bg=self.cor_primaria,
            fg="white"
        )
        titulo.pack(side=tk.LEFT)
        
        frame_user = tk.Frame(frame_header_content, bg=self.cor_primaria)
        frame_user.pack(side=tk.RIGHT)
        
        tk.Label(
            frame_user,
            text=f"👤 {self.usuario_logado['nome']}",
            font=("Segoe UI", 11),
            bg=self.cor_primaria,
            fg="white"
        ).pack(side=tk.LEFT, padx=10)
        
        btn_logout = tk.Button(
            frame_user,
            text="Sair",
            font=("Segoe UI", 10),
            bg="white",
            fg=self.cor_primaria,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.tela_login,
            padx=15,
            pady=5
        )
        btn_logout.pack(side=tk.LEFT)
        
        # Conteúdo principal
        frame_conteudo = tk.Frame(self.root, bg=self.cor_fundo, padx=40, pady=30)
        frame_conteudo.pack(fill=tk.BOTH, expand=True)
        
        # Título da seção
        tk.Label(
            frame_conteudo,
            text="Bem-vindo ao EasyTickets",
            font=("Segoe UI", 18, "bold"),
            bg=self.cor_fundo,
            fg=self.cor_texto
        ).pack(anchor="w", pady=(0, 20))
        
        # Frame de botões
        frame_botoes = tk.Frame(frame_conteudo, bg=self.cor_fundo)
        frame_botoes.pack(fill=tk.X, pady=20)
        
        btn_cadastrar = self.criar_botao_estilizado(
            frame_botoes,
            "➕ Cadastrar Evento",
            self.tela_cadastro,
            self.cor_sucesso,
            largura=22,
            altura=3
        )
        btn_cadastrar.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
        
        btn_visualizar = self.criar_botao_estilizado(
            frame_botoes,
            "📋 Visualizar Eventos",
            self.tela_visualizacao,
            self.cor_secundaria,
            largura=22,
            altura=3
        )
        btn_visualizar.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
        
        btn_editar = self.criar_botao_estilizado(
            frame_botoes,
            "✏️ Editar Evento",
            self.tela_edicao,
            self.cor_primaria,
            largura=22,
            altura=3
        )
        btn_editar.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
        
        # Segunda linha de botões
        frame_botoes2 = tk.Frame(frame_conteudo, bg=self.cor_fundo)
        frame_botoes2.pack(fill=tk.X, pady=10)
        
        btn_comprar = self.criar_botao_estilizado(
            frame_botoes2,
            "🛒 Comprar Ingressos",
            self.tela_compra,
            "#9C27B0",
            largura=22,
            altura=3
        )
        btn_comprar.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
    
    def tela_cadastro(self):
        """Tela para cadastrar novo evento"""
        self.limpar_tela()
        self.root.configure(bg=self.cor_fundo)
        
        # Header
        frame_header = tk.Frame(self.root, bg=self.cor_primaria, height=60)
        frame_header.pack(fill=tk.X)
        frame_header.pack_propagate(False)
        
        tk.Label(
            frame_header,
            text="➕ Cadastrar Novo Evento",
            font=("Segoe UI", 18, "bold"),
            bg=self.cor_primaria,
            fg="white"
        ).pack(pady=15)
        
        # Frame principal com scroll
        canvas = tk.Canvas(self.root, bg=self.cor_fundo, highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.cor_fundo)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Card de formulário
        card_form = self.criar_card(scrollable_frame)
        card_form.pack(padx=50, pady=30, fill=tk.BOTH, expand=True)
        
        frame_campos = tk.Frame(card_form, bg=self.cor_card, padx=40, pady=30)
        frame_campos.pack()
        
        # Nome do evento
        tk.Label(
            frame_campos,
            text="Nome do Evento:",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        entry_nome = tk.Entry(
            frame_campos,
            width=50,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_nome.grid(row=1, column=0, pady=(0, 15), ipady=8, sticky="ew")
        
        # Data e Horário lado a lado
        frame_data_hora = tk.Frame(frame_campos, bg=self.cor_card)
        frame_data_hora.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        
        tk.Label(
            frame_data_hora,
            text="Data (DD/MM/AAAA):",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        entry_data = tk.Entry(
            frame_data_hora,
            width=25,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_data.grid(row=1, column=0, ipady=8, padx=(0, 15))
        
        tk.Label(
            frame_data_hora,
            text="Horário (HH:MM):",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=1, sticky="w", pady=(0, 5))
        
        entry_horario = tk.Entry(
            frame_data_hora,
            width=25,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_horario.grid(row=1, column=1, ipady=8)
        
        # Local
        tk.Label(
            frame_campos,
            text="Local:",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=3, column=0, sticky="w", pady=(0, 5))
        
        entry_local = tk.Entry(
            frame_campos,
            width=50,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_local.grid(row=4, column=0, pady=(0, 15), ipady=8, sticky="ew")
        
        # Descrição
        tk.Label(
            frame_campos,
            text="Descrição:",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=5, column=0, sticky="w", pady=(0, 5))
        
        text_descricao = tk.Text(
            frame_campos,
            width=50,
            height=6,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9",
            wrap=tk.WORD
        )
        text_descricao.grid(row=6, column=0, pady=(0, 15), sticky="ew")
        
        # Valor e Quantidade lado a lado
        frame_valor_qtd = tk.Frame(frame_campos, bg=self.cor_card)
        frame_valor_qtd.grid(row=7, column=0, sticky="ew", pady=(0, 20))
        
        tk.Label(
            frame_valor_qtd,
            text="Valor do Ingresso (R$):",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        entry_valor = tk.Entry(
            frame_valor_qtd,
            width=25,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_valor.grid(row=1, column=0, ipady=8, padx=(0, 15))
        
        tk.Label(
            frame_valor_qtd,
            text="Quantidade Disponível:",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=1, sticky="w", pady=(0, 5))
        
        entry_quantidade = tk.Entry(
            frame_valor_qtd,
            width=25,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_quantidade.grid(row=1, column=1, ipady=8)
        
        frame_campos.columnconfigure(0, weight=1)
        frame_data_hora.columnconfigure(0, weight=1)
        frame_data_hora.columnconfigure(1, weight=1)
        frame_valor_qtd.columnconfigure(0, weight=1)
        frame_valor_qtd.columnconfigure(1, weight=1)
        
        # Frame para botões
        frame_botoes = tk.Frame(card_form, bg=self.cor_card, pady=20)
        frame_botoes.pack()
        
        def salvar_evento():
            nome = entry_nome.get().strip()
            data = entry_data.get().strip()
            horario = entry_horario.get().strip()
            local = entry_local.get().strip()
            descricao = text_descricao.get("1.0", tk.END).strip()
            valor = entry_valor.get().strip()
            quantidade = entry_quantidade.get().strip()
            
            if not nome or not data or not horario or not local or not valor or not quantidade:
                messagebox.showwarning("Atenção", "Por favor, preencha todos os campos obrigatórios!")
                return
            
            try:
                valor_float = float(valor.replace(",", "."))
                quantidade_int = int(quantidade)
                
                if valor_float < 0 or quantidade_int < 0:
                    messagebox.showwarning("Atenção", "Valor e quantidade devem ser números positivos!")
                    return
            except ValueError:
                messagebox.showerror("Erro", "Valor do ingresso e quantidade devem ser números válidos!")
                return
            
            evento = {
                "id": len(self.eventos) + 1,
                "nome": nome,
                "data": data,
                "horario": horario,
                "local": local,
                "descricao": descricao,
                "valor": valor_float,
                "quantidade_disponivel": quantidade_int,
                "criado_por": self.usuario_logado['nome']
            }
            
            self.eventos.append(evento)
            
            if self.salvar_eventos():
                messagebox.showinfo("Sucesso", "Evento cadastrado com sucesso! 🎉")
                self.criar_menu_principal()
        
        btn_salvar = self.criar_botao_estilizado(
            frame_botoes,
            "💾 Salvar Evento",
            salvar_evento,
            self.cor_sucesso,
            largura=20
        )
        btn_salvar.pack(side=tk.LEFT, padx=10)
        
        btn_voltar = self.criar_botao_estilizado(
            frame_botoes,
            "← Voltar",
            self.criar_menu_principal,
            "#757575",
            largura=20
        )
        btn_voltar.pack(side=tk.LEFT, padx=10)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def tela_visualizacao(self):
        """Tela para visualizar todos os eventos com cards bonitos"""
        self.limpar_tela()
        self.root.configure(bg=self.cor_fundo)
        
        # Header
        frame_header = tk.Frame(self.root, bg=self.cor_secundaria, height=60)
        frame_header.pack(fill=tk.X)
        frame_header.pack_propagate(False)
        
        tk.Label(
            frame_header,
            text="📋 Eventos Disponíveis",
            font=("Segoe UI", 18, "bold"),
            bg=self.cor_secundaria,
            fg="white"
        ).pack(pady=15)
        
        # Frame principal com scroll
        canvas = tk.Canvas(self.root, bg=self.cor_fundo, highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.cor_fundo)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Conteúdo
        frame_conteudo = tk.Frame(scrollable_frame, bg=self.cor_fundo, padx=30, pady=20)
        frame_conteudo.pack(fill=tk.BOTH, expand=True)
        
        if not self.eventos:
            card_vazio = self.criar_card(frame_conteudo)
            card_vazio.pack(fill=tk.X, pady=10, padx=20)
            
            tk.Label(
                card_vazio,
                text="📭 Nenhum evento cadastrado ainda.",
                font=("Segoe UI", 14),
                bg=self.cor_card,
                fg=self.cor_texto_claro,
                pady=30
            ).pack()
        else:
            for evento in self.eventos:
                card_evento = self.criar_card(frame_conteudo)
                card_evento.pack(fill=tk.X, pady=10, padx=20)
                
                frame_card_content = tk.Frame(card_evento, bg=self.cor_card, padx=25, pady=20)
                frame_card_content.pack(fill=tk.BOTH, expand=True)
                
                # Nome do evento
                tk.Label(
                    frame_card_content,
                    text=evento['nome'],
                    font=("Segoe UI", 16, "bold"),
                    bg=self.cor_card,
                    fg=self.cor_primaria
                ).pack(anchor="w", pady=(0, 10))
                
                # Informações principais
                frame_info = tk.Frame(frame_card_content, bg=self.cor_card)
                frame_info.pack(fill=tk.X, pady=(0, 10))
                
                info_text = f"📅 {evento['data']} às {evento['horario']}  |  📍 {evento['local']}"
                tk.Label(
                    frame_info,
                    text=info_text,
                    font=("Segoe UI", 11),
                    bg=self.cor_card,
                    fg=self.cor_texto
                ).pack(side=tk.LEFT)
                
                # Descrição
                tk.Label(
                    frame_card_content,
                    text=evento['descricao'],
                    font=("Segoe UI", 10),
                    bg=self.cor_card,
                    fg=self.cor_texto_claro,
                    wraplength=800,
                    justify=tk.LEFT
                ).pack(anchor="w", pady=(0, 15))
                
                # Rodapé do card com preço e quantidade
                frame_rodape = tk.Frame(frame_card_content, bg=self.cor_card)
                frame_rodape.pack(fill=tk.X)
                
                tk.Label(
                    frame_rodape,
                    text=f"💰 R$ {evento['valor']:.2f}",
                    font=("Segoe UI", 14, "bold"),
                    bg=self.cor_card,
                    fg=self.cor_sucesso
                ).pack(side=tk.LEFT)
                
                tk.Label(
                    frame_rodape,
                    text=f"🎫 {evento['quantidade_disponivel']} ingressos disponíveis",
                    font=("Segoe UI", 11),
                    bg=self.cor_card,
                    fg=self.cor_texto_claro
                ).pack(side=tk.RIGHT)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botão voltar
        frame_footer = tk.Frame(self.root, bg=self.cor_fundo, pady=15)
        frame_footer.pack(fill=tk.X)
        
        btn_voltar = self.criar_botao_estilizado(
            frame_footer,
            "← Voltar ao Menu",
            self.criar_menu_principal,
            "#757575",
            largura=20
        )
        btn_voltar.pack()
    
    def tela_edicao(self):
        """Tela para editar eventos"""
        self.limpar_tela()
        self.root.configure(bg=self.cor_fundo)
        
        # Adicionar fundo decorativo
        self.criar_fundo_decorativo(self.root)
        
        if not self.eventos:
            # Header
            frame_header = tk.Frame(self.root, bg=self.cor_primaria, height=60)
            frame_header.pack(fill=tk.X)
            frame_header.pack_propagate(False)
            
            tk.Label(
                frame_header,
                text="✏️ Editar Evento",
                font=("Segoe UI", 18, "bold"),
                bg=self.cor_primaria,
                fg="white"
            ).pack(pady=15)
            
            frame_central = tk.Frame(self.root, bg=self.cor_fundo)
            frame_central.pack(expand=True, fill=tk.BOTH, pady=50)
            
            tk.Label(
                frame_central,
                text="📭 Nenhum evento cadastrado para editar.",
                font=("Segoe UI", 14),
                bg=self.cor_fundo,
                fg=self.cor_texto_claro
            ).pack()
            
            btn_voltar = self.criar_botao_estilizado(
                frame_central,
                "← Voltar ao Menu",
                self.criar_menu_principal,
                "#757575",
                largura=20
            )
            btn_voltar.pack(pady=20)
            return
        
        # Header
        frame_header = tk.Frame(self.root, bg=self.cor_primaria, height=60)
        frame_header.pack(fill=tk.X)
        frame_header.pack_propagate(False)
        
        tk.Label(
            frame_header,
            text="✏️ Editar Evento",
            font=("Segoe UI", 18, "bold"),
            bg=self.cor_primaria,
            fg="white"
        ).pack(pady=15)
        
        # Frame principal
        canvas = tk.Canvas(self.root, bg=self.cor_fundo, highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.cor_fundo)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Card de formulário
        card_form = self.criar_card(scrollable_frame)
        card_form.pack(padx=50, pady=30, fill=tk.BOTH, expand=True)
        
        frame_selecao = tk.Frame(card_form, bg=self.cor_card, padx=40, pady=20)
        frame_selecao.pack()
        
        tk.Label(
            frame_selecao,
            text="Selecione o evento:",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        var_evento = tk.StringVar()
        combo_eventos = ttk.Combobox(
            frame_selecao,
            textvariable=var_evento,
            width=50,
            font=("Segoe UI", 11),
            state="readonly"
        )
        combo_eventos['values'] = [f"{e['nome']} - {e['data']}" for e in self.eventos]
        combo_eventos.pack(side=tk.LEFT)
        
        frame_campos = tk.Frame(card_form, bg=self.cor_card, padx=40, pady=20)
        frame_campos.pack()
        
        # Campos (mesma estrutura do cadastro)
        tk.Label(
            frame_campos,
            text="Nome do Evento:",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        entry_nome = tk.Entry(
            frame_campos,
            width=50,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_nome.grid(row=1, column=0, pady=(0, 15), ipady=8, sticky="ew")
        
        frame_data_hora = tk.Frame(frame_campos, bg=self.cor_card)
        frame_data_hora.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        
        tk.Label(
            frame_data_hora,
            text="Data (DD/MM/AAAA):",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        entry_data = tk.Entry(
            frame_data_hora,
            width=25,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_data.grid(row=1, column=0, ipady=8, padx=(0, 15))
        
        tk.Label(
            frame_data_hora,
            text="Horário (HH:MM):",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=1, sticky="w", pady=(0, 5))
        
        entry_horario = tk.Entry(
            frame_data_hora,
            width=25,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_horario.grid(row=1, column=1, ipady=8)
        
        tk.Label(
            frame_campos,
            text="Local:",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=3, column=0, sticky="w", pady=(0, 5))
        
        entry_local = tk.Entry(
            frame_campos,
            width=50,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_local.grid(row=4, column=0, pady=(0, 15), ipady=8, sticky="ew")
        
        tk.Label(
            frame_campos,
            text="Descrição:",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=5, column=0, sticky="w", pady=(0, 5))
        
        text_descricao = tk.Text(
            frame_campos,
            width=50,
            height=6,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9",
            wrap=tk.WORD
        )
        text_descricao.grid(row=6, column=0, pady=(0, 15), sticky="ew")
        
        frame_valor_qtd = tk.Frame(frame_campos, bg=self.cor_card)
        frame_valor_qtd.grid(row=7, column=0, sticky="ew", pady=(0, 20))
        
        tk.Label(
            frame_valor_qtd,
            text="Valor do Ingresso (R$):",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        entry_valor = tk.Entry(
            frame_valor_qtd,
            width=25,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_valor.grid(row=1, column=0, ipady=8, padx=(0, 15))
        
        tk.Label(
            frame_valor_qtd,
            text="Quantidade Disponível:",
            font=("Segoe UI", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).grid(row=0, column=1, sticky="w", pady=(0, 5))
        
        entry_quantidade = tk.Entry(
            frame_valor_qtd,
            width=25,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        entry_quantidade.grid(row=1, column=1, ipady=8)
        
        frame_campos.columnconfigure(0, weight=1)
        frame_data_hora.columnconfigure(0, weight=1)
        frame_data_hora.columnconfigure(1, weight=1)
        frame_valor_qtd.columnconfigure(0, weight=1)
        frame_valor_qtd.columnconfigure(1, weight=1)
        
        def carregar_evento(event=None):
            selecionado = combo_eventos.current()
            if selecionado >= 0:
                evento = self.eventos[selecionado]
                entry_nome.delete(0, tk.END)
                entry_nome.insert(0, evento['nome'])
                entry_data.delete(0, tk.END)
                entry_data.insert(0, evento['data'])
                entry_horario.delete(0, tk.END)
                entry_horario.insert(0, evento['horario'])
                entry_local.delete(0, tk.END)
                entry_local.insert(0, evento['local'])
                text_descricao.delete("1.0", tk.END)
                text_descricao.insert("1.0", evento['descricao'])
                entry_valor.delete(0, tk.END)
                entry_valor.insert(0, str(evento['valor']))
                entry_quantidade.delete(0, tk.END)
                entry_quantidade.insert(0, str(evento['quantidade_disponivel']))
        
        combo_eventos.bind('<<ComboboxSelected>>', carregar_evento)
        
        def salvar_edicao():
            selecionado = combo_eventos.current()
            if selecionado < 0:
                messagebox.showwarning("Atenção", "Por favor, selecione um evento para editar!")
                return
            
            nome = entry_nome.get().strip()
            data = entry_data.get().strip()
            horario = entry_horario.get().strip()
            local = entry_local.get().strip()
            descricao = text_descricao.get("1.0", tk.END).strip()
            valor = entry_valor.get().strip()
            quantidade = entry_quantidade.get().strip()
            
            if not nome or not data or not horario or not local or not valor or not quantidade:
                messagebox.showwarning("Atenção", "Por favor, preencha todos os campos obrigatórios!")
                return
            
            try:
                valor_float = float(valor.replace(",", "."))
                quantidade_int = int(quantidade)
                
                if valor_float < 0 or quantidade_int < 0:
                    messagebox.showwarning("Atenção", "Valor e quantidade devem ser números positivos!")
                    return
            except ValueError:
                messagebox.showerror("Erro", "Valor do ingresso e quantidade devem ser números válidos!")
                return
            
            evento = self.eventos[selecionado]
            evento['nome'] = nome
            evento['data'] = data
            evento['horario'] = horario
            evento['local'] = local
            evento['descricao'] = descricao
            evento['valor'] = valor_float
            evento['quantidade_disponivel'] = quantidade_int
            
            if self.salvar_eventos():
                messagebox.showinfo("Sucesso", "Evento atualizado com sucesso! 🎉")
                self.criar_menu_principal()
        
        frame_botoes = tk.Frame(card_form, bg=self.cor_card, pady=20)
        frame_botoes.pack()
        
        btn_salvar = self.criar_botao_estilizado(
            frame_botoes,
            "💾 Salvar Alterações",
            salvar_edicao,
            self.cor_sucesso,
            largura=20
        )
        btn_salvar.pack(side=tk.LEFT, padx=10)
        
        btn_voltar = self.criar_botao_estilizado(
            frame_botoes,
            "← Voltar",
            self.criar_menu_principal,
            "#757575",
            largura=20
        )
        btn_voltar.pack(side=tk.LEFT, padx=10)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def tela_compra(self):
        """Tela para comprar ingressos"""
        self.limpar_tela()
        self.root.configure(bg=self.cor_fundo)
        
        # Header
        frame_header = tk.Frame(self.root, bg="#9C27B0", height=60)
        frame_header.pack(fill=tk.X)
        frame_header.pack_propagate(False)
        
        tk.Label(
            frame_header,
            text="🛒 Comprar Ingressos",
            font=("Segoe UI", 18, "bold"),
            bg="#9C27B0",
            fg="white"
        ).pack(pady=15)
        
        # Filtrar eventos com ingressos disponíveis
        eventos_disponiveis = [e for e in self.eventos if e['quantidade_disponivel'] > 0]
        
        if not eventos_disponiveis:
            frame_central = tk.Frame(self.root, bg=self.cor_fundo)
            frame_central.pack(expand=True, fill=tk.BOTH, pady=50)
            
            card_vazio = self.criar_card(frame_central)
            card_vazio.pack(padx=50, pady=30)
            
            tk.Label(
                card_vazio,
                text="😔 Nenhum evento com ingressos disponíveis no momento.",
                font=("Segoe UI", 14),
                bg=self.cor_card,
                fg=self.cor_texto_claro,
                pady=30
            ).pack()
            
            btn_voltar = self.criar_botao_estilizado(
                card_vazio,
                "← Voltar ao Menu",
                self.criar_menu_principal,
                "#757575",
                largura=20
            )
            btn_voltar.pack(pady=20)
            return
        
        # Frame principal
        canvas = tk.Canvas(self.root, bg=self.cor_fundo, highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.cor_fundo)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Card de seleção
        card_selecao = self.criar_card(scrollable_frame)
        card_selecao.pack(padx=50, pady=30, fill=tk.BOTH, expand=True)
        
        frame_conteudo = tk.Frame(card_selecao, bg=self.cor_card, padx=40, pady=30)
        frame_conteudo.pack()
        
        # Seleção de evento
        tk.Label(
            frame_conteudo,
            text="Selecione o evento:",
            font=("Segoe UI", 12, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(anchor="w", pady=(0, 10))
        
        var_evento = tk.StringVar()
        combo_eventos = ttk.Combobox(
            frame_conteudo,
            textvariable=var_evento,
            width=60,
            font=("Segoe UI", 11),
            state="readonly"
        )
        combo_eventos['values'] = [
            f"{e['nome']} - {e['data']} ({e['quantidade_disponivel']} disponíveis)"
            for e in eventos_disponiveis
        ]
        combo_eventos.pack(fill=tk.X, pady=(0, 20), ipady=8)
        
        # Frame para informações do evento selecionado
        frame_info = tk.Frame(frame_conteudo, bg=self.cor_card)
        frame_info.pack(fill=tk.X, pady=20)
        
        label_info = tk.Label(
            frame_info,
            text="Selecione um evento para ver os detalhes",
            font=("Segoe UI", 10),
            bg=self.cor_card,
            fg=self.cor_texto_claro,
            wraplength=700,
            justify=tk.LEFT
        )
        label_info.pack(anchor="w")
        
        # Quantidade de ingressos
        frame_quantidade = tk.Frame(frame_conteudo, bg=self.cor_card)
        frame_quantidade.pack(fill=tk.X, pady=20)
        
        tk.Label(
            frame_quantidade,
            text="Quantidade de ingressos:",
            font=("Segoe UI", 12, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(side=tk.LEFT, padx=(0, 15))
        
        var_quantidade = tk.StringVar(value="1")
        spinbox_quantidade = tk.Spinbox(
            frame_quantidade,
            from_=1,
            to=100,
            textvariable=var_quantidade,
            width=10,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            bd=5,
            bg="#F9F9F9"
        )
        spinbox_quantidade.pack(side=tk.LEFT)
        
        # Frame para resumo da compra
        frame_resumo = tk.Frame(frame_conteudo, bg="#F9F9F9", relief=tk.FLAT, bd=1)
        frame_resumo.pack(fill=tk.X, pady=20, padx=10)
        
        frame_resumo_content = tk.Frame(frame_resumo, bg="#F9F9F9", padx=20, pady=15)
        frame_resumo_content.pack()
        
        label_resumo = tk.Label(
            frame_resumo_content,
            text="Resumo da Compra",
            font=("Segoe UI", 13, "bold"),
            bg="#F9F9F9",
            fg=self.cor_texto
        )
        label_resumo.pack(anchor="w", pady=(0, 10))
        
        label_total = tk.Label(
            frame_resumo_content,
            text="Total: R$ 0,00",
            font=("Segoe UI", 16, "bold"),
            bg="#F9F9F9",
            fg=self.cor_sucesso
        )
        label_total.pack(anchor="w")
        
        # Frame para método de pagamento
        frame_pagamento = tk.Frame(frame_conteudo, bg=self.cor_card)
        frame_pagamento.pack(fill=tk.X, pady=20)
        
        tk.Label(
            frame_pagamento,
            text="Método de Pagamento:",
            font=("Segoe UI", 12, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(anchor="w", pady=(0, 10))
        
        var_metodo_pagamento = tk.StringVar(value="cartao")
        
        frame_opcoes_pagamento = tk.Frame(frame_pagamento, bg=self.cor_card)
        frame_opcoes_pagamento.pack(fill=tk.X)
        
        # Opção Cartão
        frame_cartao = tk.Frame(frame_opcoes_pagamento, bg="#F9F9F9", relief=tk.FLAT, bd=1)
        frame_cartao.pack(side=tk.LEFT, padx=(0, 10), fill=tk.BOTH, expand=True)
        
        radio_cartao = tk.Radiobutton(
            frame_cartao,
            text="💳 Cartão (Débito/Crédito)",
            variable=var_metodo_pagamento,
            value="cartao",
            font=("Segoe UI", 11),
            bg="#F9F9F9",
            fg=self.cor_texto,
            activebackground="#F9F9F9",
            activeforeground=self.cor_texto,
            selectcolor="#F9F9F9",
            cursor="hand2"
        )
        radio_cartao.pack(anchor="w", padx=15, pady=12)
        
        # Opção PIX
        frame_pix = tk.Frame(frame_opcoes_pagamento, bg="#F9F9F9", relief=tk.FLAT, bd=1)
        frame_pix.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        radio_pix = tk.Radiobutton(
            frame_pix,
            text="📱 PIX",
            variable=var_metodo_pagamento,
            value="pix",
            font=("Segoe UI", 11),
            bg="#F9F9F9",
            fg=self.cor_texto,
            activebackground="#F9F9F9",
            activeforeground=self.cor_texto,
            selectcolor="#F9F9F9",
            cursor="hand2"
        )
        radio_pix.pack(anchor="w", padx=15, pady=12)
        
        evento_selecionado = [None]
        
        def atualizar_info(event=None):
            selecionado = combo_eventos.current()
            if selecionado >= 0:
                evento = eventos_disponiveis[selecionado]
                evento_selecionado[0] = evento
                
                info_text = f"""
📅 Data: {evento['data']} às {evento['horario']}
📍 Local: {evento['local']}
📝 Descrição: {evento['descricao']}
💰 Valor unitário: R$ {evento['valor']:.2f}
🎫 Ingressos disponíveis: {evento['quantidade_disponivel']}
"""
                label_info.config(text=info_text.strip())
                
                # Atualizar quantidade máxima
                spinbox_quantidade.config(to=evento['quantidade_disponivel'])
                
                # Atualizar total
                try:
                    qtd = int(var_quantidade.get())
                    if qtd > evento['quantidade_disponivel']:
                        qtd = evento['quantidade_disponivel']
                        var_quantidade.set(str(qtd))
                    total = qtd * evento['valor']
                    label_total.config(text=f"Total: R$ {total:.2f}")
                except:
                    pass
        
        def atualizar_total(event=None):
            if evento_selecionado[0]:
                try:
                    qtd = int(var_quantidade.get())
                    evento = evento_selecionado[0]
                    if qtd > evento['quantidade_disponivel']:
                        qtd = evento['quantidade_disponivel']
                        var_quantidade.set(str(qtd))
                        messagebox.showwarning("Atenção", f"Quantidade máxima disponível: {evento['quantidade_disponivel']}")
                    elif qtd < 1:
                        qtd = 1
                        var_quantidade.set("1")
                    total = qtd * evento['valor']
                    label_total.config(text=f"Total: R$ {total:.2f}")
                except ValueError:
                    var_quantidade.set("1")
                    if evento_selecionado[0]:
                        total = evento_selecionado[0]['valor']
                        label_total.config(text=f"Total: R$ {total:.2f}")
        
        combo_eventos.bind('<<ComboboxSelected>>', atualizar_info)
        var_quantidade.trace('w', lambda *args: atualizar_total())
        spinbox_quantidade.bind('<KeyRelease>', atualizar_total)
        
        # Frame de botões
        frame_botoes = tk.Frame(card_selecao, bg=self.cor_card, pady=20)
        frame_botoes.pack()
        
        def finalizar_compra():
            selecionado = combo_eventos.current()
            if selecionado < 0:
                messagebox.showwarning("Atenção", "Por favor, selecione um evento!")
                return
            
            evento = eventos_disponiveis[selecionado]
            
            try:
                quantidade = int(var_quantidade.get())
            except ValueError:
                messagebox.showerror("Erro", "Por favor, informe uma quantidade válida!")
                return
            
            if quantidade < 1:
                messagebox.showwarning("Atenção", "A quantidade deve ser pelo menos 1!")
                return
            
            if quantidade > evento['quantidade_disponivel']:
                messagebox.showerror("Erro", f"Quantidade indisponível! Apenas {evento['quantidade_disponivel']} ingressos disponíveis.")
                return
            
            metodo_pagamento = var_metodo_pagamento.get()
            metodo_texto = "Cartão (Débito/Crédito)" if metodo_pagamento == "cartao" else "PIX"
            
            # Confirmar compra
            total = quantidade * evento['valor']
            confirmacao = messagebox.askyesno(
                "Confirmar Compra",
                f"Confirma a compra de {quantidade} ingresso(s) para o evento:\n\n"
                f"{evento['nome']}\n"
                f"Data: {evento['data']} às {evento['horario']}\n"
                f"Local: {evento['local']}\n"
                f"Método de Pagamento: {metodo_texto}\n\n"
                f"Total: R$ {total:.2f}"
            )
            
            if confirmacao:
                # Atualizar quantidade disponível
                evento['quantidade_disponivel'] -= quantidade
                
                # Salvar compra
                compras = self.carregar_compras()
                nova_compra = {
                    "id": len(compras) + 1,
                    "id_evento": evento['id'],
                    "nome_evento": evento['nome'],
                    "comprador": self.usuario_logado['nome'],
                    "email_comprador": self.usuario_logado['email'],
                    "quantidade": quantidade,
                    "valor_unitario": evento['valor'],
                    "valor_total": total,
                    "metodo_pagamento": metodo_texto,
                    "data_compra": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }
                compras.append(nova_compra)
                
                if self.salvar_eventos() and self.salvar_compras(compras):
                    mensagem_sucesso = f"Compra realizada com sucesso!\n\n"
                    mensagem_sucesso += f"Evento: {evento['nome']}\n"
                    mensagem_sucesso += f"Quantidade: {quantidade} ingresso(s)\n"
                    mensagem_sucesso += f"Método de Pagamento: {metodo_texto}\n"
                    mensagem_sucesso += f"Total pago: R$ {total:.2f}\n\n"
                    if metodo_pagamento == "pix":
                        mensagem_sucesso += "📱 Pagamento via PIX processado!\n"
                    else:
                        mensagem_sucesso += "💳 Pagamento via Cartão processado!\n"
                    mensagem_sucesso += "\nObrigado pela sua compra!"
                    
                    messagebox.showinfo("Compra Realizada! 🎉", mensagem_sucesso)
                    self.criar_menu_principal()
        
        btn_comprar = self.criar_botao_estilizado(
            frame_botoes,
            "💳 Finalizar Compra",
            finalizar_compra,
            "#9C27B0",
            largura=25
        )
        btn_comprar.pack(side=tk.LEFT, padx=10)
        
        btn_voltar = self.criar_botao_estilizado(
            frame_botoes,
            "← Voltar",
            self.criar_menu_principal,
            "#757575",
            largura=25
        )
        btn_voltar.pack(side=tk.LEFT, padx=10)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

def main():
    root = tk.Tk()
    app = SistemaIngressos(root)
    root.mainloop()

if __name__ == "__main__":
    main()
