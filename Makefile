PYTHON:=python3

# building a source distribution
build-package:
	# creates a directory called dist and builds your new package, django-mdpages-0.1.tar.gz.
	$(PYTHON) setup.py sdist

# Building a wheel
build-wheel:
	$(PYTHON) setup.py bdist_wheel

1-build-distribution:
	$(PYTHON) setup.py sdist bdist_wheel
2-test-with-testpypi:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
3-upload-to-pypi:
	twine upload dist/*
