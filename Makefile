NAME := swag
.PHONY: build run

build:
	docker build -t $(NAME) .

run:
	docker run -d -p 5000:8080 --name $(NAME) $(NAME)

devrun:
	docker run -d -p 5000:8080 --name $(NAME) -v $(PWD):/app $(NAME)

sh:
	docker run -it --rm -p 5000:8080 --name $(NAME) -v $(PWD):/app $(NAME) sh
