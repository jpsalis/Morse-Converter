# Morse-Converter
Offline command line program designed to convert back-and-forth between text and morse code, with a real-time interpreter.

 * Custom short tone and long tone mappings can be assigned to match the input type.
 * defaults for tones, audio frequency and word speed can be assigned in `~/.config/morseconv/defaults.yaml` if desired (Data type subject to change until submission).
 * Compatability with bash shell's input and output operators, allowing files to be imported rather than text


## Usage
`morseconv`
    * Real Time interpeter

`morseconv [-t | -m] [-s char] [-l char] text [text ...]`
    * Single argument

    
### Examples 
    morseconv "test text" : implied text > morse
    morseconv "... --- ..." : implied morse > text
    morseconv -t "this is text"
    morseconv -m "... --- ..."
    morseconv text here
    cat filename | xargs morseconv: File input
    morseconv > filename:                   File output

## Flags
Operations that will be supported by the complete project.

### Basic
    -m, --morse         input is morse, expect alpha output
    -t, --text          input is alpha, expect morse output

### Etc:
    -h, --help          help dialog and version
    --version           effecive program version

    -e, --errorhandle   change how invalid text is handled
    -f, --file          use alternate source for lookup table. Must be yaml file.

## Other options:
    -s, --short         short tone override (Must be a single character or list of possible)
    -l, --long          long tone override (Must be a single character or list of possible)