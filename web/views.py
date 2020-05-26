
from json import JSONEncoder
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
#import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
from datetime import datetime



@csrf_exempt

def submit_income(request):

    #TODO: valiadate dta, user might be fake,token might be fake,amount might be...

    this_token=request.POST['token']
    this_user=User.objects.filter(token__token=this_token).get()
    if "date" not in request.POST:
        date=datetime.now()
    else:
        date=request.POST['date']

    Income.objects.create(user=this_user,amount=request.POST['amount'],date=date,text=request.POST["text"])
    #print( "i am in submit expense")
    #print (request.POST)


    return JsonResponse(
        {"status":"ok"},encoder=JSONEncoder
    )




def submit_expense(request):

    #TODO: valiadate dta, user might be fake,token might be fake,amount might be...

    this_token=request.POST['token']
    this_user=User.objects.filter(token__token=this_token).get()
    if "date" not in request.POST:
        date=datetime.now()
    else:
        date=request.POST['date']

    Expense.objects.create(user=this_user,amount=request.POST['amount'],date=date,text=request.POST["text"])
    #print( "i am in submit expense")
    #print (request.POST)


    return JsonResponse(
        {"status":"ok"},encoder=JSONEncoder
    )
