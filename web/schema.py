from social.query import Query as MainQuery
import graphene
from social.mutations import Mutation as MainMutation





class Query(MainQuery,graphene.ObjectType):
    pass

class Mutation(MainMutation,graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query,mutation=Mutation)