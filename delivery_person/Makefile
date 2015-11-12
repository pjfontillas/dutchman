PIP_OPTS ?= --upgrade

env:
	virtualenv -p `which python2.7` env

deps: env
	env/bin/pip install -r requirements/base.txt $(PIP_OPTS)

start:
	env/bin/python delivery.py

clean:
	rm -rf env

.PHONY: deps start clean
