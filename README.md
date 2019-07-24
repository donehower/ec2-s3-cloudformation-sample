## Files

`ec2-s3.yaml`
- CloudFormation template with EC2 configurations and bootstrap commands.

`create_instance.py`
- Submits the template and required parameters to CloudFormation

`write_test_file.py`
- A test script to write a sample line of data to a json file on the instance which is then copied to S3.

## Set-up Assumptions
- terminal running the create_instance.py script has valid credentials in the ~/aws/credentials file
- two buckets are referenced in the CloudFormation template; both are assumed to have been created prior to running the script
- the role referenced in the CloudFormation template granting the instance access to S3 has been created prior to running the script