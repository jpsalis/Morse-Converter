# Morse-Converter
Offline command line program designed to convert back-and-forth between text and morse code, with a real-time interpreter.

 * Allows a text or morse message to be converted into a `.wav` file, with configurable word speed and frequency.
 * Custom short tone and long tone mappings can be assigned to match the input type.
 * defaults for tones, audio frequency and word speed can be assigned in `~/.config/morseconv/defaults.yaml` if desired (Data type subject to change until submission).

## Usage
`morseconv`

`morseconv [Input Hint] [-s char] [-l char] [-t] text [-o outputdir]`

`morseconv [Input Hint] [-s char] [-l char] [-i] filename [-o outputdir]`
    
### Examples 
    morseconv "test text" : implied text > morse
    morseconv "--- ... ---" : implied morse > text
    morseconv                                               : realtime interpreter
    morseconv -A -i text.txt -o text.txt                    : implicit text file to morse file
    morseconv Mayday                      : implicit text over multiple parameters
    morseconv -o verycool.txt text here with no parameter?  : conversion without

## Flags
### Input Type Hint:
    -M, --morse         input is morse, expect alpha output
    -m, --to_morse
    -T, --text         input is alpha, expect morse output
    -t, --to_text

### Options:
    -s, --short         character to use as short tone.
    -l, --long          character to use as long tone.
    -i, --input         input file: Must be a text file.
    -o, --output        output file: Must be a text file or audio file.
    -w, --wpm           output audio at a specific speed
    -f, --frequency     output audio tone at a specific frequency

### Etc:
    -h, --help          help dialog and version
    -v, --verbose       explain what is being done
    -d, --debug         Information for error diagnosis
