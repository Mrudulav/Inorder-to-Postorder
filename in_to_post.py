"""
CSCI-603: InToPost
Author: Sean Strout @ RIT CS
Author: {YOUR NAME HERE}

The main program and class for an infix to postfix expression
converter.

Usage: python3 inToPost.py source-file.in
"""

from myqueue import MyQueue
from mystack import MyStack
from sys import argv

class InToPost:
    """
    A class that converts infix expressions from a source file into postfix.
    :slot: expressions (list of queue of strings):  The converted postfix expressions
    :slot: src_file (string):  The name of the source file
    :slot: precedence (dict):  A dictionary that maps the tokens in the
    language (string) to their precedence level (1 being lowest to 3 the
    highest)
    """
    __slots__ = 'expressions', 'src_file', 'precedence'

    # the recognized tokens in the language
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '//'
    OPEN_PAREN = '('
    CLOSE_PAREN = ')'

    def __init__(self, filename):
        """
        Create a new instance.
        :param filename: The name of the source file
        :return: None
        """
        self.expressions = []
        self.src_file = filename
        self.precedence = {}
        self.precedence[InToPost.MULTIPLY] = 3
        self.precedence[InToPost.DIVIDE] = 3
        self.precedence[InToPost.ADD] = 2
        self.precedence[InToPost.SUBTRACT] = 2
        self.precedence[InToPost.OPEN_PAREN] = 1

    def __convert(self, tokens):
        """
        A private helper function that takes one infix expression
        and converts it to postfix.  For example:

            tokens = [ '(', 'A', '+', 'B', ')', '*', 'C' ]
            returns (as a queue): [ 'A', 'B', '+', 'C', '*' ]

        :param tokens: A list of strings for the infix expression
        :return: A queue of strings for the postfix expression
        """
        return MyQueue()   # change this to your implementation

    def convert(self):
        """
        Convert the source file from infix to postfix expressions.
        :return: None
        """
        with open(self.src_file) as f:
            for expression in f:
                tokens = expression.split()
                if len(tokens) > 0:
                    self.expressions.append(self.__convert(tokens))

    def emit(self):
        """
        Print the postfix expressions.
        :return: None
        """
        for expression in self.expressions:
            while not expression.is_empty():
                print(expression.peek(), end=' ')
                expression.dequeue()
            print()

def main():
    """
    The main program prompts for the source file.  It then converts
    the infix expressions to postfix and displays them.
    :return: None
    """
    if len(argv) != 2:
        print('Usage: python3 in_to_post.py source-file.in')
        return

    inToPost = InToPost(argv[1])
    print("InToPost: converting expressions from infix to postfix...")
    inToPost.convert()
    print("InToPost: emitting postfix expressions...")
    inToPost.emit()

if __name__ == '__main__':
    main()