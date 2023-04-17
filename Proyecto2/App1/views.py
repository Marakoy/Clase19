from django.shortcuts import render
from App1.models import Curso
from django.http import HttpResponse

def curso(self):
    curso = Curso(nombre="vista",curso=19673)
    curso.save()
    texto= f"----> Asignatura: {curso.nombre}, curso: {curso.curso}"
    return HttpResponse(texto)

# Create your views here.
