from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rating, Movie
from .serializers import RatingSerializer
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

class SubmitRatingView(APIView):
    def post(self, request):
        try:
            serializer = RatingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({'error': 'Duplicate rating entry for this user and movie.'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class UserRatingHistoryView(APIView):
    def get(self, request, user_id):
        try:
            ratings = Rating.objects.filter(user_id=user_id).select_related('movie')
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
