# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:12:05 2023

@author: ruppg
"""

def get_expert(dict_msg):

    csv_header=['loco_class','loco_name','msg_type','asset','device','asset_uic','mvb_device','storage','open_time','close_time',
                'code','description','occurrencies']
    msg_name='event_mdfc'
    import csv
    list_msg=dict_msg[msg_name]
    
    value_mdfc=[]
    for item in list_msg:
       # print(item)
        
        loco_name=item['loco_name']
        loco_class=item['loco_class']
        msg_type=item['type']
    
        asset=item['asset']
        device=item['device']
        asset_uic=item['asset_uic']
    
        
        
        
    
        storage=item['content']['storage']
        mvb_device=item['content']['mvb_device']
        code=item['content']['code']
        occurrencies=item['content']['occurrencies']
        open_time=item['content']['open_time']
        
        
        
        
        if item['is_open']==True:
        
            close_time=''
        else:
            close_time=item['content']['close_time']
            
            
        if not item['content']['description']:
        #print("Dictionary is empty")
            description=''
        else:
            description=item['content']['description']['en']
        
        
        row_static=(loco_class,loco_name,msg_type,asset,device,asset_uic,mvb_device,storage,open_time,close_time,
                    code,description,
                   occurrencies)
        
           
        value_mdfc.append(row_static)
    


    return value_mdfc