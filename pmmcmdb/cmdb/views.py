import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from cmdb.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status   #状态码对象
from rest_framework.decorators import api_view	#view装饰器
from rest_framework.response import Response    #响应对象

#v1.0
def index(request):
	latest_question_list = Question.objects.order_by('-pub_data')[:5]
	template = loader.get_template('cmdb/index.html')
	context = {
		'latest_question_list' : latest_question_list,
	}
	return HttpResponse(template.render(context,request))
    # return HttpResponse("Hello, world. You're at the polls index.")

def left(request,a):
	return HttpResponse(a)

#v2.0
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def spider(request):
	result = {'a':'你好','b':'我好','c':'大家好'}
	# return HttpResponse(json.dumps(result))
	# return JsonResponse(result)
	# context = {
		# 'latest_question_list' : Question.objects.order_by('-pub_data')[:5],
	# }
	# return JsonResponse(context)

	# serializer = SnippetSerializer(Question)
	# # return HttpResponse(serializer)
	# content = JSONRenderer().render(serializer.data)
	# return HttpResponse(content)

	# serializer = SnippetSerializer()
	# return HttpResponse(JSONRenderer().render(serializer.data))
	snippets = Question.objects.all()
	serializer = SnippetSerializer(snippets,many=True)
	return JSONResponse(serializer.data)

#v3.0
@csrf_exempt
def snippet_list(request):
    """
    列出所有的实例，或创建一个新的实例.
    """
    if request.method == 'GET':
        snippets = Question.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Question.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

#v4.0
@api_view(['GET', 'POST'])
def snippet_list_v4(request):
    """
    列出所有的实例，或创建一个新的实例.
    """
    if request.method == 'GET':
        snippets = Question.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail_v4(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Question.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#v4.0
'''
测试用例：
http://www.python.com/cmdb/question_v4/1.json
http://www.python.com/cmdb/question_v4/1.api
'''
@api_view(['GET', 'POST'])
def snippet_list_v4(request, format=None):
    """
    列出所有的实例，或创建一个新的实例.
    """
    if request.method == 'GET':
        snippets = Question.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail_v4(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Question.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)