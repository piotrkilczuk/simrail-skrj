.PHONY: build build-docker

build:
	rm -v build/*.pdf
	libreoffice --headless --convert-to pdf --outdir build/ src/templates/*.fodt

build-docker:
	docker build . -t skrj-build
	docker run -v `pwd`:/workdir skrj-build
