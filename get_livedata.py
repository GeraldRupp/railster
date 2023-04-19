# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:22:55 2023

@author: ruppg
"""


def get_livedata(dict_msg):

    msg_name='mre_live'


    break_all=0
    list_msg=dict_msg[msg_name]
    
    value_string=[]
    value_int=[]
    value_float=[]
    value_bool=[]
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
        
        
        header=['loco_class','loco_name','type','timestamp','asset','device','asset_uic','source']
        row_static=(loco_class,loco_name,msg_type,timestamp,asset,device,asset_uic,source)
    
        
        for key, value in item['content'].items():
           #print(key, value)
    
    
            if type(value)==int:
                typeValue='int'
                value_int.append(row_static+(key,value,typeValue))
                
                
            elif type(value)==str:
                typeValue='str'
                value_string.append(row_static+(key,value,typeValue))
            elif type(value)==float:
                typeValue='float'
                value_float.append(row_static+(key,value,typeValue))
                
                
            elif type(value)==bool:
                typeValue='bool'
                value_bool.append(row_static+(key,value,typeValue))        
               # print('bool anwesend')
                
                #break_all=1
                #break
        
            else:
                print('break bei typeValue')
                break
                
        if break_all ==1:
            break
    #write_csv(msg_name+'_strings',value_string)
    #write_csv(msg_name+'_ints',value_int)
    #write_csv(msg_name+'_floats',value_float)
    #write_csv(msg_name+'_bools',value_bool)
    
    return value_string,value_int,value_float,value_bool
