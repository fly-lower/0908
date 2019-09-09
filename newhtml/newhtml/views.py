from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render,render_to_response


def index(request):
    return HttpResponse('Welcom !')

def about(request):
    return  HttpResponse('About Page')

def game(request):
    gamelist={'英雄联盟':'lol.jpg','黑暗之魂':'dks.jpg','上古卷轴':'ldc.jpg','魔兽世界':'wow.jpg','Dota2':'dota.jpg'}
    return render(request,'game.html',locals())

