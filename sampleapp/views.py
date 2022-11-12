from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random

@csrf_exempt
def testpost(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')

        a = int(a)
        b = int(b)

        result = a + b
        json_data = {'answer': result}
        return JsonResponse(result)


def index(request):
    return HttpResponse('hello')
