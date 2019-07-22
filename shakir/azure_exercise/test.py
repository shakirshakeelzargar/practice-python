from azure.storage.blob import BlockBlobService
from io import BytesIO
from shutil import copyfileobj 
accountkey="pRy7Hsb9wIbCWkVRgrTioBRiPKuiTpGnoxmIZ7p5SUgMedIsT335m0ad7ap7m/SHoXf+85UUikrv5U2VWqpMyw=="
accountName="storagesci"
containerName="python-course"
with BytesIO() as input_blob:
    with BytesIO() as output_blob:
        block_blob_service = BlockBlobService(account_name='storagesci', account_key='accountkey')
        # Download as a stream
        block_blob_service.get_blob_to_stream(containerName, 'myinputfilename', input_blob)

        # Do whatever you want to do - here I am just copying the input stream to the output stream
        copyfileobj(input_blob, output_blob)


        # Create the a new blob
        block_blob_service.create_blob_from_stream('mycontainer', 'myoutputfilename', output_blob)

        # Or update the same blob
        block_blob_service.create_blob_from_stream('mycontainer', 'myinputfilename', output_blob)