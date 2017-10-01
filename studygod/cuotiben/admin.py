from django.contrib import admin

from .models import StudyGroup
from .models import User
from .models import Problem

admin.site.register(StudyGroup)
admin.site.register(User)
admin.site.register(Problem)
# Register your models here.
