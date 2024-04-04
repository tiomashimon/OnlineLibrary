define USAGE
Commands:
	make app					Up application and database infrastructure
	make app-logs				Follow the logs in app container
	make app-down				Down application and all infrastructure
    make container-shell		Go to container shell
    make migrate				Apply all made migrations
    make makemigrations			Make migrations to models
    make createsuperuser		Create admin user
    make collectstatic			Collect static

endef


.PHONY: app
app:
	docker compose -f docker-compose.yml --env-file .env up --build -d

.PHONY: app-logs
app-logs:
	docker logs main-app -f

.PHONY: app-down
app-down:
	docker compose -f docker-compose.yml --env-file .env down

.PHONY: container-shell
container-shell:
	docker exec -it main-app ash


.PHONY: migrate
migrate:
	docker exec -it main-app python manage.py migrate

.PHONY: makemigrations
makemigrations:
	docker exec -it main-app python manage.py makemigrations

.PHONY: createsuperuser
createsuperuser:
	docker exec -it main-app python manage.py createsuperuser

.PHONY: collectstatic
collectstatic:
	docker exec -it main-app python manage.py collectstatic

