from django.http import JsonResponse
from rest_framework.decorators import api_view
from nasaApp.services import ApodServices


@api_view(['GET'])
def apod_api(request):

    result_list = ApodServices.get_apod_basic()
    context = {
        "result_list": result_list
    }
    return JsonResponse(context)