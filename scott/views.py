from django.http import HttpResponse
from django.shortcuts import render


def base(request):
    return render(request, 'base.html',{})
    #return HttpResponse("Hello, world. Scott is hot.")

def fastapi(request):
    return render(request, 'fastapi.html',{})

def flask(request):
    return render(request, 'flask.html',{})

def trade_bot(request):
    return render(request, 'trade_bot.html',{})

def bg_nav(request):
    return render(request, 'bg_nav.html',{})

def certif(request):
    return render(request, 'certif.html',{})

def web_react(request):
    return render(request, 'web_react.html',{})

def roster(request):
    return render(request, 'roster.html',{})

def team_creator(request):
    return render(request, 'team_creator.html',{})

def prof_exp(request):
    return render(request, 'prof_exp.html',{})



