from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        # snippets는 모든 Snippet의 쿼리셋
        snipptes = Snippet.objects.all()
        # 쿼리셋을 serialize할 때 many=True옵션 추가
        serializer = SnippetSerializer(snipptes, many=True)
        # JSON방식으로 response
        # 기본적으로 JsonResponse는 dict형 객체를 받아 처리하나
        # safe옵션이 Flase이면 주어진 데이터가 dict가 아니어도 됨 (지금의 경우 리스트 객체가 옴)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # request로 전달된 데이터들을 JSONParser를 사용해 파이썬 데이터 형식으로 파싱
        data = JSONParser().parse(request)
        #
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=210)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
