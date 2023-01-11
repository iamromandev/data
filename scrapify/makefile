.PHONY: up
up:
	docker-compose up -d --build

.PHONY: down
down:
	docker-compose down

.PHONY: restart
restart:
	make down
	make up

.PHONY: clean
clean:
	docker system prune -a --force
	docker volume prune --force

