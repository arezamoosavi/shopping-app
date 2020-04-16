import graphene
from graphene import Schema, relay, resolve_only_args
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


def create_order(delivery_method, payment_method):
    new_order = Orders(delivery_method=delivery_method, payment_method=payment_method)
    new_order.save()
    return new_order

class IntroduceOrders(relay.ClientIDMutation):
    class Input:
        delivery_method = graphene.String(required=True)
        payment_method = graphene.String(required=True)

    order = graphene.Field(OrdersType)

    @classmethod
    def mutate_and_get_payload(
        cls, root, info, delivery_method, payment_method, client_mutation_id=None
    ):
        order = create_order(delivery_method, payment_method)
        return IntroduceOrders(order=order)



class ProductInput(graphene.InputObjectType):
    name = graphene.String()
    category = graphene.String()
    quantity = graphene.Int()
    

class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductsType)

    class Arguments:
        input = ProductInput(required=True)

    @staticmethod
    def mutate(root, info, input):
        product = Products.objects.create(**input)
        product.save()
        return CreateProduct(product=product)

class Mutation(graphene.ObjectType):
    add_order = IntroduceOrders.Field()
    add_product = CreateProduct.Field()