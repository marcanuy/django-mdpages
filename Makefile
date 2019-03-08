# building a source distribution
build-package:
	# creates a directory called dist and builds your new package, django-staticpages-0.1.tar.gz.
	python setup.py sdist

# Building a wheel
build-wheel:
	python setup.py bdist_wheel

1-build-distribution:
	python setup.py sdist bdist_wheel
2-test-with-testpypi:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
3-upload-to-pypi:
	twine upload dist/*
