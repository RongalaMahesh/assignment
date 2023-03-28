import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# List the queues
response = sqs.list_queues()

# Print the queue URLs
if 'QueueUrls' in response:
    print('Queues:')
    for queue_url in response['QueueUrls']:
        print(queue_url)
else:
    print('No queues found.')