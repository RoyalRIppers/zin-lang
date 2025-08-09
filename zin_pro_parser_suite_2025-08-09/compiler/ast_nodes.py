from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List, Optional, Union, Dict

# --- Expression nodes
@dataclass
class Expr: ...
@dataclass
class Literal(Expr):
    value: Any
@dataclass
class Identifier(Expr):
    name: str
@dataclass
class Unary(Expr):
    op: str
    right: Expr
@dataclass
class Binary(Expr):
    left: Expr
    op: str
    right: Expr
@dataclass
class Assign(Expr):
    target: Identifier
    op: str  # '=', '+=', ...
    value: Expr
@dataclass
class Call(Expr):
    callee: Expr
    args: List[Expr] = field(default_factory=list)

# --- Statements
@dataclass
class Stmt: ...
@dataclass
class VarDecl(Stmt):
    type_name: str
    name: str
    init: Optional[Expr] = None
@dataclass
class Return(Stmt):
    value: Optional[Expr]
@dataclass
class Print(Stmt):
    value: Expr
@dataclass
class Sleep(Stmt):
    value: Expr
@dataclass
class Block(Stmt):
    statements: List[Stmt] = field(default_factory=list)
@dataclass
class If(Stmt):
    cond: Expr
    then: Block
    otherwise: Optional[Block] = None
@dataclass
class While(Stmt):
    cond: Expr
    body: Block = field(default_factory=Block)
@dataclass
class For(Stmt):
    var: str
    start: Expr
    end: Expr
    body: Block
@dataclass
class FnParam:
    type_name: str
    name: str
@dataclass
class FnDecl(Stmt):
    name: str
    params: List[FnParam]
    return_type: Optional[str]
    body: Block
@dataclass
class StructField:
    type_name: str
    name: str
@dataclass
class StructDecl(Stmt):
    name: str
    fields: List[StructField]
@dataclass
class Program:
    decls: List[Stmt] = field(default_factory=list)

def ast_to_json(node: Any) -> Any:
    from dataclasses import is_dataclass, asdict
    if is_dataclass(node):
        d = asdict(node)
        for k, v in d.items():
            d[k] = ast_to_json(v)
        d["__type__"] = node.__class__.__name__
        return d
    if isinstance(node, list):
        return [ast_to_json(x) for x in node]
    return node
