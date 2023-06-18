
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNleftPRINTleftORleftANDleftNOTleftLESSLESSEQEQUALNOTEQUALGREATERGREATEREQleftADDSUBleftMODleftMULTDIVleftLBLOCKleftVECTORADD AND ASSIGN COLON COMMA DEF DIV ELSE EQUAL EXIT FOR GREATER GREATEREQ ID IF INT LBLOCK LBRACE LENGTH LESS LESSEQ LIST LPAREN MOD MULT NOT NOTEQUAL NULL OR PRINT QUESTIONMARK RBLOCK RBRACE RETURN RPAREN SCAN SEMI STRING SUB TO VAR VECTOR WHILE\n    prog : func prog\n    | empty\n    func : DEF type ID LPAREN flist RPAREN LBRACE body RBRACE\n    | DEF type ID LPAREN flist RPAREN RETURN expr SEMI\n    \n    body : stmt body\n         | empty\n    \n    stmt :    expr SEMI\n            | defvar SEMI\n            | if_statement\n            | ifelse_statement\n            | while_statement\n            | for_statement\n            | RETURN expr SEMI\n            | LBRACE body RBRACE\n            | func\n    if_statement : IF LPAREN expr RPAREN stmtifelse_statement : IF LPAREN expr RPAREN stmt ELSE stmtwhile_statement : WHILE LPAREN expr RPAREN stmtfor_statement : FOR LPAREN ID ASSIGN expr TO expr RPAREN stmt\n    defvar : VAR type ID\n           | VAR type ID ASSIGN expr\n    \n    defvar : VAR error ID\n           | VAR error ID ASSIGN expr\n    \n    flist : type ID\n          | type ID COMMA flist\n          | empty\n    \n    type : INT\n         | VECTOR\n         | NULL\n         | STRING\n    expr : expr QUESTIONMARK expr COLON expr\n    | ID LPAREN clist RPAREN\n    | ID LBLOCK expr RBLOCK ASSIGN expr\n    | ID LBLOCK expr RBLOCK\n    | LBLOCK clist RBLOCK\n    | expr ADD expr\n    | expr SUB expr\n    | expr MULT expr\n    | expr DIV expr\n    | expr MOD expr\n    | expr GREATER expr\n    | expr LESS expr\n    | expr EQUAL expr\n    | expr GREATEREQ expr\n    | expr LESSEQ expr\n    | expr NOTEQUAL expr\n    | expr OR expr\n    | expr AND expr\n    | ID ASSIGN expr\n    | NOT expr\n    | ADD expr\n    | SUB expr\n    | ID\n    | INT\n    | STRING\n    | builtin_methods\n    \n    clist : expr\n          | expr COMMA clist\n          | empty\n    empty :\n    builtin_methods : LENGTH LPAREN expr RPAREN\n                    | SCAN LPAREN RPAREN\n                    | PRINT LPAREN expr RPAREN\n                    | LIST LPAREN expr RPAREN\n                    | EXIT LPAREN expr RPAREN\n    '
    
_lr_action_items = {'DEF':([0,2,19,23,25,29,30,31,32,34,56,58,73,91,95,110,129,130,140,141,144,146,148,149,],[4,4,4,4,4,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,4,4,-16,-18,4,-17,4,-19,]),'$end':([0,1,2,3,5,56,91,],[-60,0,-60,-2,-1,-3,-4,]),'INT':([4,12,18,19,20,23,25,29,30,31,32,33,34,35,36,37,38,42,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,83,84,86,88,89,90,91,95,110,112,125,127,128,129,130,131,136,140,141,144,145,146,148,149,],[7,7,7,39,39,39,39,-9,-10,-11,-12,39,-15,39,39,39,39,7,39,39,39,-3,-7,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-8,39,39,39,39,39,39,-4,-14,-13,39,39,39,39,39,39,39,39,-16,-18,39,39,-17,39,-19,]),'VECTOR':([4,12,18,42,],[8,8,8,8,]),'NULL':([4,12,18,42,],[9,9,9,9,]),'STRING':([4,12,18,19,20,23,25,29,30,31,32,33,34,35,36,37,38,42,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,83,84,86,88,89,90,91,95,110,112,125,127,128,129,130,131,136,140,141,144,145,146,148,149,],[10,10,10,40,40,40,40,-9,-10,-11,-12,40,-15,40,40,40,40,10,40,40,40,-3,-7,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-8,40,40,40,40,40,40,-4,-14,-13,40,40,40,40,40,40,40,40,-16,-18,40,40,-17,40,-19,]),'ID':([6,7,8,9,10,13,19,20,23,25,29,30,31,32,33,34,35,36,37,38,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,81,82,83,84,85,86,88,89,90,91,95,110,112,125,127,128,129,130,131,136,140,141,144,145,146,148,149,],[11,-27,-28,-29,-30,16,22,22,22,22,-9,-10,-11,-12,22,-15,22,22,22,22,22,22,22,-3,-7,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-8,113,114,22,22,117,22,22,22,22,-4,-14,-13,22,22,22,22,22,22,22,22,-16,-18,22,22,-17,22,-19,]),'LPAREN':([11,22,43,44,45,46,47,48,49,50,],[12,52,83,84,85,86,87,88,89,90,]),'RPAREN':([12,14,15,16,18,21,22,39,40,41,52,76,77,78,79,80,87,92,94,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,115,116,118,119,120,121,122,123,124,126,132,133,134,135,137,143,147,],[-60,17,-26,-24,-60,-25,-53,-54,-55,-56,-60,-57,-59,-51,-52,-50,119,123,-49,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-35,-60,129,130,132,-62,133,134,135,-32,-34,-58,-61,-63,-64,-65,-31,-33,148,]),'COMMA':([16,22,39,40,41,76,78,79,80,94,97,98,99,100,101,102,103,104,105,106,107,108,109,111,119,123,124,132,133,134,135,137,143,],[18,-53,-54,-55,-56,112,-51,-52,-50,-49,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-35,-62,-32,-34,-61,-63,-64,-65,-31,-33,]),'LBRACE':([17,19,23,25,29,30,31,32,34,56,58,73,91,95,110,129,130,140,141,144,146,148,149,],[19,23,23,23,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,23,23,-16,-18,23,-17,23,-19,]),'RETURN':([17,19,23,25,29,30,31,32,34,56,58,73,91,95,110,129,130,140,141,144,146,148,149,],[20,33,33,33,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,33,33,-16,-18,33,-17,33,-19,]),'RBRACE':([19,23,24,25,26,29,30,31,32,34,55,56,57,58,73,91,95,110,140,141,146,149,],[-60,-60,56,-60,-6,-9,-10,-11,-12,-15,95,-3,-5,-7,-8,-4,-14,-13,-16,-18,-17,-19,]),'LBLOCK':([19,20,22,23,25,29,30,31,32,33,34,35,36,37,38,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,83,84,86,88,89,90,91,95,110,112,125,127,128,129,130,131,136,140,141,144,145,146,148,149,],[35,35,53,35,35,-9,-10,-11,-12,35,-15,35,35,35,35,35,35,35,-3,-7,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-8,35,35,35,35,35,35,-4,-14,-13,35,35,35,35,35,35,35,35,-16,-18,35,35,-17,35,-19,]),'NOT':([19,20,23,25,29,30,31,32,33,34,35,36,37,38,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,83,84,86,88,89,90,91,95,110,112,125,127,128,129,130,131,136,140,141,144,145,146,148,149,],[38,38,38,38,-9,-10,-11,-12,38,-15,38,38,38,38,38,38,38,-3,-7,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-8,38,38,38,38,38,38,-4,-14,-13,38,38,38,38,38,38,38,38,-16,-18,38,38,-17,38,-19,]),'ADD':([19,20,22,23,25,27,29,30,31,32,33,34,35,36,37,38,39,40,41,51,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,80,83,84,86,88,89,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,115,116,118,119,120,121,122,123,124,125,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,],[36,36,-53,36,36,60,-9,-10,-11,-12,36,-15,36,36,36,36,-54,-55,-56,60,36,36,36,-3,-7,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-8,60,60,-51,-52,60,36,36,36,36,36,36,-4,60,60,-14,60,-36,-37,-38,-39,-40,60,60,60,60,60,60,60,60,-13,-35,36,60,60,60,-62,60,60,60,-32,-34,36,36,36,36,36,36,-61,-63,-64,-65,36,60,60,60,-16,-18,60,60,36,36,-17,60,36,-19,]),'SUB':([19,20,22,23,25,27,29,30,31,32,33,34,35,36,37,38,39,40,41,51,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,80,83,84,86,88,89,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,115,116,118,119,120,121,122,123,124,125,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,],[37,37,-53,37,37,61,-9,-10,-11,-12,37,-15,37,37,37,37,-54,-55,-56,61,37,37,37,-3,-7,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-8,61,61,-51,-52,61,37,37,37,37,37,37,-4,61,61,-14,61,-36,-37,-38,-39,-40,61,61,61,61,61,61,61,61,-13,-35,37,61,61,61,-62,61,61,61,-32,-34,37,37,37,37,37,37,-61,-63,-64,-65,37,61,61,61,-16,-18,61,61,37,37,-17,61,37,-19,]),'VAR':([19,23,25,29,30,31,32,34,56,58,73,91,95,110,129,130,140,141,144,146,148,149,],[42,42,42,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,42,42,-16,-18,42,-17,42,-19,]),'IF':([19,23,25,29,30,31,32,34,56,58,73,91,95,110,129,130,140,141,144,146,148,149,],[43,43,43,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,43,43,-16,-18,43,-17,43,-19,]),'WHILE':([19,23,25,29,30,31,32,34,56,58,73,91,95,110,129,130,140,141,144,146,148,149,],[44,44,44,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,44,44,-16,-18,44,-17,44,-19,]),'FOR':([19,23,25,29,30,31,32,34,56,58,73,91,95,110,129,130,140,141,144,146,148,149,],[45,45,45,-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,45,45,-16,-18,45,-17,45,-19,]),'LENGTH':([19,20,23,25,29,30,31,32,33,34,35,36,37,38,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,83,84,86,88,89,90,91,95,110,112,125,127,128,129,130,131,136,140,141,144,145,146,148,149,],[46,46,46,46,-9,-10,-11,-12,46,-15,46,46,46,46,46,46,46,-3,-7,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-8,46,46,46,46,46,46,-4,-14,-13,46,46,46,46,46,46,46,46,-16,-18,46,46,-17,46,-19,]),'SCAN':([19,20,23,25,29,30,31,32,33,34,35,36,37,38,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,83,84,86,88,89,90,91,95,110,112,125,127,128,129,130,131,136,140,141,144,145,146,148,149,],[47,47,47,47,-9,-10,-11,-12,47,-15,47,47,47,47,47,47,47,-3,-7,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-8,47,47,47,47,47,47,-4,-14,-13,47,47,47,47,47,47,47,47,-16,-18,47,47,-17,47,-19,]),'PRINT':([19,20,23,25,29,30,31,32,33,34,35,36,37,38,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,83,84,86,88,89,90,91,95,110,112,125,127,128,129,130,131,136,140,141,144,145,146,148,149,],[48,48,48,48,-9,-10,-11,-12,48,-15,48,48,48,48,48,48,48,-3,-7,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-8,48,48,48,48,48,48,-4,-14,-13,48,48,48,48,48,48,48,48,-16,-18,48,48,-17,48,-19,]),'LIST':([19,20,23,25,29,30,31,32,33,34,35,36,37,38,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,83,84,86,88,89,90,91,95,110,112,125,127,128,129,130,131,136,140,141,144,145,146,148,149,],[49,49,49,49,-9,-10,-11,-12,49,-15,49,49,49,49,49,49,49,-3,-7,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-8,49,49,49,49,49,49,-4,-14,-13,49,49,49,49,49,49,49,49,-16,-18,49,49,-17,49,-19,]),'EXIT':([19,20,23,25,29,30,31,32,33,34,35,36,37,38,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,83,84,86,88,89,90,91,95,110,112,125,127,128,129,130,131,136,140,141,144,145,146,148,149,],[50,50,50,50,-9,-10,-11,-12,50,-15,50,50,50,50,50,50,50,-3,-7,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-8,50,50,50,50,50,50,-4,-14,-13,50,50,50,50,50,50,50,50,-16,-18,50,50,-17,50,-19,]),'ASSIGN':([22,113,114,117,124,],[54,127,128,131,136,]),'SEMI':([22,27,28,39,40,41,51,74,78,79,80,94,97,98,99,100,101,102,103,104,105,106,107,108,109,111,113,114,119,123,124,132,133,134,135,137,138,139,143,],[-53,58,73,-54,-55,-56,91,110,-51,-52,-50,-49,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-35,-20,-22,-62,-32,-34,-61,-63,-64,-65,-31,-21,-23,-33,]),'QUESTIONMARK':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,59,-54,-55,-56,59,59,59,-51,-52,-50,59,-49,59,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-35,59,59,59,-62,59,59,59,-32,-34,-61,-63,-64,-65,59,59,59,59,-33,59,]),'MULT':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,62,-54,-55,-56,62,62,62,62,62,62,62,62,62,62,62,-38,-39,62,62,62,62,62,62,62,62,62,-35,62,62,62,-62,62,62,62,-32,-34,-61,-63,-64,-65,62,62,62,62,62,62,]),'DIV':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,63,-54,-55,-56,63,63,63,63,63,63,63,63,63,63,63,-38,-39,63,63,63,63,63,63,63,63,63,-35,63,63,63,-62,63,63,63,-32,-34,-61,-63,-64,-65,63,63,63,63,63,63,]),'MOD':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,64,-54,-55,-56,64,64,64,64,64,64,64,64,64,64,64,-38,-39,-40,64,64,64,64,64,64,64,64,-35,64,64,64,-62,64,64,64,-32,-34,-61,-63,-64,-65,64,64,64,64,64,64,]),'GREATER':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,65,-54,-55,-56,65,65,65,-51,-52,65,65,65,65,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,65,65,-35,65,65,65,-62,65,65,65,-32,-34,-61,-63,-64,-65,65,65,65,65,65,65,]),'LESS':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,66,-54,-55,-56,66,66,66,-51,-52,66,66,66,66,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,66,66,-35,66,66,66,-62,66,66,66,-32,-34,-61,-63,-64,-65,66,66,66,66,66,66,]),'EQUAL':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,67,-54,-55,-56,67,67,67,-51,-52,67,67,67,67,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,67,67,-35,67,67,67,-62,67,67,67,-32,-34,-61,-63,-64,-65,67,67,67,67,67,67,]),'GREATEREQ':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,68,-54,-55,-56,68,68,68,-51,-52,68,68,68,68,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,68,68,-35,68,68,68,-62,68,68,68,-32,-34,-61,-63,-64,-65,68,68,68,68,68,68,]),'LESSEQ':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,69,-54,-55,-56,69,69,69,-51,-52,69,69,69,69,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,69,69,-35,69,69,69,-62,69,69,69,-32,-34,-61,-63,-64,-65,69,69,69,69,69,69,]),'NOTEQUAL':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,70,-54,-55,-56,70,70,70,-51,-52,70,70,70,70,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,70,70,-35,70,70,70,-62,70,70,70,-32,-34,-61,-63,-64,-65,70,70,70,70,70,70,]),'OR':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,71,-54,-55,-56,71,71,71,-51,-52,-50,71,71,71,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-35,71,71,71,-62,71,71,71,-32,-34,-61,-63,-64,-65,71,71,71,71,71,71,]),'AND':([22,27,39,40,41,51,74,76,78,79,80,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,115,116,118,119,120,121,122,123,124,132,133,134,135,137,138,139,142,143,147,],[-53,72,-54,-55,-56,72,72,72,-51,-52,-50,72,72,72,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,72,-48,-35,72,72,72,-62,72,72,72,-32,-34,-61,-63,-64,-65,72,72,72,72,72,72,]),'RBLOCK':([22,35,39,40,41,75,76,77,78,79,80,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,119,123,124,126,132,133,134,135,137,143,],[-53,-60,-54,-55,-56,111,-57,-59,-51,-52,-50,124,-49,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-35,-60,-62,-32,-34,-58,-61,-63,-64,-65,-31,-33,]),'COLON':([22,39,40,41,78,79,80,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,119,123,124,132,133,134,135,137,143,],[-53,-54,-55,-56,-51,-52,-50,-49,125,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-35,-62,-32,-34,-61,-63,-64,-65,-31,-33,]),'TO':([22,39,40,41,78,79,80,94,97,98,99,100,101,102,103,104,105,106,107,108,109,111,119,123,124,132,133,134,135,137,142,143,],[-53,-54,-55,-56,-51,-52,-50,-49,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-35,-62,-32,-34,-61,-63,-64,-65,-31,145,-33,]),'ELSE':([29,30,31,32,34,56,58,73,91,95,110,140,141,146,149,],[-9,-10,-11,-12,-15,-3,-7,-8,-4,-14,-13,144,-18,-17,-19,]),'error':([42,],[82,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,2,],[1,5,]),'func':([0,2,19,23,25,129,130,144,148,],[2,2,34,34,34,34,34,34,34,]),'empty':([0,2,12,18,19,23,25,35,52,112,],[3,3,15,15,26,26,26,77,77,77,]),'type':([4,12,18,42,],[6,13,13,81,]),'flist':([12,18,],[14,21,]),'body':([19,23,25,],[24,55,57,]),'stmt':([19,23,25,129,130,144,148,],[25,25,25,140,141,146,149,]),'expr':([19,20,23,25,33,35,36,37,38,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,83,84,86,88,89,90,112,125,127,128,129,130,131,136,144,145,148,],[27,51,27,27,74,76,78,79,80,76,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,115,116,118,120,121,122,76,137,138,139,27,27,142,143,27,147,27,]),'defvar':([19,23,25,129,130,144,148,],[28,28,28,28,28,28,28,]),'if_statement':([19,23,25,129,130,144,148,],[29,29,29,29,29,29,29,]),'ifelse_statement':([19,23,25,129,130,144,148,],[30,30,30,30,30,30,30,]),'while_statement':([19,23,25,129,130,144,148,],[31,31,31,31,31,31,31,]),'for_statement':([19,23,25,129,130,144,148,],[32,32,32,32,32,32,32,]),'builtin_methods':([19,20,23,25,33,35,36,37,38,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,83,84,86,88,89,90,112,125,127,128,129,130,131,136,144,145,148,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'clist':([35,52,112,],[75,92,126,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> func prog','prog',2,'p_prog','MyParser.py',16),
  ('prog -> empty','prog',1,'p_prog','MyParser.py',17),
  ('func -> DEF type ID LPAREN flist RPAREN LBRACE body RBRACE','func',9,'p_func','MyParser.py',26),
  ('func -> DEF type ID LPAREN flist RPAREN RETURN expr SEMI','func',9,'p_func','MyParser.py',27),
  ('body -> stmt body','body',2,'p_body','MyParser.py',42),
  ('body -> empty','body',1,'p_body','MyParser.py',43),
  ('stmt -> expr SEMI','stmt',2,'p_stmt','MyParser.py',53),
  ('stmt -> defvar SEMI','stmt',2,'p_stmt','MyParser.py',54),
  ('stmt -> if_statement','stmt',1,'p_stmt','MyParser.py',55),
  ('stmt -> ifelse_statement','stmt',1,'p_stmt','MyParser.py',56),
  ('stmt -> while_statement','stmt',1,'p_stmt','MyParser.py',57),
  ('stmt -> for_statement','stmt',1,'p_stmt','MyParser.py',58),
  ('stmt -> RETURN expr SEMI','stmt',3,'p_stmt','MyParser.py',59),
  ('stmt -> LBRACE body RBRACE','stmt',3,'p_stmt','MyParser.py',60),
  ('stmt -> func','stmt',1,'p_stmt','MyParser.py',61),
  ('if_statement -> IF LPAREN expr RPAREN stmt','if_statement',5,'p_if_statement','MyParser.py',83),
  ('ifelse_statement -> IF LPAREN expr RPAREN stmt ELSE stmt','ifelse_statement',7,'p_ifelse_statement','MyParser.py',89),
  ('while_statement -> WHILE LPAREN expr RPAREN stmt','while_statement',5,'p_while_statement','MyParser.py',95),
  ('for_statement -> FOR LPAREN ID ASSIGN expr TO expr RPAREN stmt','for_statement',9,'p_for_statement','MyParser.py',101),
  ('defvar -> VAR type ID','defvar',3,'p_defvar','MyParser.py',112),
  ('defvar -> VAR type ID ASSIGN expr','defvar',5,'p_defvar','MyParser.py',113),
  ('defvar -> VAR error ID','defvar',3,'p_defvar_error','MyParser.py',129),
  ('defvar -> VAR error ID ASSIGN expr','defvar',5,'p_defvar_error','MyParser.py',130),
  ('flist -> type ID','flist',2,'p_flist','MyParser.py',139),
  ('flist -> type ID COMMA flist','flist',4,'p_flist','MyParser.py',140),
  ('flist -> empty','flist',1,'p_flist','MyParser.py',141),
  ('type -> INT','type',1,'p_type','MyParser.py',156),
  ('type -> VECTOR','type',1,'p_type','MyParser.py',157),
  ('type -> NULL','type',1,'p_type','MyParser.py',158),
  ('type -> STRING','type',1,'p_type','MyParser.py',159),
  ('expr -> expr QUESTIONMARK expr COLON expr','expr',5,'p_expr','MyParser.py',165),
  ('expr -> ID LPAREN clist RPAREN','expr',4,'p_expr','MyParser.py',166),
  ('expr -> ID LBLOCK expr RBLOCK ASSIGN expr','expr',6,'p_expr','MyParser.py',167),
  ('expr -> ID LBLOCK expr RBLOCK','expr',4,'p_expr','MyParser.py',168),
  ('expr -> LBLOCK clist RBLOCK','expr',3,'p_expr','MyParser.py',169),
  ('expr -> expr ADD expr','expr',3,'p_expr','MyParser.py',170),
  ('expr -> expr SUB expr','expr',3,'p_expr','MyParser.py',171),
  ('expr -> expr MULT expr','expr',3,'p_expr','MyParser.py',172),
  ('expr -> expr DIV expr','expr',3,'p_expr','MyParser.py',173),
  ('expr -> expr MOD expr','expr',3,'p_expr','MyParser.py',174),
  ('expr -> expr GREATER expr','expr',3,'p_expr','MyParser.py',175),
  ('expr -> expr LESS expr','expr',3,'p_expr','MyParser.py',176),
  ('expr -> expr EQUAL expr','expr',3,'p_expr','MyParser.py',177),
  ('expr -> expr GREATEREQ expr','expr',3,'p_expr','MyParser.py',178),
  ('expr -> expr LESSEQ expr','expr',3,'p_expr','MyParser.py',179),
  ('expr -> expr NOTEQUAL expr','expr',3,'p_expr','MyParser.py',180),
  ('expr -> expr OR expr','expr',3,'p_expr','MyParser.py',181),
  ('expr -> expr AND expr','expr',3,'p_expr','MyParser.py',182),
  ('expr -> ID ASSIGN expr','expr',3,'p_expr','MyParser.py',183),
  ('expr -> NOT expr','expr',2,'p_expr','MyParser.py',184),
  ('expr -> ADD expr','expr',2,'p_expr','MyParser.py',185),
  ('expr -> SUB expr','expr',2,'p_expr','MyParser.py',186),
  ('expr -> ID','expr',1,'p_expr','MyParser.py',187),
  ('expr -> INT','expr',1,'p_expr','MyParser.py',188),
  ('expr -> STRING','expr',1,'p_expr','MyParser.py',189),
  ('expr -> builtin_methods','expr',1,'p_expr','MyParser.py',190),
  ('clist -> expr','clist',1,'p_clist','MyParser.py',259),
  ('clist -> expr COMMA clist','clist',3,'p_clist','MyParser.py',260),
  ('clist -> empty','clist',1,'p_clist','MyParser.py',261),
  ('empty -> <empty>','empty',0,'p_empty','MyParser.py',271),
  ('builtin_methods -> LENGTH LPAREN expr RPAREN','builtin_methods',4,'p_builtin_methods','MyParser.py',277),
  ('builtin_methods -> SCAN LPAREN RPAREN','builtin_methods',3,'p_builtin_methods','MyParser.py',278),
  ('builtin_methods -> PRINT LPAREN expr RPAREN','builtin_methods',4,'p_builtin_methods','MyParser.py',279),
  ('builtin_methods -> LIST LPAREN expr RPAREN','builtin_methods',4,'p_builtin_methods','MyParser.py',280),
  ('builtin_methods -> EXIT LPAREN expr RPAREN','builtin_methods',4,'p_builtin_methods','MyParser.py',281),
]
