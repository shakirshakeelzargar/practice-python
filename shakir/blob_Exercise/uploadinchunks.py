from azure.storage.blob import BlockBlobService
import base64
import os
accountey="pRy7Hsb9wIbCWkVRgrTioBRiPKuiTpGnoxmIZ7p5SUgMedIsT335m0ad7ap7m/SHoXf+85UUikrv5U2VWqpMyw=="
accountName="storagesci"
container_name="python-course"
file_path='./files/file.csv'
blob_name='sss.csv'

blob_service =BlockBlobService(account_name=accountName, account_key=accountey )

def upload():
    blob_service.create_container(container_name, None, None, False)
    #blob_service.put_block_blob(container_name, blob_name, '', 'BlockBlob')

    chunk_size = 65536
    block_ids = []
    index = 0
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if data:
                length = len(data)
                block_id = base64.b64encode(bytes(index))
                blob_service.put_block(container_name, blob_name, data, block_id)
                block_ids.append(block_id)
                index += 1
            else:
                break

    resp = blob_service.put_block_list(container_name, blob_name, block_ids)

def download(blob_service, container_name, blob_name, file_path):
    props = blob_service.get_blob_properties(container_name, blob_name)
    blob_size = int(props['content-length'])

    chunk_size = 65536
    index = 0
    with open(file_path, 'wb') as f:
        while index < blob_size:
            range = 'bytes=' + str(index) + '-' + str(index + chunk_size - 1)
            data = blob_service.get_blob(container_name, blob_name, x_ms_range=range)
            length = len(data)
            index += length
            if length > 0:
                f.write(data)
                if length < chunk_size:
                    break
            else:
                break

upload()