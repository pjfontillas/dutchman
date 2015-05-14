PIP_OPTS ?= --upgrade

env:
	virtualenv -p `which python2.7` env

deps: env
	env/bin/pip install -r requirements/setuptools.txt $(PIP_OPTS)
	env/bin/pip install -r requirements/base.txt $(PIP_OPTS)
	env/bin/pip install -r requirements/dev.txt $(PIP_OPTS)

start:
	env/bin/python homer.py

clean:
	rm -rf env

.PHONY: deps start clean
