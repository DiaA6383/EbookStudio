from pydub import AudioSegment
import os
from tqdm import tqdm

def concatenate_audiobooks(directory):
    """
    Concatenates all MP3 files in the given directory and its subdirectories into a single MP3 file.

    Parameters:
    directory (str): The path to the main directory containing the audiobook chapters.

    Returns:
    str: The path to the concatenated audiobook file.
    """
    files_to_concatenate = []
    for subdir, dirs, files in os.walk(directory):
        for file in sorted(files):  # Sort the files to maintain order
            if file.endswith(".mp3"):
                files_to_concatenate.append(os.path.join(subdir, file))

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

    output_path = os.path.join(directory, "concatenated.mp3")
    concatenated.export(output_path, format="mp3")
    return output_path

# Call the function
concatenated_file_path = concatenate_audiobooks("/Users/alejandrodiaz/Desktop/Concatanate/Dune")
if concatenated_file_path:
    print(f"Concatenated audiobook saved to: {concatenated_file_path}")
