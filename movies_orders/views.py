from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from movies_orders.serializers import MovieOrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request,movie_id):
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, movie_id=movie_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
