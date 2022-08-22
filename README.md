# Morse-Converter
Offline command line program designed to convert back-and-forth between text and morse code, with a real-time interpreter.

 * Custom short tone and long tone mappings can be assigned to match the input type.
 * defaults for tones, audio frequency and word speed can be assigned in `~/.config/morseconv/defaults.yaml` if desired (Data type subject to change until submission).
 * Compatability with bash shell's input and output operators, allowing files to be imported rather than text


## Usage
```
project.py [-h] [--version] [-t | -m] [-e {pass,print,raw,err}] (-w WORDS [WORDS ...] | -f FILE)
```
   
### Examples 
    morseconv -w "test text"     : implied text > morse, word input
    morseconv -w "... --- ..."   : implied morse > text, word input
    morseconv -tw "this is text" : 
    morseconv -mw "... --- ..."
    morseconv -w text here
    morseconv -f filename
    ... > filename

## Flags
Operations that will be supported by the complete project.
```
-m, --morse         input is morse, expect alpha output
-t, --text          input is alpha, expect morse output
-h, --help          help dialog and version
--version           effecive program version
-e, --errorhandle   change how invalid text is handled
-f, --file          use alternate source for lookup table. Must be yaml file.
-w, --word          may change the name of this flag. Indicates that the source should be literally interpreted as morse or ascii text.
```
## TODO:
May change the -w flag to -t for text or -T, and change the -t flag to -a for --ascii.
