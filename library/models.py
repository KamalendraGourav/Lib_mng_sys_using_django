from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    #used in issue book
    def __str__(self):
        return self.user.first_name+'['+str(self.enrollment)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id


class Book(models.Model):
    makechoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('cinematics', 'Cinematics'),
        ('fiction','Fiction'),
        ('technology','Technology'),
        ('storyTeller','StoryTeller'),
        ('novel','Novel'),
        ('detective','Detective'),
        ('mystery','Mystery'),
        ('other','Other')

        ]
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=makechoice,default='education')
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'


def get_expiry():
    return datetime.today() + timedelta(days=20)

class IssuedBook(models.Model):

    #moved this in forms.py
    enrollment=[(student.enrollment,str(student.get_name)+' ['+str(student.enrollment)+']') for student in StudentExtra.objects.all()]

    enrollment=models.CharField(max_length=30)
    isbn=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.enrollment


class blog(models.Model):
    title= models.CharField(blank=True, max_length=255)
    slug=models.SlugField()
    intro=models.TextField()
    body = models.TextField()
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


    


