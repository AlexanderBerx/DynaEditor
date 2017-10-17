import os
import json
from maya import cmds


def get_attr_type(node, attr):
    try:
        return cmds.attributeQuery(attr, node=node, attributeType=True)
    except RuntimeError:
        return None
        

def get_attr_min(node, attr):
    if cmds.attributeQuery(attr, node=node, minExists=True):
        return cmds.attributeQuery(attr, node=node, min=True)
    
    
def get_attr_max(node, attr):
    if cmds.attributeQuery(attr, node=node, maxExists=True):
        return cmds.attributeQuery(attr, node=node, max=True)
    
        
def get_attr_default_value(node, attr):
    try: 
        return cmds.attributeQuery(attr, node=node, listDefault=True)
    except RuntimeError:
        return None
        
    
def get_attr_enum(node, attr):
    if not cmds.attributeQuery(attr, node=node, enum=True):
        return None
    # if the enum can't be displayed as a string no point to check it
    if not cmds.getAttr("{0}.{1}".format(node, attr), asString=True):
        return None
    
    attr_value = cmds.getAttr("{0}.{1}".format(node, attr))
    attr_range = cmds.attributeQuery(attr, node=node, range=True)
    attr_enum = []
    
    for i in range(int(attr_range[0]), int(attr_range[1])+1):
        cmds.setAttr("{0}.{1}".format(node, attr), i)
        value = cmds.getAttr("{0}.{1}".format(node, attr), asString=True)
        if not value:
            return attr_enum
        attr_enum.append(value)
        
    cmds.setAttr("{0}.{1}".format(node, attr), attr_value)
    return attr_enum
    
    
def iter_obj_attrs(obj):
    for attr in cmds.listAttr(obj, write=True):
        # if type fetching fails no point in checking further
        # same goes for child attrs
        _type = get_attr_type(obj, attr)
        if not _type or cmds.attributeQuery(attr, node=obj, listParent=True):
            continue
            
        nice_name = cmds.attributeQuery(attr, node=obj, niceName=True)
        _min = get_attr_min(obj, attr)
        _max = get_attr_max(obj, attr)
        default_value = get_attr_default_value(obj, attr)
        options = get_attr_enum(obj, attr)
        file_path = cmds.attributeQuery(attr, node=obj, usedAsFilename=True)
        color = cmds.attributeQuery(attr, node=obj, usedAsColor=True)
            
        categories = cmds.attributeQuery(attr, node=obj, categories=True)
        
        yield [_type, attr, nice_name, _min, _max, default_value, options, file_path, color, categories]
        

def attr_mapping_to_file(obj, output):
    output = os.path.normpath(output)
    with open(output, 'w') as file_out:
        json.dump(list(iter_obj_attrs(obj)), file_out, indent=4)
