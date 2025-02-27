# get_azure_token.py
from azure.identity import ClientSecretCredential
import os

def get_azure_token(tenant_id, client_id, client_secret):
    credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    token = credential.get_token('https://cognitiveservices.azure.com/.default')
    return token.token

if __name__ == "__main__":
    token = get_azure_token(
        os.getenv('AZURE_TENANT_ID'),
        os.getenv('AZURE_CLIENT_ID'),
        os.getenv('AZURE_CLIENT_SECRET')
    )
    # Set GitHub Action output
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        fh.write(f'azure_openai_key={token}')
