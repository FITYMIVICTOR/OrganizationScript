import os
import shutil

def organize_downloads(fichero_descargar):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".bmp", ".svg"],
        'Documents': ['.pdf', '.docx', '.xlsx', '.pptx', '.txt', '.md'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Archives': ['.zip', '.rar', '.tar.gz'],
        "Others": []
    }
    for file in os.listdir(fichero_descargar):
        if os.path.isfile(os.path.join(fichero_descargar, file)):
            file_ext = os.path.splitext(file)[1].lower()
            destination_folder = next((ftype for ftype, exts in file_types.items() if file_ext in exts), 'Others')

            os.makedirs(os.path.join(fichero_descargar, destination_folder), exist_ok=True)
            shutil.move(os.path.join(fichero_descargar, file), os.path.join(fichero_descargar, destination_folder, file))
        print("Downloads organized!")

if __name__ == "__main__":
    downloads_path = r"C:\Users\blanc\Downloads"
    organize_downloads(downloads_path)