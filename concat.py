from pydub import AudioSegment
import os
from tqdm import tqdm

def concatenate_in_folder(folder_path, output_file):
    """
    Concatenates all MP3 files in the given subfolder into a single MP3 file.

    Parameters:
    folder_path (str): The path to the subfolder containing MP3 files.
    output_file (str): The path where the concatenated MP3 file will be saved.
    """
    concatenated = AudioSegment.empty()
    files_to_concatenate = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]

    with tqdm(total=len(files_to_concatenate), desc=f"Concatenating in {folder_path}", unit="file") as pbar:
        for file in sorted(files_to_concatenate):
            file_path = os.path.join(folder_path, file)
            audiobook_segment = AudioSegment.from_mp3(file_path)
            concatenated += audiobook_segment
            pbar.update(1)

    concatenated.export(output_file, format="mp3")

# ASCII Art
print(r"""
   ____              _                                           _ _  
 |  _ \            | |                                         | | | 
 | |_) | ___   ___ | | _____    __ _ _ __ ___    ___ ___   ___ | | | 
 |  _ < / _ \ / _ \| |/ / __|  / _` | '__/ _ \  / __/ _ \ / _ \| | | 
 | |_) | (_) | (_) |   <\__ \ | (_| | | |  __/ | (_| (_) | (_) | |_| 
 |____/ \___/ \___/|_|\_\___/  \__,_|_|  \___|  \___\___/ \___/|_(_) 
                                                                     
""")

# Prompt for input and output directory
input_directory = input("Enter the path of the main directory: ")
output_directory = input("Enter the path for the output files: ")

# Ensure output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each subfolder
for folder in os.listdir(input_directory):
    folder_path = os.path.join(input_directory, folder)
    if os.path.isdir(folder_path):
        output_file = os.path.join(output_directory, f"concatenated_{folder}.mp3")
        concatenate_in_folder(folder_path, output_file)
