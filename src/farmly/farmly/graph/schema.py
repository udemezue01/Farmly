import graphene
from graphene_django import DjangoObjectType

from product.models import(


	Product,
	Order,
	Review

	)



class ProductType(DjangoObjectType):

	class Meta:

		model = Product



class OrderType(DjangoObjectType):

	class Meta:

		model  = Order



class ReviewType(DjangoObjectType):

	class Meta:

		model = Review