from django.db import models

# Create your models here.
class formHospital(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	prof_pic = models.ImageField(upload_to='images/')
	username = models.CharField(max_length=50)
	email_id = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
	confirm_password = models.CharField(max_length=50)
	addr_line1 = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	pincode = models.IntegerField()