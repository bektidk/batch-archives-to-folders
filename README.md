# Batch Archives to Folders

A simple Python script to batch extract multiple archive files (such as ZIP, RAR, and others) into folders with the same name as the archive. This tool automates the extraction process, creating organized folders for each archive and optionally deleting the original archive files after extraction.

## Features

- Automatically extracts multiple archives at once.
- Creates folders named after each archive for better organization.
- Handles various archive formats (ZIP, RAR, etc.).
- Optionally deletes the archive files after extraction.
- Includes error handling and logging to track progress and potential issues.

## Prerequisites

- **Python 3.6+** is required.
- Required libraries: `os`, `zipfile`, `shutil`, `rarfile` (install via `pip install rarfile` if handling RAR files).

## Installation

1. Clone this repository:
   
   ```bash
   git clone https://github.com/your-username/batch-archives-to-folders.git
   cd batch-archives-to-folders
   ```

3. Install any necessary dependencies:
   ```bash
   pip install rarfile
   ```

## Usage

1. Place the archive files in the target directory, for example, `My Folder`.
   
2. Run the script with Python:
   ```bash
   python batch_archives_to_folders.py
   ```
   
3. Follow any prompts for deletion options or directory input.

### Optional Arguments

- Customize the extraction path by modifying the `target_directory` variable in the script.
- To enable or disable the deletion of original archives after extraction, adjust the `delete_after_extraction` setting.

## Logging

The script generates a log file `extraction_log.txt` to track extracted files, any skipped files, and any errors encountered during the process.

## Example

Given the following directory structure:

```python
My Folder/
├── archive1.zip
├── archive2.zip
└── archive3.rar
```

Running the script will create:

```python
My Folder/
├── archive1/
│   └── [contents of archive1.zip]
├── archive2/
│   └── [contents of archive2.zip]
├── archive3/
│   └── [contents of archive3.rar]
```

## Notes

- Ensure you have permissions to create and delete files in the target directory.
- For handling additional formats beyond ZIP and RAR, additional libraries may be required.

