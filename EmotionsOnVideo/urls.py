from django.urls import path
from .views import *
urlpatterns = [
    path('face_emotion_img/', face_emotion, name='Face_Emotion')
]
