import os
import sys


# path contains the first argument,
#a valid file system address
path = sys.argv[1]
print(f"Start in {path}")

# List files and directory in user folder (path)
user_folders = os.listdir(path)

type_for_doc = ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx')
type_for_video = ('.avi', '.mp4', '.mov', '.mkv')
type_for_audio = ('.mp3', '.ogg', '.wav', '.amr')
type_for_picture = ('.jpeg', '.png', '.jpg')

all_extensions = set()
sorted_doc = []
sorted_video = []
sorted_audio = []
sorted_picture = []
sorted_unknown_types = []

for file in user_folders:

    for extension in file:

        dot_file = file.rfind('.')
        all_extensions.add(file[dot_file:])
    
    if file.endswith(type_for_doc):
        sorted_doc.append(file)

    elif file.endswith(type_for_video):
        sorted_video.append(file)

    elif file.endswith(type_for_audio):
        sorted_audio.append(file)

    elif file.endswith(type_for_picture):
        sorted_picture.append(file)

    else:
        sorted_unknown_types.append(file)
        
print('\n\t-== Folder sorting result ==-\n')
print(f'Document files:\n{sorted_doc}\n')
print(f'Video files:\n{sorted_video}\n')
print(f'Audio files:\n{sorted_audio}\n')
print(f'Picture files:\n{sorted_picture}\n')
print(f'Other types:\n{sorted_unknown_types}\n')
print(f'All extensions in your folder:\n{list(all_extensions)}')
