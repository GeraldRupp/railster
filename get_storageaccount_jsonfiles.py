# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:04:37 2023

@author: ruppg
"""

nogo_list=['position','merged','mre_packed','mre_unpacked','loco_power_on','external_gps','default_communication','alert_railpowerbox_nocom'
          ,'no_power_on','log_mdfc','alert_mdfc_download']



def get_jsonfile_names():

    from azure.storage.blob import BlobServiceClient
    
    account_name = 'geraldsstorageaccount'
    account_key = '01nyMBNHu7vvfrDSTZAbVNaGYaLNr8BDxT/FHb4qpXgkn32Jfxnxae6ZeHIfzTnwZ2PlXdG/rAOd+AStjFPYzQ=='
    container_name = 'railster'
    
    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
    container_client = blob_service_client.get_container_client(container_name)
    
    ##########################################
    ## Get all json-files in container
    ##########################################
    json_files=[]
    # List all the blobs in the container
    blobs = container_client.list_blobs()
    
    # Iterate through each blob in the container
    for blob in blobs:
        # Check if the blob is a JSON file
        if blob.name.endswith('.json'):
            # Print the file name
            json_files.append(blob.name)
    
    
    ##########################################
    ## select several json-files randomly 
    ##########################################
    import random
    
    # Define a list of items
    
    
    # Use random.sample to select 5 items randomly
    random_json = random.sample(json_files, 10)
    
    return json_files,random_json




def load_railster_jsonfiles(container_client,random_json,nogo_list):
    import json
    dict_msg={}

    for json_file in random_json:
        # Get a reference to the blob
        blob_client = container_client.get_blob_client(json_file)
    
        # Download the blob's content as bytes
        blob_data = blob_client.download_blob().content_as_bytes()
    
        # Convert the bytes to string using utf-8-sig encoding
        # Convert the bytes to string
    
        json_string = blob_data.decode('utf-8-sig')
           
            
        json_strings = json_string.split("\r\n")
    
    # Load each JSON string as a JSON object
        for json_str in json_strings:
            # Ignore any empty strings
            if not json_str.strip():
                continue
    
            # Load the JSON string as a JSON object
            json_obj = json.loads(json_str)
    
    
        
        # 
            msgtype_i=json_obj['type'] 
            
            
            if msgtype_i in nogo_list:
                continue
            
            
            
            if msgtype_i not in dict_msg.keys():
                dict_msg[msgtype_i ] = []
    
    
    
            dict_msg[msgtype_i].append(json_obj)
            
    return dict_msg