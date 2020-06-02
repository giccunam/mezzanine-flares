from django.views.generic import View
from django.shortcuts import render
from mezzanine_flares.models import PlotXRay
from mezzanine_flares.forms import PlotXRay_Form
from django.http import HttpResponseRedirect


class Service_Plot_View(View):
    initial={'key':'value'}
    form_class=PlotXRay_Form
    template_name = 'mezzanine_flares/service-plot.html'

    def get(self, request, *args, **kwargs):
        #var1 = self.kwargs['var1']
        form=self.form_class(initial=self.initial)        
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        
        if 'cancel_page_button' in request.POST:
            return HttpResponseRedirect('/')

        if 'execute_page_button' in request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                plotXRay = form.save()
                print("output: "+str(plotXRay.flux_finish))
                #GENERAR LA IMAGEN QUE TENEMOS ALMACENADA EN LA DB CON LA INFO EN plotXRay
                PATH='/home/vdelaluz/git/running/static/flares/'
                with open('/home/vdelaluz/credentials/db.json') as json_file:
                    config = json.load(json_file)
                x = []
                y = []

                try:
                    cnx = mysql.connector.connect(**config)
                    cursor = cnx.cursor()
                    query = ("SELECT time_tag, flux FROM FluxHighEnergy WHERE flux > 0.00000002 ORDER BY time_tag")
                    #data_query = (mydate, flux, satellite)
                    #print(mydate)
                    cursor.execute(query)#,data_query)
                    for (time_tag, flux) in cursor:
                        print(f"{time_tag}\t{flux}")
                        x.append(time_tag)
                        y.append(flux)
        
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Something is wrong with your user name or password")
                    elif err.errno == errorcode.ER_BAD_DB_ERROR:
                        print("Database does not exist")
                    else:
                        print(err)
                else:
                    cnx.close()


                fig, ax = plt.subplots()
                ax.set(xlabel='time', ylabel='flux',
                       title='view2D')
                #plt.axis([x_A, x_B,  y_A, y_B])
                ax.grid()

                ax.plot(x, y)
                fig.savefig(PATH+"/last_flux.png")
                urlpic= PATH+"/last_flux.png"
                return render(request, 'myplugin/plot.html' , {'urlpic': urlpic})
            else:
                print('form not valid')
                return render(request, self.template_name, {'form': form})

        return HttpResponseRedirect('/')
  
    #@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Service_Plot_View, self).dispatch(*args, **kwargs)




class MyPlugin_View(View):
    initial={'kay':'value'}
    #form_class=Paciente_Form
    template_name = 'myplugin/myplugin-plot.html'

    def get(self, request, *args, **kwargs):
        #var1 = self.kwargs['var1']  
        return render(request, self.template_name)

    #@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyPlugin_View, self).dispatch(*args, **kwargs)

    
