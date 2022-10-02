from django.shortcuts import render
from travelapp.models import Destination

def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})
