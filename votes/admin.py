from django.contrib import admin
from votes.models import Vote

class VoteAdmin(admin.ModelAdmin):
     list_display = ('identity', 'vote_time', 'question','priority','vote')
     list_filter = ['vote']

admin.site.register(Vote, VoteAdmin)


