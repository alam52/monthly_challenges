from urllib import response
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_msgs = {
    'january':'First month',
    'february': 'Second month',
    'march': 'Third month',
    'april': 'Fourth month',
    'may': 'Fifth month',
    'june': 'Sixth month',
    'july': 'Seventh month',
    'august': 'Eight month',
    'september': 'Ninth month',
    'october': 'Tenth month',
    'november': 'Eleventh month',
    'december': None
    }

# Create your views here.
def index(request):

    months = list(monthly_msgs.keys())
    return render(request, "challenges/index.html", {
        "months": months,
    })

def monthy_challenges_num(request, month):
    months = list(monthly_msgs.keys())
    
    try:
        msg_by_num = months[month-1]
    except:
        return HttpResponseNotFound('<h1>Incorrect Month Number</h1>')
    redirect_path = reverse("month-challenge", args=[msg_by_num])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):

    try:
        challenge_text = monthly_msgs[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month,
        })
    except:
        raise Http404()