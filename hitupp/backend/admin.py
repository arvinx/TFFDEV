"""
admin.py

Settings for administrative web pages 
 
"""
from backend.models import Business, Event, Comment, Photo, Invitation, \
UserProfile, GroupProfile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

class GroupProfileInline(admin.StackedInline):
    model = GroupProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class GroupAdmin(GroupAdmin):
    inlines = (GroupProfileInline, )

class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ['name']

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'start_time', 'end_time']
    search_fields = ['name']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'time_posted', 'text']
    search_fields = ['text']
    
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['uploader', 'description']
    search_fields = ['description']
    
class InvitationAdmin(admin.ModelAdmin):
    list_display = ['user', '__unicode__']  
    search_fields = ['user__username']

# Re-register UserAdmin and GroupAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)

admin.site.register(Event, EventAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Invitation, InvitationAdmin)

