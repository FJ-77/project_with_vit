from django.db import models

class Advert(models.Model):
	title = models.CharField(max_length=50, verbose_name='Title')
	text = models.TextField(verbose_name='Text')
	image = models.ImageField(upload_to='adv_imgs/', blank = True, default = 'adv_imgs/default.img')
