### PROJECT: 2023_Illumina_vs_BGI
## Step1. FastQC Results Comparison
collaboration project between Kateryna Pantiukh & Elin Org and Tomasz Kościółek & Kinga Zielińska & Łukasz Szydłowski

This repository contains a script to compare the results of the Kraken program for the same samples sequenced using two different NGS platforms: Illumina and BGI. The Kraken program is commonly used to evaluate the quality of Next-Generation Sequencing (NGS) reads.

>
>!! We used GTDB release 214 database as a custom database for Kraken.
>
### Prerequisites

To run the script and reproduce the results, you need to have the following software and data installed:

- Kraken (version 2.1.1): Link https://github.com/DerrickWood/kraken
- Braken (version 2.8): Link https://github.com/jenniferlu717/Bracken
- Prebuild GTDB custom Kraken database
- seqtk Link https://github.com/lh3/seqtk
- Illumina sequencing data
- BGI sequencing data
  
### Analysis Scheme
<img width="1468" alt="pipeline" src="https://github.com/Chartiza/2023_Illumina_vs_BGI/assets/15068419/9976336c-b472-4ecc-b43a-36813df91577">

### Results
