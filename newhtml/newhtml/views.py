from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render,render_to_response


def index(request):
    return HttpResponse('Welcom !')

def about(request):
    return  HttpResponse('About Page')

def game(request,age):
    # gamelist={'aa':'lol.jpg','黑暗之魂':'dks.jpg','上古卷轴':'ldc.jpg','魔兽世界':'wow.jpg','Dota2':'dota.jpg'}
    gamelist=[{'name':'英雄联盟','agelimit':5, 'img':'lol.jpg'},
              {'name':'Dota2','agelimit':16, 'img':'dota.jmp.jpg'},
              {'name':'上古卷轴','agelimit':18, 'img':'lds.jpg'},
              {'name':'魔兽世界','agelimit':30, 'img':'wow.jpg'},
              {'name':'黑暗之魂','agelimit':40, 'img':'dks.jpg'}]
    palyer_age = int(age)
    return render(request,'game.html',locals())

def gethtml(request):
    html="""
    <html>
        <head>
            <title>原始网页</title>
        </head>
        <body>
            <h1>第一个标签h1</h1>
            <h2>第二个标签{{name}}</h2>
            <a href ='https://baidu.com/s?wd=风景'>风景</a>
            <p>{{context}}</p>
        </body>
    </html>"""
    template_obj = Template(html)
    params = dict(name='刘彻',context='500多岁')
    content_obj = Context(params)
    result = template_obj.render(content_obj)
    return HttpResponse(result)





