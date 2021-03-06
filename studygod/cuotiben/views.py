from django.shortcuts import render
from .models import StudyGroup, User, Problem
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
import json
from .forms import ImageUploadForm, QuestionUploadForm
from datetime import datetime
from .utils import filter_by_category,recommend
from django.db.models import Q
#temprary user id
user_id = 1

def index(request):
	if request.method == 'GET':
		if request.GET.get('log in'):
			return
	if request.POST.post == ('log out'):
		return
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
			result = filter_by_category(cat, list(all_categories), 30)
			
			my_filter_qs = Q()
			for r in result:
				my_filter_qs = my_filter_qs | Q(category=r)
			problems = Problem.objects.filter(my_filter_qs, owner = -1)
		else:
			problems = Problem.objects.filter(owner = -1)
		context = {'prob': problems}
		return render(request, 'index.html', context)

def creategroup(request):
	if request.method == 'GET':
		return render(request, 'createGroups.html')
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			new_group = StudyGroup(
						name = form.cleaned_data['name'],
						info = form.cleaned_data['info'],
							)
			new_group.picture = form.cleaned_data['image']
			new_group.save()
		return JsonResponse({'status':200, 'responseText': 'Success'})

def groups(request):
	if request.method == 'GET':
		user = User.objects.filter(pk = user_id)[0]
		groups = user.study_groups.all()
		context = {'groups':groups}
		return render(request, 'groups.html', context)

def upload(request):
	if request.method == 'GET':
		user_id = 1
		user = User.objects.filter(pk = user_id)[0]
		groups = user.study_groups.all()
		courses = user.problem_set.values_list('course', flat = True).distinct()
		topics = user.problem_set.values_list('category', flat = True).distinct()
		context = {'groups':groups, 'courses':courses, 'topics':topics}
		return render(request, 'uploadproblem.html', context)
	if request.method == 'POST':
		form = QuestionUploadForm(request.POST, request.FILES)
		owner = 1
		if form.cleaned_data['access'] == 'Public': 
			owner = -1
		elif form.cleaned_data['access'] == 'Group': 
			group = user.study_groups.filter('name' == form.cleaned_data['group'])[0]
			people = group.user_set.all()

		new_problem = Problem(
			number = form.cleaned_data['question'],
			solution_number = form.cleaned_data['solution'],
			# people = people,
			# name = form.cleaned_data['name'],
			# category = form.cleaned_data['category'],
			# course = form.cleaned_data['course'],
			# school = 'UC Berkeley',
			# upload_time = datetime.now(),
			# owner = owner,
			)
		new_problem.save()
		# if form.cleaned_data['group']:
		# 	new_problem.study_groups.add(group)
			
		return JsonResponse(json.dump({'status':200, 'responseText':'Successfully uploaded'}))
	return HttpResponse(str(request.method))

