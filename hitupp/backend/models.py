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
from consts import CROWD_CHOICES, VENUE_CHOICES
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

class Genre(models.Model):
    """
    This model contains information regarding a particular genre
    """
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)

class GenrePreference(models.Model):
    """
    Model for each user's genre preference
    """
    goer = models.ForeignKey('Goer')
    genre = models.ForeignKey(Genre)
    coefficient = models.IntegerField(default=100)

class Goer(models.Model):
    """
    Model for goers
    """   
    user = models.OneToOneField(User)
    friends = models.ManyToManyField("self", blank=True)
    
    # these fields contain preferences specific to this goer
    crowd = models.CharField(max_length=2, choices=CROWD_CHOICES)
    venue = models.CharField(max_length=2, choices=VENUE_CHOICES)
    genre = models.ManyToManyField(Genre, through='GenrePreference')
    
    def __unicode__(self):
        return self.user.username
        
class Thrower(models.Model):
    """
    Model to represent businesses, sponsors, associations, ...etc.
    """
    user = models.OneToOneField(User)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username    
    

class UserProfile(models.Model):
    """
    Model for additional user profile information. auth.models.User already
    took care of username, first/last name, email, password, and activation.
    """
    # required to hook up with Django's User model
    user = models.OneToOneField(User)
    hype = models.IntegerField(default=0)
    status = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=1024, blank=True)
    
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
    
def create_group_profile(sender, instance, created, **kwargs):
    """
    Handler for automatically creating a Group profile whenever a Group is 
    created.
    """
    if created:
        GroupProfile.objects.create(group=instance)
post_save.connect(create_group_profile, sender=Group)

class Event(models.Model):
    """
    Model to record vital information regarding an event or activity
    """
    name = models.CharField(max_length=256)
    description = models.TextField()
    location = models.CharField(max_length=256)
    address = models.CharField(max_length=1024)
    goers = models.ManyToManyField(User, blank=True)
    throwers = models.ManyToManyField(Thrower)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class Invitation(models.Model):
    """
    Model for recording invitation for friendship, group, or event
    """
    # the user that is being invited
    invitee = models.ForeignKey(User)
    inviter = models.ForeignKey(User, related_name="outgoing_invitation")
    
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
        
class Notification(models.Model):
    """
    Model to keep track of notification to users
    """
    user = models.ForeignKey(User)
    message = models.CharField(max_length=512)
    
    notify_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    notify_object = generic.GenericForeignKey('notify_type', 'object_id')

