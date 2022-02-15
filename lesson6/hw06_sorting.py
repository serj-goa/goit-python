import os
import re
import shutil
import sys
from pathlib import Path


def create_new_folder(path):
    try:
        os.makedirs(path)

    except FileExistsError as e:
        print('New folder is created...')


def del_empty_dirs(folders_list):
    for f in folders_list:
        folder_name = Path(f)

        if 'Sorted files' not in f:

            try:
                shutil.rmtree(folder_name)

            except Exception as e:
                print(e)


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


def get_path():
    try:
        arg_path = sys.argv[1]
        print(f"Sorting start in {arg_path}")

    except IndexError as e:
        print(f'{e}, you didn\'t pass the path as an argument')
        return None

    except Exception as e:
        print(f'{e}, you didn\'t pass the path as an argument')
        return None

    return arg_path


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


def main():
    for new_path in NEW_PATH_TO_FOLDERS:
        create_new_folder(new_path)

    files_and_folders_sort(path)
    sort_extensions(files_list)
    move_and_rename_files(files_path_to_replace)
    del_empty_dirs(empty_folder_list)
    work_report(sorted_all_categories, all_extensions)


def moving_file(new_path, new_file_name, file):
    new_file = f'{new_path}{new_file_name}'
    shutil.move(file, new_file)


def move_and_rename_files(files_path_to_replace):
    for file in files_path_to_replace:

        end_word = file[file.rfind('.'):]

        name = normalize(file[file.rfind('\\') + 1:file.rfind('.')])
        rename_file = f'\\{name}{end_word}'

        for ind, extensions in enumerate(NOTABLE_EXTENSIONS):
            if file.endswith(extensions) and extensions == TYPE_FOR_ARCHIVE:

                archive_name_folder = f'{NEW_ARCHIVE_PATH}\\{name}'
                create_new_folder(archive_name_folder)

                try:
                    shutil.unpack_archive(file, archive_name_folder)
                except Exception as e:
                    print(e)

                moving_file(NEW_PATH_TO_FOLDERS[0], rename_file, file)
                break

            elif file.endswith(extensions):
                moving_file(NEW_PATH_TO_FOLDERS[ind], rename_file, file)
                break
        else:
            moving_file(NEW_PATH_TO_FOLDERS[-1], rename_file, file)


def sort_extensions(files_list):
    for file in files_list:

        dot_file = file.rfind('.')
        all_extensions.add(file[dot_file:])

        for ind, extensions in enumerate(NOTABLE_EXTENSIONS):
            if file.endswith(extensions):
                sorted_all_categories[ind].append(file)
                break
        else:
            sorted_all_categories[-1].append(file)


def work_report(sorted_all_categories, all_extensions):
    print('\n\t-== Folder sorting result ==-\n')
    print(f'Document files:\n{sorted_all_categories[2]}\n')
    print(f'Video files:\n{sorted_all_categories[4]}\n')
    print(f'Audio files:\n{sorted_all_categories[1]}\n')
    print(f'Picture files:\n{sorted_all_categories[3]}\n')
    print(f'Archive files:\n{sorted_all_categories[0]}\n')
    print(f'Other types:\n{sorted_all_categories[-1]}\n')
    print(f'All extensions in your folder:\n{list(all_extensions)}')


if __name__ == '__main__':
    path = get_path()

    if path:
        empty_folder_list = []
        files_list = []
        files_path_to_replace = []
        folders_list = []

        TYPE_FOR_AUDIO = ('.mp3', '.ogg', '.wav', '.amr')
        TYPE_FOR_ARCHIVE = ('.zip', '.gz', '.tar')
        TYPE_FOR_DOC = ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx')
        TYPE_FOR_PICTURE = ('.jpeg', '.png', '.jpg', '.svg')
        TYPE_FOR_VIDEO = ('.avi', '.mp4', '.mov', '.mkv')
        NOTABLE_EXTENSIONS = (TYPE_FOR_ARCHIVE, TYPE_FOR_AUDIO, TYPE_FOR_DOC, TYPE_FOR_PICTURE, TYPE_FOR_VIDEO)

        all_extensions = set()
        sorted_archive = []
        sorted_audio = []
        sorted_doc = []
        sorted_picture = []
        sorted_unknown_types = []
        sorted_video = []
        sorted_all_categories = (sorted_archive, sorted_audio, sorted_doc, sorted_picture, sorted_video, sorted_unknown_types)

        NEW_ARCHIVE_PATH = os.path.join(path, 'Sorted files\\Archive')
        NEW_AUDIO_PATH = os.path.join(path, 'Sorted files\\Audio')
        NEW_DOC_PATH = os.path.join(path, 'Sorted files\\Document')
        NEW_PICTURE_PATH = os.path.join(path, 'Sorted files\\Picture')
        NEW_UNKNOWN_TYPES_PATH = os.path.join(path, 'Sorted files\\Unknown types')
        NEW_VIDEO_PATH = os.path.join(path, 'Sorted files\\Video')

        NEW_PATH_TO_FOLDERS = (NEW_ARCHIVE_PATH, NEW_AUDIO_PATH, NEW_DOC_PATH, NEW_PICTURE_PATH, NEW_VIDEO_PATH, NEW_UNKNOWN_TYPES_PATH)

        main()
