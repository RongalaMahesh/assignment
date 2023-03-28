import boto3
import configparser
#


def create_queue(KUMAR):
    sqs = boto3.resource('sqs')
    queue = sqs.create_queue(QueueName=KUMAR)
    return queue.url


def send_message_to_queue(queue_url, message_body):
    sqs = boto3.client('sqs')
    sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    KUMAR = config['queue']['name']
    queue_url = create_queue(KUMAR)

    message_body = 'Hello, SQS!'
    send_message_to_queue(queue_url, message_body)


