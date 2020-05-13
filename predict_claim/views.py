from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import User_Input
from .serializers import User_InputSerializer
from .apps import model_wts
import pandas as pd
import numpy as np
import json

# Create your views here.
class User_InputView(viewsets.ModelViewSet):
	queryset = User_Input.objects.all()
	serializer_class = User_InputSerializer


@api_view(["POST"])
def predict(request):
    try:
        inport=request.data
        unit=np.array(list(inport.values()))
        unit=unit.reshape(1,-1)
        model= model_wts('/Volumes/Loopdisk/Fraud_predict_web_service/src/model_weight/deci_tree.pkl')
        prediction = model._predict(unit)
        df=pd.DataFrame(prediction, columns=['Fraud reported'])
        df=df.replace({1:'Fraud', 0:'Not Fraud'})
        df = df.to_dict()['Fraud reported'].get(0)
        return JsonResponse('Claim Assessed as {}'.format(df), safe=False)
        # 
        # return df
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
