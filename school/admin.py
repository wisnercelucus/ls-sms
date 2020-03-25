from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Responsible)
admin.site.register(Pupil)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(ScoreRecorded)
admin.site.register(Attendance)
admin.site.register(Document)
admin.site.register(AcademicYear)
admin.site.register(School)
admin.site.register(PupilResponsible)
admin.site.register(PupilGradeAtAcademicYear)
admin.site.register(TeachCourseAtSchool)

