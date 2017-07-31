import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from src import models


class ApiAccount(SQLAlchemyObjectType):
    class Meta:
        model = models.API_ACCOUNT
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_api_groups = SQLAlchemyConnectionField(ApiAccount)

schema = graphene.Schema(query=Query, types=[ApiAccount])
