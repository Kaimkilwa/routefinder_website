from django.db import models
import datetime
from django.contrib.auth.models import User
# from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField


STATUS = ( 
    (0,"Draft"),
    (1,"Publish")
)


class Categories( models.Model):
    created_on   =  models.DateTimeField(auto_now_add=True, null = True, blank= True)
    image        =  models.FileField(upload_to='avatars/', null=True, blank=True, default='./img/clients/client-8.png') 
    servicename  =  models.CharField(max_length= 200, null= True , blank= True, unique = True)
    slug         =  models.SlugField(max_length=200, unique=True, null= True)
    description  =  RichTextField( null=True, blank=True )
    parent       =  models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete= models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name_plural = "service Categories"
    def __str__(self):
        full_path = [self.servicename]                  
        k = self.parent 
        while k is not None:
            full_path.append(k.servicename)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    def image_url(self):
        if self.image:
            return self.image.url
        return '#'


class ServiceModel(models.Model):
    category    =    models.ForeignKey('Categories', null=True, blank=True,on_delete= models.CASCADE)
    title       =    models.CharField(max_length=200, unique=True)
    slug        =    models.SlugField(max_length=200, unique=True)
    # author      =    models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', null = True, blank = True)
    updated_on  =    models.DateTimeField(auto_now= True)
    description =    RichTextField()
    created_on  =    models.DateTimeField(auto_now_add=True)
    status      =    models.IntegerField(choices=STATUS, default=0)
    file        =    models.FileField(upload_to='images/', null=True, blank=True)
    applied_in  =    models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural =" sub Service "

    def __str__(self):
        return self.title


    def get_category_list(self):
        k = self.category # for now ignore this instance method
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

class AbooutUsModel(models.Model):
    image        =    models.FileField(upload_to = 'about/', null = True , blank =True)
    oursolution1 =    models.CharField(max_length = 300 , null = True,blank = True)
    oursolution2 =    models.CharField(max_length = 300 , null = True,blank = True)
    oursolution3 =    models.CharField(max_length = 300 , null = True,blank = True)
    oursolution4 =    models.CharField(max_length = 300 , null = True,blank = True)
    oursolution5 =    models.CharField(max_length = 300 , null = True,blank = True)
    title        =    models.CharField(max_length=200, unique=True)
    slug         =    models.SlugField(max_length=200, unique=True)
    ServiceModel.author      =    models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on   =    models.DateTimeField(auto_now= True)
    description  =    RichTextField(null = True, blank=True)
    created_on   =    models.DateTimeField(auto_now_add=True)
    status       =    models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural ="This is about the  Company Profile"
    def __str__(self):
        return self.title

    def image_url(self):
        if self.image:
            return self.image.url
        return '#'
class TeamModel(models.Model):
    name          =     models.CharField(max_length = 250, null = True,blank= True )
    title         =     models. CharField(max_length =250, null= True, blank = True)
    description   =     RichTextField(null = True, blank = True)
    image         =     models.FileField(upload_to='avatars/', null=True, blank=True, default='../static/img/profile-default-lrg.png')
    created_on    =     models.DateTimeField(auto_now_add=True,  null= True, blank= True) 

    class Meta:
        verbose_name_plural = " Team"

    def __str__(self):
        return self.name

    def image_url(self):
        if self.image:
            return self.image.url
        return '#'

class ContactModel(models.Model):
    profilepic      =      models.FileField( upload_to='pic/' , blank= True, null= True)
    customername    =      models. CharField(max_length = 200, blank= True, null = True)
    customeremail   =      models. EmailField(blank = True, null = True)
    subject         =      models . CharField( max_length = 200 , null = True, blank = 200)
    massege         =      RichTextField( blank = True , null = True) 
    created_on    =        models.DateTimeField(auto_now_add=True,  null= True, blank= True) 

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = " Customer massege"      


class VisiionMission(models.Model):
    vision          = RichTextField()
    mission         = RichTextField()
    
    class Meta:
        verbose_name_plural= 'Vision and Mission of the Company'
    def __str__(self):
        return self.vision

class Associates(models.Model):
    associateName =     models.CharField(max_length = 250, null = True,blank= True )
    asociateTitle =     models. CharField(max_length =250, null= True, blank = True)
    associateDesc =     RichTextField(null = True, blank = True)
    associateImage =    models.FileField(upload_to='avatars/', null=True, blank=True, default='../static/img/profile-default-lrg.png')
    created_on    =     models.DateTimeField(auto_now_add=True,  null= True, blank= True) 

    class Meta:
        verbose_name_plural = " Our Associates"

    def __str__(self):
        return self.associateName

    def image_url(self):
        if self.associateImage:
            return self.associateImage.url
        return '#'

class ClientModel(models.Model):
    clientname          =     models.CharField(max_length = 250, null = True,blank= True )
    title         =     models. CharField(max_length =250, null= True, blank = True)
    description   =     RichTextField(null = True, blank = True)
    clentpic         =     models.FileField(upload_to='avatars/', null=True, blank=True, default='../static/img/profile-default-lrg.png')
    created_on    =     models.DateTimeField(auto_now_add=True,  null= True, blank= True) 

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.clientname

    def image_url(self):
        if self.clentpic:
            return self.clentpic.url
        return '#'






   
    
        

