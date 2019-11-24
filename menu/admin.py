from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# register your models here.

class Categoriesadmin(admin.ModelAdmin):
	"""docstring for categoriesadmin"""
	prepopulated_fields = {'slug': ('servicename',)}
	list_display = ('servicename', 'slug', 'parent','image','created_on')
			
class PostAdmin(admin.ModelAdmin):
    list_display = ('category','title', 'applied_in', 'status','created_on','file','updated_on','author')
    list_filter = ("status",)
    search_fields = ['title', 'created_on']
    prepopulated_fields = {'slug': ('title',)}

class Aboutadmin(admin.ModelAdmin):
	"""docstring for categoriesadmin"""
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'slug', 'created_on')
      
class ComtactAdmin(admin.ModelAdmin):
    list_display = ('customername','customeremail', 'subject', 'massege','created_on','profilepic',)
    list_filter = ("customername",'customeremail','subject')
    search_fields = ['subject', 'customeremail','customername']
    
class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientname','title', 'clentpic','created_on',)
    list_filter = ('clientname','title','created_on')
    search_fields = ['clientname', 'title','created_on',]
   
					
admin.site.register(ServiceModel, PostAdmin)
admin.site.register(Categories,   Categoriesadmin)
admin.site.register(AbooutUsModel,Aboutadmin) 
admin.site.register(TeamModel) 

admin.site.register(ContactModel,ComtactAdmin)
admin.site.register(VisiionMission)
admin.site.register(Associates) 
admin.site.register(ClientModel,ClientAdmin)
