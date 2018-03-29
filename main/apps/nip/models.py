from __future__ import unicode_literals
from django.db import models
from django.views import View
import bcrypt
import re

EMAILREGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class RegistrationManager(models.Manager):
   def regis_basic_validator(self, postData):
       errors={}
       if len(postData['first_name']) < 5:
           errors['first_name'] = "Your name should be more than 5 characters"
       if len(postData['last_name']) < 5:
           errors['last_name'] = "Your last name should be more than 5 characters"
       if not EMAILREGEX.match(postData['email']):
           errors['email'] = "Your email needs to have the correct format."
       if len(postData['Password']) < 8:
           errors['Password'] = "Your password needs to be at least 8 characters"
       if postData['confirm_pw'] != postData['Password']:
           errors['confirm_pw'] = "Your passwords need to match"
       if postData['birthday'] == 1900-01-01:
           errors['birthday'] = "Please enter a valid date"
       if User.objects.filter(email=postData['email']) == []:
           error['ex_email'] = "You already have an account"
       return errors
   def log_basic_validator(self, postData):
       errors ={}
       if not EMAILREGEX.match(postData['email']):
           errors['email'] = "Your email needs to have the correct format."
       password = User.objects.get(email=postData['email']).password
       print password
       if bcrypt.checkpw(postData['Password'].encode(), password.encode()) != True:
           errors['Password'] = "Please revise your email and password"
       return errors

class User(models.Model):
   first_name = models.CharField(max_length= 40)
   last_name = models.CharField(max_length= 40)
   image = models.BinaryField(blank=True)
   email = models.CharField(max_length = 55)
   status = models.CharField(max_length = 20)
   password = models.CharField(max_length = 255)
   created_at = models.DateTimeField(auto_now_add = True)
   updated_at = models.DateTimeField(auto_now = True)
   facebook = models.TextField(null=True)
   linkedin = models.TextField(null=True)
   github = models.TextField(null=True)
   instagram = models.TextField(null=True)
   slack = models.TextField(null=True)
   def __repr__(self):
       return "<User object: {} {}, {}, {}, {} | {} | {} | {} | {}>".format(self.first_name, self.last_name, self.email,self.status, self.facebook, self.linkedin, self.github, self.instagram, self.slack)


class Stack(models.Model):
   student = models.ForeignKey(User,related_name = "current_stack", null=True)
   name = models.CharField(max_length= 40)
   created_at = models.DateTimeField(auto_now_add = True)
   updated_at = models.DateTimeField(auto_now = True)
   def __repr__(self):
       return "<Stack object: {}, {}>".format(self.student, self.name)


class Skill(models.Model):
   name = models.CharField(max_length= 40)
   created_at = models.DateTimeField(auto_now_add = True)
   updated_at = models.DateTimeField(auto_now = True)
   language = models.ForeignKey(Stack, related_name='skills')
   user = models.ManyToManyField(User, related_name="strengths", null=True)
   def __repr__(self):
       return "<Skill object: {} {}, {}>".format(self.name, self.language, self.user)



