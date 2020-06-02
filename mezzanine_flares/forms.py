from django.forms import ModelForm, ModelChoiceField
#from sciesmex_records.models import Report, Slide, Report_Slide
from mezzanine_flares.models import PlotXRay
#from wget import download
#from astropy.io.votable.tree import Field
#from sciesmex_setings.models import Meeting, Participant, Contribution
#from django.contrib.auth.models import User

class PlotXRay_Form(ModelForm):
     class Meta:
        model = PlotXRay
        fields = ['satellite','flux_init','flux_finish','initial_date','end_date']

