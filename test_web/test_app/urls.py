from django.urls import path
from test_app.views import home , aboutUs, contact_us

urlpatterns = [
    path('', home, name='home'),  
    path('aboutUs' ,aboutUs , name='aboutUs'),
    path('contact_us' ,contact_us, name='contact_us')
]
