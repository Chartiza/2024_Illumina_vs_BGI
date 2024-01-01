import os
import pandas as pd

# Get a list of all files in the current directory that start with 'bgi'
dir_path = '/gpfs/space/home/pantiukh/2023_Illumina_vs_BGI/Kraken/kraken_Illumina'  # current directory
filenames = [f for f in os.listdir(dir_path) if f.startswith('ill')]

# Initialize an empty DataFrame to store the merged data
merged_df = pd.DataFrame()

for i, filename in enumerate(filenames):
    # Read each file into a pandas DataFrame
    df = pd.read_csv(os.path.join(dir_path, filename), sep='\t')

    # Keep only the rows with 'fraction_total_reads' > 0.01
    df = df[df['fraction_total_reads'] > 0.01]

    # Get the file name without extension
    filename_no_ext = os.path.splitext(filename)[0]

    # If this is the first file, initialize the merged_df DataFrame
    if i == 0:
        merged_df = df[['name', 'fraction_total_reads']]
        merged_df.columns = ['name', filename_no_ext]  # Rename the column to the file's name (without extension)
    else:
        # If this is not the first file, merge it with the existing DataFrame
        df_temp = df[['name', 'fraction_total_reads']]
        df_temp.columns = ['name', filename_no_ext]  # Rename the column to the file's name (without extension)
        merged_df = pd.merge(merged_df, df_temp, on='name', how='outer')

# Replace all NaN values with 0 (you can skip this step if NaN values are fine)
merged_df.fillna(0, inplace=True)

# Write the merged DataFrame to a CSV file
merged_df.to_csv('Illumina_merged_output_part.csv', index=False) 
