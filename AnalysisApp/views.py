import json

from django.http import HttpResponse
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

import numpy_encoder
from FederatedServer import FederatedServer

import logging
logger = logging.getLogger(__name__)
fs = FederatedServer() #creating federated server object

@api_view(['GET', 'PUT'])
def update(request):#receiving request from client to update weight
    if request.method == 'PUT':
        json_data = JSONParser().parse(request)#get weight from request
        fs.update(json_data)#update weight to federated server
        return HttpResponse("Request Update Weight OK", status.HTTP_200_OK)
    else:
        return HttpResponse("Request OK", status.HTTP_200_OK)
    
def weight(request):#function to return global weight
    global_weight = fs.avg()#federated server will calculatee average weights of all local weights and then sent to client as global weight
    global_weight_to_json = json.dumps(global_weight, cls=numpy_encoder.NumpyEncoder)
    return HttpResponse(global_weight_to_json, status.HTTP_200_OK)
