import json


def file_to_s3():
	'''Writes a line of sample data to a json file in the current directory.'''
	
    data = [{'date': 20190724, 'state': 'CA'}, {'date': 20190723, 'state': 'TN'}]
    with open('testdata.json', 'w') as f:
        json.dump(data, f)

    return

def delete_instance(stack_name):
    t = 'arn:aws:sns:us-west-2:811937106259:' + stack_name

    sns = boto3.client('sns', region_name='us-west-2')
    sns.publish(
        TopicArn=t,
        Message='delete'
    )


if __name__ == '__main__':
    file_to_s3()

    s = os.environ['STACK_NAME']
    delete_instance(s)
