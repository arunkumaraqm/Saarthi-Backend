from django.shortcuts import render
from .models import *
from .serializers import IceSerializer
from .forms import BookForm
import json

from django.http.response import JsonResponse
from django.core.serializers import json
from django.core import serializers
qstojson = lambda data: json.Serializer().serialize(data)
from django.http.response import HttpResponse

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_book(request):
	if request.method == 'GET':
		return HttpResponse(str(request.GET.get('name')))

@api_view(['POST', 'GET'])
def books(request):
	if request.method == 'POST':
		book = BookForm(request.POST)
		mydict = {
			'status_code': 201,
			'status': 'success',
			'data': [

			]
		}
		mydict['data'].append(request.POST)
		print(book)
		book.save()
		return JsonResponse(mydict)

	if request.method == 'GET':
		mydict = {
			'status_code': 200,
			'status': 'success',
			'data': [

			]
		}

		allbooks = []
		for bookqs in Book.objects.all():
			book = {
				'id': bookqs.id,
				'name': bookqs.name
			}
			allbooks += [book]
		mydict['data'] = allbooks
		return JsonResponse(mydict)

	# if request.method == 'GET':
	# 	return HttpResponse('hello')

# @api_view(['POST', 'PATCH'])
# def get_num(request, *args, **kwargs):
# 	if request.method == 'POST' or request.method == 'PATCH':
# 		num = kwargs['num']
# 		return HttpResponse(str(num))


@api_view(['PATCH', 'POST', 'DELETE', 'GET'])
def get_book_by_id(request, *args, **kwargs):

	# if request.method == 'GET':
		# return HttpResponse('hello')
	if request.method == 'DELETE':
		return delete_book_by_id(request, *args, **kwargs)

	id = kwargs['id']
	print(id)
	mydict = {
		'status_code': 200,
		'status': 'success',
		'data': [

		]
	}
	bookqs = Book.objects.get(pk=id)
	form = BookForm(request.POST or None, instance=bookqs)
	if form.is_valid():
		form.save()
		bookqs = Book.objects.get(pk=id)
		book = {
				'id': id,
				'name': bookqs.name
		}
		mydict['data'].append(book)
		return JsonResponse(mydict)
	else: 
		return HttpResponse('Invalid book information.')

@api_view(['POST'])
def remove_book_post(request, *args, **kwargs):
	if request.method == 'POST':
		return delete_book_by_id(request, *args, **kwargs)

def delete_book_by_id(request, *args, **kwargs):
	id = kwargs['id']
	print(id)
	mydict = {
            'status_code': 200,
			'status': 'success',
			'message': '',
			'data': [

			]
        }
	bookqs = Book.objects.get(pk=id)
	name = bookqs.name
	bookqs.delete()

	message = f'The book {name} was deleted successfully'
	mydict['message'] = message
	return JsonResponse(mydict)
