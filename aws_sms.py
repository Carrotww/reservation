import boto3
from botocore.exceptions import ClientError


def send_sms_message(sms_voice_v2_client, configuration_set, context_keys,
                     country_parameters, destination_number, dry_run, keyword,
                     max_price, message_body, message_type, origination_number,
                     ttl):
    try:
        response = sms_voice_v2_client.send_text_message(
            ConfigurationSetName=configuration_set,
            Context=context_keys,
            DestinationCountryParameters=country_parameters,
            DestinationPhoneNumber=destination_number,
            DryRun=dry_run,
            Keyword=keyword,
            MaxPrice=max_price,
            MessageBody=message_body,
            MessageType=message_type,
            OriginationIdentity=origination_number,
            TimeToLive=ttl
        )

    except ClientError as e:
        print(e.response)
    else:
        return response['MessageId']


def main():
    configuration_set = "MyConfigurationSet"
    context_keys = {"key1": "value1"}
    country_parameters = {
        "IN_TEMPLATE_ID": "TEMPLATE01234",
        "IN_ENTITY_ID": "ENTITY98765"
    }
    destination_number = "+14258918757"
    dry_run = False
    keyword = "MyKeyword"
    max_price = "2.00"
    message_body = ("This is a test message sent from Amazon Pinpoint "
                    "using the AWS SDK for Python (Boto3). ")
    message_type = "TRANSACTIONAL"
    origination_number = "+18449831743"
    ttl = 120

    print(
        f"Sending text message to {destination_number}.")

    message_id = send_sms_message(
        boto3.client('pinpoint-sms-voice-v2'), configuration_set, context_keys,
        country_parameters, destination_number, dry_run, keyword, max_price,
        message_body, message_type, origination_number, ttl)

    print(f"Message sent!\nMessage ID: {message_id}")


if __name__ == '__main__':
    main()