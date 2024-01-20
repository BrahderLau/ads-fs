from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
 
import numpy as np
import pandas as pd
import matplotlib as pl
pl.use('Agg') #Agg is a non-interactive backend, only save to files
import matplotlib.pyplot as plt
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'charts/index.html'

    def get(self, request, **kwargs):
        return super().get(request, **kwargs)
 
class Api(TemplateView):
    # Create your views here.
    def getNums(request):
        n = np.array([2,3,4])
        name1 = "name-1" + str(n[1])
        return HttpResponse('{"name:":'+name1+',"age":31,"city":"New York"}')
 
    def getAvg(request):
        s1=request.GET.get("val","")
        print (s1)
        if len(s1)==0:
            return HttpResponse("none")
        l1=s1.split(',')
        ar=np.array(l1,dtype=int)
 
        return HttpResponse(str(np.average(ar)))
 
    def getGraph(request):
        x = np.arange(0,2 * np.pi, 0.01) # starts from 0, ends till 6.28 and adds by 0.01
        s = np.cos(x)**2 # ** is the operator for "power of".
        plt.plot(x,s)
 
        plt.xlabel('xlabel(X)')
        plt.ylabel('ylabel(y)')
        plt.title('Basic Graph!')
        plt.grid(True)
 
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response
 
    def getData(request):
        samp = np.random.randint(100,600,size=(4,5)) #size means the array size
        df = pd.DataFrame(samp, index=['alex','danny','lina','david'],columns=['Jan','Feb','Mar','Apr','May'])
        return HttpResponse(df.to_html(classes='table table-bordered'))
 