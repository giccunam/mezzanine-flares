from django.conf.urls import url, include#, patterns  
#from django.conf.urls.defaults import *
from mezzanine_flares.views import MyPlugin_View, Service_Plot_View
#import views

urlpatterns = [
    url(r'^flares', MyPlugin_View.as_view()),
    url(r'^service-plot', Service_Plot_View.as_view()), 
]
