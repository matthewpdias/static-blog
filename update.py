import boto3
import yaml

s3 = boto3.resource('s3')

with open("s3.yaml", 'r') as stream:
  try:
      configuration = yaml.load(stream)
  except yaml.YAMLError as exc:
    print(exc)

print(configuration)

filename = "error.html"
with open(filename, 'rb') as data:
    s3.Bucket(configuration['bucket']).put_object(Key=filename, Body=data)
