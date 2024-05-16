### PROJECT: 2023_Illumina_vs_BGI
## Step1. FastQC Results Comparison
collaboration project between Kateryna Pantiukh & Elin Org and Tomasz Kościółek & Kinga Zielińska & Łukasz Szydłowski

This repository contains a script to compare the results of the FastQC program for the same samples sequenced using two different NGS platforms: Illumina and BGI. The FastQC program is commonly used to evaluate the quality of Next-Generation Sequencing (NGS) reads.

### Prerequisites

To run the script and reproduce the results, you need to have the following software and data installed:

- FastQC (version 0.11.9): Link to FastQC https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
- Illumina sequencing data
- BGI sequencing data

### Analysis Scheme
<img width="728" alt="Screenshot 2023-06-07 at 12 17 45" src="https://github.com/Chartiza/2023_Illumina_vs_BGI-FastQC/assets/15068419/f7be2eca-f03c-43b0-8eca-0d5bc5945329">

### Results
1. Total number of sequencing was much higher at BGI cohort.
2. Both cohort have 0 Sequences flagged as poor quality.
3. All reads from both cohort are 150 bp lengh.
4. Here is a plot representing the CG content of the same samples for different platforms.

![GC_content](https://github.com/Chartiza/2023_Illumina_vs_BGI-FastQC/assets/15068419/ca119253-d1ca-41b9-b897-bc0f8e9385b9)

6. All samples from both cohort pass Per base sequence quality check.
7. Here is a distribution of Sequence Duplication Levels check results:

BGI. Sequence Duplication Levels 
- pass    1561
- warn     297
- fail      24

Illumina. Sequence Duplication Levels 
- pass    1743
- warn     138
- fail       1

8. Here is a plot representing the Total Deduplicated Percentage of the same samples for different platforms. The point colored according to Sequence Duplication Levels check result of BGI platform.

![Total_Deduplicated_Percentage](https://github.com/Chartiza/2023_Illumina_vs_BGI-FastQC/assets/15068419/56340eef-f394-4a8e-a612-fbbb15ed0f5c)

9. Here is a distribution of Sequence Duplication Levels check results:

BGI. Overrepresented sequences 
- pass    1881
- warn       1

Illumina. Overrepresented sequences 
- pass    1880
- warn       2

10. All samples from both cohort pass Adapter Content check.

---
This project is licensed under the MIT License.

