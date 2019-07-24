import json


def file_to_s3():
	'''Writes a line of sample data to a json file in the current directory.'''
	
    data = [{'date': 20190724, 'state': 'CA'}, {'date': 20190723, 'state': 'TN'}]
    with open('testdata.json', 'w') as f:
        json.dump(data, f)

    return


if __name__ == '__main__':
    file_to_s3()
