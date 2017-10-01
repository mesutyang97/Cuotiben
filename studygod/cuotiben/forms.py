from django import forms
class ImageUploadForm(forms.Form):
	image = forms.ImageField()
	name = forms.CharField()
	info = forms.CharField()