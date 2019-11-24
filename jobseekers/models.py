from django.db import models
# import birthday
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers


# Create your models here.
STATUS = ( 
    (0,"Draft"),
    (1,"Publish")
)
GENDER = {
	('M','Male'),
	('F', 'Female'),
}
LOCATION = {
	('', 'Select'),
	('AR', 'Arusha'),
	('DA', 'Dar es Salaam'),
	('DO', 'Dodoma'),
	('KG', 'Kagera'),
	('Mw', 'Mwanza'),
	('KG', 'Kigoma'),


}
NATIONALITY={
	('','Select'),
	('AF','Afghan'),
	('AL','Albanian'),
	('AlG','Algerian'),
	('AN','andorran'),
	('ANG','Angolan'),
	('ANGU','Anguilban'),
	('ANT','Antarctic'),
	('ANTI','Antiguan or Burbudan'),
	('ARG','Argentine'),
	('ARGE','Armenian'),
	('ARU','Aruban'),
	('AUS','Australian'),
	('AUST','Austrian'),
	('AZ','Azerbaijani'),
	('BA','Bahamian'),
	('BAH','bahraini'),
	('BAN','Bangladesh'),
	('BAR','barbadian'),
	('BE','Belarusian'),
	('BEL','Belgian'),
	('BELI','Belizean'),
	('BEN','Beninese,Beninois'),
	('BER','Bermudian'),
	('BH','Bhutene'),
	('BAL','Balivian'),
	('BO','Bosnian OR Herzegovian'),
	('BOT','Botswanan'),
	('BUO','Bouvet Island'),
	('BR','Brazilian'),
	
}
QUALIFICATION ={
	('PH','PHD'),
	('MA', 'Masters'),
	('BA','Bachelor'),
	('PO', 'Postgraduate'),
	('DE', 'Deploma'),
	('CE', 'certificate'),
	('NO', 'Non of the above'),


}
EXPERIENCE= {
	('','No exprience'),
	('one','1 year'),
	('TWO','2 year'),
	('FOUR','4 year'),
	('FIVE','5 year'),
	('SIX',' 6 year'),
	('SEVEN','7 year'),
	('EIGHT','8 year'),
	('NINE','9 year'),
	('TEN','10 year'),
	('AB','Above ten year'),
	
}

class JobseekersPersonalIfor(models.Model):
	email = models.EmailField( null=True, unique= True )
	password = models.CharField( max_length = 200,null=True,)
	firstname= models.CharField(max_length = 200,null=True,)
	middlname = models.CharField(max_length=200, null = True)
	lastname = models.CharField(max_length = 200,null=True,)
	birthday = models.DateField(null=True)
	updated_on  =    models.DateTimeField(auto_now= True,null=True,)
	created_on  =    models.DateTimeField(auto_now_add=True,null=True,)
	status      =    models.IntegerField(choices=STATUS, default=0,null=True,)
	gender   = models.CharField( max_length=200,choices = GENDER,null=True,)
	location = models.CharField( max_length=200,  choices=LOCATION ,default='none',null=True,)
	phone_number = PhoneNumberField(null=True,)
	nationality  = models.CharField(max_length=200 ,  choices = NATIONALITY ,null=True,)
	class Meta:
		verbose_name_plural ='Jobseekers personal info'
	def __str__(self):
		return self.firstname

class JobseekersJobinfor(models.Model):
	personalinfo         = models.ForeignKey(JobseekersPersonalIfor, on_delete=models.CASCADE)
	highest_qualification = models.CharField(max_length=200,choices= QUALIFICATION , null = True)
	years_of_exprience = models.CharField(max_length= 200,choices=EXPERIENCE ,null= True)
	cv                 = models.FileField(upload_to= 'cv/%Y/%m/%d/',blank= True,null= True)
	receive_job_notifation     = models.BooleanField(default=False, null= True)
	class Meta:
		verbose_name_plural ='Jobseekers job infor'
	def __str__(self):
		return self.highest_qualification
	

	

	
   
    



