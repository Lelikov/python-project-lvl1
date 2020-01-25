install:
	@poetry install

lint:
	@poetry run flake8 --ignore E305 brain_games
