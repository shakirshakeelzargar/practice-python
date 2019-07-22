from  azure.storage.blob import BlockBlobService

def uploadFile():
    accountey="xxxxx"
    accountName="xxxx"
    containerName="xxxx-xxxx"

    blobService =BlockBlobService(account_name=accountName, account_key=accountey )
    blobService.create_container(containerName)
    blobService.create_blob_from_path(containerName, "image1.jpg", "./images/python.jpg")

uploadFile()