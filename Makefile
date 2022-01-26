all:
	docker build -t github.com/giuscri/morris .
	docker run --rm github.com/giuscri/morris
