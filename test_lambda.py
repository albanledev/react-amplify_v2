import boto3
import json

def test_lambda():
    client = boto3.client('lambda', region_name='eu-west-1')
    response = client.invoke(
        FunctionName='backTest-alban',
        Payload=json.dumps({"key": "value"})
    )
    payload = response['Payload'].read()
    result = json.loads(payload)
    assert 'expected_key' in result  # Replace with your expected output

if __name__ == "__main__":
    test_lambda()
    print("Lambda test passed.")
