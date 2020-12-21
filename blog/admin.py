from django.contrib import admin

# Registered the models here.
from .models import Post

admin.site.register(Post)