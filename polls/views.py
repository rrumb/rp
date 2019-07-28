from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Elevator


#def index(request):
#    latest_list = Elevator.objects.order_by('-comm_number')[:5]
#    output=''
#    for q in latest_list:
#        output = str(q.comm_number)
#        output = output + '  = ' + str(q.status_control)
#        output = output + '/'  + str(q.status_connection) + '<br>'
#    return HttpResponse(output)


def index(request):
    latest_list = Elevator.objects.order_by('-comm_number')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_list': latest_list,
    }
    return render(request, 'polls/index.html', context)


def elevator_check(request, elevator):
    try:
        q = Elevator.objects.get(comm_number=elevator)
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except Elevator.DoesNotExist:
        raise Http404("Elevator does not exist")
    return render(request, 'polls/detail.html', {'Elevator': q})

    
def status_update(request, elevator, status):
    q = Elevator.objects.get(comm_number=elevator)
    q.status_control=status
    q.save()
    output=str(elevator)+'ok'+str(status)
    return HttpResponse(output)
