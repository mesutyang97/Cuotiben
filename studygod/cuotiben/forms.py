from django import forms
class ImageUploadForm(forms.Form):
	image = forms.ImageField()
	name = forms.CharField()
	info = forms.CharField()

class QuestionUploadForm(forms.Form):
	problem = forms.ImageField()
	solution = forms.ImageField()
	course = forms.CharField()
	group = forms.CharField()
	topic = forms.CharField()
	title = forms.CharField()
	comment = forms.CharField()