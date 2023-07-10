import graphene
from graphene_django.debug import DjangoDebug

import products.schema

class Query(products.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')

schema = graphene.Schema(query=Query)
