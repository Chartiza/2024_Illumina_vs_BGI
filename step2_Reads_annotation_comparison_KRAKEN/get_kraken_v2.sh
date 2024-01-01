#!/bin/bash
#SBATCH -J kraken
#SBATCH --partition=amd
#SBATCH -t 190:00:00
#SBATCH --error=kraken_err1
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=12
#SBATCH --mem=512G
#SBATCH --mail-user=<pantiukh@gmail.com>
#SBATCH --mail-type=BEGIN,END,FAIL

module load kraken2/2.1.1
module load bracken/2.8
module load seqtk

PWD='/gpfs/space/home/pantiukh/2023_Illumina_vs_BGI/Kraken'
bgi_path='/gpfs/space/GI/GV/EGCUT_data/omics_data/microbiomics/BGI_raw'
KRAKEN_DB='/gpfs/space/home/pantiukh/release214/GTDB_Kraken2'

while read FQ; do

    # Illumina reads
    base="${FQ%_*}"
    ill1="$base"_350.raw.fq1.gz
    ill2="$base"_350.raw.fq2.gz
    
    # sample name
    NAMEs=`echo "$ill1" | cut -d'/' -f16`
    echo "Run sample $NAMEs"
    echo $(date)

    # BGI reads
    bgi1=$bgi_path'/*/'$NAMEs'/*_1.fq.gz'
    bgi2=$bgi_path'/*/'$NAMEs'/*_2.fq.gz'

    # Define Illumina reads number
    rn_ill=$(expr $(zcat $ill1 | wc -l) / 4)

    # Cut BGI reads files
    seqtk sample -s100 $bgi1 $rn_ill > /gpfs/space/home/pantiukh/2023_Illumina_vs_BGI/Kraken/temp/bgi_$NAMEs'_1.fq'
    seqtk sample -s100 $bgi2 $rn_ill > /gpfs/space/home/pantiukh/2023_Illumina_vs_BGI/Kraken/temp/bgi_$NAMEs'_2.fq'

    rn_bgi_new=$(expr $(wc -l < /gpfs/space/home/pantiukh/2023_Illumina_vs_BGI/Kraken/temp/bgi_$NAMEs'_1.fq') / 4)

    echo "Illumina RN: $rn_ill"
    echo "BGI RN: $rn_bgi_new"
    echo $(date)

    # Run Kraken for Illumina
    kraken2 --paired --gzip-compressed --threads 20 --db $KRAKEN_DB $ill1 $ill2 --output $PWD/temp/ill_${NAMEs}.kraken2 --report $PWD/temp/ill_${NAMEs}.kreport --use-names
    bracken -d $KRAKEN_DB -i $PWD/temp/ill_${NAMEs}.kreport -o $PWD/kraken_Illumina/ill_${NAMEs}.bracken -r 150 -l 'S' -t 20

    # Run Kraken for BGI
    kraken2 --paired --gzip-compressed --threads 20 --db $KRAKEN_DB $bgi1 $bgi2 --output $PWD/temp/bgi_${NAMEs}.kraken2 --report $PWD/temp/bgi_${NAMEs}.kreport --use-names
    bracken -d $KRAKEN_DB -i $PWD/temp/bgi_${NAMEs}.kreport -o $PWD/kraken_BGI/bgi_${NAMEs}.bracken -r 150 -l 'S' -t 20

    # remove temporary files
    rm $PWD/temp/*

    echo $(date)
    echo '...............'

done </gpfs/space/home/pantiukh/2023_Illumina_vs_BGI/Kraken/all_Illumina_raw_path.csv
 
module purge
 