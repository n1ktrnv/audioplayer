up:
	docker-compose up --build -d app-service

stop:
	docker-compose stop

push:
	docker-compose build
	docker tag audioplayer-app n1ktrnv/audioplayer:latest
	docker push n1ktrnv/audioplayer

check:
	docker-compose up --build -d checks-service