#!/usr/bin/env python3.6

import boto3
sess = boto3.Session(region_name="us-east-1",)

client = sess.client("s3")

bucket_name = "elvis-sample-bucket"

response = client.create_bucket(Bucket=bucket_name)
print("Amazon S3 bucket has been created")
