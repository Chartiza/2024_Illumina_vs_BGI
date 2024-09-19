import os
import re
import pandas as pd

def parse_file(filename):
    data = {}

    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract information using regular expressions
    data['Filename'] = re.search(r'Filename\s+(.+)', lines[3]).group(1)
    data['Platform'] = 'Illumina'
    data['Total Sequences'] = int(re.search(r'Total Sequences\s+(\d+)', lines[6]).group(1))
    data['Sequences flagged as poor quality'] = int(re.search(r'Sequences flagged as poor quality\s+(\d+)', lines[7]).group(1))
    data['Sequence length'] = int(re.search(r'Sequence length\s+(\d+)', lines[8]).group(1))
    data['%GC'] = int(re.search(r'%GC\s+(\d+)', lines[9]).group(1))
    data['Per base sequence quality'] = re.search(r'>>Per base sequence quality\s+(\w+)', lines[11]).group(1)

    # Search for 'Sequence Duplication Levels' within a range of lines
    start_line = 35000
    end_line = len(lines)
    pattern = r'>>Sequence Duplication Levels\s+(\w+)'

    for line_num in range(start_line, end_line):
        if line_num < len(lines):
            line = lines[line_num]
            match = re.search(pattern, line)
            if match:
                data['Sequence Duplication Levels'] = match.group(1)
                break
    else:
        data['Sequence Duplication Levels'] = 'not found'

    # Search for 'Total Deduplicated Percentage' within a range of lines
    pattern = r'#Total Deduplicated Percentage\s+(\w+)'

    for line_num in range(start_line, end_line):
        if line_num < len(lines):
            line = lines[line_num]
            match = re.search(pattern, line)
            if match:
                data['Total Deduplicated Percentage'] = float(re.search(pattern, line).group(1))
                break
    else:
        data['Total Deduplicated Percentage'] = 'not found'

    # Search for 'Overrepresented sequences' within a range of lines
    pattern = r'>>Overrepresented sequences\s+(\w+)'

    for line_num in range(start_line, end_line):
        if line_num < len(lines):
            line = lines[line_num]
            match = re.search(pattern, line)
            if match:
                data['Overrepresented sequences'] = match.group(1)
                break
    else:
        data['Overrepresented sequences'] = 'not found'

    # Search for 'Adapter Content' within a range of lines
    pattern = r'>>Adapter Content\s+(\w+)'

    for line_num in range(start_line, end_line):
        if line_num < len(lines):
            line = lines[line_num]
            match = re.search(pattern, line)
            if match:
                data['Adapter Content'] = match.group(1)
                break
    else:
        data['Adapter Content'] = 'not found'

    return data

### Apply function to all files in a folder

def process_files_in_folder(folder_path):
    data_list = []

    # Traverse through the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt') and file.startswith('fastqc_data'):
                file_path = os.path.join(root, file)
                parsed_data = parse_file(file_path)
                data_list.append(parsed_data)

    # Create a DataFrame from the parsed data list
    df = pd.DataFrame(data_list)

    # Write the DataFrame to a table file
    output_file = os.path.join(result_path, 'Combined_illumina_results.txt')
    write_dataframe_to_file(df, output_file)

def write_dataframe_to_file(dataframe, filename):
    dataframe.to_csv(filename, sep='\t', index=False)

# Usage example
result_path = '/gpfs/space/home/pantiukh/2023_Illumina_vs_BGI/fastQC/parse_fastqc'
folder_path = '/gpfs/space/home/pantiukh/2023_Illumina_vs_BGI/fastQC/Illumina_raw/read_2'
process_files_in_folder(folder_path)
 