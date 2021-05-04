# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:05:25 2020

@author: waisullah yousofi
"""


import os,io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'automated-shape-297117-968ac5ca917b.json'
client=vision.ImageAnnotatorClient()


def detectText(img):
    with io.open(img,'rb') as image_file:
        content=image_file.read()
#storing the binary information into content variable.

    image = vision.Image(content=content)
#passing the image
    
    response= client.text_detection(image=image)
#vision api is going to use text detection method to extract the texts of the image
    
    texts=response.text_annotations
#and here we r storing detected text in response object

    listoftxt=[]
    file1=open("detectedtxtsfile.txt",'w',encoding='utf-8')
    for text in texts:
        listoftxt.append(text.description)
    file1.write(listoftxt[0])
    file1.close()
    print(listoftxt[1:])
        

filename='hand.PNG'
folder_path=r'D:\Downloads\My document\Virtualenvt\googleVisionAPI'
texts=detectText(os.path.join(folder_path,filename))
print(texts)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        