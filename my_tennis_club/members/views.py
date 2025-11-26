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
  nombre = Member.objects.filter(firstname__icontains='ranni').values()
  mydata = Member.objects.filter(Q(firstname='ranni') | Q(firstname='tilin')).values()
  apellido = Member.objects.filter(lastname__icontains='caria').values()
  mayor_3 = Member.objects.filter(id__gte=22).values()
  ordenado = Member.objects.all().order_by('firstname').values()
  filtrar_con_in = Member.objects.filter(firstname__in=['ranni', 'davi', 'ana']).values()
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'members': members,
    'columna': columna,
    'mydata': mydata,
    'apellido': apellido,
    'mayor_3': mayor_3,
    'ordenado': ordenado,
    'nombre': nombre,
    'filtrar_con_in': filtrar_con_in,
  }
  return HttpResponse(template.render(context, request))