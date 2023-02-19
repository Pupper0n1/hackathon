from django.views.generic import TemplateView

class GalleryPage(TemplateView):
    template_name = 'gallery.html'

class GoodbyePage(TemplateView):
    template_name = 'goodbye.html'

class HomePage(TemplateView):
    template_name = 'index.html'
