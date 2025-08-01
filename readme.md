### Setup (on Mac)

Clone the repo

```bash
git clone <repo-url>
```

Setup venv, then install with pip.
On Mac:

```bash
python3 -m venv venv
source venv/bin/activate
pip install .
```

## How to run

```bash
# change one sound file into ogg
sound_convert path/to/file

# specify the output file type
sound_convert path/to/file -o ogg

# convert files recursively in a directory, default is wav for input and ogg for output
sound_convert path/to/directory -r

# convert files recursively, specifying multiply possible input types
sound_convert path/to/directory -r -f mp3 wav

# convert files recursively, specifying output type and possible input types. Multiple input types allowed. Here mp3 is specified as output, wav and ogg as input
sound_convert path/to/directory -r -o mp3 -f wav ogg
```

## Arguments

- `input`: File or directory path
- `-o`, `--output`: Specify the output format
- `-r`, `--recursive`: Recursively process directories
- `-f`, `--format`: Specify multiple allowed input types. The default is wav. Multiple formats are allowed, but using a format in input and output will fail.

---
