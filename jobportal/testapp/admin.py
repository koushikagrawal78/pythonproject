from django.contrib import admin
from testapp.models import hydjobs
from testapp.models import bengjobs
from testapp.models import chenjobs
from testapp.models import punejobs
from testapp.models import mumjobs
# Register your models here.
class hydjobsadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(hydjobs,hydjobsadmin)

class bengjobsadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(bengjobs,bengjobsadmin)

class chenjobsadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(chenjobs,chenjobsadmin)

class punejobsadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(punejobs,punejobsadmin)

class mumjobsadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(mumjobs,mumjobsadmin)
