from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import ArticleSerializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from rest_framework import status

@api_view(['GET','PSOT'])
def article_list(request):

    if request.method == 'GET':
         articles = Article.objects.all()
         serializer = ArticleSerializers(articles, many=True)
         return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist :
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializers(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        article.delete()
        return Response('deleted',status=status.HTTP_404_NOT_FOUND)



