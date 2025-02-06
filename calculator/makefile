.PHONY: start

build:
	docker build -t cmd-tool .
	
start:
	docker run -t cmd-tool .

remove:
	@echo "Stopping and removing all containers for cmd-tool..."
	@docker ps -a -q --filter "ancestor=cmd-tool" | xargs -r docker stop | xargs -r docker rm
	@echo "Removing the cmd-tool image..."
	@docker rmi -f cmd-tool