up:
	docker-compose up --build -d app

stop:
	docker-compose stop

push:
	docker-compose build
	docker tag audioplayer-app n1ktrnv/audioplayer:latest
	docker push n1ktrnv/audioplayer