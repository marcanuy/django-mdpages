MdPages - Markdown Pages
========================

Mdpages is a simple Django app to generate pages from Markdown files.

Pages also can have a Table of Content automatically generated based
on headings.

Quick start
-----------

Supposing you want to create an **About** page, having the markdown
file at `/pages/content/about.md`.

1. Add "mdpages" to your INSTALLED_APPS setting like this:

.. code:: python

   INSTALLED_APPS = [
	   ...
	   'mdpages',
   ]

2. Set the location of the directory that will contain the Markdown
   files in settings with `MDPAGES_CONTENT_DIR`:

.. code:: python

   MDPAGES_CONTENT_DIR = '{}/pages/content/'.format(BASE_DIR)

3. Add the template that will contain the Markdown generated content,
   you will have two variables available: `body` and `toc` (for the
   table of contents), for example create a template
   `/templates/mdpages/page.html` with contents like:

.. code:: python

   {% extends "base.html" %}

   {% block title %}{{title}}{%endblock%}
   {% block description %}{{description}}{%endblock%}

   {% block content %}
   <div class="container">
        {{ toc|safe }}
	<hr>
	{{ body|safe }}
   </div>
   {% endblock %}

And add the template path to settings `MDPAGES_TEMPLATE_NAME`:

.. code:: python
	
   MDPAGES_TEMPLATE_NAME = 'mdpages/page.html'

4. Create a view using `staticages.views.MdPageView` specifying
   the name of the Markdown file `md_file` and the `template_name`:

.. code:: python

   from mdpages.views import MdPageView

   class AboutView(MdPageView):
	   md_file = 'language-learning.md'

	   # any kind of extra content used in your template
	   extra_context = {
		   'title': 'About page',
		   'description': 'This is the about page of the site.'
	   }

5. Use it in your `urls.py`:

.. code:: python

   from .views import AboutView

   urlpatterns = [
	   path('about', AboutView.as_view()),	
   ]

Reference
---------

- Markdown library https://python-markdown.github.io/reference/
