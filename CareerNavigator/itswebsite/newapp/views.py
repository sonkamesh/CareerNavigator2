from django.shortcuts import render
from .models import Professions
from django.views.generic import DetailView


def newapp_home(request):
    profs = Professions.objects.order_by('-date')
    return render(request, 'newapp/newapp_home.html', {'profs':profs})


class NewappDetailView(DetailView):
    model = Professions
    template_name = 'newapp/details_view.html'
    context_object_name = 'prof'
