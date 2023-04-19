# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:22:02 2023

@author: ruppg
"""

def get_mrealert(dict_msg):   
    
    msg_name='mre_alert'
    header=['loco_class','loco_name','type','timestamp','asset','device','asset_uic','source','Fehler_Name','Fehler_Code']



    
    import csv
    import io
    
    break_all=0
    list_msg=dict_msg[msg_name]

    value_alert=[]
    for item in list_msg:
       # print(item)

        loco_name=item['loco_name']
        loco_class=item['loco_class']
        msg_type=item['type']
        timestamp=item['timestamp']
        asset=item['asset']
        device=item['device']
        asset_uic=item['asset_uic']
        source=item['source']



        row_static=(loco_class,loco_name,msg_type,timestamp,asset,device,asset_uic,source)

        Fehler_Name=item['content']['name']
        Fehler_Code=list(item['content']['context'].keys())[0]

        row_new=row_static+(Fehler_Name,Fehler_Code)

        value_alert.append(row_new)
    
            
    return value_alert