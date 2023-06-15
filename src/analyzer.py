import logging
import os
import re
from collections import defaultdict

import ast
from _ast import (
    Add, Module, Interactive,
    Expression, FunctionDef, AsyncFunctionDef, ClassDef, Return,
    Delete, Assign, AugAssign, AnnAssign, For,
    withitem, alias,
    keyword, arg, arguments, ExceptHandler, comprehension,
    NotIn, NotEq, LtE, Lt, IsNot, Is, In, GtE, Gt, Eq, USub,
    UAdd, AsyncFor, While, If, With, AsyncWith, Raise, Try,
    Assert, Import, ImportFrom, Global, Nonlocal, Expr, Pass,
    Break, Continue, Slice, BoolOp, BinOp, UnaryOp, Lambda,
    IfExp, Dict, Set, ListComp, SetComp, DictComp, GeneratorExp,
    Await, Yield, YieldFrom, Compare, Call, FormattedValue,
    JoinedStr, Constant, NamedExpr, Attribute, Subscript,
    Starred, Name, List, Tuple, Del, Load, Store, And, Or,
    BitAnd, BitOr, BitXor, Div, FloorDiv, LShift, Mod, Mult,
    MatMult, Pow, RShift, Sub, Invert, Not
)
from typing import Any

logger = logging.getLogger(__name__)


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = defaultdict(bool)

    def visit_Module(self, node: Module) -> Any:
        print('Module')
        print(node.__dict__)
        self.stats['Module'] = True
        self.generic_visit(node)

    def visit_Interactive(self, node: Interactive) -> Any:
        print('Interactive')
        print(node.__dict__)
        self.stats['Interactive'] = True
        self.generic_visit(node)

    def visit_Expression(self, node: Expression) -> Any:
        print('Expression')
        print(node.__dict__)
        self.stats['Expression'] = True
        self.generic_visit(node)

    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        print('FunctionDef')
        print(node.__dict__)
        self.stats['FunctionDef'] = True
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: AsyncFunctionDef) -> Any:
        print('AsyncFunctionDef')
        print(node.__dict__)
        self.stats['AsyncFunctionDef'] = True
        self.generic_visit(node)

    def visit_ClassDef(self, node: ClassDef) -> Any:
        print('ClassDef')
        print(node.__dict__)
        self.stats['ClassDef'] = True
        self.generic_visit(node)

    def visit_Return(self, node: Return) -> Any:
        print('Return')
        print(node.__dict__)
        self.stats['Return'] = True
        self.generic_visit(node)

    def visit_Delete(self, node: Delete) -> Any:
        print('Delete')
        print(node.__dict__)
        self.stats['Delete'] = True
        self.generic_visit(node)

    def visit_Assign(self, node: Assign) -> Any:
        print('Assign')
        print(node.__dict__)
        self.stats['Assign'] = True
        self.generic_visit(node)

    def visit_AugAssign(self, node: AugAssign) -> Any:
        print('AugAssign')
        print(node.__dict__)
        self.stats['AugAssign'] = True
        self.generic_visit(node)

    def visit_AnnAssign(self, node: AnnAssign) -> Any:
        print('AnnAssign')
        print(node.__dict__)
        self.stats['AnnAssign'] = True
        self.generic_visit(node)

    def visit_For(self, node: For) -> Any:
        print('For')
        print(node.__dict__)
        self.stats['For'] = True
        self.generic_visit(node)

    def visit_AsyncFor(self, node: AsyncFor) -> Any:
        print('AsyncFor')
        print(node.__dict__)
        self.stats['AsyncFor'] = True
        self.generic_visit(node)

    def visit_While(self, node: While) -> Any:
        print('While')
        print(node.__dict__)
        self.stats['While'] = True
        self.generic_visit(node)

    def visit_If(self, node: If) -> Any:
        print('If')
        print(node.__dict__)
        self.stats['If'] = True
        self.generic_visit(node)

    def visit_With(self, node: With) -> Any:
        print('With')
        print(node.__dict__)
        self.stats['With'] = True
        self.generic_visit(node)

    def visit_AsyncWith(self, node: AsyncWith) -> Any:
        print('AsyncWith')
        print(node.__dict__)
        self.stats['AsyncWith'] = True
        self.generic_visit(node)

    def visit_Raise(self, node: Raise) -> Any:
        print('Raise')
        print(node.__dict__)
        self.stats['Raise'] = True
        self.generic_visit(node)

    def visit_Try(self, node: Try) -> Any:
        print('Try')
        print(node.__dict__)
        self.stats['Try'] = True
        self.generic_visit(node)

    def visit_Assert(self, node: Assert) -> Any:
        print('Assert')
        print(node.__dict__)
        self.stats['Assert'] = True
        self.generic_visit(node)

    def visit_Import(self, node: Import) -> Any:
        print('Import')
        print(node.__dict__)
        self.stats['Import'] = True
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ImportFrom) -> Any:
        print('ImportFrom')
        print(node.__dict__)
        self.stats['ImportFrom'] = True
        self.generic_visit(node)

    def visit_Global(self, node: Global) -> Any:
        print('Global')
        print(node.__dict__)
        self.stats['Global'] = True
        self.generic_visit(node)

    def visit_Nonlocal(self, node: Nonlocal) -> Any:
        print('Nonlocal')
        print(node.__dict__)
        self.stats['Nonlocal'] = True
        self.generic_visit(node)

    def visit_Expr(self, node: Expr) -> Any:
        print('Expr')
        print(node.__dict__)
        self.stats['Expr'] = True
        self.generic_visit(node)

    def visit_Pass(self, node: Pass) -> Any:
        print('Pass')
        print(node.__dict__)
        self.stats['Pass'] = True
        self.generic_visit(node)

    def visit_Break(self, node: Break) -> Any:
        print('Break')
        print(node.__dict__)
        self.stats['Break'] = True
        self.generic_visit(node)

    def visit_Continue(self, node: Continue) -> Any:
        print('Continue')
        print(node.__dict__)
        self.stats['Continue'] = True
        self.generic_visit(node)

    def visit_Slice(self, node: Slice) -> Any:
        print('Slice')
        print(node.__dict__)
        self.stats['Slice'] = True
        self.generic_visit(node)

    def visit_BoolOp(self, node: BoolOp) -> Any:
        print('BoolOp')
        print(node.__dict__)
        self.stats['BoolOp'] = True
        self.generic_visit(node)

    def visit_BinOp(self, node: BinOp) -> Any:
        print('BinOp')
        print(node.__dict__)
        self.stats['BinOp'] = True
        self.generic_visit(node)

    def visit_UnaryOp(self, node: UnaryOp) -> Any:
        print('UnaryOp')
        print(node.__dict__)
        self.stats['UnaryOp'] = True
        self.generic_visit(node)

    def visit_Lambda(self, node: Lambda) -> Any:
        print('Lambda')
        print(node.__dict__)
        self.stats['Lambda'] = True
        self.generic_visit(node)

    def visit_IfExp(self, node: IfExp) -> Any:
        print('IfExp')
        print(node.__dict__)
        self.stats['IfExp'] = True
        self.generic_visit(node)

    def visit_Dict(self, node: Dict) -> Any:
        print('Dict')
        print(node.__dict__)
        self.stats['Dict'] = True
        self.generic_visit(node)

    def visit_Set(self, node: Set) -> Any:
        print('Set')
        print(node.__dict__)
        self.stats['Set'] = True
        self.generic_visit(node)

    def visit_ListComp(self, node: ListComp) -> Any:
        print('ListComp')
        print(node.__dict__)
        self.stats['ListComp'] = True
        self.generic_visit(node)

    def visit_SetComp(self, node: SetComp) -> Any:
        print('SetComp')
        print(node.__dict__)
        self.stats['SetComp'] = True
        self.generic_visit(node)

    def visit_DictComp(self, node: DictComp) -> Any:
        print('DictComp')
        print(node.__dict__)
        self.stats['DictComp'] = True
        self.generic_visit(node)

    def visit_GeneratorExp(self, node: GeneratorExp) -> Any:
        print('GeneratorExp')
        print(node.__dict__)
        self.stats['GeneratorExp'] = True
        self.generic_visit(node)

    def visit_Await(self, node: Await) -> Any:
        print('Await')
        print(node.__dict__)
        self.stats['Await'] = True
        self.generic_visit(node)

    def visit_Yield(self, node: Yield) -> Any:
        print('Yield')
        print(node.__dict__)
        self.stats['Yield'] = True
        self.generic_visit(node)

    def visit_YieldFrom(self, node: YieldFrom) -> Any:
        print('YieldFrom')
        print(node.__dict__)
        self.stats['YieldFrom'] = True
        self.generic_visit(node)

    def visit_Compare(self, node: Compare) -> Any:
        print('Compare')
        print(node.__dict__)
        self.stats['Compare'] = True
        self.generic_visit(node)

    def visit_Call(self, node: Call) -> Any:
        print('Call')
        print(node.__dict__)
        self.stats['Call'] = True
        self.generic_visit(node)

    def visit_FormattedValue(self, node: FormattedValue) -> Any:
        print('FormattedValue')
        print(node.__dict__)
        self.stats['FormattedValue'] = True
        self.generic_visit(node)

    def visit_JoinedStr(self, node: JoinedStr) -> Any:
        print('JoinedStr')
        print(node.__dict__)
        self.stats['JoinedStr'] = True
        self.generic_visit(node)

    def visit_Constant(self, node: Constant) -> Any:
        print('Constant')
        print(node.__dict__)
        self.stats['Constant'] = True
        self.generic_visit(node)

    def visit_NamedExpr(self, node: NamedExpr) -> Any:
        print('NamedExpr')
        print(node.__dict__)
        self.stats['NamedExpr'] = True
        self.generic_visit(node)

    def visit_Attribute(self, node: Attribute) -> Any:
        print('Attribute')
        print(node.__dict__)
        self.stats['Attribute'] = True
        self.generic_visit(node)

    def visit_Subscript(self, node: Subscript) -> Any:
        print('Subscript')
        print(node.__dict__)
        self.stats['Subscript'] = True
        self.generic_visit(node)

    def visit_Starred(self, node: Starred) -> Any:
        print('Starred')
        print(node.__dict__)
        self.stats['Starred'] = True
        self.generic_visit(node)

    def visit_Name(self, node: Name) -> Any:
        print('Name')
        print(node.__dict__)
        self.stats['Name'] = True
        self.generic_visit(node)

    def visit_List(self, node: List) -> Any:
        print('List')
        print(node.__dict__)
        self.stats['List'] = True
        self.generic_visit(node)

    def visit_Tuple(self, node: Tuple) -> Any:
        print('Tuple')
        print(node.__dict__)
        self.stats['Tuple'] = True
        self.generic_visit(node)

    def visit_Del(self, node: Del) -> Any:
        print('Del')
        print(node.__dict__)
        self.stats['Del'] = True
        self.generic_visit(node)

    def visit_Load(self, node: Load) -> Any:
        print('Load')
        print(node.__dict__)
        self.stats['Load'] = True
        self.generic_visit(node)

    def visit_Store(self, node: Store) -> Any:
        print('Store')
        print(node.__dict__)
        self.stats['Store'] = True
        self.generic_visit(node)

    def visit_And(self, node: And) -> Any:
        print('And')
        print(node.__dict__)
        self.stats['And'] = True
        self.generic_visit(node)

    def visit_Or(self, node: Or) -> Any:
        print('Or')
        print(node.__dict__)
        self.stats['Or'] = True
        self.generic_visit(node)

    def visit_Add(self, node: Add) -> Any:
        print('Add')
        print(node.__dict__)
        self.stats['Add'] = True
        self.generic_visit(node)

    def visit_BitAnd(self, node: BitAnd) -> Any:
        print('BitAnd')
        print(node.__dict__)
        self.stats['BitAnd'] = True
        self.generic_visit(node)

    def visit_BitOr(self, node: BitOr) -> Any:
        print('BitOr')
        print(node.__dict__)
        self.stats['BitOr'] = True
        self.generic_visit(node)

    def visit_BitXor(self, node: BitXor) -> Any:
        print('BitXor')
        print(node.__dict__)
        self.stats['BitXor'] = True
        self.generic_visit(node)

    def visit_Div(self, node: Div) -> Any:
        print('Div')
        print(node.__dict__)
        self.stats['Div'] = True
        self.generic_visit(node)

    def visit_FloorDiv(self, node: FloorDiv) -> Any:
        print('FloorDiv')
        print(node.__dict__)
        self.stats['FloorDiv'] = True
        self.generic_visit(node)

    def visit_LShift(self, node: LShift) -> Any:
        print('LShift')
        print(node.__dict__)
        self.stats['LShift'] = True
        self.generic_visit(node)

    def visit_Mod(self, node: Mod) -> Any:
        print('Mod')
        print(node.__dict__)
        self.stats['Mod'] = True
        self.generic_visit(node)

    def visit_Mult(self, node: Mult) -> Any:
        print('Mult')
        print(node.__dict__)
        self.stats['Mult'] = True
        self.generic_visit(node)

    def visit_MatMult(self, node: MatMult) -> Any:
        print('MatMult')
        print(node.__dict__)
        self.stats['MatMult'] = True
        self.generic_visit(node)

    def visit_Pow(self, node: Pow) -> Any:
        print('Pow')
        print(node.__dict__)
        self.stats['Pow'] = True
        self.generic_visit(node)

    def visit_RShift(self, node: RShift) -> Any:
        print('RShift')
        print(node.__dict__)
        self.stats['RShift'] = True
        self.generic_visit(node)

    def visit_Sub(self, node: Sub) -> Any:
        print('Sub')
        print(node.__dict__)
        self.stats['Sub'] = True
        self.generic_visit(node)

    def visit_Invert(self, node: Invert) -> Any:
        print('Invert')
        print(node.__dict__)
        self.stats['Invert'] = True
        self.generic_visit(node)

    def visit_Not(self, node: Not) -> Any:
        print('Not')
        print(node.__dict__)
        self.stats['Not'] = True
        self.generic_visit(node)

    def visit_UAdd(self, node: UAdd) -> Any:
        print('UAdd')
        print(node.__dict__)
        self.stats['UAdd'] = True
        self.generic_visit(node)

    def visit_USub(self, node: USub) -> Any:
        print('USub')
        print(node.__dict__)
        self.stats['USub'] = True
        self.generic_visit(node)

    def visit_Eq(self, node: Eq) -> Any:
        print('Eq')
        print(node.__dict__)
        self.stats['Eq'] = True
        self.generic_visit(node)

    def visit_Gt(self, node: Gt) -> Any:
        print('Gt')
        print(node.__dict__)
        self.stats['Gt'] = True
        self.generic_visit(node)

    def visit_GtE(self, node: GtE) -> Any:
        print('GtE')
        print(node.__dict__)
        self.stats['GtE'] = True
        self.generic_visit(node)

    def visit_In(self, node: In) -> Any:
        print('In')
        print(node.__dict__)
        self.stats['In'] = True
        self.generic_visit(node)

    def visit_Is(self, node: Is) -> Any:
        print('Is')
        print(node.__dict__)
        self.stats['Is'] = True
        self.generic_visit(node)

    def visit_IsNot(self, node: IsNot) -> Any:
        print('IsNot')
        print(node.__dict__)
        self.stats['IsNot'] = True
        self.generic_visit(node)

    def visit_Lt(self, node: Lt) -> Any:
        print('Lt')
        print(node.__dict__)
        self.stats['Lt'] = True
        self.generic_visit(node)

    def visit_LtE(self, node: LtE) -> Any:
        print('LtE')
        print(node.__dict__)
        self.stats['LtE'] = True
        self.generic_visit(node)

    def visit_NotEq(self, node: NotEq) -> Any:
        print('NotEq')
        print(node.__dict__)
        self.stats['NotEq'] = True
        self.generic_visit(node)

    def visit_NotIn(self, node: NotIn) -> Any:
        print('NotIn')
        print(node.__dict__)
        self.stats['NotIn'] = True
        self.generic_visit(node)

    def visit_comprehension(self, node: comprehension) -> Any:
        print('comprehension')
        print(node.__dict__)
        self.stats['comprehension'] = True
        self.generic_visit(node)

    def visit_ExceptHandler(self, node: ExceptHandler) -> Any:
        print('ExceptHandler')
        print(node.__dict__)
        self.stats['ExceptHandler'] = True
        self.generic_visit(node)

    def visit_arguments(self, node: arguments) -> Any:
        print('arguments')
        print(node.__dict__)
        self.stats['arguments'] = True
        self.generic_visit(node)

    def visit_arg(self, node: arg) -> Any:
        print('arg')
        print(node.__dict__)
        self.stats['arg'] = True
        self.generic_visit(node)

    def visit_keyword(self, node: keyword) -> Any:
        print('keyword')
        print(node.__dict__)
        self.stats['keyword'] = True
        self.generic_visit(node)

    def visit_alias(self, node: alias) -> Any:
        print('alias')
        print(node.__dict__)
        self.stats['alias'] = True
        self.generic_visit(node)

    def visit_withitem(self, node: withitem) -> Any:
        print('withitem')
        print(node.__dict__)
        self.stats['withitem'] = True
        self.generic_visit(node)


class AnayzerRunner(object):
    def __init__(self, root_dir: str):
        self.stats = defaultdict(bool)
        self.filename_to_analyzer_result = defaultdict(dict)
        self.root_dr = os.path.abspath(root_dir)
        self.files_paths = []
        for data in os.walk(root_dir):
            current_dir, _, files = data
            for file in files:
                if ".py" in file:
                    self.files_paths.append(
                        os.path.abspath(
                            os.path.join(
                                current_dir,
                                file
                            )
                        )
                    )

    def process_analyzer_results(
            self,
            analyzer: Analyzer,
            filename: str
    ):
        logger.info(analyzer.stats)
        for key in analyzer.stats:
            self.stats[key] |= analyzer.stats[key]
        self.filename_to_analyzer_result[
            filename.replace(self.root_dr, '')
        ] = analyzer.stats

    def run(self):
        for filename in self.files_paths:
            with open(filename, 'r') as source:
                tree = ast.parse(source.read())
                analyzer = Analyzer()
                analyzer.visit(tree)
                self.process_analyzer_results(analyzer, filename)


def main():
    with open("test_module.py", "r") as source:
        tree = ast.parse(source.read())

    analyzer = Analyzer()
    analyzer.visit(tree)
