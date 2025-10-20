import json
import boto3

def lambda_handler(event, context):
    print("Evento recebido:")
    print(json.dumps(event, indent=2))

    for record in event.get('Records', []):
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print(f"Novo arquivo detectado: {key} no bucket {bucket}")

    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído com sucesso!')
    }
