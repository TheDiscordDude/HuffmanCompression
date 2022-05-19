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
There are 2 argumenst you can pass to the programm : 
- The name of the file you wish to compress
- Weither or not you want to the Huffman tree to be printed `Y/N`

For example: 
```
python3 main.py alice.txt y
```
Will compress the file and display the tree in Json format.

You can also use this command : 
`python3 main.py`

You will then be prompted to put the name of the file you wish to compress.
```
Which file do you wish to compress ? text_file.txt
```
There are 2 outputs for this program : 
- The compressed file : `text_file_comp.bin`
- The alphabet file used to decompress the file : `text_file_freq.txt` 

If you want to, the huffman tree can be displayed in json format
`Do you wish to see the huffman tree in json format ? Y/N`
You can see what it looks like thanks to [this website](https://jsonvisio.com/editor).

You will then have the result of the entire process.
```
File compressed successfully
Compression rate : 52.77777777777778%
Average bit count : 4.1875
```

### Installation

You just need to clone the project repo to a directory : 

`git clone https://github.com/TheDiscordDude/HuffmanCompression/`
