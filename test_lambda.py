import boto3

def test_lambda_exists():
    client = boto3.client('lambda', region_name='eu-west-1')
    functions = client.list_functions()['Functions']
    lambda_names = [f['FunctionName'] for f in functions]
    assert 'backTest-alban' in lambda_names, "Lambda 'backTest-alban' does not exist"

if __name__ == "__main__":
    test_lambda_exists()
    print("Lambda existence test passed.")

if __name__ == "__main__":
    test_lambda()
    print("Lambda test passed.")
