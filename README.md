# get-tab-pdf

## Overview
`get-tab-pdf` is a macOS command-line tool for downloading PDFs from Google Chrome tabs in bulk. The PDFs are downloaded to a location specified by the user.

## Requirements
- Python 3.9 or later
- macOS
- Google Chrome

## Installation
Install with pip:
```bash
pip install get-tab-pdf
```

## Usage
Run the tool with the command:
```bash
get-tab-pdf downloadDestination
```

For example, if you want to download the PDFs to the Downloads directory, use:
```bash
get-tab-pdf Downloads
```

`get-tab-pdf` downloads all open PDFs in a specific Google Chrome window. When the tool is run:
1. A menu is displayed. The menu lists the active tabs from all active Google Chrome windows.
2. The user can navigate through the menu to select the window they want to download the PDFs from.
3. The tool will download all PDFs from the selected window, to the location specified when the user ran the command. Non-PDF tabs will be ignored.

## Arguments
- `downloadDestination` - Directory where you want the PDFs to be downloaded. If you enter an invalid location, an error will be displayed.

Available options can be displayed using the `--help` option:
```bash
get-tab-pdf --help
```

## License
This project is licensed under the MIT License. See `LICENSE` for details.
