#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-26 18:54:49
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
# @Version : 0.0.1
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import ast

# Create your models here.
@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length = 50)
    qq = models.CharField(max_length = 10)
    addr = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title
@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name



# Create your models here.
@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Blog(models.Model):
    name = models.CharField(max_length = 100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
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
