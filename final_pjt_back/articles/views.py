from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
# from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_like(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    user = request.user

    if article.liked_by.filter(id=user.id).exists():
        article.liked_by.remove(user)
        article.like_count -= 1
        article.save()
        return Response({'message': '게시글 좋아요 취소!'}, status=status.HTTP_200_OK)

    article.liked_by.add(user)
    article.like_count += 1
    article.save()
    return Response({'message': '게시글 좋아요 성공!'}, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = article.comment_set.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_like(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = article.comment_set.get(pk=comment_pk)
    user = request.user

    if comment.liked_by.filter(id=user.id).exists():
        comment.liked_by.remove(user)
        comment.like_count -= 1
        comment.save()
        return Response({'message': '댓글 좋아요 취소!'}, status=status.HTTP_200_OK)

    comment.liked_by.add(user)
    comment.like_count += 1
    comment.save()

    return Response({'message': '댓글 좋아요 성공!'}, status=status.HTTP_200_OK)