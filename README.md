# Terminal recorder to mp4

A terminal recorder that records terminal sessions to mp4.

It may need the fonts `ttf-dejavu`

## Arguments

- `-o outputFile.mp4`/`--output outputFile.mp4` sets a custom output path and file name

- `--fps 24` the fps of the mp4 file

- `--cast` if added, saves the .cast files alongside the .mp4 file

- `-f`/`--force` overrides the existing files.

## Running the script

1. Install python3
https://www.python.org/downloads/

2. Install pip3
https://www.linuxscrew.com/install-pip

3. Clone repository
`git clone git@github.com:bind-systems/terminal-rec-mp4.git`

4. Change into the repository directory
`cd terminal-rec-mp4`

5. Install requirements
`pip3 install -U -r requirements.txt`

6. Run the program
`./recterminal/recterminal.py`

## Building the script

1. Install python3
https://www.python.org/downloads/

2. Install pip3
https://www.linuxscrew.com/install-pip

3. Clone repository
`git clone git@github.com:bind-systems/terminal-rec-mp4.git`

4. Install build tools
`pip install build setuptools`

5. Build
`python3 -m build`

6. Install the built files
`pip install dist/recterminal-(...).whl`

And then you can run `recterminal` in the terminal anywhere.