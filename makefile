.PHONY: start

build:
	docker build -t cmd-tool .
	
start:
	docker run -t cmd-tool .