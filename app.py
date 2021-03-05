#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_explample.aws_cdk_explample_stack import AwsCdkExplampleStack


app = core.App()
AwsCdkExplampleStack(app, "aws-cdk-explample")

app.synth()
