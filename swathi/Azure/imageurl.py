from azure.storage.blob import BlockBlobService, PublicAccess
from azure.storage.blob.models import Blob
import requests

def imageurlfun():
    block_blob_service = BlockBlobService(account_name='', account_key='')
    container_name =''

    response = requests.get('https://images.unsplash.com/photo-1509803874385-db7c23652552?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80',stream=True)       
    block_blob_service.create_blob_from_stream(container_name,'remoteURL.png',response.raw)


imageurlfun()
print("image sent")
