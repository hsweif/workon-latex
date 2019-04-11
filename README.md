# workon-latex
## Introduction
This repository is used as a collection of the latex templates that I often used with some simple assistant tools. I think it may be convinent to provide repo that you can easily get useful latex templates and tools with simple `git pull` command.
It will be wonderful if you would like to contribute your favorite latex template to the collections. Just make a pull request.
Most of the templates were downloaded from Overleaf. If any of them is protected by any kind of copyright or licence please let me know and I will remove them.
The update frequency may be irregular because I'm quite busy, but feel free to launch issues and make PR. Hope that it would become an useful repo someday.

## Related tools
It is highly recommended to write latex in Visual Studio Code with Latex Workshop which you can find in the marketplace.

## Usage
Use below command to create a new document named DOC from template named TEM. You can get all existed templates with `python3 main.py -l`.
You can find your documents in directory `./documents`.
```python
python3 main.py -t TEM -d DOC
```