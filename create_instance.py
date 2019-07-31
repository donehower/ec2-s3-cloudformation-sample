import boto3


def setup_stack(client, bucket, key):
    '''
    Creates a stack based on the CloudFormation template provided.
    :param client: A CloudFormation client
    :param bucket: Bucket containing the CF template
    :param key: Key for the CF template

    :returns: Nothing.  Prints stack details to console.
    '''
    base_url = 'https://s3-us-west-2.amazonaws.com/'
    template = base_url + bucket + key
    res = client.create_stack(
        StackName='testingFileTransfers',
        TemplateURL=template,
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
    print(res)

    return


if __name__ == '__main__':

    client = boto3.client('cloudformation')
    setup_stack(client, 'datalake-tesing', 'ec2-s3.yaml')
