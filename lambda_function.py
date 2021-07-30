import json

import base64


def lambda_handler(event, context):
    try:
        base64_message = event.get('body')
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
    except AttributeError:
        pass

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from NEW Lambda!')
    }
