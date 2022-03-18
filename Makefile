

.PHONY: install
install: .venv
	. .venv/bin/activate; pip install ./geoserver

.venv: .venv/_installed

db_layers: .venv
	. .venv/bin/activate; scripts/db_layers.py

.venv/_installed: requirements.txt
	test -d .venv || python3 -m venv .venv
	. .venv/bin/activate; pip install -r requirements.txt
	touch .venv/_installed