# ImageMol human beta-secretase-1 (BACE-1) inhibition

This model has been developed using ImageMol, a deep learning model pretrained on 10 million unlabelled small molecules and fine-tuned in a second step to predict the binding of inhibitors to the human beta secretase 1 (BACE-1) protein. The BACE-1 dataset from MoleculeNet contains 1522 compounds with their associated pIC50. A compound with pIC50 => 7 is considered a BACE-1 inhibitor.

This model was incorporated on 2023-01-11.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8c0o`
- **Slug:** `image-mol-bace`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Alzheimer`
- **Target Organism:** `Homo sapiens`
- **Tags:** `BACE`, `Chemical graph model`, `MoleculeNet`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of BACE-1 inhibition (>0.5: Inhibitor). Compounds with pIC50 => 7 are considered BACE-1 inhibitors

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| bace_inh_prob | float | high | probability of inhibiting BACE-1 (cut-off pIC50=>7) |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8c0o](https://hub.docker.com/r/ersiliaos/eos8c0o)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8c0o.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8c0o.zip)

### Resource Consumption
- **Model Size (Mb):** `44`
- **Environment Size (Mb):** `8389`


### References
- **Source Code**: [https://github.com/ChengF-Lab/ImageMol](https://github.com/ChengF-Lab/ImageMol)
- **Publication**: [https://www.nature.com/articles/s42256-022-00557-6](https://www.nature.com/articles/s42256-022-00557-6)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [DhanshreeA](https://github.com/DhanshreeA)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos8c0o
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos8c0o
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
