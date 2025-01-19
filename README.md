# Paradox Conflict Detector

## Fork

Fixed issue with uncode encoding https://github.com/NicolasGrosjean/Paradox_Conflict_Detector/issues/1

Fixed common files being detected as conflicts (readme.md, changelog.md)

## Motivation

There are a lot of mods and it is difficult to know which mod is compatible with which one.

This tool helps to detect conflicts between mods to know they are not compatible and help to do a compatch.

## Installation

* Download or clone this repository.
* Install python (for example with [miniconda](https://docs.conda.io/en/latest/miniconda.html)
I recommend you to install a Python environment with conda or virtualenv.

## Usage


### Basic Usage

Run the following command to print the conflicts:

```
python src/detect_conflicts.py "<mod_repo_path>" "<file_exception_path>"
```

With *mod_repo_path* the path of the directory containing all the mods,
*file_exception_path* the path of a file containing at each line a file name which can duplicated between mods.
The quotes are necessary to manage spaces in directory names.

For example

```
python src/detect_conflicts.py "D:\Documents\Paradox Interactive\Crusader Kings III\mod" "config\file_exception.txt"
```

### Advanced Usage

#### Compute conflicts on a subset of mods

You can specify a list of mods on which compute conflicts by adding `-filtering_mod_path "<filtering_mod_path>"` to the command line.
With *file_exception_path* the path of a file containing at each line a mod name in which conflicts will be computed.

For example

```
python src/detect_conflicts.py "D:\Documents\Paradox Interactive\Crusader Kings III\mod" "config\file_exception.txt" -filtering_mod_path "config\my_mod_list.txt"
```

#### Compute conflicts on a Paradox Launcher playset

In Paradox launcher we can define a playset: a list of mods.

For this feature you need to install the sqlite3 package :

```
pip install sqlite3
```

You can specify a playset to compute conflicts only on these mods by adding `-playset_name "<playset_name>"` to the command line.
The quotes are necessary to manage spaces in playset name.

For example

```
python src/detect_conflicts.py "D:\Documents\Paradox Interactive\Crusader Kings III\mod" "config\file_exception.txt" -playset_name "Historical Playset"
```

#### Set output in a file

You can put the output in a file by this way by redirecting the standard output with a *>*. For example

```
python src/detect_conflicts.py "<mod_repo_path>" > conflicts.rtf
```

## Tests

You can run the tests (unittest) with VScode settings provided in the repository or with another way.

For example you can use the following commands:

```
cd tests
python -m unittest discover
```

## Future

- Compute conflict detection files and not only on file names.

## License

OneBaronyACounty is released under the [MIT License](http://www.opensource.org/licenses/MIT).
