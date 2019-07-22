
from azure.storage.blob import BlockBlobService
accountkey=''
accountName=''
containerName=''
blobService=BlockBlobService(account_name=accountName,account_key=accountkey)
blobService.create_container(containerName)
blobService.create_blob_from_path(containerName,"cloud.png","cloud.png")


    
