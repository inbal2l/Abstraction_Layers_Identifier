# Abstraction Layers Identifier

This project was created to explore the concept of "Abstraction Layers" in C++. 
For more info, please see the talk: "Let's Talk About Abstraction Layers" by Inbal Levi.

## Install

Currently only Ubuntu installation is supported (WSL can be used for windows environment).

### Setting the environment by opening the pre-prepared virtual environment

The virtual environemnt contains all you need to run the script. You can open it by running:
  1. source ./venv/bin/activate

### Setting the environment by installing requirements directly

It is not recommended, but you can also install all the requirements directly on your environment.
To prepare the environment (requrements: python3, pip3), please run:

  1. sudo apt update
  2. sudo apt install python3
  3. sudo apt install python3-pip

To install the requirements for the script, please run:
  1. python -m pip install -r requirements.txt

## Run

To run the script on your own .cpp file, please follow the steps:

  1. Create your file under: ./cpp_examples
  2. from root folder, run: 
    python ./layers_identifier -f ./cpp_examples/<your_file_name>.cpp
