# Project 4 Chess Tournament OpenClassRooms

Here is the software created by Edward Peytavin to create, inform and manage several chess tournaments with a single database.<br />
Please ensure that each player has their INE code before starting the tournaments.<br />
As requested, the number of rounds is set to 4.<br />
Each tournament can accommodate a maximum of 8 players, if you want to create tournaments with more players, contact our technical team to adapt the code.

## Installation

First open in the console, navigate through the folders of the computer in order to find yourself in the root of the "project4OC" folder.
Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install antiorm,
db, pip, setuptools, tinydb and wheel.

Once in the folder, run the command:

```bash
pip install -r requirements.txt
```

## Launch

Open the console, navigate through the folders of the computer in order to find yourself in the root of the "project4OC" folder.<br />

Once in the folder, run the command:

```bash
python3 main.py
```

The software will launch, and you can start browsing and interacting with it.<br />
Please make sure to read all the instruction and the information asked for a good utilization of the software.

## Flake8_HTML

To generate another flake8-html report please first deleate the current report "flake8_rapport" in the "project4OC" folder, then open the console, navigate through the folders of the computer in order to find yourself in the root of the "project4OC" folder and run the next command:

```bash
python3 -m flake8 --format=html --htmldir=flake8_rapport
```
The report will be created with the "flake8_rapport" name.

## Requirements

python ≥ 3.7 <br />
requirements.txt
