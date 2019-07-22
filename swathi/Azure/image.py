
from azure.storage.blob import BlockBlobService
accountkey='pRy7Hsb9wIbCWkVRgrTioBRiPKuiTpGnoxmIZ7p5SUgMedIsT335m0ad7ap7m/SHoXf+85UUikrv5U2VWqpMyw=='
accountName='storagesci'
containerName='python-course'
blobService=BlockBlobService(account_name=accountName,account_key=accountkey)
blobService.create_container(containerName)
blobService.create_blob_from_path(containerName,"cloud.png","C:/Users/swathi.i/Downloads/cloud.png")


    