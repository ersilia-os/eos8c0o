# ImageMol human beta-secretase-1 (BACE-1) inhibition

Flags binders of human beta-secretase 1, the protease whose cleavage of amyloid precursor protein initiates amyloid-beta production. The MoleculeNet BACE-1 collection of roughly 1,500 compounds with measured pIC50 values supplied the training signal, thresholded so that compounds at pIC50 of 7 or above count as inhibitors. The served weights are the authors' own fine-tuning of ImageMol, an encoder pretrained on ten million unlabelled molecules drawn as images. The dataset is small and centred on a single target, so coverage of other chemistry is thin.

This model was incorporated on 2023-01-11.Last packaged on 2026-09-25.

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
- **Interpretation:** Probability of BACE-1 inhibition, with inhibitors defined at pIC50 of 7 or above.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| bace_inh_prob | float | high | probability of inhibiting BACE-1 (cut-off pIC50=>7) |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8c0o](https://hub.docker.com/r/ersiliaos/eos8c0o)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8c0o.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8c0o.zip)

### Resource Consumption
- **Model Size (Mb):** `44`
- **Environment Size (Mb):** `1215`
- **Image Size (Mb):** `1337.83`

**Computational Performance (seconds):**
- 10 inputs: `26.69`
- 100 inputs: `17.04`
- 10000 inputs: `171.51`

### References
- **Source Code**: [https://github.com/ChengF-Lab/ImageMol](https://github.com/ChengF-Lab/ImageMol)
- **Publication**: [https://doi.org/10.1038/s42256-022-00557-6](https://doi.org/10.1038/s42256-022-00557-6)
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
