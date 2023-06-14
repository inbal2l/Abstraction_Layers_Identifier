
# Imports
import sys
import pandas as pd
import argparse
from layers_identifier import LayersIdentifier


def get_args():
    """! get args from command line (cpp file name, etc.)
    @return     args object, which contains command line arguments
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-f", "--file", help="file to process")
    arg_parser.add_argument("-v", "--verbose", action='store_true', help="add detailed prints (tokens table)")

    args = arg_parser.parse_args()
    return args

def main():
    """! Main function, creates file lines table, identify layers, prints warnings
    @return     None.
    """
    args = get_args()
    # f'./test1.cpp'
    with open(args.file) as f:
        lines = f.readlines()

    # Define token dictionary (layers indication for specific token), and indicator dictionary
    token_dict = {"i": "Types", "std::cout": "IO", ">>": "IO", "iss": "IO", 'iss("0 1 2")': "IO", "rn::istream_view<int>(": "Ranges"}
    indicator_dict = {"int": "Types", "double": "Types","std::istringstream": "IO"}

    # Create identifier
    l_identify = LayersIdentifier()

    # Create table of file lines
    table = pd.DataFrame()
    table['lines'] = lines
    table['lines'] = table['lines'].apply(lambda x: x.strip().replace(";",""))
    table['line_num']=table.index + 1

    for line in table['lines']:
        l_identify.indicator_to_token (line, indicator_dict, token_dict)

    table['tokens']=table['lines'].apply(lambda x: l_identify.tokenizer(x,token_dict)[0])
    table['layers']=table['lines'].apply(lambda x: l_identify.tokenizer(x,token_dict)[1])

    table = table[['line_num','lines','tokens','layers']]

    # Append warnings to table
    table['warning'] = table['layers'].apply(lambda x: len(set(x))>1)

    # Prints results
    if args.verbose:
        print("File table for: " + args.file)
        print(table)
    print("Warnings for: " + args.file)

    if len(table[table['warning']]) > 1:
        warnings_table = table[table['warning']]
        for row_num in range(len(warnings_table)):
            line = warnings_table.iloc[row_num]
            print(l_identify.warning_text(line))
    elif len(table[table['warning']]) == 1:
        print(l_identify.warning_text(table[table['warning']].iloc[0]))

if __name__ == "__main__":
    sys.exit(main())