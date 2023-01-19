# ImageMol BACE

## Model Identifiers

- Slug: image-mol-bace
- Ersilia ID: eos8c0o
- Tags: BACE, classification

## Model Description

- Input: SMILES string
- Output: inference probability and predicted class
- Model type: Binary Classification
- Training set: 1513 compounds in the data set from MoleculeNet
- Mode of training: No training was carried out; the model checkpoint fined tuned on BACE dataset have been provided by the authors.

## Source Code

- Code: https://github.com/HongxinXiang/ImageMol
- Checkpoints: https://drive.google.com/file/d/1q9-QCGbaACzw-QO2pOrK-FrGMr1yz1L0/view?usp=sharing

## License

License used by the original source code: MIT License
Ersilia's License: GPLv3

## History

- This model was downloaded and incorporated into Ersilia on 16/01/2023
- Only the image pre-processing and smile-to-image conversion code have been copied over from the model codebase. Normal PyTorch syntax is used to run inference on new samples.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
