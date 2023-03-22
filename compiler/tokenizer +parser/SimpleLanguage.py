#Liam Bockelmann
#ID: 108613490


import sys
import ply.lex as lex
import ply.yacc as yacc

symbol_table = dict()

class Node:
	def __init__(self):
		pass

	def evaluate(self):
		return 0

	def execute(self):
		return 0

class BlockNode(Node):
	def __init__(self, s):
		self.s1 = [s]

	def execute(self):
		for statement in self.s1:
			statement.execute()

class ExpressionNode(Node):
	def evaluate(self):
		return None

class IntNode(ExpressionNode):
	def __init__(self, val):
		self.val = int(val)

	def evaluate(self):
		return self.val

class RealNode(ExpressionNode):
	def __init__(self, val):
		self.val = float(val)

	def evaluate(self):
		return self.val

class BoolNode(ExpressionNode):
	def __init__(self, val):
		self.val = val

	def evaluate(self):
		return self.val

class StringNode(ExpressionNode):
	def __init__(self, val):
		self.val = val

	def evaluate(self):
		return self.val

class ExpNode(ExpressionNode):
	def __init__(self, base, expo):
		self.base = base
		self.expo = expo

	def evaluate(self):
		return self.base.evaluate() ** self.expo.evaluate()

class ListNode(ExpressionNode):
	def __init__(self, val):
		self.val = val

	def evaluate(self):
		res = []
		for n in self.val:
			res.append(n.evaluate())
		return res

class IndexNode(ExpressionNode):
	def __init__(self, obj, ind):
		self.obj = obj
		self.ind = ind

	def evaluate(self):
		return self.obj.evaluate()[self.ind.evaluate()]

class UnaryOpNode(ExpressionNode):
	def __init__(self, op, val):
		self.op = op
		self.val = val

	def evaluate(self):
		return -self.value.evaluate()

class UnaryNotNode(ExpressionNode):
	def __init__(self, op, val):
		self.op = op
		self.val = val

	def evaluate(self):
		return not self.val.evaluate()

class BoolOpNode(ExpressionNode):
	def __init__(self, op, v1, v2):
		self.op = op
		self.v1 = v1
		self.v2 = v2

	def evaluate(self):
		if self.op.vid == 'and':
			res = self.v1.evaluate() and self.v2.evaluate()
		elif self.op.vid == 'or':
			res = self.v1.evaluate() or self.v2.evaluate()
		return res

class BinOpNode(ExpressionNode):
	def __init__(self, op, v1, v2):
		self.op = op
		self.v1 = v1
		self.v2 = v2

	def evaluate(self):
		if self.op == '+':
			return self.v1.evaluate() + self.v2.evaluate()
		elif self.op == '-':
			return self.v1.evaluate() - self.v2.evaluate()
		elif self.op == '*':
			return self.v1.evaluate() * self.v2.evaluate()
		elif self.op == '/':
			return self.v1.evaluate() / self.v2.evaluate()
		elif self.op == '%':
			return self.v1.evaluate() % self.v2.evaluate()
		elif self.op == '//':
			return self.v1.evaluate() // self.v2.evaluate()

class CompNode(ExpressionNode):
	def __init__(self, op, v1, v2):
		self.op = op
		self.v1 = v1
		self.v2 = v2

	def evaluate(self):
		if self.op == '<':
			return self.v1.evaluate() < self.v2.evaluate()
		elif self.op == '<=':
			return self.v1.evaluate() <= self.v2.evaluate()
		elif self.op == '==':
			return self.v1.evaluate() == self.v2.evaluate()
		elif self.op == '<>':
			return self.v1.evaluate() != self.v2.evaluate()
		elif self.op == '>':
			return self.v1.evaluate() > self.v2.evaluate()
		elif self.op == '>=':
			return self.v1.evaluate() >= self.v2.evaluate()

class IDNode(ExpressionNode):
	def __init__(self, vid):
		self.vid = vid

	def evaluate(self):
		return symbol_table[self.vid]

class ContainsNode(ExpressionNode):
	def __init__(self, obj, tgt):
		self.obj = obj
		self.tgt = tgt

	def evaluate(self):
		return self.obj.evaluate().__contains__(self.tgt.evaluate())

class StatementNode(Node):
	def execute(self):
		pass

class PrintNode(StatementNode):
	def __init__(self, exp):
		self.exp = exp

	def execute(self):
		print(str(self.exp.evaluate()))

class AssignNode(StatementNode):
	def __init__(self, vnode, exp):
		self.vnode = vnode
		self.exp = exp

	def execute(self):
		symbol_table[self.vnode.vid] = self.exp.evaluate()

class AssignToListNode(StatementNode):
	def __init__(self, vnode, ind, exp):
		self.vnode = vnode
		self.exp = exp
		self.ind = ind

	def execute(self):
		symbol_table[self.vnode.vid][self.ind.evaluate()] = self.exp.evaluate()

class IfNode(StatementNode):
	def __init__(self, cond, block):
		self.cond = cond
		self.block = block

	def execute(self):
		if(self.cond.evaluate()):
			self.block.execute()

class IfElseNode(StatementNode):
	def __init__(self, cond, iblock, eblock):
		self.cond = cond
		self.iblock = iblock
		self.eblock = eblock

	def execute(self):
		if(self.cond.evaluate()):
			self.iblock.execute()
		else:
			self.eblock.execute()

class WhileNode(StatementNode):
	def __init__(self, cond, block):
		self.cond = cond
		self.block = block

	def execute(self):
		while self.cond.evaluate():
			self.block.execute()

reserved = {
	'if' : 'IF',
	'else' : 'ELSE',
	'while' : 'WHILE',
	'not' : 'NOT',
	'and' : 'AND',
	'or' : 'OR',
	'in' : 'IN',
	'print' : 'PRINT'
}

tokens = [
	'INTEGER','REAL','STRING',
	'COMMA',
	'LPAREN','RPAREN',
	'LBLOCK','RBLOCK',
	'BOOL',
	'EXP',
	'MULT','DIV','MOD','INTDIV',
	'ADD','SUB',
	'LESS','LESSEQ','EQUAL','NOTEQUAL','GREATER','GREATEREQ',
	'ASSIGN',
	'LBRACE','RBRACE',
	'SEMI','ID'
] + list(reserved.values())

t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBLOCK = r'\['
t_RBLOCK = r'\]'
t_MULT = r'\*'
t_DIV = r'/'
t_EXP = r'\*\*'
t_MOD = r'%'
t_INTDIV = r'//'
t_ADD = r'\+'
t_SUB = r'-'
t_LESS = r'<'
t_LESSEQ = r'<='
t_EQUAL = r'=='
t_NOTEQUAL = r'<>'
t_GREATER = r'>'
t_GREATEREQ = r'>='
t_ASSIGN = r'='
t_LBRACE = r'{'
t_RBRACE = r'}'
t_SEMI = r';'
t_ignore = ' \t'

def t_REAL(token):
	r'\d*(\d\.|\.\d)\d*'
	token.value = RealNode(token.value)
	return token

def t_INTEGER(token):
	r'\d+'
	token.value = IntNode(token.value)
	return token

def t_STRING(token):
	r'(\"[^\"]*\") | (\'[^\']*\')'
	token.value = StringNode(token.value[1:len(token.value) - 1])
	return token

def t_BOOL(token):
	r'True|False'
	token.value = BoolNode(token.value == "True")
	return token

def t_ID(token):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	token.type = reserved.get(token.value, 'ID')
	token.value = IDNode(token.value)
	return token

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(token):
	print("Illegal character '%s'" % token.value[0])
	token.lexer.skip(1)

precedence = (
	('right','ASSIGN'),
	('left','PRINT'),
	('left','OR'),
	('left','AND'),
	('left','NOT'),
	('left','UNOT'),
	('left','LESS','LESSEQ','EQUAL','NOTEQUAL','GREATER','GREATEREQ'),
	('left','IN'),
	('left','ADD','SUB'),
	('left','INTDIV'),
	('left','UMINUS'),
	('left','MOD'),
	('left','MULT','DIV'),
	('right','EXP'),
	('left','LBLOCK'),
	('left','LIST'),
	('left','INDEX')
	)

def p_block(t):
	"""
	block : LBRACE inblock RBRACE
	"""
	t[0] = t[2]

def p_emptyblock(t):
	'''
	block : LBRACE RBRACE
	'''
	t[0] = BlockNode([])
	t[0].s1 = []

def p_inblock(t):
	"""
	inblock : statement inblock
	"""
	t[0] = t[2]
	t[0].s1.insert(0,t[1])

def p_inblock2(t):
	"""
	inblock : statement
	"""
	t[0] = BlockNode(t[1])

def p_smt(t):
	"""
	statement : print_smt
			  | assign_smt
			  | assign_to_list
			  | if_smt
			  | ifelse
			  | while_smt
			  | solo_block
	"""
	t[0] = t[1]

def p_statement_print(token):
	'print_smt : PRINT LPAREN expression RPAREN SEMI %prec PRINT'
	token[0] = PrintNode(token[3])

def p_statement_assign(token):
	'''assign_smt : ID ASSIGN expression SEMI %prec ASSIGN'''
	token[0] = AssignNode(token[1], token[3])

def p_statment_assign_to_list(token):
	'''assign_to_list : ID LBLOCK expression RBLOCK ASSIGN expression SEMI %prec ASSIGN'''
	token[0] = AssignToListNode(token[1],token[3],token[6])

def p_statement_while(token):
	'while_smt : WHILE LPAREN expression RPAREN block'
	token[0] = WhileNode(token[3],token[5])

def p_statment_if(token):
	'if_smt : IF LPAREN expression RPAREN block'
	token[0] = IfNode(token[3],token[5])

def p_statement_solo_block(token):
	'solo_block : block'
	token[0] = BlockNode(token[1])

def p_statment_ifelse(token):
	'ifelse : if_smt ELSE block'
	token[0] = IfElseNode(token[1].cond, token[1].block, token[3])

def p_empty(p):
	'empty :'
	pass

def p_expression_inlist(token):
	'''expression : expression IN expression %prec IN'''
	token[0] = ContainsNode(token[3],token[1])

def p_expression_index(token):
	'''expression : STRING LBLOCK expression RBLOCK
				  | expression LBLOCK expression RBLOCK %prec INDEX'''
	token[0] = IndexNode(token[1], token[3])

def p_expression_group(token):
	'expression : LPAREN expression RPAREN'
	token[0] = token[2]

def p_expression_list(token):
	'''expression : LBLOCK expression term RBLOCK
				  | LBLOCK RBLOCK %prec LIST'''
	token[0] = []
	if len(token) > 3:
		token[3].insert(0,token[2])
		token[0] = token[3]
	token[0] = ListNode(token[0])

def p_expression_term(token):
	'''term : COMMA expression term
			| empty %prec LIST'''
	if len(token) > 2:
		token[0] = token[2]
		token[3].insert(0,token[0])
		token[0] = token[3]
	else:
		token[0] = []

def p_expression_compare(token):
	'''expression : expression LESS expression
				  | expression LESSEQ expression
				  | expression EQUAL expression
				  | expression NOTEQUAL expression
				  | expression GREATER expression
				  | expression GREATEREQ expression'''
	token[0] = CompNode(token[2],token[1],token[3])

def p_expression_boolop(token):
	'''expression : expression AND expression
				  | expression OR expression'''
	token[0] = BoolOpNode(token[2],token[1],token[3])

def p_expression_unot(token):
	'''expression : NOT expression %prec UNOT'''
	token[0] = UnaryNotNode(token[1],token[2])

def p_expression_binop(token):
	'''expression : expression ADD expression
				  | expression SUB expression
				  | expression MULT expression
				  | expression DIV expression
				  | expression MOD expression
				  | expression INTDIV expression'''
	token[0] = BinOpNode(token[2],token[1],token[3])

def p_expression_exp(token):
	'''expression : expression EXP expression'''
	token[0] = ExpNode(token[1], token[3])

def p_expression_unaryminus(token):
	'''expression : SUB expression %prec UMINUS'''
	token[0] = UnaryOpNode(token[1],token[2])

def p_expression_string(token):
	'''expression : STRING'''
	token[0] = token[1]

def p_expression_int(token):
	'expression : INTEGER'
	token[0] = token[1]

def p_expression_real(token):
	'expression : REAL'
	token[0] = token[1]

def p_expression_bool(token):
	'expression : BOOL'
	token[0] = token[1]

def p_expression_id(token):
	'expression : ID'
	token[0] = token[1]

def p_error(p):
	print(p)
	raise SyntaxError

parser = yacc.yacc()
lexer = lex.lex()

f = open(sys.argv[1], mode='r')
try:
	ast = yacc.parse(f.read())
	ast.execute()
except SyntaxError:
	print("Syntax Error")
except Exception:
	print("Semantic Error")
