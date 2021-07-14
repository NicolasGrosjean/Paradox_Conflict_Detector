import sqlite3


def read_playsets(db_path: str) -> dict:
    mods = dict()
    for raw_mod in read_sqlite_data(db_path, "mods"):
        mods[raw_mod[0]] = raw_mod[5]
    playsets = dict()
    for raw_playset in read_sqlite_data(db_path, "playsets"):
        playsets[raw_playset[0]] = dict()
        playsets[raw_playset[0]]['name'] = raw_playset[1]
        playsets[raw_playset[0]]['mods'] = []
    for mod_playset in read_sqlite_data(db_path, "playsets_mods"):
        playsets[mod_playset[0]]['mods'].append(mods[mod_playset[1]])
    return playsets


def read_sqlite_data(db_path: str, table: str) -> list:
    sqlite_db = sqlite3.connect(
        db_path,
        check_same_thread=False,
        detect_types=sqlite3.PARSE_DECLTYPES,
    )
    try:
        c = sqlite_db.cursor()
        try:
            res = c.execute(f"SELECT * FROM {table};")
            return res.fetchall()
        finally:
            c.close()
    finally:
        sqlite_db.close()


if __name__ == "__main__":
    playsets = read_playsets(
        "D:\Documents\Paradox Interactive\Crusader Kings III\launcher-v2.sqlite"
    )
    for playset in playsets.values():
        print(playset['name'])
        print(playset['mods'])
        print('===========================')
