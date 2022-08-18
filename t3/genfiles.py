import os
import glob

# files = list(glob.glob(os.path.join("shots",'*.*')))
files = list(glob.glob(os.path.join("shots",'*.*')))
# print(files)


# -*- coding: utf-8 -*-
import argparse
import torch
import torchvision.models
import torchvision.transforms as transforms
from PIL import Image


theimages = files


def prepare_image(image):
    if image.mode != 'RGB':
        image = image.convert("RGB")
    Transform = transforms.Compose([
            transforms.Resize([224,224]),      
            transforms.ToTensor(),
            ])
    image = Transform(image)   
    image = image.unsqueeze(0)
    return image

def predict(image, model):
    image = prepare_image(image)
    with torch.no_grad():
        preds = model(image)
    score = preds.detach().numpy().item()
    print('Popularity score: '+str(round(score,2))+"  "+str(x))

for x in theimages:
    image = Image.open(x)
    model = torchvision.models.resnet50()
    # model.avgpool = nn.AdaptiveAvgPool2d(1) # for any size of the input
    model.fc = torch.nn.Linear(in_features=2048, out_features=1)
    model.load_state_dict(torch.load('model/model-resnet50.pth',map_location=torch.device('cpu'))) 
    model.eval()
    predict(image, model)

from torchvision.transforms import ToPILImage
from IPython.display import Image
to_img = ToPILImage()

# display tensor
a = torch.Tensor(3, 64, 64).normal_()
to_img(a)

# display imagefile
Image('frame374020.jpg')



