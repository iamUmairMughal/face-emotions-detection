from django.http import JsonResponse
from rest_framework.decorators import api_view
from .Testing import predict_result

@api_view(['POST'])
def face_emotion(request):
    text = predict_result(request.FILES['picture'])
    return JsonResponse({"Prediction": text}, safe=False)