import json
import boto3

rekognition = boto3.client('rekognition', region_name='ap-south-1')
s3 = boto3.client('s3')

bucket_name = "face-rekognito"
testing_bucket = "face-db-images"

def get_images_from_s3(bucket_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    images = [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].lower().endswith(('jpg', 'jpeg', 'png'))]
    return images

def lambda_handler(event, context):
    stored_images = get_images_from_s3(bucket_name)

    for stored_image in stored_images:
        response = rekognition.compare_faces(
            # random person
            # SourceImage={'S3Object': {'Bucket': testing_bucket , 'Name': 'random.jpeg'}},

            # half face
            # SourceImage={'S3Object': {'Bucket': testing_bucket , 'Name': 'elon-musk2.jpeg'}},
            # SourceImage={'S3Object': {'Bucket': testing_bucket , 'Name': 'BillGates2.jpg'}},
            SourceImage={'S3Object': {'Bucket': testing_bucket , 'Name': 'BillGates3.jpeg'}},

            # same image
            # SourceImage={'S3Object': {'Bucket': bucket_name , 'Name': 'elon-musk.jpeg'}},

            TargetImage={'S3Object': {'Bucket': bucket_name, 'Name': stored_image}}
        )

        if response['FaceMatches']:
            similarity_score = response['FaceMatches'][0]['Similarity']
            # similarity_score = response['FaceMatches'][0]
            return f"yes, matched with {stored_image}, confidence: {similarity_score:.2f}%"
            # return similarity_score

    return "no result found"