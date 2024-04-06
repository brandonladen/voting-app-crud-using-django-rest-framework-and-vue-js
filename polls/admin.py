from django.contrib import admin
from Accounts.models import Candidate, Vote, Post
# Register your models here.
admin.site.register(Candidate)
admin.site.register(Post)
admin.site.register(Vote)