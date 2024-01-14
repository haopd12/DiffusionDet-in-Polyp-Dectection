import xml.etree.ElementTree as ET
import os
import json
# xml_file_path = 'E:/BKAI LAB/Code/DiffusionDet/DiffusionDet/polyp-havard/PolypsSet/dataset2019/Annotation/1.xml'
def get_annotation(path, dataset_anno_path, folder):
    full_path = os.path.join(dataset_anno_path,path)
    tree = ET.parse(full_path)
    root = tree.getroot()
    size_tag = root.find('.//size')
    width = size_tag.find('width').text
    height = size_tag.find('height').text
    anno = {
        "id": int(path[:-4]),
        "image_name": path[:-4]+'.jpg',
        "image_path": 'PolypsSet/val2019/Image/{}/{}.jpg'.format(folder,path[:-4]), 
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
      
        
dataset_anno_path = 'E:/BKAI LAB/Code/DiffusionDet/DiffusionDet/polyp-havard/PolypsSet/val2019/Annotation'
dataset_list = os.listdir(dataset_anno_path)
# dataset_list.sort()
annotations = []

for folder in dataset_list:
    list_path = os.listdir(os.path.join(dataset_anno_path, folder))
    dataset_image_path = os.listdir(os.path.join('E:/BKAI LAB/Code/DiffusionDet/DiffusionDet/polyp-havard/PolypsSet/val2019/Image',folder))
    
    # print(list_path)
    for path in list_path:
        path_check = path[:-4] + ".jpg"
        if (path_check in dataset_image_path):
            get_annotation(path, os.path.join(dataset_anno_path, folder), folder)
            print('*************{}***************'.format(path))
    # break
json_file = './valid_instance.json'
with open(json_file, 'w', encoding='utf8') as f:

    json.dump(annotations, f, indent=4, ensure_ascii=False)