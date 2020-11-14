from django.db import models

from django.conf import settings




class Product(models.Model):

	user  				= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)


	name				= 	models.CharField(max_length = 3000, blank = True)
	description			= 	models.CharField(max_length = 50000, blank = True)
	category 			= 	models.CharField(max_length = 300, blank = True)

	price 				= 	models.IntegerField(blank = True)

	featured_image 		= 	models.FileField(blank = True)
	gallery_images		= 	models.FileField(blank = True)
	created_at 			= 	models.DateTimeField(auto_now_add = True, auto_now = False)


	def __str__(self):

		return str(self.user) + ' - ' + self.title


class Order(models.Model):

	user 				= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	product 			= 	models.ForeignKey(Product, on_delete = models.CASCADE)
	amount 				= 	models.IntegerField(blank = True)


	def __str__(self):

		return str(self.user) + ' - ' + 'Order'





class Review(models.Model):

	user 				= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	text 				= 	models.CharField(max_length = 3000, blank = True)
	rating 				= 	models.BooleanField(default = False, blank = True)

	created_at			= 	models.DateTimeField(auto_now_add = True, auto_now = False)



	def __str__(self):

		return str(self.user) + ' - ' + 'Review'