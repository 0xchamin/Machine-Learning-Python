from django.db import models

# Create your models here.

class TodoItem(models.Model):
    content = models.TextField()
    #date_create =
    #author
    # """docstring for TodoItem."""
    # def __init__(self, arg):
    #     super(TodoItem, self).__init__()
    #     self.arg = arg
