import boto3
import json


ses = boto3.client("ses")
def sending_email():
    try:
        response = ses.send_email(
            Destination={
                'BccAddresses': [
                ],
                'CcAddresses': [
                    'abc@example.com',
                ],
                'ToAddresses': [
                    '123@example.com',
                    '456@example.com',
                ],
            },
            Message={
                'Subject': {
                    'Data': "Your review has been Posted"
                },
                'Body': {
                    'Text': {
                        'Data': "Your review has been Posted \n" +
                                "Thank You\n"

                    }
                }
            },
            ReplyToAddresses=[
            ],
            ReturnPath='',
            ReturnPathArn='',
            Source='hello@example.com',
            SourceArn='',
        )

        return {
            'statusCode': 200,
            'headers': {"Access-Control-Allow-Origin": "*"},
            'body': json.dumps('e-mail sent ')
        }
    except Exception as e:
        print(e)
        return {

            'statusCode': 500,
            'headers': {"Access-Control-Allow-Origin": "*"},
            'body': json.dumps('Error occured while sending an review e-mail')
        }