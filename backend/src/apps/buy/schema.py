import graphene

from graphene_django.types import DjangoObjectType

from apps.buy.models import Orders, Products


class OrdersType(DjangoObjectType):
    class Meta:
        model = Orders


class ProductsType(DjangoObjectType):
    class Meta:
        model = Products


class Query(object):
    all_orders = graphene.List(OrdersType)
    all_products = graphene.List(ProductsType)

    def resolve_all_orders(self, info, **kwargs):
        return Orders.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Products.objects.all()