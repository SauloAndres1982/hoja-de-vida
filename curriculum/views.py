from django.views.generic import TemplateView

# Create your views here.
class PerfilView(TemplateView):
    template_name = 'curriculum/perfil.html'