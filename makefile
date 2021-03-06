ARGUMENTS = $(filter-out $@,$(MAKECMDGOALS)) $(filter-out --,$(MAKEFLAGS))

manage_caseworker:
	PIPENV_DOTENV_LOCATION=caseworker.env pipenv run ./manage.py $(ARGUMENTS)

manage_exporter:
	PIPENV_DOTENV_LOCATION=exporter.env pipenv run ./manage.py $(ARGUMENTS)

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

run_caseworker:
	PIPENV_DOTENV_LOCATION=caseworker.env pipenv run ./manage.py collectstatic --no-input && PIPENV_DOTENV_LOCATION=caseworker.env pipenv run ./manage.py runserver localhost:8200

run_exporter:
	PIPENV_DOTENV_LOCATION=exporter.env pipenv run ./manage.py collectstatic --no-input && PIPENV_DOTENV_LOCATION=exporter.env pipenv run ./manage.py runserver localhost:8300

run_unit_tests_caseworker:
	PIPENV_DOTENV_LOCATION=caseworker.env pipenv run pytest unit_tests/caseworker --cov=. --cov-config=.coveragerc --cov-report=html -vv -x $(ARGUMENTS)

run_unit_tests_exporter:
	PIPENV_DOTENV_LOCATION=exporter.env pipenv run pytest unit_tests/exporter --cov=. --cov-config=.coveragerc --cov-report=html -vv -x $(ARGUMENTS)

secrets:
	cp example.caseworker.env caseworker.env
	cp example.exporter.env exporter.env
