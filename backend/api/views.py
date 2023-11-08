from django.http import JsonResponse
from rest_framework.decorators import api_view

def getUrl(request):
    routes=[
        {'GET': 'url'},
        {'POST': 'income'},
    ]
    return JsonResponse(routes, safe=False)