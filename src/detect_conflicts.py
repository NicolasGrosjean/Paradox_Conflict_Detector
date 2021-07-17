import argparse
import os


def get_args():
    parser = argparse.ArgumentParser(
        description="Detect conflicts between Paradox mods"
    )
    parser.add_argument(
        "mod_repo_path",
        type=str,
        help="Path of the directory containing all the mods",
    )
    parser.add_argument(
        "-file_exception_path",
        type=str,
        help="Path of a file containing at each line a file name which can duplicated between mods",
    )
    return parser.parse_args()


class ModMetadata:
    name: str
    path: str


NORMAL_DUPLICATED_FILES = ["descriptor.mod", "thumbnail.png"]


def read_mod_descriptor_file(path: str) -> ModMetadata:
    res = ModMetadata()
    with open(path, "r") as f:
        lines = f.readlines()
    for line in lines:
        s_line = line.split("=")
        if s_line[0] == "name":
            res.name = s_line[1].replace("\n", "").replace('"', "")
        elif s_line[0] == "path":
            res.path = s_line[1].replace("\n", "").replace('"', "")
    return res


def list_mod_files(mod_path: str) -> set:
    res = set()
    for _, _, files in os.walk(mod_path):
        for file in files:
            res.add(file)
    return res


def index_mod_by_files(mod_repo_path: str) -> dict():
    """
    Return dictionary with file names as keys, and list of mod names (from mod_repo_path) which have this file
    """
    mods_by_file = dict()
    for mod_desc_file in os.listdir(mod_repo_path):
        if not mod_desc_file.endswith("mod"):
            continue
        metadata = read_mod_descriptor_file(os.path.join(mod_repo_path, mod_desc_file))
        mod_files = list_mod_files(
            os.path.join(mod_repo_path, metadata.path[4:])
            if metadata.path.startswith("mod/")
            else metadata.path
        )
        for file in mod_files:
            if file not in mods_by_file:
                mods_by_file[file] = []
            mods_by_file[file].append(metadata.name)
    return mods_by_file


def detect_conflicts(
    mod_repo_path: str, file_exceptions=NORMAL_DUPLICATED_FILES
) -> dict:
    """
    Return dictionary according this example: { mod1: { mod2: ['file1', 'file2], mod3: ['file42']}}

    Returned files are not in file_exceptions
    """
    conflicts_by_mod = dict()
    mods_by_file = index_mod_by_files(mod_repo_path)
    for file, mods in mods_by_file.items():
        if len(mods) > 1 and file not in file_exceptions:
            for mod in mods:
                if mod not in conflicts_by_mod:
                    conflicts_by_mod[mod] = dict()
                for mod2 in mods:
                    if mod == mod2:
                        continue
                    if mod2 not in conflicts_by_mod[mod]:
                        conflicts_by_mod[mod][mod2] = []
                    conflicts_by_mod[mod][mod2].append(file)
    return conflicts_by_mod


if __name__ == "__main__":
    args = get_args()
    if args.file_exception_path is not None:
        with open(args.file_exception_path, "r") as f:
            file_exceptions = f.readlines()
        for i in range(len(file_exceptions)):
            file_exceptions[i] = file_exceptions[i].replace("\n", "")
    else:
        file_exceptions = NORMAL_DUPLICATED_FILES
    conflicts_by_mod = detect_conflicts(
        args.mod_repo_path,
        file_exceptions,
    )
    for mod in conflicts_by_mod:
        print(f"Conflicts with {mod}:")
        for mod2 in conflicts_by_mod[mod]:
            print(f"- {mod2} on files {conflicts_by_mod[mod][mod2]}")
        print("\n")
