fmt:
	black -S -l 120 src scripts
dep:
	pip install -U -r requirements.txt
dep-dev:
	pip install -U -r requirements_dev.txt
