import apps.buy.schema
import graphene

from graphene_django.debug import DjangoDebug


class Query(apps.buy.schema.Query,graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(apps.buy.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)