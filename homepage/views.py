from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = '<!DOCTYPE html>\
            <html>\
            <body\
              <h1 style="font-size:300%;text-align:center;color:black">PureFocus</h1>\
                <img src="media/LOGO Blue.png" alt="Pure Focus" style="max-width:90%;height: auto;"\
            </body>\
            </html>'
    return HttpResponse(html)
