# Morse-Converter
Offline command line program designed to convert back-and-forth between text and morse code.

 * Compatability with bash shell's output operator
 * Flag to allow file input, allowing files to be imported rather than text
 * automatically determines input type
 * allows manual override for ambiguous text
 * cleans up user input of stray spaces and other discrepancies
 * allows input handler to be changed according to needs 


## Usage
```
morseconv [-h] [--version] [-t | -m] [-e {pass,print,raw,err}] (-w WORDS [WORDS ...] | -f FILE)
```

#### Examples
```
morseconv -w "test text"     : implied text > morse, word input
morseconv -w "... --- ..."   : implied morse > text, word input
morseconv -tw "this is text" : 
morseconv -mw "... --- ..."
morseconv -w text here
morseconv -f filename
... > filename
... | dev/null
```

#### Flags
```
-h, --help            show this help message and exit
--version             show program's version number and exit
-t, --text            source is text. Convert to morse
-m, --morse           source is morse. Convert to text
-e {pass,print,raw,err}, --err_handle {pass,print,raw,err}
                      change invalid character handler.
-w WORDS [WORDS ...], --words WORDS [WORDS ...]
                      morse or ascii words to convert
-f FILE, --file FILE  morse or text file to convert
```
