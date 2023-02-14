.PHONY: build build-docker

DOCKER_IMAGE=ghcr.io/piotrkilczuk/simrail-skrj:latest

build:
	rm -v build/*.pdf
	libreoffice --headless --convert-to pdf --outdir build/ src/templates/*.fodt

build-docker:
	docker run -v `pwd`:/workdir $(DOCKER_IMAGE)

docker-image:
	docker build --pull . -t $(DOCKER_IMAGE)
	docker push $(DOCKER_IMAGE)
