from model.sistema import Sistema

if __name__ == "__main__":
    try:
        sistema = Sistema()
        sistema.inicializar_dados()
        sistema.menu_principal()
    except Exception as e:
        print(f"Erro fatal no sistema: {e}")
        input("Pressione Enter para sair...")