from django.urls import path, include
from .views import LEDControlView

urlpatterns = [
    path('control/', LEDControlView.as_view(), name='led-control'),
]
