## ATMachine

# For usage create a env with : 

python3 -m venv venv 

# And then start it with :  

source venv/bin/activate

# Then install the pakage for coverage report :

python3 -m pip install coverage

# Run it with :

coverage run <file_with_the_tests>

# For viewing of the covrage report : 

covrage report

# If you want to run the program manually create a .txt file and provide it to main.py or object_main.py 

main.py <input.txt>

object_main.py <input2.txt>

# There are 3 input files provided that can be changed.


## Script for runnig all the tests and a combined report!

# To run everyting first start the venv with coverage installed and then the following: 

chmod +x scripts/run_coverage.sh

./scripts/run_coverage.sh

# For viewing of the coverage report

open htmlcov/index.html


