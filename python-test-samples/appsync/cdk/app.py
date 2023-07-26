#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import CdkStack


app = cdk.App()
CdkStack(app, "test-local-resolver-api-stack", env={'region': 'ap-south-1'})


app.synth()
