from django.shortcuts import render

# Create your views here.

from rest_framework import views, response, status
from .serializers import LEDControlSerializer
import neopixel
import board

# Assuming the setup from your previous script
npins = 240 * 3
pixels = neopixel.NeoPixel(board.D18, npins, brightness=0.1)

class LEDControlView(views.APIView):
    def get(self, request):
        # This could return the current settings, or just a confirmation message
        return response.Response({"message": "LED Controller is online."}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LEDControlSerializer(data=request.data)
        if serializer.is_valid():
            color = serializer.validated_data.get('color')
            brightness = serializer.validated_data.get('brightness')
            if color:
                # Convert hex color to RGB tuple
                color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                pixels.fill(color)
            if brightness is not None:
                pixels.brightness = brightness
                pixels.show()
            return response.Response({"message": "LED settings updated."}, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


