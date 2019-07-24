import boto3


if __name__ == '__main__':

    client = boto3.client('cloudformation')

    res = client.create_stack(
        StackName='testingFileTransfers',
        TemplateURL='https://s3-us-west-2.amazonaws.com/<bucket name>/ec2-s3.yaml',
        Parameters=[
            {
                'ParameterKey': 'NameOfService',
                'ParameterValue': 'testingFileTransfers'
            },
            {
                'ParameterKey': 'KeyName',
                'ParameterValue': 'skdec2'
            }
        ],
        Capabilities=['CAPABILITY_NAMED_IAM']
    )
