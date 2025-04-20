#Given a string input_string, your task is to write a function that transforms all the lowercase
#letters to uppercase and all the uppercase letters to lowercase. If the character is not a letter,
#do not transform it.
#The transformation should be done without using any built-in Python methods, it is not allowed to
#use built-in Python functions like lower(), upper(), or similar in your code.
#For example, for the input string "HelLo WoRld 123", the output should be "hELlO wOrLD 123".

class AlphabetCaseConversion:

    def solution(input_string):

        upr_lwr = dict(zip([chr(x) for x in range(65, 91)], [chr(y) for y in range(97, 123)]))
        lwr_upr = dict(zip([chr(x) for x in range(97, 123)] , [chr(y) for y in range(65, 91)]))

        ret_str = ''
        for c in input_string:
            if c in upr_lwr:
                ret_str += upr_lwr.get(c)
            elif c in lwr_upr:
                ret_str += lwr_upr.get(c)
            else:
                ret_str += c
        return ret_str

#if __name__ == '__main__':
