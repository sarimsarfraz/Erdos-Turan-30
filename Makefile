.PHONY: core all clean

core:
	python3 run_all.py --core

all:
	python3 run_all.py --all

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
