from pydub import AudioSegment
import os
import re
from tqdm import tqdm

def sort_key(file_path):
    """
    Custom sorting function to sort files first by disk number and then alphabetically.
    """
    match = re.search(r'Disc (\d+)', file_path)
    if match:
        return (int(match.group(1)), file_path)
    return (0, file_path)

def concatenate_audiobooks(input_directory, output_file):
    """
    Concatenates all MP3 files in the given directory and its subdirectories into a single MP3 file.

    Parameters:
    input_directory (str): The path to the directory containing the audiobook chapters.
    output_file (str): The path where the concatenated audiobook file will be saved.

    Returns:
    str: The path to the concatenated audiobook file.
    """
    files_to_concatenate = []
    for subdir, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".mp3"):
                files_to_concatenate.append(os.path.join(subdir, file))

    files_to_concatenate.sort(key=sort_key)

    # Display the concatenation order
    print("The following files will be concatenated in this order:")
    for file in files_to_concatenate:
        print(file)

    # Ask user to proceed or not
    proceed = input("Do you want to proceed with concatenation? (yes/no): ").strip().lower()
    if proceed != 'yes':
        print("Concatenation cancelled.")
        return

    concatenated = AudioSegment.empty()
    for file in tqdm(files_to_concatenate, desc="Concatenating files", unit="file"):
        audiobook_segment = AudioSegment.from_mp3(file)
        concatenated += audiobook_segment

    concatenated.export(output_file, format="mp3")
    return output_file

# Prompt for input directory and output file path
input_directory = input("Enter the path of the directory containing the audiobook chapters: ")
output_file_path = input("Enter the path for the output concatenated file (including filename): ")

# Call the function
concatenated_file_path = concatenate_audiobooks(input_directory, output_file_path)
if concatenated_file_path:
    print(f"Concatenated audiobook saved to: {concatenated_file_path}")
