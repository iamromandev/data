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

# dev
.PHONY: up-dev
up-dev:
	docker-compose -f docker-compose.dev.yml up -d --build

.PHONY: down-dev
down-dev:
	docker-compose -f docker-compose.dev.yml down

.PHONY: restart-dev
restart-dev:
	make down-dev
	make up-dev

.PHONY: clean
clean:
	docker system prune -a --force
	docker volume prune --force

