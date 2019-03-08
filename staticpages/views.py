import os
import markdown
from markdown.extensions.toc import TocExtension

from django.conf import settings
from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import TemplateView


class StaticPageView(TemplateView):
    template_name = settings.STATICPAGES_TEMPLATE_NAME
    md_file = 'language-learning.md'
    
    def get_context_data(self, **kwargs):
        # load markdown file
        f = open(os.path.join(settings.STATICPAGES_CONTENT_DIR, self.md_file))
        file_content = f.read()
        f.close()
        
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        body = md.convert(file_content)
        toc = md.toc

        context = super().get_context_data(**kwargs)
        context['body'] = body
        context['toc'] = toc
        
        return context

