include .env
export $(shell sed 's/=.*//' .env)

up:
	docker compose -f compose/base.yml up -d

down:
	docker compose -f compose/base.yml down -v

logs:
	docker compose -f compose/base.yml logs -f --tail=200

init-minio:
	@echo "Criando bucket $(S3_BUCKET)"
	docker exec -it $$(docker ps -qf name=minio) mc alias set local http://localhost:9000 $(MINIO_ROOT_USER) $(MINIO_ROOT_PASSWORD) || true
	docker exec -it $$(docker ps -qf name=minio) mc mb -p local/$(S3_BUCKET) || true

seed:
	python scripts/seed_landing.py  # opcional para subir CSV fake no s3

e2e:
	airflow dags trigger lake_unimed_e2e