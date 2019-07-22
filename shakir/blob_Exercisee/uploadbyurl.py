
from  azure.storage.blob import BlockBlobService
import requests

file=requests.get("https://cdn.instructables.com/FRN/GME6/IXQFY5HZ/FRNGME6IXQFY5HZ.LARGE.jpg",stream=True)
def uploadFile():
    accountey="xxxx"
    accountName="xxxxx"
    containerName="xxx-xxx"

    blobService =BlockBlobService(account_name=accountName, account_key=accountey )
    blobService.create_container(containerName)
    blobService.create_blob_from_stream(containerName, "image4.jpg", file.raw)

uploadFile()
