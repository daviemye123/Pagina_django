from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date", "video_game_favorite", "amd_intel", "music_favorite")
  
admin.site.register(Member, MemberAdmin)
