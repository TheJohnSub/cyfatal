from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render


from .models import Incident, IncidentSource


def index(request):
	latest_incident_list = Incident.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'latest_incident_list': latest_incident_list,
	}
	return HttpResponse(template.render(context, request))

#def detail(request, incident_id):
#    return HttpResponse("You're looking at incident %s." % incident_id) 
def detail(request, incident_id):
	try:
		incident = Incident.objects.get(pk=incident_id)
		incident_sources = IncidentSource.objects.filter(Incident=incident)
		template = loader.get_template('details.html')
		context = {
			'incident': incident,
			'incident_sources': incident_sources
		}
	except Incident.DoesNotExist:
		raise Http404("Data does not exist")
	return HttpResponse(template.render(context, request))
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, 'incidents/detail.html', {'incident': incident})  

def about_page_view(request):
	return render(request, 'about.html')

def contact_page_view(request):
	return render(request, 'contact.html')