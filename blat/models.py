from django.db import models
from django.contrib.auth.models import User

class Blat(models.Model):
	text = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	via = models.URLField(blank=True)
	created_by= models.ForeignKey(User, on_delete=models.CASCADE)
	def __unicode__(self):
		return self.text[:500]
	def total_likes(self):
		return self.like_set.count()
class Like(models.Model):
	blat = models.ForeignKey(Blat, on_delete=models.CASCADE)
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(blank=True)
	blog = models.URLField(blank=True)