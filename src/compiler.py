from src.tac_generator import TACGenerator
from src.lexer import Lexer
from src.semantic import Semantic
from src.syntax import Syntax
from src.util import Util


class Compiler:

    @staticmethod
    def compile(folder, file_name):
        code = Util.read_code_from_file(f'../resources/{folder}/{file_name}.txt')
        if not code:
            return

        print(f"\n-------------- Compilando arquivo {file_name} -------------- ")
        try:
            lexer = Lexer()
            tokens, symbol_table = lexer.start_lexer(code, folder, file_name)
            try:
                syntax = Syntax(tokens, symbol_table, None)
                syntax.start_syntax(folder, file_name)
                try:
                    semantic = Semantic(tokens, symbol_table, folder, file_name)
                    semantic.start_semantic()
                    try:
                        address = TACGenerator(tokens, symbol_table, folder, file_name)
                        address.generate()
                    except SyntaxError as e:
                        Util.print_error(f"\nErro durante a transformação para código de 3 endereços: {e}")
                except SyntaxError as e:
                    Util.print_error(f"\nErro durante a análise semântica: {e}")
            except SyntaxError as e:
                Util.print_error(f"\nErro durante a análise sintática: {e}")
        except SyntaxError as e:
            Util.print_error(f"\nErro durante a análise léxica: {e}")
