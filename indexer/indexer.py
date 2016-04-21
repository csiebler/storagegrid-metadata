import boto3
import boto3.session
from botocore.utils import fix_s3_host
import requests
import tailer
import re
from elasticsearch import Elasticsearch
from requests.packages.urllib3.exceptions import InsecureRequestWarning
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

parser = configparser.ConfigParser()
parser.read('/indexer/indexer.conf')
endpoint = parser.get('config', 'endpoint')
access_key = parser.get('config', 'access_key')
secret_key = parser.get('config', 'secret_key')

audit_log = '/mnt/auditlogs/audit.log'

session = boto3.session.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)
s3 = session.resource(service_name='s3', endpoint_url=endpoint, region_name='us-west-2', verify=False)
s3.meta.client.meta.events.unregister('before-sign.s3', fix_s3_host)

es = Elasticsearch('elasticsearch:9200')

print "Indexer started..."

buckets = []
for bucket in s3.buckets.all():
    buckets.append(bucket.name)

print "Will monitor the following buckets: " +  ', '.join(buckets)

pattern = re.compile(r'.*?S3BK\(CSTR\):"(.+?)".*?S3KY\(CSTR\):"(.+?)".*?ATYP\(FC32\):(.+?)].*')

for line in tailer.follow(open(audit_log)):

    m = pattern.match(line)
    if m:
        bucket = m.group(1)
        key = m.group(2)
        action = m.group(3)
        id = bucket + "/" + key
        print id

        if bucket in buckets and action == 'SPUT':
            obj = s3.Object(bucket, key)
            response = obj.get()
            metadata = response['Metadata']
            print("PUT: %s/%s with metdata: %s" % (key, bucket, metadata))
            es.index(index='objects', doc_type='object', id=id, body=metadata)

        if bucket in buckets and action == 'SUPD':
            obj = s3.Object(bucket, key)
            response = obj.get()
            metadata = response['Metadata']
            print("SUPD: %s/%s with metdata: %s" % (key, bucket, metadata))
            es.index(index='objects', doc_type='object', id=id, body=metadata)

        if bucket in buckets and action == 'SDEL':
            print("DEL: %s/%s" % (bucket, key))
            es.delete(index='objects', doc_type='object', id=id, ignore=[400, 404])

