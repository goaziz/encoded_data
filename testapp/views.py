from rest_framework.response import Response
from rest_framework import views, status
import base64

from .models import CipherText

class TextCipherView(views.APIView):
    def post(self, request):
        data = request.data['name']
        encoded_data = base64.b64encode(data.encode('utf-8'))
        encoded_str = str(encoded_data, 'utf-8')
        name_model = CipherText(name=encoded_str)
        name_model.save()
        return Response({'encoded_data': encoded_str, 'status': status.HTTP_201_CREATED})