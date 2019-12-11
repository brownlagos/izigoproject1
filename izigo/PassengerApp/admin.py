from django.contrib import admin

# Register your models here.
from .models import Post

#this is to make your table show
admin.site.register(Post)