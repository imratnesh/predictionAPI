# -*- coding: utf-8 -*-
from . import views as prediction_view
from django.urls import path

app = 'predictions'
urlpatterns = [
         path('create_token/',prediction_view.login, name='token'),
         # path('predict/',prediction_view.makePrediction(), 'predict')
         path('predict/',prediction_view.image_prediction, name='predict'),
         path('sample_api/', prediction_view.sample, name='api')
      ]