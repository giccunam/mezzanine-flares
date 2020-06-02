#Revision 20200507
#Autor: Dr. Victor De la Luz


#from django.db import models
#from django.contrib.auth.models import User
#from django.core.files import File 
#from thumbs import ImageWithThumbsField
#from mezzanine.utils.models import upload_to
#from wget import download
from django.apps.config import MODELS_MODULE_NAME
#from django_countries.fields import CountryField


from django.db import models
from django.contrib.auth.models import User
#from django.core.files import File 
#from thumbs import ImageWithThumbsField
#from mezzanine.utils.models import upload_to
#from wget import download
from django.apps.config import MODELS_MODULE_NAME
#from django_countries.fields import CountryField

class PlotXRay(models.Model):    
    SATELLITE_CHOICES = (
        ('1', 'GOES 15'),
        ('2', 'GOES 16'),
    )
    BAND_CHOICES = (
        ('1', 'Soft X-Ray'),
        ('2', 'Hard X-Ray'),
    )
    satellite = models.CharField(max_length=16, choices=SATELLITE_CHOICES)
    band = models.CharField(max_length=16, choices=BAND_CHOICES)
    flux_init = models.FloatField(blank=True,null=True,default=0.0)
    flux_finish = models.FloatField(blank=True,null=True,default=10.0)
    initial_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
