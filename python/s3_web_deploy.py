import os
import sys

from boto3 import client as Client
from boto3.s3.transfer import S3Transfer


def deploy(includes, excludes=['.git', 'deploy.py']):
    client = Client(
        's3', aws_access_key_id='type here', aws_secret_access_key='type here'
    )
    transfer = S3Transfer(client)
    bucket_name = 'type here'
    content_types = {
        'html': 'text/html', 'css': 'text/css', 'js': 'application/javascript', 'pdf': 'application/pdf',
        'jpeg': 'image/jpeg', 'jpg': 'image/jpg', 'png': 'image/png', 'gif': 'image/gif'
    }
    for root, dirs, files in os.walk("."):
        for _file in files:
            if includes and _file not in includes:
                continue
            path = os.path.join(root, _file).replace("\\", "/")
            if set(path.split("/")).intersection(excludes):
                continue
            s3_key = path[2:]
            extra_args = {}
            content_type = content_types.get(path.split('.')[-1], '')
            if content_type:
                extra_args['ContentType'] = content_type
            transfer.upload_file(path, bucket_name, s3_key, extra_args=extra_args)
            client.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=s3_key)
            print(path, bucket_name, s3_key)


if __name__ == '__main__':
    deploy(sys.argv[1:])

