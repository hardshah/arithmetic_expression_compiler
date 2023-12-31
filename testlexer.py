from lexer import lexer

INPUT_CODE = """
x = 5;
y = 10;
z = x + y * 2;
"""
def main():
    lexer.input(INPUT_CODE)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)

if __name__ == "__main__":
    main()