python lower.py "data/Adam_input.txt"
python simplify.py "data/Adam_input_lower.txt"
python upper.py "data/Adam_input.txt"
python simplify.py "data/Adam_input_upper.txt"
python scramble_text.py -i "data/Adam_input_upper_simple.txt"
python run_deciphering.py -i data/warpeace_input.txt -d data/Adam_input_upper_simple_scrambled.txt
python accuracy.py "data/Adam_input_lower_simple.txt"