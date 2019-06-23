from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from game.models import Level
from django.dispatch import reciever
from django.db.models.signals import post_save

# Create your models here.

class Player(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	current_level = models.ForeignKey(Level, default = Level.DEFAULT_LEVEL)
	current_level_time = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username
	
	def get_level(self):
		return self.current_level.level_id

	def get_name(self):
		return self.user.first_name + " " + self.user.last_name

# @reciever(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Player.objects.create(user=instance)
# 	instance.player.save()