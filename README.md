# bandcamp-utils

A simple set of tools to work with Bandcamp programmatically

## Features

- An archive extractor for Bandcamp zip files specifically.

More (maybe) as I find a need.

## Install

Make sure you have poetry installed (https://python-poetry.org/)

Then, install bandcamp-utils by running:

```bash
poetry install
```

## Usage

### Archive Extractor

> [!NOTE]  
> You can provide the following .env values in `.env`

```toml
ARCHIVE_EXTRACTOR_FOLDER=C:\Users\Maxime\Downloads
```

:::

```bash
poetry run extract
```

The script will extract all files to an `Extracted` folder, which will be placed alongside your zip files.

> [!NOTE]  
> You'll be asked to paste the folder where the zip files are contained if you have not provided a .env file with the `ARCHIVE_EXTRACTOR_FOLDER` completed.
