from django.db import models

class About(models.Model):
	title = models.CharField(max_length=200 , default='About')

	about = models.TextField(default='')
	mission = models.TextField(default='')
	vision = models.TextField(default='')
	embed_video_url = models.CharField(max_length=200 , default='https://www.youtube.com/embed/?')
