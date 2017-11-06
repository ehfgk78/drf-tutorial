from django.http import JsonResponse
from django.shortcuts import render


from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snipptes = Snippet.objects.all()
        serializer = SnippetSerializer(snipptes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=210)
        return JsonResponse(serializer.errors, status=400)
