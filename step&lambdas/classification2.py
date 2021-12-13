import json
import base64
import boto3
# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2021-12-13-17-23-37-178"
def lambda_handler(event, context):
   # Decode the image data
    body = event["body"]
    image = base64.b64decode(event["body"]["image_data"]) ## TODO: fill in
    # Instantiate a Predictor
    runtime = boto3.client('runtime.sagemaker')
    
    # Make a prediction:
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType="image/png",Body=image)
    inferences = json.loads(response['Body'].read().decode('utf-8'))
    print("...inferences:", inferences)
    # We return the data back to the Step Function    
    return {
        'statusCode': 200,
        'body': {
            "inferences": inferences
        }
    }