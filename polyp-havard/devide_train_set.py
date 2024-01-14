import xml.etree.ElementTree as ET
import os
import json
# xml_file_path = 'E:/BKAI LAB/Code/DiffusionDet/DiffusionDet/polyp-havard/PolypsSet/train2019/Annotation/1.xml'
def get_annotation(path, train_anno_path):
    full_path = os.path.join(train_anno_path,path)
    tree = ET.parse(full_path)
    root = tree.getroot()
    size_tag = root.find('.//size')
    width = size_tag.find('width').text
    height = size_tag.find('height').text
    anno = {
        "id": int(path[:-4]),
        "image_name": path[:-4]+'.jpg',
        "image_path": './PolypsSet/train2019/Image/{}.jpg'.format(path[:-4]), 
        "width": int(width),
        "height": int(height)
    }
    anno["annotation"] = []
    elements = root.findall('.//object')
    if (elements is not None):
        for ele in elements:
            bbox = ele.find('bndbox')
            name = ele.find('name').text
            x_min = bbox.find('xmin').text
            y_min = bbox.find('ymin').text
            x_max = bbox.find('xmax').text
            y_max = bbox.find('ymax').text
            anno["annotation"].append({
                "category": name,
                "x_min": int(x_min),
                "x_max": int(x_max),
                "y_min": int(y_min),
                "y_max": int(y_max)
            })
    if len(anno["annotation"]) > 0:
        annotations.append(anno)
      
        
train_anno_path = 'E:/BKAI LAB/Code/DiffusionDet/DiffusionDet/polyp-havard/PolypsSet/train2019/Annotation'
train_list = os.listdir(train_anno_path)
# train_list.sort()
annotations = []
for path in train_list:
    get_annotation(path, train_anno_path)
    print('*************{}***************'.format(path))
    # break
json_file = './train_instance.json'
with open(json_file, 'w', encoding='utf8') as f:

    json.dump(annotations, f, indent=4, ensure_ascii=False)