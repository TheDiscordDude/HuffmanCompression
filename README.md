# HuffmanCompression

--- 

### Table of Contents 

- [Description](#description)
- [How to use](#how-to-use)

---
## Description 

This is a project done as an exercise for my university. This program can compress a text file using the Huffman compression algorithm. 
You can find documentation on this method of compression [here](https://www.ic.tu-berlin.de/fileadmin/fg121/Source-Coding_WS12/selected-readings/10_04051119.pdf).

### Technologies

You can run this program with Python 3.8.
No dependencies are required and no special features of Python3.8 is used.
So you might be able to use older versions of Python. 

---
## How to use

This program is used in  command line.
To use, you just need to use this command : 
`python3 main.py`

You will then be prompted to put the name of the file you wish to compress.
```
Which file do you wish to compress ? text_file.txt
```
There are 2 outputs for this program : 
- The compressed file : `text_file_comp.bin`
- The alphabet file used to decompress the file : `text_file_freq.txt` 

The entire Huffman tree will then be presented to you in JSON  format.
You can see what this looks like thanks to [this](https://jsonvisio.com/editor) website.

You will then have the result of the entire process.
```
File compressed successfully
Compression rate : 52.77777777777778%
Average bit count : 4.1875
```

### Installation

You just need to clone the project to a directory : 

`git clone https://github.com/TheDiscordDude/HuffmanCompression/`

