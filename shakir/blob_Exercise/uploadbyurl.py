
from  azure.storage.blob import BlockBlobService
import requests

file=requests.get("https://cdn.instructables.com/FRN/GME6/IXQFY5HZ/FRNGME6IXQFY5HZ.LARGE.jpg",stream=True)
def uploadFile():
    accountey="pRy7Hsb9wIbCWkVRgrTioBRiPKuiTpGnoxmIZ7p5SUgMedIsT335m0ad7ap7m/SHoXf+85UUikrv5U2VWqpMyw=="
    accountName="storagesci"
    containerName="python-course"

    blobService =BlockBlobService(account_name=accountName, account_key=accountey )
    blobService.create_container(containerName)
    blobService.create_blob_from_stream(containerName, "image4.jpg", file.raw)

uploadFile()
