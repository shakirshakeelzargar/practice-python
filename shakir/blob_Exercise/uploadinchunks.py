import os
import config
#from random_data import RandomData
import base64
import datetime
import random
import string

import time
from azure.storage import CloudStorageAccount, AccessPolicy
from azure.storage.blob import BlockBlobService, PageBlobService, AppendBlobService
from azure.storage.models import CorsRule, Logging, Metrics, RetentionPolicy, ResourceTypes, AccountPermissions
from azure.storage.blob.models import BlobBlock, ContainerPermissions, ContentSettings


def randomString(stringLength=32):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

accountey="xxxxx"
accountName="xxxx"
container_name="xxxx"

blockblob_service = BlockBlobService(account_name=accountName, account_key=accountey )


def block_blob_operations():
        file_to_upload = "10MB.zip"
        block_size = 2097152
        
        # Create an page blob service object
        #blockblob_service = account.create_block_blob_service()
        #container_name = 'python-course'

        try:
            # Create a new container
            #print('1. Create a container with name - ' + container_name)
            #blockblob_service.create_container(container_name)
            
            blocks = []
            
            # Read the file
            print('2. Upload file to block blob')
            with open(file_to_upload, "rb") as file:
                file_bytes = file.read(block_size)
                while len(file_bytes) > 0:
                    block_id = randomString(10) 
                    blockblob_service.put_block(container_name, file_to_upload, file_bytes, block_id)                    
                    
                    blocks.append(BlobBlock(id=block_id))
                    
                    file_bytes = file.read(block_size)
            
            blockblob_service.put_block_list(container_name, file_to_upload, blocks)
            
            print('3. Get the block list')
            blockslist = blockblob_service.get_block_list(container_name, file_to_upload, None, 'all')
            blocks = blockslist.committed_blocks

            print('4. Enumerate blocks in block blob')
            for block in blocks:
                print('Block ' + block.id)
        finally:
            print("EXECUTED")
            print(blocks)
            #print('5. Delete container')
            #if blockblob_service.exists(container_name):
                #blockblob_service.delete_container(container_name)
block_blob_operations()