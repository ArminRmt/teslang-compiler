
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNleftPRINTleftORleftANDleftNOTleftLESSLESSEQEQUALNOTEQUALGREATERGREATEREQleftADDSUBleftMODleftMULTDIVleftLBLOCKleftVECTORADD AND ASSIGN BUILTIN_METHODES COLON COMMA DEF DIV ELSE EQUAL EXIT EXIT FOR GREATER GREATEREQ ID IF INT LBLOCK LBRACE LENGTH LENGTH LESS LESSEQ LIST LPAREN MOD MULT NOT NOTEQUAL NULL OR PRINT QUESTIONMARK RBLOCK RBRACE RETURN RPAREN SCAN SCAN SEMI STRING SUB TO TYPE VAR VECTOR WHILE\n    prog : func prog\n         | empty\n    func : DEF TYPE ID LPAREN flist RPAREN LBRACE body RBRACE\n    | DEF TYPE ID LPAREN flist RPAREN RETURN expr SEMI\n    \n    body : stmt body\n         | empty\n    \n    stmt :    expr SEMI\n            | defvar SEMI\n            | if_statement\n            | ifelse_statement\n            | while_statement\n            | for_statement\n            | RETURN expr SEMI\n            | LBRACE body RBRACE\n            | func\n    if_statement : IF LPAREN expr RPAREN stmtifelse_statement : IF LPAREN expr RPAREN stmt ELSE stmtwhile_statement : WHILE LPAREN expr RPAREN stmtfor_statement : FOR LPAREN ID EQUAL expr TO expr RPAREN stmtdefvar : VAR TYPE ID\n    | VAR TYPE ID ASSIGN expr\n    \n    flist : TYPE ID\n          | TYPE ID COMMA flist\n          | empty\n    expr : expr QUESTIONMARK expr COLON expr\n    | ID LPAREN clist RPAREN\n    | expr LBLOCK expr RBLOCK\n    | LBLOCK clist RBLOCK\n    | expr ADD expr\n    | expr SUB expr\n    | expr MULT expr\n    | expr DIV expr\n    | expr MOD expr\n    | expr GREATER expr\n    | expr LESS expr\n    | expr EQUAL expr\n    | expr GREATEREQ expr\n    | expr LESSEQ expr\n    | expr NOTEQUAL expr\n    | expr OR expr\n    | expr AND expr\n    | ID ASSIGN expr\n    | NOT expr\n    | ADD expr\n    | SUB expr\n    | ID\n    | INT\n    | STRING\n    | builtin_methods\n    \n    clist : expr\n          | expr COMMA clist\n          | empty\n    \n    type : INT\n         | VECTOR\n         | NULL\n         | STRING\n    empty :\n    builtin_methods : LENGTH LPAREN expr RPAREN\n                    | SCAN LPAREN RPAREN\n                    | PRINT LPAREN expr RPAREN\n                    | LPAREN expr RPAREN\n                    | EXIT LPAREN expr RPAREN\n    '
    
_lr_action_items = {'DEF':([0,2,15,20,22,26,27,28,29,31,52,54,70,86,90,106,122,123,130,131,133,135,137,138,],[4,4,4,4,4,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,4,4,-16,-18,4,-17,4,-19,]),'$end':([0,1,2,3,5,52,86,],[-57,0,-57,-2,-1,-3,-4,]),'TYPE':([4,8,14,39,],[6,9,9,78,]),'ID':([6,9,15,16,19,20,22,26,27,28,29,30,31,32,33,34,35,48,49,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,78,79,80,81,82,84,85,86,90,106,108,118,121,122,123,124,130,131,133,134,135,137,138,],[7,12,18,18,18,18,18,-9,-10,-11,-12,18,-15,18,18,18,18,18,18,-3,-7,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-8,109,18,18,112,18,18,18,-4,-14,-13,18,18,18,18,18,18,-16,-18,18,18,-17,18,-19,]),'LPAREN':([7,15,16,18,19,20,22,26,27,28,29,30,31,32,33,34,35,40,41,42,43,44,45,46,48,49,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,80,82,84,85,86,90,106,108,118,121,122,123,124,130,131,133,134,135,137,138,],[8,19,19,48,19,19,19,-9,-10,-11,-12,19,-15,19,19,19,19,79,80,81,82,83,84,85,19,19,-3,-7,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-8,19,19,19,19,19,-4,-14,-13,19,19,19,19,19,19,-16,-18,19,19,-17,19,-19,]),'RPAREN':([8,10,11,12,14,17,18,36,37,38,48,50,73,74,75,76,77,83,87,88,89,93,94,95,96,97,98,99,100,101,102,103,104,105,107,108,110,111,113,114,115,116,117,119,120,125,126,127,128,136,],[-57,13,-24,-22,-57,-23,-46,-47,-48,-49,-57,89,-50,-52,-44,-45,-43,114,117,-42,-61,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-28,-57,122,123,125,-59,126,127,-26,-27,-51,-58,-60,-62,-25,137,]),'COMMA':([12,18,36,37,38,73,75,76,77,88,89,93,94,95,96,97,98,99,100,101,102,103,104,105,107,114,117,119,125,126,127,128,],[14,-46,-47,-48,-49,108,-44,-45,-43,-42,-61,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-28,-59,-26,-27,-58,-60,-62,-25,]),'LBRACE':([13,15,20,22,26,27,28,29,31,52,54,70,86,90,106,122,123,130,131,133,135,137,138,],[15,20,20,20,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,20,20,-16,-18,20,-17,20,-19,]),'RETURN':([13,15,20,22,26,27,28,29,31,52,54,70,86,90,106,122,123,130,131,133,135,137,138,],[16,30,30,30,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,30,30,-16,-18,30,-17,30,-19,]),'RBRACE':([15,20,21,22,23,26,27,28,29,31,51,52,53,54,70,86,90,106,130,131,135,138,],[-57,-57,52,-57,-6,-9,-10,-11,-12,-15,90,-3,-5,-7,-8,-4,-14,-13,-16,-18,-17,-19,]),'LBLOCK':([15,16,18,19,20,22,24,26,27,28,29,30,31,32,33,34,35,36,37,38,47,48,49,50,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,75,76,77,79,80,82,84,85,86,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,113,114,115,116,117,118,119,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,],[32,32,-46,32,32,32,56,-9,-10,-11,-12,32,-15,32,32,32,32,-47,-48,-49,56,32,32,56,-3,-7,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-8,56,56,56,56,56,32,32,32,32,32,-4,56,-61,-14,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-13,-28,32,56,56,56,-59,56,56,-26,32,-27,32,32,32,32,-58,-60,-62,56,56,-16,-18,56,32,32,-17,56,32,-19,]),'NOT':([15,16,19,20,22,26,27,28,29,30,31,32,33,34,35,48,49,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,80,82,84,85,86,90,106,108,118,121,122,123,124,130,131,133,134,135,137,138,],[35,35,35,35,35,-9,-10,-11,-12,35,-15,35,35,35,35,35,35,-3,-7,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-8,35,35,35,35,35,-4,-14,-13,35,35,35,35,35,35,-16,-18,35,35,-17,35,-19,]),'ADD':([15,16,18,19,20,22,24,26,27,28,29,30,31,32,33,34,35,36,37,38,47,48,49,50,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,75,76,77,79,80,82,84,85,86,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,113,114,115,116,117,118,119,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,],[33,33,-46,33,33,33,57,-9,-10,-11,-12,33,-15,33,33,33,33,-47,-48,-49,57,33,33,57,-3,-7,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-8,57,57,-44,-45,57,33,33,33,33,33,-4,57,-61,-14,57,57,-29,-30,-31,-32,-33,57,57,57,57,57,57,57,57,-13,-28,33,57,57,57,-59,57,57,-26,33,-27,33,33,33,33,-58,-60,-62,57,57,-16,-18,57,33,33,-17,57,33,-19,]),'SUB':([15,16,18,19,20,22,24,26,27,28,29,30,31,32,33,34,35,36,37,38,47,48,49,50,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,75,76,77,79,80,82,84,85,86,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,113,114,115,116,117,118,119,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,],[34,34,-46,34,34,34,58,-9,-10,-11,-12,34,-15,34,34,34,34,-47,-48,-49,58,34,34,58,-3,-7,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-8,58,58,-44,-45,58,34,34,34,34,34,-4,58,-61,-14,58,58,-29,-30,-31,-32,-33,58,58,58,58,58,58,58,58,-13,-28,34,58,58,58,-59,58,58,-26,34,-27,34,34,34,34,-58,-60,-62,58,58,-16,-18,58,34,34,-17,58,34,-19,]),'INT':([15,16,19,20,22,26,27,28,29,30,31,32,33,34,35,48,49,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,80,82,84,85,86,90,106,108,118,121,122,123,124,130,131,133,134,135,137,138,],[36,36,36,36,36,-9,-10,-11,-12,36,-15,36,36,36,36,36,36,-3,-7,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-8,36,36,36,36,36,-4,-14,-13,36,36,36,36,36,36,-16,-18,36,36,-17,36,-19,]),'STRING':([15,16,19,20,22,26,27,28,29,30,31,32,33,34,35,48,49,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,80,82,84,85,86,90,106,108,118,121,122,123,124,130,131,133,134,135,137,138,],[37,37,37,37,37,-9,-10,-11,-12,37,-15,37,37,37,37,37,37,-3,-7,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-8,37,37,37,37,37,-4,-14,-13,37,37,37,37,37,37,-16,-18,37,37,-17,37,-19,]),'VAR':([15,20,22,26,27,28,29,31,52,54,70,86,90,106,122,123,130,131,133,135,137,138,],[39,39,39,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,39,39,-16,-18,39,-17,39,-19,]),'IF':([15,20,22,26,27,28,29,31,52,54,70,86,90,106,122,123,130,131,133,135,137,138,],[40,40,40,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,40,40,-16,-18,40,-17,40,-19,]),'WHILE':([15,20,22,26,27,28,29,31,52,54,70,86,90,106,122,123,130,131,133,135,137,138,],[41,41,41,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,41,41,-16,-18,41,-17,41,-19,]),'FOR':([15,20,22,26,27,28,29,31,52,54,70,86,90,106,122,123,130,131,133,135,137,138,],[42,42,42,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,42,42,-16,-18,42,-17,42,-19,]),'LENGTH':([15,16,19,20,22,26,27,28,29,30,31,32,33,34,35,48,49,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,80,82,84,85,86,90,106,108,118,121,122,123,124,130,131,133,134,135,137,138,],[43,43,43,43,43,-9,-10,-11,-12,43,-15,43,43,43,43,43,43,-3,-7,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-8,43,43,43,43,43,-4,-14,-13,43,43,43,43,43,43,-16,-18,43,43,-17,43,-19,]),'SCAN':([15,16,19,20,22,26,27,28,29,30,31,32,33,34,35,48,49,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,80,82,84,85,86,90,106,108,118,121,122,123,124,130,131,133,134,135,137,138,],[44,44,44,44,44,-9,-10,-11,-12,44,-15,44,44,44,44,44,44,-3,-7,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-8,44,44,44,44,44,-4,-14,-13,44,44,44,44,44,44,-16,-18,44,44,-17,44,-19,]),'PRINT':([15,16,19,20,22,26,27,28,29,30,31,32,33,34,35,48,49,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,80,82,84,85,86,90,106,108,118,121,122,123,124,130,131,133,134,135,137,138,],[45,45,45,45,45,-9,-10,-11,-12,45,-15,45,45,45,45,45,45,-3,-7,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-8,45,45,45,45,45,-4,-14,-13,45,45,45,45,45,45,-16,-18,45,45,-17,45,-19,]),'EXIT':([15,16,19,20,22,26,27,28,29,30,31,32,33,34,35,48,49,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,80,82,84,85,86,90,106,108,118,121,122,123,124,130,131,133,134,135,137,138,],[46,46,46,46,46,-9,-10,-11,-12,46,-15,46,46,46,46,46,46,-3,-7,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-8,46,46,46,46,46,-4,-14,-13,46,46,46,46,46,46,-16,-18,46,46,-17,46,-19,]),'ASSIGN':([18,109,],[49,121,]),'SEMI':([18,24,25,36,37,38,47,71,75,76,77,88,89,93,94,95,96,97,98,99,100,101,102,103,104,105,107,109,114,117,119,125,126,127,128,129,],[-46,54,70,-47,-48,-49,86,106,-44,-45,-43,-42,-61,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-28,-20,-59,-26,-27,-58,-60,-62,-25,-21,]),'QUESTIONMARK':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,55,-47,-48,-49,55,55,55,55,-44,-45,-43,-42,-61,55,55,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-28,55,55,55,-59,55,55,-26,-27,-58,-60,-62,55,55,55,55,]),'MULT':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,59,-47,-48,-49,59,59,59,59,59,59,59,59,-61,59,59,59,59,-31,-32,59,59,59,59,59,59,59,59,59,-28,59,59,59,-59,59,59,-26,-27,-58,-60,-62,59,59,59,59,]),'DIV':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,60,-47,-48,-49,60,60,60,60,60,60,60,60,-61,60,60,60,60,-31,-32,60,60,60,60,60,60,60,60,60,-28,60,60,60,-59,60,60,-26,-27,-58,-60,-62,60,60,60,60,]),'MOD':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,61,-47,-48,-49,61,61,61,61,61,61,61,61,-61,61,61,61,61,-31,-32,-33,61,61,61,61,61,61,61,61,-28,61,61,61,-59,61,61,-26,-27,-58,-60,-62,61,61,61,61,]),'GREATER':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,62,-47,-48,-49,62,62,62,62,-44,-45,62,62,-61,62,62,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,62,62,-28,62,62,62,-59,62,62,-26,-27,-58,-60,-62,62,62,62,62,]),'LESS':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,63,-47,-48,-49,63,63,63,63,-44,-45,63,63,-61,63,63,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,63,63,-28,63,63,63,-59,63,63,-26,-27,-58,-60,-62,63,63,63,63,]),'EQUAL':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,112,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,64,-47,-48,-49,64,64,64,64,-44,-45,64,64,-61,64,64,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,64,64,-28,64,64,124,64,-59,64,64,-26,-27,-58,-60,-62,64,64,64,64,]),'GREATEREQ':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,65,-47,-48,-49,65,65,65,65,-44,-45,65,65,-61,65,65,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,65,65,-28,65,65,65,-59,65,65,-26,-27,-58,-60,-62,65,65,65,65,]),'LESSEQ':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,66,-47,-48,-49,66,66,66,66,-44,-45,66,66,-61,66,66,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,66,66,-28,66,66,66,-59,66,66,-26,-27,-58,-60,-62,66,66,66,66,]),'NOTEQUAL':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,67,-47,-48,-49,67,67,67,67,-44,-45,67,67,-61,67,67,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,67,67,-28,67,67,67,-59,67,67,-26,-27,-58,-60,-62,67,67,67,67,]),'OR':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,68,-47,-48,-49,68,68,68,68,-44,-45,-43,68,-61,68,68,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-28,68,68,68,-59,68,68,-26,-27,-58,-60,-62,68,68,68,68,]),'AND':([18,24,36,37,38,47,50,71,73,75,76,77,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,110,111,113,114,115,116,117,119,125,126,127,128,129,132,136,],[-46,69,-47,-48,-49,69,69,69,69,-44,-45,-43,69,-61,69,69,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,69,-41,-28,69,69,69,-59,69,69,-26,-27,-58,-60,-62,69,69,69,69,]),'RBLOCK':([18,32,36,37,38,72,73,74,75,76,77,88,89,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,108,114,117,119,120,125,126,127,128,],[-46,-57,-47,-48,-49,107,-50,-52,-44,-45,-43,-42,-61,119,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-28,-57,-59,-26,-27,-51,-58,-60,-62,-25,]),'COLON':([18,36,37,38,75,76,77,88,89,91,93,94,95,96,97,98,99,100,101,102,103,104,105,107,114,117,119,125,126,127,128,],[-46,-47,-48,-49,-44,-45,-43,-42,-61,118,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-28,-59,-26,-27,-58,-60,-62,-25,]),'TO':([18,36,37,38,75,76,77,88,89,93,94,95,96,97,98,99,100,101,102,103,104,105,107,114,117,119,125,126,127,128,132,],[-46,-47,-48,-49,-44,-45,-43,-42,-61,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-28,-59,-26,-27,-58,-60,-62,-25,134,]),'ELSE':([26,27,28,29,31,52,54,70,86,90,106,130,131,135,138,],[-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,133,-18,-17,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,2,],[1,5,]),'func':([0,2,15,20,22,122,123,133,137,],[2,2,31,31,31,31,31,31,31,]),'empty':([0,2,8,14,15,20,22,32,48,108,],[3,3,11,11,23,23,23,74,74,74,]),'flist':([8,14,],[10,17,]),'body':([15,20,22,],[21,51,53,]),'stmt':([15,20,22,122,123,133,137,],[22,22,22,130,131,135,138,]),'expr':([15,16,19,20,22,30,32,33,34,35,48,49,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,79,80,82,84,85,108,118,121,122,123,124,133,134,137,],[24,47,50,24,24,71,73,75,76,77,73,88,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,110,111,113,115,116,73,128,129,24,24,132,24,136,24,]),'defvar':([15,20,22,122,123,133,137,],[25,25,25,25,25,25,25,]),'if_statement':([15,20,22,122,123,133,137,],[26,26,26,26,26,26,26,]),'ifelse_statement':([15,20,22,122,123,133,137,],[27,27,27,27,27,27,27,]),'while_statement':([15,20,22,122,123,133,137,],[28,28,28,28,28,28,28,]),'for_statement':([15,20,22,122,123,133,137,],[29,29,29,29,29,29,29,]),'builtin_methods':([15,16,19,20,22,30,32,33,34,35,48,49,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,79,80,82,84,85,108,118,121,122,123,124,133,134,137,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'clist':([32,48,108,],[72,87,120,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> func prog','prog',2,'p_prog','MyParser.py',25),
  ('prog -> empty','prog',1,'p_prog','MyParser.py',26),
  ('func -> DEF TYPE ID LPAREN flist RPAREN LBRACE body RBRACE','func',9,'p_func','MyParser.py',34),
  ('func -> DEF TYPE ID LPAREN flist RPAREN RETURN expr SEMI','func',9,'p_func','MyParser.py',35),
  ('body -> stmt body','body',2,'p_body','MyParser.py',44),
  ('body -> empty','body',1,'p_body','MyParser.py',45),
  ('stmt -> expr SEMI','stmt',2,'p_smt','MyParser.py',55),
  ('stmt -> defvar SEMI','stmt',2,'p_smt','MyParser.py',56),
  ('stmt -> if_statement','stmt',1,'p_smt','MyParser.py',57),
  ('stmt -> ifelse_statement','stmt',1,'p_smt','MyParser.py',58),
  ('stmt -> while_statement','stmt',1,'p_smt','MyParser.py',59),
  ('stmt -> for_statement','stmt',1,'p_smt','MyParser.py',60),
  ('stmt -> RETURN expr SEMI','stmt',3,'p_smt','MyParser.py',61),
  ('stmt -> LBRACE body RBRACE','stmt',3,'p_smt','MyParser.py',62),
  ('stmt -> func','stmt',1,'p_smt','MyParser.py',63),
  ('if_statement -> IF LPAREN expr RPAREN stmt','if_statement',5,'p_if_statement','MyParser.py',80),
  ('ifelse_statement -> IF LPAREN expr RPAREN stmt ELSE stmt','ifelse_statement',7,'p_ifelse_statement','MyParser.py',85),
  ('while_statement -> WHILE LPAREN expr RPAREN stmt','while_statement',5,'p_while_statement','MyParser.py',90),
  ('for_statement -> FOR LPAREN ID EQUAL expr TO expr RPAREN stmt','for_statement',9,'p_for_statement','MyParser.py',95),
  ('defvar -> VAR TYPE ID','defvar',3,'p_defvar','MyParser.py',100),
  ('defvar -> VAR TYPE ID ASSIGN expr','defvar',5,'p_defvar','MyParser.py',101),
  ('flist -> TYPE ID','flist',2,'p_flist','MyParser.py',111),
  ('flist -> TYPE ID COMMA flist','flist',4,'p_flist','MyParser.py',112),
  ('flist -> empty','flist',1,'p_flist','MyParser.py',113),
  ('expr -> expr QUESTIONMARK expr COLON expr','expr',5,'p_expr','MyParser.py',125),
  ('expr -> ID LPAREN clist RPAREN','expr',4,'p_expr','MyParser.py',126),
  ('expr -> expr LBLOCK expr RBLOCK','expr',4,'p_expr','MyParser.py',127),
  ('expr -> LBLOCK clist RBLOCK','expr',3,'p_expr','MyParser.py',128),
  ('expr -> expr ADD expr','expr',3,'p_expr','MyParser.py',129),
  ('expr -> expr SUB expr','expr',3,'p_expr','MyParser.py',130),
  ('expr -> expr MULT expr','expr',3,'p_expr','MyParser.py',131),
  ('expr -> expr DIV expr','expr',3,'p_expr','MyParser.py',132),
  ('expr -> expr MOD expr','expr',3,'p_expr','MyParser.py',133),
  ('expr -> expr GREATER expr','expr',3,'p_expr','MyParser.py',134),
  ('expr -> expr LESS expr','expr',3,'p_expr','MyParser.py',135),
  ('expr -> expr EQUAL expr','expr',3,'p_expr','MyParser.py',136),
  ('expr -> expr GREATEREQ expr','expr',3,'p_expr','MyParser.py',137),
  ('expr -> expr LESSEQ expr','expr',3,'p_expr','MyParser.py',138),
  ('expr -> expr NOTEQUAL expr','expr',3,'p_expr','MyParser.py',139),
  ('expr -> expr OR expr','expr',3,'p_expr','MyParser.py',140),
  ('expr -> expr AND expr','expr',3,'p_expr','MyParser.py',141),
  ('expr -> ID ASSIGN expr','expr',3,'p_expr','MyParser.py',142),
  ('expr -> NOT expr','expr',2,'p_expr','MyParser.py',143),
  ('expr -> ADD expr','expr',2,'p_expr','MyParser.py',144),
  ('expr -> SUB expr','expr',2,'p_expr','MyParser.py',145),
  ('expr -> ID','expr',1,'p_expr','MyParser.py',146),
  ('expr -> INT','expr',1,'p_expr','MyParser.py',147),
  ('expr -> STRING','expr',1,'p_expr','MyParser.py',148),
  ('expr -> builtin_methods','expr',1,'p_expr','MyParser.py',149),
  ('clist -> expr','clist',1,'p_clist','MyParser.py',186),
  ('clist -> expr COMMA clist','clist',3,'p_clist','MyParser.py',187),
  ('clist -> empty','clist',1,'p_clist','MyParser.py',188),
  ('type -> INT','type',1,'p_type','MyParser.py',201),
  ('type -> VECTOR','type',1,'p_type','MyParser.py',202),
  ('type -> NULL','type',1,'p_type','MyParser.py',203),
  ('type -> STRING','type',1,'p_type','MyParser.py',204),
  ('empty -> <empty>','empty',0,'p_empty','MyParser.py',210),
  ('builtin_methods -> LENGTH LPAREN expr RPAREN','builtin_methods',4,'p_builtin_methods','MyParser.py',218),
  ('builtin_methods -> SCAN LPAREN RPAREN','builtin_methods',3,'p_builtin_methods','MyParser.py',219),
  ('builtin_methods -> PRINT LPAREN expr RPAREN','builtin_methods',4,'p_builtin_methods','MyParser.py',220),
  ('builtin_methods -> LPAREN expr RPAREN','builtin_methods',3,'p_builtin_methods','MyParser.py',221),
  ('builtin_methods -> EXIT LPAREN expr RPAREN','builtin_methods',4,'p_builtin_methods','MyParser.py',222),
]
