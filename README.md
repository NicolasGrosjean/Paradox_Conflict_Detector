# Paradox Conflict Detector

## Motivation

There are a lot of mods and it is difficult to know which mod is compatible with which one.

This tool helps to detect conflicts between mods to know they are not compatible and help to do a compatch.

## Installation

* Download or clone this repository.
* Install python (for example with [miniconda](https://docs.conda.io/en/latest/miniconda.html)
I recommend you to install a Python environment with conda or virtualenv.

## Usage

Edit lines 80 and 81 of *src/detect_conflicts.py* to specify mod repository directory and files which can be duplicated in mods.

Run the following command to print the conflicts:

```
python src/detect_conflicts.py
```

You can put the output in a file by this way:

```
python src/detect_conflicts.py > conflicts.txt
```

## Tests

You can run the tests (unittest) with VScode settings provided in the repository or with another way.

For example you can use the following commands:

```
cd tests
python -m unittest discover
```

## Future

- Put mod repository directory and exception files as parameters
- Compute conflicts on a playset (list of mods)
- Compute conflict detection files and not only on file names.

## License

OneBaronyACounty is released under the [MIT License](http://www.opensource.org/licenses/MIT).
