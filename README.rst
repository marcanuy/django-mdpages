=====
StaticPages
=====

Staticpages is a simple Django app to generate pages from files.
You can create about pages or a blog based in static files without
touching database.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "staticpages" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'staticpages',
    ]

2. Set the content directory where files will be located

3. Include the staticpages URLconf in your project urls.py like this::

    path('', include('polls.urls')),

