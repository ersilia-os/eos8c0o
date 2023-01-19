# imports
import os
import csv
import sys

import torch
import torchvision

from image_dataloader import smiles_to_image, ImageData

MODEL_CKPT = "bace.pth"
DEVICE = 'cpu'

device = torch.device(DEVICE)

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# checkpoints directory
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

def load_model():
    ckpt_path = os.path.join(checkpoints_dir, MODEL_CKPT)
    model = torchvision.models.resnet18(weights=None)
    model.fc = torch.nn.Linear(model.fc.in_features, 1)  # Single node in FC layer for binary classification task
    checkpoint = torch.load(ckpt_path)
    model.load_state_dict(checkpoint)
    return model

# model to be run
def my_model(smiles_list):
    model = load_model()
    model.eval()
    img_processor = ImageData()
    outputs = list()
    for idx, smi in enumerate(smiles_list):
        path = f"{os.getcwd()}/{idx}.png"
        smiles_to_image(smi, savePath=path)
        img_tensor = img_processor.get_image(path).to(device)
        with torch.no_grad():
            prob = torch.sigmoid(model(img_tensor))
            pred = 1 if prob > 0.5 else 0  # threshold from the original model code
        outputs.append((prob.item(), pred))
        os.remove(path=path)
    return outputs

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["prob", "class"])  # header
    for o in outputs:
        writer.writerow(o)
