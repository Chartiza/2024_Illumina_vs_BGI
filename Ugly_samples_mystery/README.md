### PROJECT: 2023_Illumina_vs_BGI

## Step1. FastQC Results Comparison
check folder "step1_Reads_quality_comparison_FASTQ"
## Step2. KRAKEN aggregation
check folder "step2_KRAKEN_aggregation"

# "bad" & "ugly" sample groups
### OriginalResults_Kraken1.ipynb
Check lab parameters and their correlation with "bad" & "ugly" sample groups
- BGI batch number (No)
- Reads number (No)
- DNA concentration (No)
- DNA quality (No)
- Number of species (Yes, only for the "ugly" group)

### reRun_Kraken2.ipynb
Check if the problem connected with calculation and program. Run Kraken one more time.
- "ugly" sample groups disaperad 
- "bad" sample groups still present

### reRun other taxanomic profiling program

