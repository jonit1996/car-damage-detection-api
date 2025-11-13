from django.shortcuts import render

# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .inference import detect_damage
#from django.views.decorators.csrf import csrf_exempt
import os


@api_view(['POST'])
def detect_damage_api(request):
    """Handle POST /api/detect/ with image file."""
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image_dir = 'media'
        os.makedirs(image_dir, exist_ok=True)
        image_path = os.path.join(image_dir, image.name)

        # Save image locally
        with open(image_path, 'wb+') as dest:
            for chunk in image.chunks():
                dest.write(chunk)

        detections = detect_damage(image_path)
        return Response({"status": "success", "detections": detections}, status=200)
    
    return Response({"error": "Please send an image file using POST."}, status=400)