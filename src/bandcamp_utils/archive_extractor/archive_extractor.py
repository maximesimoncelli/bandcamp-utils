from pathlib import Path
import os
import zipfile 
from dotenv import load_dotenv

load_dotenv()

def read_folder_with_zip_files():
    """Read all zip files located in a set folder, and returns a tuple consisting of the dirpath, the various directories contained within, and the eventual files present."""
    if os.getenv("ARCHIVE_EXTRACTOR_FOLDER"):
        folder = os.getenv("ARCHIVE_EXTRACTOR_FOLDER")
    else:
        folder = input("Enter the path to the folder containing the zip files: ")
    zip_files = os.walk(folder)
    (dirpath, dirnames, filenames) = next(zip_files)
    return (dirpath, dirnames, filenames)

def create_extract_folder(dirpath: str) -> str:
    """Create an extract folder if it's not already created"""
    extract_folder = os.path.join(dirpath, "Extracted")
    Path(extract_folder).mkdir(parents=True, exist_ok=True)
    return extract_folder

def extract_zip_files_to_folder(dirpath: str, extract_folder: str, filenames: list[str]):
    """Iterate over the filenames list, and extract the zip file to the extract_folder"""
    for filename in filenames:
        if filename.find('zip') > 0:
            number_of_dashes =filename.count('-')

            artist_name = filename.split("-", number_of_dashes)[:number_of_dashes]
            album_name = filename.split("-", number_of_dashes)[-1].replace('.zip', '').strip()

            if len(artist_name) > 1:
                artist_name = "-".join(artist_name).strip()
            else:
                artist_name = artist_name[0].strip()

            print("Artist: %s\nAlbum: %s\n" % (artist_name, album_name))

            full_zip_path = os.path.join(dirpath, filename)

            full_extract_path = os.path.join(extract_folder, artist_name, album_name)
            print(full_extract_path)

            with zipfile.ZipFile(full_zip_path, 'r') as zip_ref:
                zip_ref.extractall(full_extract_path)
        else:
            continue

def main():
    (dirpath, dirnames, filenames) = read_folder_with_zip_files()
    extract_folder = create_extract_folder(dirpath=dirpath)
    extract_zip_files_to_folder(extract_folder=extract_folder, dirpath=dirpath,     filenames=filenames)
