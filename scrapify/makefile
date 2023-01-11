# local
.PHONY: build
build:
	docker-compose -f docker-compose.yml build

.PHONY: up
up:
	docker-compose -f docker-compose.yml up -d

.PHONY: down
down:
	docker-compose -f docker-compose.yml down

.PHONY: restart
restart:
	make down
	make up

# dev
.PHONY: build-dev
build-dev:
	docker-compose -f docker-compose.dev.yml build

.PHONY: up-dev
up-dev:
	docker-compose -f docker-compose.dev.yml up -d

.PHONY: down-dev
down-dev:
	docker-compose -f docker-compose.dev.yml down

.PHONY: restart-dev
restart-dev:
	make down-dev
	make up-dev

# system
.PHONY: clean
clean:
	docker system prune -a --force
	docker volume prune --force

