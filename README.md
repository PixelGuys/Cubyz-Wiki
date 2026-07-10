# Cubyz Wiki Source Repository

This repository contains source markdown files of Cubyz Wiki.

## Changing Wiki

To begin changing the wiki, you have to first get yourself a local copy. You can do this
either through commands, with use of `git`:

```
git clone https://github.com/PixelGuys/Cubyz-Wiki
```

Or by [downloading zip archive from Github](https://github.com/PixelGuys/Cubyz-Wiki/archive/refs/heads/main.zip) and unpacking it.
Regardless of the route you choose, you should have your own local folder called `Cubyz-Wiki`.

If you haven't yet opened a terminal, please open one and navigate to `Cubyz-Wiki` directory.

```
cd Cubyz-Wiki
```

To locally build Cubyz Wiki you will need Python interpreter in [version 3.10 or newer](https://www.python.org/downloads/).
To install necessary requirements it is recommended to create isolated environment:

```
python -m venv .env
```

Mind that not every linux distro ships `venv` package alongside interpreter. You have to
check the exact details for your distro.

After creating virtual environment, you have to activate it:

Linux:

```
source .env/bin/activate
```

Windows:

```
.\.env\Scripts\activate
```

Once virtual environment is activated, you can proceed to install Cubyz Wiki requirements:

```
pip install -r requirements.txt
```

Afterwards you should be able to build Cubyz Wiki files:

```
zensical build --clean
```

You can also serve the built documentation locally, so the changes are reflected in real time:

```
zensical serve
```
