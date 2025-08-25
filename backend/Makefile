help:
	@echo
	@echo "##### BACKEND COMMANDS #####"
	@echo
	@echo "install                            -- install backend dependencies"
	@echo "lint                               -- lint backend"
	@echo "lint-fix                           -- lint fix backend"
	@echo "mypy                               -- type check backend"
	@echo "format                             -- format backend"
	@echo "dev                                -- start backend development server"
	@echo "shell                              -- start django shell"
	@echo "migrate                            -- apply database migrations"
	@echo "collect-static                     -- collect static files"
	@echo "seed-dev-data                      -- seed dev data"
	@echo "generate-configs                   -- generate nginx and gunicorn configs"
	@echo "copy-configs                       -- copy configs to respective directory"
	@echo "remove-configs                     -- remove generated configs"



# Backend

install:
	uv sync --frozen

lint:
	uv run ruff check ./backend ./scripts

lint-fix:
	uv run ruff check --fix ./backend ./scripts

mypy:
	MYPYPATH=$$(pwd)/backend:$$(pwd)/scripts uv run mypy ./backend ./scripts

format:
	uv run ruff format ./backend ./scripts

dev:
	cd backend && uv run gunicorn  ./backend./core.wsgi:application

shell:
	uv run python backend/manage.py shell

migrate:
	uv run python backend/manage.py migrate

collect-static:
	uv run python backend/manage.py collectstatic --noinput

generate-configs:
	uv run python scripts/generate_configs.py

copy-configs: generate-configs
	sudo cp ./nginx.conf /etc/nginx/nginx.conf
	sudo cp ./gunicorn.service /etc/systemd/system/gunicorn.service

remove-configs:
	rm nginx.conf gunicorn.service

seed-dev-data:
	uv run python backend/manage.py seed_dev_data

