import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Set up the queue attributes
queue_name = 'mahesh'
queue_attributes = {
    'DelaySeconds': '0',
    'VisibilityTimeout': '30'
}

# Create the queue
response = sqs.create_queue(
    QueueName=queue_name,
    Attributes=queue_attributes
)

# Print the URL of the newly created queue
print(f'Queue created: {response["QueueUrl"]}')

