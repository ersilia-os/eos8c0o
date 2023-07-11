# ImageMol human beta-secretase-1 (BACE-1) inhibition

This model has been developed using ImageMol, a deep learning model pretrained on 10 million unlabelled small molecules and fine-tuned in a second step to predict the binding of inhibitors to the human beta secretase 1 (BACE-1) protein. The BACE-1 dataset from MoleculeNet contains 1522 compounds with their associated pIC50. A compound with pIC50 => 7 is considered a BACE-1 inhibitor.

## Identifiers

* EOS model ID: `eos8c0o`
* Slug: `image-mol-bace`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of BACE-1 inhibition (>0.5: Inhibitor). Compounds with pIC50 => 7 are considered BACE-1 inhibitors

## References

* [Publication](https://www.nature.com/articles/s42256-022-00557-6)
* [Source Code](https://github.com/ChengF-Lab/ImageMol)
* Ersilia contributor: [DhanshreeA](https://github.com/DhanshreeA)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos8c0o)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8c0o.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos8c0o) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://www.nature.com/articles/s42256-022-00557-6) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!