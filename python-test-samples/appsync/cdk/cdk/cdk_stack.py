from aws_cdk import (
    aws_appsync as appsync,
    Stack,
    App as CdkApp,
)
from aws_cdk.aws_appsync import (
    CfnGraphQLSchema,
    CfnGraphQLApi,
    CfnApiKey,
    CfnDataSource,
    CfnResolver
)
from constructs import Construct


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create CDK stack for AWS AppSync
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_appsync/CfnGraphQLApi.html
        # Following code creates a local resolvers AppSync API which responds to queries and mutations following guide at -
        # https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-local-resolvers.html
        # Schema for the AppSync API is in schema.graphql
        # schema {
        #     query: Query
        #     mutation: Mutation
        #     subscription: Subscription
        # }

        # type Subscription {
        #     inbox(to: String!): Page
        #     @aws_subscribe(mutations: ["page"])
        # }

        # type Mutation {
        #     page(body: String!, to: String!): Page!
        # }

        # type Page {
        #     from: String!
        #     to: String!
        #     body: String!
        #     sentAt: String!
        # }

        # type Query {
        #     me: String
        # }
        #

        appsyncgraphqlapi = appsync.CfnGraphQLApi(
            self,
            "AppSyncGraphQLApi",
            name="test-local-resolvers-api",
            authentication_type="API_KEY",
            xray_enabled=False
        )

        appsyncgraphqlschema = appsync.CfnGraphQLSchema(
            self,
            "AppSyncGraphQLSchema",
            definition="""
                schema {
                query: Query
                mutation: Mutation
                subscription: Subscription
                }

                type Subscription {
                inbox(to: String!): Page @aws_subscribe(mutations: ["page"])
                }

                type Mutation {
                page(body: String!, to: String!): Page!
                }

                type Page {
                from: String!
                to: String!
                body: String!
                sentAt: String!
                }

                type Query {
                me: String
                }

            """,
            api_id="2b66o56s35bu5ii6fx5vrwkmrq"
        )

        appsyncdatasource = appsync.CfnDataSource(
            self,
            "AppSyncDataSource",
            name="TestLocalResolversApiDataSource",
            description="First data source created with the console.",
            type="NONE",
            api_id="2b66o56s35bu5ii6fx5vrwkmrq"
        )

        appsyncapikey = appsync.CfnApiKey(
            self,
            "AppSyncApiKey",
            expires=1690988400,
            api_id="2b66o56s35bu5ii6fx5vrwkmrq",
            api_key_id="da2-qlzy7m6zwfayncndycco3tprle"
        )
