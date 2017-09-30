from django.shortcuts import render
from .models import StudyGroup, User, Problem
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
import json
from .forms import ImageUploadForm
from datetime import datetime
#temprary user id
user_id = 1

def index(request):
	if request.method == 'GET':
		if request.GET.get('log out'):
			pass
		
	else:
		return HttpResponseBadRequest

def problems(request):
	if request.method == 'GET':
		user = User.objects.get(pk = user_id)
		cats = user.problem_set.all().values_list('category', flat = True).distinct()
		courses = user.problem_set.all().values_list('course', flat = True).distinct()
		source_types = user.problem_set.all().values_list('source_type', flat = True).distinct()
		probs = user.problem_set.all().order_by('upload_time')
		context = {'problems': probs, 'categories':cats, 'courses':courses, 'source_types': source_types}
		return render(request, 'index.html', context)
	return HttpResponse(probs)

#def studygroups(request):

def about(request):
	user = User.objects.filter(pk = user_id)
	context = {'name':user.name, 'email':user.email}
	return HttpResponse(json.dump(context), content_type = 'application/json')


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
		if request.GET.get('group'):
			user = User.objects.filter(pk = user_id)
			groups = user.study_groups.all().values('name')
			context ={'studygroups':groups}
			return JsonResponse(context, safe = False)
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			group = request.POST.get('group')

			new_problem = Problem(
				number = form.cleaned_data['image'],
				#solution_number = 
				people = User.objects.get(pk = user_id),
				name = request.POST.get('name'),
				category = request.POST.get('category'),
				course = request.POST.get('course'),
				school = request.POST.get('school'),
				upload_time = datetime.now(),
				year = request.POST.get('year'),
				study_groups = user.study_groups.filter('name' == group)[0],
				owner = user_id,
				)
		
		#public? private? study group?
		return

