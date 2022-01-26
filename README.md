# IOC-Generator

### Quickly generate common Indicators of Compromise (IOCs) from files with Python.

An analyst can quickly generate common Indicators of Compromise (IOCs) from a single file or directory that can then be incorporated into tools like Mandiant's IOCe.

``` noLineNumbers
Python Automated IOC Generator 
File Name, MD5 hash value, SHA-1 hash value, SHA-256 hash value, and File Size in Bytes.

Enter: 
'1' for single file, or 
'2' to select a directory of files as input: 
```

The file is processed and each of the IOCs are generated and output to the screen, as well as to a text file called "output.txt" which is located in the same directory the python script resides.

``` noLineNumbers
Python Automated IOC Generator 
File Name, MD5 hash value, SHA-1 hash value, SHA-256 hash value, and File Size in Bytes.

Enter: 
'1' for single entry, or 
'2' to select a directory of files as input: 1

Enter path to file: 2innocent.pdf

File name: 2innocent.pdf


MD5: 90ffd2359008d82298821d16b21778c5c39aec36

SHA-1: 90ffd2359008d82298821d16b21778c5c39aec36

SHA-256: 3df79d34abbca99308e79cb94461c1893582604d68329a41fd4bec1885e6adb4

Size in bytes:  13264


Artifacts generated on: Wed Jan 26 16:40:46 2022
created by Python Automated IOC Generator
```

For more information about this script, check out my article on "[Security Automation with Python — Quickly generate common IOCs from files with Python](https://www.brettfullam.com/security-automation-with-python-quickly-generate-common-iocs-from-files-with-python/  "Quickly generate common IOCs from files with Python")." 

## Getting Started

1. Download the script or use git to clone the repository

2. No extra dependencies needed.  This script was created using Python3, and all of the necessary dependencies are already included in the standard Python installation.

3. The repository includes the following:

* The finished version of the script using only using standard Python libraries (file name ending in ".py")
* An alternate version of the Python script using commands on the host system via "subprocess" (file name ending in "-subprocess.py")
* License
* README.md file
* 2innocent.pdf sample file
* ioc-samples directory that contains 2 sample files

``` nolinenumbers
.
├── 2innocent.pdf
├── LICENSE
├── README.md
├── ioc-samples
├── iocs-from-file-or-directory.py
└── iocs-from-file-or-directory-subprocess.py
```

1 directory, 5 files
There are 5 files and 1 directory in total:
```
The directory, which contains 2innocent.pdf and highly_malicious.txt, are harmless sample files for you to test the "directory_as_input" functionality included in the script to see first hand how multiple files are processed.

