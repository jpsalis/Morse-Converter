# Morse-Converter
Offline command line program designed to convert back-and-forth between text and morse code, with a real-time interpreter.

 * Allows a text or morse message to be converted into a `.wav` file, with configurable word speed and frequency.
 * Custom short tone and long tone mappings can be assigned to match the input type.
 * defaults for tones, audio frequency and word speed can be assigned in `~/.config/morseconv/defaults.yaml` if desired (Data type subject to change until submission).

## Usage
`morseconv`

`morseconv [-t | -m] [-s char] [-l char] text [text ...]`

`morseconv [Input Hint] [-s char] [-l char] [-i]`
    
### Examples 
    morseconv "test text" : implied text > morse
    morseconv "... --- ..." : implied morse > text
    morseconv                                               : realtime interpreter
    morseconv -t "this is text" 
    morseconv -m "... --- ..." 
    morseconv text here with no parameter?                  : conversion without (Might not include)

## Flags
### Input Type Hint:
    -m, --morse         input is morse, expect alpha output
    -t, --text         input is alpha, expect morse output

### Etc:
    -h, --help          help dialog and version
    -v, --verbose       explain what is being done
    -d, --debug         Information for error diagnosis
