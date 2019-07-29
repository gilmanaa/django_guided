from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

colors_list = ["blue","red","green","white","black"]

def index(request):
    return HttpResponse("Welcome to the colors app")

def list(request):
    return JsonResponse(colors_list,safe=False)

def add(request):
    color = request.GET.get('color')
    add_flag = True
    for c in colors_list:
        if c == color:
            add_flag = False
    if add_flag:
        colors_list.append(color)
        return JsonResponse({"msg":"color added"},status=201)
    return JsonResponse({"msg":"color already exitst"},status=409)

def getcolor(request):
    color = request.GET.get('color')
    for c in colors_list:
        if c == color:
            return HttpResponse(color)
    return JsonResponse({"Error":"404 Page Not Found","msg":"no such color"},status=404)