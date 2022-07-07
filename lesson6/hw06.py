import os
import pathlib
import re
import shutil
import sys


def create_folder(path: str, folders_name: iter) -> None:
    for folder_name in folders_name:
        folder_path = os.path.join(path, folder_name)

        try:
            os.mkdir(folder_path)
        except FileExistsError:
            print(f'Folder {folder_name} is exists')


def deleting_files_and_folders(path: str, exclusion_folders: iter) -> None:
    for obj in path.iterdir():
        if obj.is_dir() and obj.name not in exclusion_folders:
            shutil.rmtree(obj, ignore_errors=True)
        elif obj.is_file():
            os.remove(obj)


def get_folder_by_type(suffix: str) -> str:
    for folder in ALL_TYPES.keys():
        if suffix in ALL_TYPES[folder]:
            return folder
    return 'Unknown'


def get_path() -> str or None:
    try:
        path_argv = sys.argv[1]
    except IndexError:
        print('Please add sorting path!')

    if pathlib.Path(path_argv).is_dir():
        return pathlib.Path(path_argv)

    print('Incorrect path. Please add valid path!')
    return None


def get_valid_uniq_name(path: str, name: str) -> str:
    user_path = path / name

    if not is_exists_path(user_path):
        return name

    cnt = 1
    while True:
        new_name = f'({cnt})_{name}'
        new_path = path / new_name

        if not is_exists_path(new_path):
            return new_name
        cnt += 1


def is_exists_path(path: str) -> bool:
    return path.exists()


def iterate_over_folder(path: str) -> list:
    global all_files_in_path

    for p in path.iterdir():
        if p.is_dir():
            iterate_over_folder(p)

        elif p.is_file():
            all_files_in_path.append(p)

    return all_files_in_path


def moving_a_file(target: str, destination: str) -> None:
    shutil.move(target, destination)


def normalize(some_string: str) -> str:
    cyr_dict = {
        ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g',
        ord('ґ'): 'g', ord('д'): 'd', ord('е'): 'e', ord('є'): 'e',
        ord('ё'): 'jo', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'i',
        ord('і'): 'i', ord('ї'): 'ji', ord('й'): 'j', ord('к'): 'k',
        ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o',
        ord('п'): 'p', ord('р'): 'r', ord('с'): 's', ord('т'): 't',
        ord('у'): 'u', ord('ф'): 'f', ord('х'): 'h', ord('ц'): 'с',
        ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'sch', ord('ъ'): '`',
        ord('ь'): '`', ord('ы'): 'i', ord('э'): 'e', ord('ю'): 'ju',
        ord('я'): 'ja', ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V',
        ord('Г'): 'G', ord('Ґ'): 'G', ord('Д'): 'D', ord('Е'): 'E',
        ord('Є'): 'E', ord('Ё'): 'Jo', ord('Ж'): 'Zh', ord('З'): 'Z',
        ord('И'): 'I', ord('І'): 'I', ord('Ї'): 'Ji', ord('Й'): 'J',
        ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N',
        ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S',
        ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'H',
        ord('Ц'): 'С', ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Sch',
        ord('Ъ'): '`', ord('Ь'): '`', ord('Ы'): 'I', ord('Э'): 'E',
        ord('Ю'): 'Ju', ord('Я'): 'Ja'
    }

    new_str = some_string.translate(cyr_dict)
    new_str = re.sub('\W+', '_', new_str)
    return new_str


def print_result(sorted_files: dict, famous_extensions: set, unknown_extensions: set) -> None:
    print('\n.:: Files sorted by category ::.\n')

    for category, files in sorted_files.items():
        print(f'{category}: ', end='')
        print(*files, sep=', ', end='\n')

    print('-' * 56)

    if len(famous_extensions) > 0:
        print('\nFamous extensions: ', *famous_extensions)
    else:
        print('\nNo known extensions found.\n')

    if len(unknown_extensions) > 0:
        print('Unknown extensions: ', *unknown_extensions, end='\n\n')
    else:
        print('Unknown extensions were not found.\n')


def unpack_archive(file_path: str, folder_for_unpacking):
    shutil.unpack_archive(file_path, folder_for_unpacking)


def main(path: str) -> None:
    all_famous_extensions = set()
    unknown_extensions = set()
    sorted_files_by_category = dict()
    all_files_in_user_path = iterate_over_folder(path)

    sorting_folders_list = list(ALL_TYPES.keys())
    create_folder(MAIN_USER_PATH, sorting_folders_list)

    for file_path in all_files_in_user_path:
        file_extension = file_path.suffix
        folder_name_for_moving_file = get_folder_by_type(file_extension)

        if folder_name_for_moving_file != 'Unknown' and folder_name_for_moving_file in ALL_TYPES:
            all_famous_extensions.add(file_extension)
        else:
            unknown_extensions.add(file_extension)

        normalize_name = normalize(file_path.stem)
        new_file_name = normalize_name + file_extension
        new_category_path = MAIN_USER_PATH / folder_name_for_moving_file

        if not folder_name_for_moving_file in sorted_files_by_category:
            sorted_files_by_category[folder_name_for_moving_file] = [new_file_name]
        else:
            sorted_files_by_category[folder_name_for_moving_file].append(new_file_name)

        if not file_extension in ALL_TYPES['Archives']:
            valid_uniq_name = get_valid_uniq_name(new_category_path, new_file_name)
            new_file_path = MAIN_USER_PATH / folder_name_for_moving_file / valid_uniq_name
            moving_a_file(target=file_path, destination=new_file_path)

        else:
            folder_name_for_unpack = get_valid_uniq_name(new_category_path, normalize_name)
            new_folder_path_by_archive = new_category_path / folder_name_for_unpack
            create_folder(new_category_path, [folder_name_for_unpack])
            unpack_archive(file_path, new_folder_path_by_archive)

    deleting_files_and_folders(MAIN_USER_PATH, sorting_folders_list)
    print_result(sorted_files_by_category, all_famous_extensions, unknown_extensions)


if __name__ == '__main__':
    MAIN_USER_PATH = get_path()

    if MAIN_USER_PATH is None:
        quit()

    ALL_TYPES = {
        'Audio': ('.mp3', '.ogg', '.wav', '.amr'),
        'Archives': ('.zip', '.gz', '.tar'),
        'Documents': ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'),
        'Pictures': ('.jpeg', '.png', '.jpg', '.svg'),
        'Video': ('.avi', '.mp4', '.mov', '.mkv'),
        'Unknown': tuple()
    }
    all_files_in_path = []

    main(MAIN_USER_PATH)
