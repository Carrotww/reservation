import boto3
import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 AWS 자격증명 가져오기
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')
user_phone_number1 = os.getenv('USER1')
user_phone_number2 = os.getenv('USER2')
user_list = []
user_list.append(user_phone_number1)
user_list.append(user_phone_number2)
template = "문자 내용 입력"

# AWS SNS 클라이언트 생성
client = boto3.client(
    'sns',
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

def response_msg(phone_number, message):
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

for user_phone_number in user_list:
    response_msg(user_phone_number, template)