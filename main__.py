# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:12:56 2023

@author: ruppg
"""
from get_storageaccount_jsonfiles import get_jsonfile_names, load_railster_jsonfiles


from railster_jsonfiles_extract import get_expert, get_mrealert,get_livedata







from write_to_csv import write_to_csv



import time


from azure.storage.blob import BlobServiceClient
    
account_name = 'geraldsstorageaccount'
account_key = '01nyMBNHu7vvfrDSTZAbVNaGYaLNr8BDxT/FHb4qpXgkn32Jfxnxae6ZeHIfzTnwZ2PlXdG/rAOd+AStjFPYzQ=='
container_name = 'railster'
    
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
container_client = blob_service_client.get_container_client(container_name)





start_time = time.time()


nogo_list=['position','merged','mre_packed','mre_unpacked','loco_power_on','external_gps','default_communication','alert_railpowerbox_nocom'
          ,'no_power_on','log_mdfc','alert_mdfc_download']




json_files,random_json=get_jsonfile_names()







dict_msg=load_railster_jsonfiles(container_client,random_json,nogo_list)


max_rows_per_file =1700000
output_folder = r"C:\Users\ruppg\Desktop\DataAnalystic\Railster_Data\Output"


value_mdfc=get_expert(dict_msg)
write_to_csv(dict_msg, max_rows_per_file, output_folder,'msg')


value_alert=get_mrealert(dict_msg)
write_to_csv(value_alert, max_rows_per_file, output_folder,'alert')


value_string,value_int,value_float,value_bool=get_livedata(dict_msg)

    
live_type='string'
write_to_csv(value_string, max_rows_per_file, output_folder,live_type)
live_type='int'
write_to_csv(value_int, max_rows_per_file, output_folder,live_type)
live_type='float'
write_to_csv(value_float, max_rows_per_file, output_folder,live_type)
live_type='bool'
write_to_csv(value_bool, max_rows_per_file, output_folder,live_type)










end_time = time.time()

print(f"Script took {end_time - start_time:.6f} seconds to execute.")