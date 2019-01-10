Dependencies:
python >=3.6

matplotlib >=3.0.0

Quick Start
=============
take the original text in "Adam_input.txt", and run:  
run.bat

It will change the text to lower cases, and eradicate some infrequent characters, encode the text 
with a random cipher key, then run our algorithm.

The five most possible solutions in the file "data\Adam_input_lower_simple_scrambled_result.txt"  
The graph of entropy is stored in "data\Adam_input_lower_simple_scrambled_entropy.jpg"  

Detailed Usage:
=============================================
run_deciphering.py [options]

Options:

  -h, --help ........... show this help message and exit

  -i INPUTFILE, --input=INPUTFILE .......... input file to train the code on

  -d DECODE, --decode=DECODE .......... file that needs to be decoded

  -e ITERATIONS, --iters=ITERATIONS ........... number of iterations to run the algorithm for

  -t TOLERANCE, --tolerance=TOLERANCE .......... percentate acceptance tolerance, before we should stop

  -p PRINT_EVERY, --print_every=PRINT_EVERY ...........number of steps after which diagnostics should be printed

We provide auxiliary files to help with the program.  
1.Change all the characters to the lower case:
python lower.py "$file_name$"

2.Eradicate infrequent symbols:
python simplify.py "$file_name$"

3.Encode the plain text with a random cipher key:
python scramble_text.py -i "$file_name$"

4.Calculate the accuracy of final result:
python "$file_name_of_original_text$" 

We also provide several plain text, including:  
"Adam_Smith.txt", "Hound.txt", "return.txt", "Scarlet.txt", "warpeace_input.txt"
