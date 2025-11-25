from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
def testing(request):
  template = loader.get_template('template.html')
  members = Member.objects.all().values()
  columna = Member.objects.all().values("video_game_favorite") 
  mydata = Member.objects.filter(Q(firstname='ranni') | Q(firstname='tilin')).values()
  mydata = Member.objects.filter(lastname__icontains='caria').values()
  mydata = Member.objects.filter(id__gte=3).values()
  mydata = Member.objects.all().order_by('firstname').values()
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'members': members,
    'columna': columna,
    'mydata': mydata,  # Agregadas las variables al contexto
  }
  return HttpResponse(template.render(context, request))