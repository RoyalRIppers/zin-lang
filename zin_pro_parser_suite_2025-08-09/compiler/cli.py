from __future__ import annotations
import argparse, json, sys, os, subprocess, shutil
from antlr4 import FileStream, CommonTokenStream
from . import version

# Generated parser (created at runtime by 'zinc gen')
# We'll add its path dynamically from default location.
GEN_PATH = os.path.join("compiler", "gen", "python")
if GEN_PATH not in sys.path:
    sys.path.insert(0, GEN_PATH)

def ensure_generated():
    try:
        import ZinLexer, ZinParser
        return True
    except Exception:
        return False

def gen_parser():
    # Detect OS and run corresponding script
    if os.name == "nt":
        script = os.path.join("scripts", "gen_parser.ps1")
        cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", script]
    else:
        script = os.path.join("scripts", "gen_parser.sh")
        cmd = ["bash", script]
    if not os.path.exists(script):
        print("ERR: generation script not found. Make sure scripts/ exists.", file=sys.stderr)
        return 2
    print("[zinc] Generating parser via ANTLR...")
    return subprocess.call(cmd)

def parse_file(path):
    if not ensure_generated():
        print("ERR: parser not generated. Run 'zinc gen' first.", file=sys.stderr)
        return 2
    from ZinLexer import ZinLexer
    from ZinParser import ZinParser
    from antlr4 import CommonTokenStream

    input_stream = FileStream(path, encoding='utf-8')
    lexer = ZinLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ZinParser(tokens)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() == 0:
        print(f"PARSE OK  {path}")
        return 0
    else:
        print(f"PARSE ERR {path}", file=sys.stderr)
        return 1

def ast_file(path):
    if not ensure_generated():
        print("ERR: parser not generated. Run 'zinc gen' first.", file=sys.stderr)
        return 2
    from .ast_builder import ASTBuilder
    from ZinLexer import ZinLexer
    from ZinParser import ZinParser
    from antlr4 import CommonTokenStream

    input_stream = FileStream(path, encoding='utf-8')
    lexer = ZinLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ZinParser(tokens)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() != 0:
        print(f"PARSE ERR {path}", file=sys.stderr)
        return 1
    builder = ASTBuilder()
    prog = builder.visit(tree)
    from .ast_nodes import ast_to_json
    print(json.dumps(ast_to_json(prog), ensure_ascii=False, indent=2))
    return 0

def main():
    ap = argparse.ArgumentParser(prog="zinc", description="Zin compiler toolkit (parser/AST)")
    ap.add_argument("-v", "--version", action="store_true", help="show version and exit")
    sub = ap.add_subparsers(dest="cmd")

    ap_gen = sub.add_parser("gen", help="generate parser from Zin.g4")
    ap_parse = sub.add_parser("parse", help="parse a .zin file")
    ap_parse.add_argument("file")
    ap_ast = sub.add_parser("ast", help="print AST JSON of a .zin file")
    ap_ast.add_argument("file")

    args = ap.parse_args()
    if args.version:
        print(version)
        return 0
    if args.cmd == "gen":
        return gen_parser()
    if args.cmd == "parse":
        return parse_file(args.file)
    if args.cmd == "ast":
        return ast_file(args.file)
    ap.print_help()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
