from django.shortcuts import render
from APP.models import Users
from APP.models import Graph
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    return render(request,'index.html')

def dataview(request):
    return render(request,'templates/base.html')

# def datasummary(request):


# 这里要用class如果要用template
# class chartview(TemplateView):
#     template_name = 'data/Fe2O3(test).html'
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#
#         # try except block needed in case none-existence
#         # context['qs']
#         entry = Graph.objects.get(name = 'Fe2O3')
#
#
#         return entry
class chartview(TemplateView):
    template_name = 'data/Fe2O3(test).html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        # try except block needed in case none-existence
        # context['qs']
        entry = Graph.objects.get(name = 'Fe2O3')
        txt_file = entry.data_text;
        list_x = []
        list_y = []
        fdata = txt_file.read()
        print("!!!!!!!!!!!!",type(fdata))
        list_xy = fdata.decode("utf-8").split("\r")
        for i in list_xy:
            pair = i.split("\t")
            list_x.append(float(pair[0]))
            list_y.append(float(pair[1]))
        myPair = zip(list_x,list_y)
        context = {'object':entry,'p':myPair}


        return context
