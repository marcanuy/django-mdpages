=====
StaticPages
=====

Staticpages is a simple Django app to generate pages from Markdown files.

Pages also can have a Table of Content automatically generated based
on headings.

Quick start
-----------

Supposing you want to create an **About** page, having the markdown
file at `/pages/content/about.md`.

1. Add "staticpages" to your INSTALLED_APPS setting like this:

		INSTALLED_APPS = [
			...
			'staticpages',
		]

2. Set the location of the directory that will contain the Markdown
   files in settings with `STATICPAGES_CONTENT_DIR`:
   
		STATICPAGES_CONTENT_DIR = '{}/pages/content/'.format(BASE_DIR)

3. Add the template that will contain the Markdown generated content,
   you will have two variables available: `body` and `toc` (for the
   table of contents), for example create a template
   `/templates/staticpages/page.html` with contents like:
   
		{% extends "base.html" %}

		{% block title %}{{title}}{%endblock%}
		{% block description %}{{description}}{%endblock%}

		{% block content %}
		<div class="container">
			{{ toc|safe }}
			<hr>
			{{ body|safe }}

		{% endblock %}

	And add the templatep path to settings
    `STATICPAGES_TEMPLATE_NAME`:
	
	    STATICPAGES_TEMPLATE_NAME = 'staticpages/page.html'

4. Create a view using `staticages.views.StaticPageView` specifying
   the name of the Markdown file `md_file` and the `template_name`:

		from staticpages.views import StaticPageView

		class AboutView(StaticPageView):
			md_file = 'language-learning.md'

			# any kind of extra content used in your template
			extra_context = {
				'title': 'About page',
				'description': 'This is the about page of the site.'
			}

5. Use it in your `urls.py`:

		 from .views import AboutView

		 urlpatterns = [
			 path('about', AboutView.as_view()),	
		 ]

