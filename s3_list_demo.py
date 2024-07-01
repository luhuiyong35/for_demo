import boto3

# 不推荐：直接在代码中硬编码AWS凭证
aws_access_key_id = 'AKIAWR4QZNN2NDEJYJ6O'
aws_secret_access_key = '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'

# 使用指定的凭证初始化S3客户端
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# 列出所有S3桶
response = s3_client.list_buckets()

# 打印每个桶的名字
for bucket in response['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')
