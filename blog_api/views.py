from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class PostCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "data is safe"})
        return Response(serializer.errors)


class PostRetriveByID(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response("Post not found")

    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response("item has been deleted")


class PostSearch(APIView):
    def get(self, request):
        search_term = request.query_params.get("title")
        if search_term:
            post = Post.objects.filter(title__icontains=search_term)
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {
                "message": "Not Found",
            },
            status=status.HTTP_404_NOT_FOUND,
        )


class UserProfile(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)

        return Response(serializer.data)
