from django.shortcuts import render
from .models import APIauth
from django.http import HttpResponseForbidden as fb
from django.http import HttpResponse
import json
# Create your views here.
def api_handler(request,api_key):
    auths=APIauth.objects.all()
    proceed=False
    for auth in auths:
        if auth.api_key==api_key:
            proceed=True
            break
    if(proceed):
        data={'message':'welcome {0}'.format(auth.user.username)}
        return HttpResponse(json.dumps(data))
    else:
        return fb
