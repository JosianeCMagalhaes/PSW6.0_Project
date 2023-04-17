from django.shortcuts import render,HttpResponse,redirect
from eventos.models import Certificado

def meus_certificados(request):
    certificados = Certificado.objects.filter(participante=request.user)
    return render(request,'meus_certificados.html',{'certificados':certificados})