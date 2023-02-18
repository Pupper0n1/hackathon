from django.views.generic import TemplateView

class GalleryPage(TemplateView):
    templateName = 'gallery.html'

class GoodbyePage(TemplateView):
    template_name = 'goodbye.html'

class HomePage(TemplateView):
    template_name = 'index.html'
