from aws_cdk import core
from aws_cdk import aws_s3 as S3
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_redshift as _redshift


class AwsCdkExplampleStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        S3.Bucket(self, 'bucket-bootcamp04-test', bucket_name='bucket-bootcamp04-test')

        vpc = ec2.Vpc(self, 'myVpc', cidr='10.0.0.0/16')
