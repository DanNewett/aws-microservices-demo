import json, time

def handler(event, context):
    method = event.get('httpMethod','GET')
    if method == 'GET':
        return { 'statusCode': 200, 'body': json.dumps({ 'ok': True, 'ts': time.time() }) }
    if method == 'POST':
        body = json.loads(event.get('body') or '{}')
        return { 'statusCode': 201, 'body': json.dumps({ 'created': True, 'item': body }) }
    return { 'statusCode': 405, 'body': 'Method Not Allowed' }
