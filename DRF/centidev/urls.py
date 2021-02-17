from django.urls import path
from django.views.generic import TemplateView

app_name = 'centidev'

urlpatterns = [
    path('', TemplateView.as_view(template_name="centidev/index.html")),
]
