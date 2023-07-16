from django.urls import path
from .views import *

urlpatterns = [
    path('pers/', Pers.as_view(), name='pers'),
    path('stage_1/', stage_1, name='stage_1'),
    path('stage_2/', stage_2, name='stage_2'),
    path('stage_3/', stage_image, name='stage_3'),
    path('stage_4/', stage_final, name='stage_4'),
    path('final/', final, name='final'),
]