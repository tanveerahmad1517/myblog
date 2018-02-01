from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Blat, Profile
from django.contrib.auth.models import User
class BlatAdmin(admin.ModelAdmin):
	list_display = ('text', 'created_on', 'total_likes')
	list_filter = ['created_on']
	search_fields = ['text']

class ProfileInline(admin.StackedInline):
	model = Profile 
	can_delete = False
class UserAdmin(UserAdmin):
	inlines = (ProfileInline,)
admin.site.register(Blat, BlatAdmin)
admin.site.unregister(User)

admin.site.register(User, UserAdmin)