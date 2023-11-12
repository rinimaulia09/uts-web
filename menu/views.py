from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def menu(request):
  template = loader.get_template('program.html')
  return HttpResponse(template.render())
