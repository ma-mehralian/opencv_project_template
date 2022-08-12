# Author: ma.mehralian

import numpy as np
import cv2 as cv

import os
from os import listdir
from os.path import isfile, join, exists
from lxml import etree
import logging
import io

def recursive_parse_xml_to_dict(xml):
  """Recursively parses XML contents to python dict.
  We assume that `object` tags are the only ones that can appear
  multiple times at the same level of a tree.
  Args:
    xml: xml tree obtained by parsing XML file contents using lxml.etree
  Returns:
    Python dictionary holding XML contents.
  """
  if not xml:
    return {xml.tag: xml.text}
  result = {}
  for child in xml:
    child_result = recursive_parse_xml_to_dict(child)
    if child.tag != 'object':
      result[child.tag] = child_result[child.tag]
    else:
      if child.tag not in result:
        result[child.tag] = []
      result[child.tag].append(child_result[child.tag])
  return {xml.tag: result}

class App:
    datasets = []
    label_map = {}
    alow_overwrite = False;
    
    # dataset = [{ 
    #    "input_dir":"...", 
    #    "output_dir":"...",
    #    "to_gray":False,
    #    "crop_roi": [x,y,w,h]
    #  },{...}]
    #
    # label_map = { "class_1": 0, "class_2":1, ... }
    #
    def __init__(self, datasets, label_map):
        self.datasets = datasets
        self.label_map = label_map

    def run(self):
        train_file = open('train.txt', 'w')
        for set in self.datasets:
            input_dir = set["input_dir"]
            output_dir = set["output_dir"] if "output_dir" in set else set["input_dir"]
            logging.info('Reading from %s', input_dir)
            xml_files = [f for f in listdir(input_dir) if isfile(join(input_dir, f)) and f.endswith(".xml")]
            for idx, x_file in enumerate(xml_files):
                if idx % 100 == 0:
                    logging.info('On image %d of %d', idx, len(xml_files))

                xml_path = os.path.join(input_dir, x_file)
                with open(xml_path, 'r') as fid:
                    xml_str = fid.read()
                xml = etree.fromstring(xml_str)
                data = recursive_parse_xml_to_dict(xml)['annotation']
                image_name = data['filename']
                image_path = os.path.join(output_dir, image_name)
                #--- read image if it neccessary
                if all(x in set for x in ['to_gray', 'crop_roi']) or set["input_dir"] != set["output_dir"]:
                    img = cv.imread(os.path.join(input_dir, image_name))
                    write_img = True
                
                #--- gray image
                if "to_gray" in set:
                    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                    image_path = os.path.join(output_dir, image_name[:-4]+"_gray.png")
                
                #--- crop image
                roi_rect = None
                if "crop_roi" in set:
                    roi_rect = set["crop_roi"]
                    img = img[roi_rect[0]:roi_rect[0]+roi_rect[2],
                            roi_rect[1]:roi_rect[1]+roi_rect[3]]
                
                if write_img:
                    if exists(image_path):
                        image_path = image_path[:-4]+"_.png"
                    cv.imwrite(image_path, img)
                    
                yolo_str = self.voc2yolo(data, roi_rect)
                yolo_path = image_path[:-4]+".txt"
                with open(yolo_path, 'w') as fid:
                    fid.write(yolo_str)
                    fid.close()
                #print(yolo_path)
                #print(yolo_str)
                train_file.write(image_path+"\n")
        train_file.close()

    def voc2yolo(self, xml, roi_rect):
        yolo_str = ""
        width = int(xml['size']['width'])
        height = int(xml['size']['height'])
        if 'object' in xml:
            for obj in xml['object']:
                difficult = bool(int(obj['difficult']))
                class_str =  obj['name'].lower()
                xmin = max(int(obj['bndbox']['xmin']), 1)
                xmax = min(int(obj['bndbox']['xmax']), width)
                ymin = max(int(obj['bndbox']['ymin']), 1)
                ymax = min(int(obj['bndbox']['ymax']), height)
                if(roi_rect):
                    xmin = min(0, xmin - roi_rect[0])
                    ymin = min(0, ymin - roi_rect[1])
                    xmax = min(0, min(xmax, roi_rect[0]+roi_rect[2])- roi_rect[0])
                    ymax = min(0, min(ymax, roi_rect[1]+roi_rect[3])- roi_rect[1])
                yolo_str = "{}{} {:.4f} {:.4f} {:.4f} {:.4f}".format(
                    yolo_str if not yolo_str else (yolo_str+"\n"),
                    self.label_map[class_str],
                    ((xmin+xmax)/2)/width, ((ymin+ymax)/2)/height, (xmax-xmin)/width, (ymax-ymin)/height)
                    # xmin/width, ymin/height, (xmax-xmin)/width, (ymax-ymin)/height)
        return yolo_str
                
def main():
    logging.basicConfig(level=logging.DEBUG)
    root_dir = "D:/path/to/voc/xmls"
    datasets = [{
        "input_dir": root_dir+"/voc",
        "output_dir": root_dir+"/yolo",
      }]
    label_map = { "car": 0, "bike":1, "truck":3 }
    app = App(datasets ,label_map)
    app.run()

if __name__ == "__main__":
    main()