git:
	@git config --global user.email ""
	@git config --global user.name "hick-hpe"
	@echo "----------------------"
	@echo "Autenticado!!!"
	@echo "----------------------"

start:
	@echo "Inicializando containers Docker..."
	@docker compose up --build