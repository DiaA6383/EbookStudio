from pydub import AudioSegment
import os
import re
from tqdm import tqdm

def sort_key(file_path):
    # Extracting disc number and file name for sorting
    match = re.search(r'Disc (\d+)', file_path)
    disc_number = int(match.group(1)) if match else 0
    file_name = os.path.basename(file_path)
    return (disc_number, file_name)

def concatenate_audiobooks(input_directory, output_file):
    concatenated = AudioSegment.empty()
    files_to_concatenate = []

    # Walking through the directory and adding files to the list
    for subdir, dirs, files in os.walk(input_directory):
        for file in sorted(files, key=lambda x: (sort_key(os.path.join(subdir, x)))):
            if file.endswith(".mp3"):
                files_to_concatenate.append(os.path.join(subdir, file))

    # Enhanced progress bar
    with tqdm(total=len(files_to_concatenate), desc="Concatenating files", unit="file") as pbar:
        for file in files_to_concatenate:
            audiobook_segment = AudioSegment.from_mp3(file)
            concatenated += audiobook_segment
            pbar.update(1)

    concatenated.export(output_file, format="mp3")
    return output_file

# ASCII Art
print(r"""
   ____              _                                           _ _  
 |  _ \            | |                                         | | | 
 | |_) | ___   ___ | | _____    __ _ _ __ ___    ___ ___   ___ | | | 
 |  _ < / _ \ / _ \| |/ / __|  / _` | '__/ _ \  / __/ _ \ / _ \| | | 
 | |_) | (_) | (_) |   <\__ \ | (_| | | |  __/ | (_| (_) | (_) | |_| 
 |____/ \___/ \___/|_|\_\___/  \__,_|_|  \___|  \___\___/ \___/|_(_) 
                                                                     
""")

# Prompt for input directory and output file path
input_directory = input("Enter the path of the input directory: ")
output_file = input("Enter the path of the output file (including .mp3): ")

# Call the function
concatenate_audiobooks(input_directory, output_file)
