import json

def lambda_handler(event, context):
    # Evento recebido do S3
    print("Evento recebido:", json.dumps(event))
    
    # Pega o nome do arquivo enviado
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    print(f"Arquivo {file_name} enviado para o bucket {bucket}.")
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Processamento concluído para {file_name}')
    }
