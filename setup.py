import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mdpages',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to generate pages from files.',
    long_description=README,
    url='https://github.com/marcanuy/django-mdpages/',
    author='Marcelo Canina',
    author_email='me@marcanuy.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='django static',
    project_urls={
        #'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Source': 'https://github.com/marcanuy/django-mdpages/',
        'Tracker': 'https://github.com/marcanuy/django-mdpages/issues',
    },
    install_requires=[
        'Django>=2.1',
        'Markdown'
    ],

)
