'''
Assumptions:
In the creation of the table:
1. Whenever a token appears after an indicator from the indicator_dict, it's a declaration. (and not, for example, a function def).
2. All tokens and indicators are separated by spaces. There are no spaces within tokens or indicators.
3. A given indicator only appears in every line of code once.
In the warning line printed:
1. A warning is onlt ever printed for 1 transition per line of code.
2. If 2 or more layers appear in the same line of code, it is always treated as a transition.
3. The transition is always from the layer that appears last, to the layer that appears before last, all layers and tokens appearing before that are ignored.
4. If no line has 2 or more layers appearing in the same line, nothing is printed.
'''

# Imports

class LayersIdentifier:
    
    @staticmethod
    def indicator_to_token (code_line, indicator_dict, token_dict):
        """! Iterate over file, adds tokens which appears after indicator into the token dictionary
        @param code_line        The input code line.
        @param indicator_dict   The indicator dictionary, in which indicators are being searched.
        @param token_dict       The token dictionary, to which tokens are being added.
        @return                 None.
        """

        line_of_words = code_line.split(' ')
        for indicator in indicator_dict:
            if indicator in line_of_words:            
                token_index = line_of_words.index(indicator) + 1
                token = line_of_words[token_index]
                token_dict[token] = indicator_dict[indicator]
        return

    @staticmethod
    def tokenizer (code_line, token_dict):
        """! Iterate over objects, identify tokens, adds them into the token dictionary
        @param code_line        The input code line.
        @param token_dict       The token dictionary, to which tokens are being added.
        @return                 A tuple of: [token_list, layer_list].
        """
        token_list=[]
        layer_list=[]
        objects = code_line.split(" ")
        for possible_token in objects:
            if possible_token in list(token_dict.keys()):
                token_list.append(possible_token)
                layer_list.append(token_dict[possible_token])
        return token_list, layer_list

    @staticmethod
    def warning_text (warning_line):
        """! Iterate over warning_line, prints warning in template format
        @param warning_line     The warning to be printed.
        @return                 Warning output string.
        """

        out_template = "Warning! On line {line_num}, variable {last_token} changes abstraction layer from {last_layer} to {first_layer}"
        line_num = int(warning_line['line_num'])
        out = out_template.format(line_num = line_num,last_token = warning_line['tokens'][-1],last_layer = warning_line['layers'][-1],first_layer = list(warning_line['layers'])[-2])
        return out
