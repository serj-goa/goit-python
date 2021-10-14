import os
import re
import shutil
import sys
from pathlib import Path


def create_new_folder(path):
    try:
        os.makedirs(new_archive_path)

    except FileExistsError:
        pass

    try:
        os.makedirs(new_audio_path)

    except FileExistsError:
        pass

    try:
        os.makedirs(new_doc_path)

    except FileExistsError:
        pass

    try:
        os.makedirs(new_picture_path)

    except FileExistsError:
        pass

    try:
        os.makedirs(new_unknown_types_path)

    except FileExistsError:
        pass

    try:
        os.makedirs(new_video_path)

    except FileExistsError:
        pass


def del_empty_dirs(folders_list):
    for f in folders_list:
        folder_name = Path(f)

        if 'Sorted files' not in f:

            try:
                shutil.rmtree(folder_name)

            except:
                pass


def files_and_folders_sort(path):
    user_folders = os.listdir(path)

    for file in user_folders:
        join_path = os.path.join(path, file)

        if os.path.isfile(join_path):
            files_list.append(file)
            files_path_to_replace.append(join_path)

        elif os.path.isdir(join_path) and file != 'Sorted files':

            empty_folder_list.append(join_path)
            folders_list.append(file)

            join_path = os.path.join(path, file)
            files_and_folders_sort(join_path)


def normalize(sentence):
    letter_dict = {ord('а'): 'a', ord('А'): 'A', ord('б'): 'b', ord('Б'): 'B',
                   ord('в'): 'v', ord('В'): 'V', ord('г'): 'g', ord('Г'): 'G',
                   ord('д'): 'd', ord('Д'): 'D', ord('е'): 'e', ord('Е'): 'E',
                   ord('ё'): 'jo', ord('Ё'): 'Jo', ord('ж'): 'zh', ord('Ж'): 'Zh',
                   ord('з'): 'z', ord('З'): 'Z', ord('и'): 'i', ord('И'): 'I',
                   ord('й'): 'y', ord('Й'): 'Y', ord('к'): 'k', ord('К'): 'K',
                   ord('л'): 'l', ord('Л'): 'L', ord('м'): 'm', ord('М'): 'M',
                   ord('н'): 'n', ord('Н'): 'N', ord('о'): 'o', ord('О'): 'O',
                   ord('п'): 'p', ord('П'): 'P', ord('р'): 'r', ord('Р'): 'R',
                   ord('с'): 's', ord('С'): 'S', ord('т'): 't', ord('Т'): 'T',
                   ord('у'): 'u', ord('У'): 'U', ord('ф'): 'f', ord('Ф'): 'F',
                   ord('х'): 'h', ord('Х'): 'H', ord('ц'): 'ts', ord('Ц'): 'Ts',
                   ord('ч'): 'ch', ord('Ч'): 'Ch', ord('ш'): 'sh', ord('Ш'): 'Sh',
                   ord('щ'): 'shch', ord('Щ'): 'Shch', ord('ы'): 'y', ord('Ы'): 'Y',
                   ord('ь'): '', ord('Ь'): '', ord('ъ'): '', ord('Ъ'): '',
                   ord('э'): 'e', ord('Э'): 'E', ord('ю'): 'ju', ord('Ю'): 'Ju',
                   ord('я'): 'Ja', ord('Я'): 'Ja'}

    latin_sentence = sentence.translate(letter_dict)
    result_sentence = re.sub(r'\W', "_", latin_sentence)

    return result_sentence


def move_and_rename_files(files_path_to_replace):
    for file in files_path_to_replace:

        end_word = file[file.rfind('.'):]

        name = normalize(file[file.rfind('\\') + 1:file.rfind('.')])
        rename_file = f'\\{name}{end_word}'

        if file.endswith(type_for_archive):
            archive_name_folder = f'{new_archive_path}\\{name}'

            try:
                os.makedirs(archive_name_folder)
            except FileExistsError:
                pass

            try:
                shutil.unpack_archive(file, archive_name_folder)
            except:
                pass

            new_file = f'{new_archive_path}{rename_file}'
            shutil.move(file, new_file)

        elif file.endswith(type_for_audio):
            new_file = f'{new_audio_path}{rename_file}'
            shutil.move(file, new_file)

        elif file.endswith(type_for_doc):
            new_file = f'{new_doc_path}{rename_file}'
            shutil.move(file, new_file)

        elif file.endswith(type_for_picture):
            new_file = f'{new_picture_path}{rename_file}'
            shutil.move(file, new_file)

        elif file.endswith(type_for_video):
            new_file = f'{new_video_path}{rename_file}'
            shutil.move(file, new_file)

        else:
            new_file = f'{new_unknown_types_path}{rename_file}'
            shutil.move(file, new_file)


def sort_extensions(files_list):
    for file in files_list:

        for _ in file:
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


if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Sorting start in {path}")

    empty_folder_list = []
    files_list = []
    files_path_to_replace = []
    folders_list = []
    folders_path_to_remove = []

    type_for_doc = ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx')
    type_for_video = ('.avi', '.mp4', '.mov', '.mkv')
    type_for_audio = ('.mp3', '.ogg', '.wav', '.amr')
    type_for_picture = ('.jpeg', '.png', '.jpg', '.svg')
    type_for_archive = ('.zip', '.gz', '.tar')

    all_extensions = set()
    sorted_archive = []
    sorted_audio = []
    sorted_doc = []
    sorted_picture = []
    sorted_unknown_types = []
    sorted_video = []

    sort_dirs = ['Sorted files']
    new_archive_path = os.path.join(path, 'Sorted files\\Archive')
    new_audio_path = os.path.join(path, 'Sorted files\\Audio')
    new_doc_path = os.path.join(path, 'Sorted files\\Document')
    new_picture_path = os.path.join(path, 'Sorted files\\Picture')
    new_unknown_types_path = os.path.join(path, 'Sorted files\\Unknown types')
    new_video_path = os.path.join(path, 'Sorted files\\Video')

    create_new_folder(path)
    files_and_folders_sort(path)
    sort_extensions(files_list)
    move_and_rename_files(files_path_to_replace)
    del_empty_dirs(empty_folder_list)

    print('\n\t-== Folder sorting result ==-\n')
    print(f'Document files:\n{sorted_doc}\n')
    print(f'Video files:\n{sorted_video}\n')
    print(f'Audio files:\n{sorted_audio}\n')
    print(f'Picture files:\n{sorted_picture}\n')
    print(f'Archive files:\n{sorted_archive}\n')
    print(f'Other types:\n{sorted_unknown_types}\n')
    print(f'All extensions in your folder:\n{list(all_extensions)}')
