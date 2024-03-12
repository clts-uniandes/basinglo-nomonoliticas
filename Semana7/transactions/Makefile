DOCKER_COMPOSE_LOCAL=docker-compose.yml

# ====================================================================================
# D O C K E R  C O M M A N D S
.PHONY: run
run:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) up

.PHONY: build
build:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) build --no-cache

.PHONY: stop
stop:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) stop

.PHONY: down
down:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) down

.PHONY: clean
clean:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) down -v --remove-orphans

.PHONY: clean_all
clean_all:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) down -v --remove-orphans --rmi all

.PHONY: run_users
run_users:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) up users
