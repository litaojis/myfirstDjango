from django.db import models
import ast

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length = 100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length = 255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authours = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

# Create your models here.
class CompressedTextField(models.TextField):

    def from_db_value(self,value,expression,connection,context):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def to_python(self,value):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def get_prep_value(self, value):
        if not value:
            return value
        try:
            value.decode('base64')
            return value
        except Exception:
            try:
                return value.encode('utf-8').encode('bz2').encode('base64')
            except Exception:
                return value

class ListField(models.TextField):
    #__metaclass__ = models.SubfieldBase
    description = 'Stores a python list'

    def __init__(self,*args,**kwargs):
        super(ListField,self).__init__(*args,**kwargs)

    def to_python(self,value):
        if not value:
            value = []
        if isinstance(value,list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self,value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self,obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

    
