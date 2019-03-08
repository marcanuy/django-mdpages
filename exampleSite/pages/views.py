from mdpages.views import MdPageView

class AboutView(MdPageView):
    md_file = 'about.md'
    
    extra_context = {
        'title': 'About Page',
        'description': 'This is my About Page meta description.'
    }
