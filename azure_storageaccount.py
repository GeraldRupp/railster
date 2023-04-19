# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:42:34 2023

@author: ruppg
"""
file_path=r'C:\Users\ruppg\Desktop\DataAnalystic\Railster_Data\Output/int_0418_2023_3.csv'
file_name=r'int_0418_2023_3.csv'


def save_file_storageaccount(file_path,file_name):


    # -*- coding: utf-8 -*-
    """
    Spyder Editor
    
    This is a temporary script file.
    """
    import time
    
    from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
    import os
    
    # Set the connection string to your storage account
    connect_str = "DefaultEndpointsProtocol=https;AccountName=geraldsstorageaccount;AccountKey=01nyMBNHu7vvfrDSTZAbVNaGYaLNr8BDxT/FHb4qpXgkn32Jfxnxae6ZeHIfzTnwZ2PlXdG/rAOd+AStjFPYzQ==;EndpointSuffix=core.windows.net"
    
    # Set the name of your container and subfolder
    container_name = 'railster'
    subfolder='transformated/'+file_name+'/'
    
    
    # Set the name and path of the CSV file you want to upload
    
    
    
    
    # Create a BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    
    # Get a container client object for the container
    container_client = blob_service_client.get_container_client(container_name)
    
    
    start_time = time.time()
    # Set the name of the file you want to upload
    
    
    
    date_str = datetime.datetime.now().date().strftime('_%d%m_%Y')
    blob_name = subfolder+file_name+date_str+'.csv'
    with open(file_path, "rb") as data:
        container_client.upload_blob(blob_name, data)
        print('gg')