"""
models.py

The definitive file for specifying the data model for the Toronto Frosh
Festival website.

"""

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import os

class Comment(models.Model):
    """
    Model for implementing comments for events, about users, photos, ...etc
    """
    user = models.ForeignKey(User)
    text = models.CharField(max_length=1024)
    time_posted = models.TimeField(auto_now_add=True)
    
    resp_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    resp_object = generic.GenericForeignKey('resp_type', 'object_id')
    
    def __unicode__(self):
        return self.text

class UserProfile(models.Model):
    """
    Model for additional user profile information. auth.models.User already
    took care of username, first/last name, email, password, and activation.
    """
    # required to hook up with Django's User model
    user = models.OneToOneField(User)
    hype = models.IntegerField(default=0)
    status = models.CharField(max_length=256, blank=True)
    
    def get_avatar_file_path(instance, filename):
        """
        Handler for specifying file path of uploaded avatar
        """
        name, extension = os.path.splitext(filename)
        if not isinstance(instance, models.AutoField):
            return "user/avatar/%d%s"%(instance.id, extension)
        else:
            return "user/avatar/%s"%filename
    avatar = models.ImageField(upload_to=get_avatar_file_path, blank=True)
    
    friends = models.ManyToManyField("self", blank=True)
    
def create_user_profile(sender, instance, created, **kwargs):
    """
    Handler for automatically creating a User profile whenever a User is 
    created.
    """
    if created:
        UserProfile.objects.create(user=instance)
        
# this line of code registers the handler to the User's post_save signal
post_save.connect(create_user_profile, sender=User)

class GroupProfile(models.Model):
    """
    Model for additional group profile information. 
    """
    group = models.OneToOneField(Group)
    hype = models.IntegerField(default=0)
    status = models.CharField(max_length=256)
    
    def get_avatar_file_path(instance, filename):
        """
        Handler for specifying file path of uploaded avatar
        """
        name, extension = os.path.splitext(filename)
        if not isinstance(instance, models.AutoField):
            return "group/avatar/%d%s"%(instance.id, extension)
        else:
            return "group/avatar/%s"%filename
    avatar = models.ImageField(upload_to=get_avatar_file_path, blank=True)
    
def create_group_profile(sender, instance, created, **kwargs):
    """
    Handler for automatically creating a Group profile whenever a Group is 
    created.
    """
    if created:
        GroupProfile.objects.create(group=instance)
post_save.connect(create_group_profile, sender=Group)

class Business(models.Model):
    """
    Model to represent businesses, sponsors, associations, ...etc.
    """
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=1024)
    description = models.TextField()
    
    def get_logo_file_path(instance, filename):
        """
        Handler for specifying file path of uploaded logo
        """
        name, extension = os.path.splitext(filename)
        if not isinstance(instance, models.AutoField):
            return "business/logo/%d%s"%(instance.id, extension)
        else:
            return "business/logo/%s"%filename
    logo = models.ImageField(upload_to=get_logo_file_path, blank=True)
    
    class Meta:
        verbose_name_plural = "businesses"
        
    def __unicode__(self):
        return self.name

class Event(models.Model):
    """
    Model to record vital information regarding an event or activity
    """
    name = models.CharField(max_length=256)
    description = models.TextField()
    location = models.CharField(max_length=256)
    address = models.CharField(max_length=1024)
    goers = models.ManyToManyField(User, blank=True)
    throwers = models.ManyToManyField(Business)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    
    def get_logo_file_path(instance, filename):
        """
        Handler for specifying file path of uploaded logo
        """
        name, extension = os.path.splitext(filename)
        if not isinstance(instance, models.AutoField):
            return "event/logo/%d%s"%(instance.id, extension)
        else:
            return "event/logo/%s"%filename
    logo = models.ImageField(upload_to=get_logo_file_path, blank=True)
    
    def __unicode__(self):
        return self.name

class Invitation(models.Model):
    """
    Model for recording invitation for friendship, group, or event
    """
    # the user that is being invited
    user = models.ForeignKey(User)
    
    invite_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    invite_object = generic.GenericForeignKey('invite_type', 'object_id')
    
    def __unicode__(self):
        if isinstance(self.invite_object, User):
            print self.invite_object
            return "Invitation to befriend %s"%(
                self.invite_object.username)
        elif isinstance(self.invite_object, Group):
            return "Invitation to join %s"%(
                self.invite_object.name)
        elif isinstance(self.invite_object, Event):
            return "Invitation to participate in %s"%(
                self.invite_object.name)
        else:
            return "Buggy Invitation Object"

class Photo(models.Model):
    """
    Model for representing a photo
    """
    uploader = models.ForeignKey(User)
    description = models.CharField(max_length=512)
    where = models.ForeignKey(Event, blank=True)
    people = models.ManyToManyField(User, related_name="tagged_photo") 
    
    def __unicode__(self):
        return self.description

