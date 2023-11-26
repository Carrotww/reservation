# aws_sms.py

import boto3
import os
from dotenv import load_dotenv

def create_sns_client(aws_access_key_id, aws_secret_access_key, aws_region):
    client = boto3.client(
        'sns',
        region_name=aws_region,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    return client

def send_sms(client, phone_number, message):
    response = client.publish(
        PhoneNumber=phone_number,
        Message=message,
        MessageAttributes={
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String',
                'StringValue': 'Transactional'
            }
        }
    )
    return response

def main(place, date, url):
    load_dotenv()

    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_region = os.getenv('AWS_REGION')
    user_list = [os.getenv('USER1')]

    template = f"빨리 빨리 예약잡아!! - carrot - \n예약 장소 : {place}, 예약 날짜 : {date} 예약 링크 : {url}"

    sns_client = create_sns_client(aws_access_key_id, aws_secret_access_key, aws_region)

    for user_phone_number in user_list:
        send_sms(sns_client, user_phone_number, template)
