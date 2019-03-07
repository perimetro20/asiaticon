import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests


@login_required
def home(request):
    access_key = os.environ['FORGE_KEY']
    access_url = '&api_key={}'.format(access_key)
    url = 'https://forex.1forge.com/1.0.3/quotes?pairs=USDMXN,USDCNH&api_key=I82Hd3XYYFGsUVAWvQFWv8fDsdcvAHrZ'
    r = requests.get(url)
    result = r.json()

    context = {
        'usdmex': result[0]['price'],
        'usdcnh': result[1]['price']
    }
    return render(request, "base/home.html", context)


def base_files(request, filename):
    location = "base/" + filename
    return render(request, location, {}, content_type="text/plain")
