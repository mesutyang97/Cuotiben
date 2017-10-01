from django.shortcuts import render
from .models import StudyGroup, User, Problem
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
import json
from .forms import ImageUploadForm
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
			problems = Problem.objects.filter(my_filter_qs)
			context = {'prob': problems}
			return render(request, 'index.html', context)
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
			if request.POST.get('public'):
				user_id = -1

			new_problem = Problem(
				number = form.cleaned_data['image1'],
				solution_number = form.cleaned_data['image2'],
				people = User.objects.get(pk = user_id),
				name = request.POST.get('name'),
				category = request.POST.get('category'),
				course = request.POST.get('course'),
				school = request.POST.get('school'),
				upload_time = datetime.now(),
				year = request.POST.get('year'),
				owner = user_id,
				)
			new_problem.save()
			if request.POST.get('group'):
				new_problem.study_groups.add(user.study_groups.filter('name' == group).get(0))
		
			return JsonResponse(json.dump({'status':200, 'responseText':'Successfully uploaded'}))
		#public? private? study group?
		return

