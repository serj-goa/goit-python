import os
import sys


# path contains the first argument,
#a valid file system address
path = sys.argv[1]
print(f"Start in {path}")

files_list = []
folders_list = []

type_for_doc = ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx')
type_for_video = ('.avi', '.mp4', '.mov', '.mkv')
type_for_audio = ('.mp3', '.ogg', '.wav', '.amr')
type_for_picture = ('.jpeg', '.png', '.jpg', '.svg')
type_for_archive = ('.zip', '.gz', '.tar', '.rar', '.7zip')

all_extensions = set()
sorted_archive = []
sorted_audio = []
sorted_doc = []
sorted_picture = []
sorted_unknown_types = []
sorted_video = []


def files_and_folders_sort(path):
    
    user_folders = os.listdir(path)
    
    for file in user_folders:        
        join_path = os.path.join(path, file)
        
        if os.path.isfile(join_path):            
            files_list.append(file)

        elif os.path.isdir(join_path):
            
            folders_list.append(file)
            join_path = os.path.join(path, file)
            files_and_folders_sort(join_path)


def sort_extensions(files_list):

    for file in files_list:

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

        elif file.endswith(type_for_archive):
            sorted_archive.append(file)

        else:
            sorted_unknown_types.append(file)
        

files_and_folders_sort(path)
sort_extensions(files_list)

print('\n\t-== Folder sorting result ==-\n')
print(f'Document files:\n{sorted_doc}\n')
print(f'Video files:\n{sorted_video}\n')
print(f'Audio files:\n{sorted_audio}\n')
print(f'Picture files:\n{sorted_picture}\n')
print(f'Archive files:\n{sorted_archive}\n')
print(f'Other types:\n{sorted_unknown_types}\n')
print(f'All extensions in your folder:\n{list(all_extensions)}')
