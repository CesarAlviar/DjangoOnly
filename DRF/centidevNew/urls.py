from django.urls import path
from django.views.generic import TemplateView

app_name = 'centidevNew'

urlpatterns = [
    path('', TemplateView.as_view(template_name="centidevNew/index.html")),
]
