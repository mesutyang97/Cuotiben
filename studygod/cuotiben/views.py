from django.shortcuts import render
from .models import StudyGroup, User, Problem
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
import json
#temprary user id
user_id = 0

def index(request):
	if request.method == 'GET':
		if request.GET.get('study groups'):
			return
		elif request.GET.get('problems'):
			user = User.objects.filter(pk = user_id)
		elif request.GET.get('log out'):
			pass
		return HttpResponse('hello world')
	else:
		return HttpResponseBadRequest

def problems(request):

def about(request):

	user = User.objects.filter(pk = user_id)
	context = {'name':user.name, 'email':user.email}
	return HttpResponse(json.dump(context), content_type = 'application/json')

def 

# Create your views here.
def public(request):
	if request.method == 'GET':
		if request.GET.get('category'):
			cat = request.GET.get('category')
			all_categories = Problem.objects.values_list('category').distinct(flat = True)
			# call least distance algorithm
			result = helper(all_categories, cat, 10)

			#run algorithm to return the top recommendations
	return 

def upload(request):
	if request.method == 'GET':
		if request.GET.get('study groups'):
			user = User.objects.filter(pk = user_id)
			groups = user.study_groups.all().values('name')
			context ={'studygroups':groups}
			return JsonResponse(context, safe = False)
	if request.method == 'POST':
		
		#public? private? study group?
		return

