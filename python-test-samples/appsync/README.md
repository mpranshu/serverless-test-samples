# Python: AWS AppSync Example

[![python: 3.9](https://img.shields.io/badge/Python-3.9-green)](https://img.shields.io/badge/Python-3.9-green)
[![AWS: AppSync](https://img.shields.io/badge/%20-AppSync-red?logo=amazonaws
)](https://img.shields.io/badge/%20-AppSync-red?logo=amazonaws)
[![test: unit](https://img.shields.io/badge/Test-Unit-blue)](https://img.shields.io/badge/Test-Unit-blue)
[![test: integration](https://img.shields.io/badge/Test-Integration-yellow)](https://img.shields.io/badge/Test-Integration-yellow)

## Introduction

This project contains automated test sample code samples for serverless applications written in Python. The project demonstrates several techniques for executing tests including mocking, emulation and testing in the cloud specifically when interacting with the AWS AppSync service. Based on current tooling, we recommend customers **focus on testing in the cloud** as much as possible.

The project uses the [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) (SAM) CLI for configuration, testing and deployment.

---

## Contents

- [Python: AWS AppSync Example](#python-aws-appsync-example)
  - [Introduction](#introduction)
  - [Contents](#contents)
  - [Key Files in the Project](#key-files-in-the-project)
  - [Sample project description](#sample-project-description)
  - [Testing Data Considerations](#testing-data-considerations)
  - [Run the Unit Test](#run-the-unit-test)
  - [Run the Integration Test](#run-the-integration-test)

---

## Key Files in the Project

- [template.yaml](template.yaml) - SAM script for deployment of the Local Resolving AppSync
- [mock_test.py](tests/unit/mock_test.py) - Unit test using mocks
- [test_api_gateway.py](tests/integration/test_api_gateway.py) - Integration tests on a live stack

[Top](#contents)

---

## Sample project description

AWS AppSync allows you to use supported data sources (AWS Lambda, Amazon DynamoDB, or Amazon OpenSearch Service) to perform various operations. However, in certain scenarios, a call to a supported data source might not be necessary.

This is where the local resolver comes in handy. Instead of calling a remote data source, the local resolver will just forward the result of the request mapping template to the response mapping template. The field resolution will not leave AWS AppSync.

Local resolvers are useful for several use cases. The most popular use case is to publish notifications without triggering a data source call. To demonstrate this use case, let’s build a paging application; where users can page each other. This example leverages Subscriptions, so if you aren’t familiar with Subscriptions, you can follow the Real-Time Data tutorial.

This project consists of an [AppSync](https://aws.amazon.com/appsync/) API that will create and test the paging application.
Reference - [Local Resolvers for AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-local-resolvers.html)

As this example depicts Local Resolvers, there are a number of resolvers that can be leveraged and additionally configured on top of this example application as required.
Refer tutorials to add those as required - [Resolver Tutorials](https://docs.aws.amazon.com/appsync/latest/devguide/tutorials.html)

[Top](#contents)

---

## Testing Data Considerations

We would be using the SDK approach to invoke tests on the AppSync resolvers using the EvaluateMappingTemplate method in AWS SDK.

[Top](#contents)

---

## Run the Unit Test

[mock_test.py](tests/unit/mock_test.py)

In the [unit test](tests/unit/mock_test.py), all references and calls to the AppSync service [are mocked on line 18](tests/unit/mock_test.py#L20).

To run the unit test, execute the following

```shell
# Run from the project directory serverless-test-samples/python-test-samples/appsync
# Create and Activate a Python Virtual Environment
# One-time setup

pip3 install virtualenv
python3 -m venv venv
source ./venv/bin/activate

# install dependencies
pip3 install -r tests/requirements.txt

# run unit tests with mocks
python3 -m pytest -s tests/unit  -v
```

[Top](#contents)

---

## Run the Integration Test

[test_api_gateway.py](tests/integration/test_api_gateway.py)

For integration tests, the full stack is deployed before testing:

```shell
# Run from the project directory serverless-test-samples/python-test-samples/apigw-lambda-dynamodb

sam build
sam deploy --guided
```

The [integration test](tests/integration/test_api_gateway.py) setup determines both the [API endpoint](tests/integration/test_api_gateway.py#L50-53) and the name of the [DynamoDB table](tests/integration/test_api_gateway.py#L56-58) in the stack.

The integration test then [populates data into the DyanamoDB table](tests/integration/test_api_gateway.py#L66-70).

The [integration test tear-down](tests/integration/test_api_gateway.py#L73-87) removes the seed data, as well as data generated during the test.

To run the integration test, create the environment variable "AWS_SAM_STACK_NAME" with the name of the test stack, and execute the test.

```shell
# Run from the project directory serverless-test-samples/python-test-samples/apigw-lambda-dynamodb
# Set the environment variables AWS_SAM_STACK_NAME and (optionally)AWS_DEFAULT_REGION
# to match the name of the stack and the region where you will test

AWS_SAM_STACK_NAME=<stack-name> AWS_DEFAULT_REGION=<region_name> python -m pytest -s tests/integration -v
```

[Top](#contents)

---
