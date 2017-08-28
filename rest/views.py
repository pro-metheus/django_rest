from django.shortcuts import render
from .models import APIauth
from django.http import HttpResponseForbidden as fb
from django.http import HttpResponse
import json
from .mappings import mapping
# Create your views here.


def api_handler(request,api_key,function='a'):
    try:
        auth=APIauth.objects.get(api_key=api_key)
    except:
        auth=0
    if(auth):
        data={'message':'{0}'.format(mapping[function](auth.user))}
        return HttpResponse(json.dumps(data))
    else:
        data={'message':'forbidden'}
        return fb(json.dumps(data))
