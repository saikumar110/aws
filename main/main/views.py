

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
import os
import pandas as pd


def Home(request):
    df  = pd.read_csv( (staticfiles_storage.path("fo11FEB2022bhav.csv")))
    
    html= df.to_html("templates/table2.html")
    return render(request, "table2.html",locals())