'''
First Project: Parser for the uC language.

Subject:
    MC921 - Construction of Compilers
Authors:
    Victor Ferreira Ferrari  - RA 187890
    Vinicius Couto Espindola - RA 188115

University of Campinas - UNICAMP - 2020

Last Modified: 24/03/2020.
'''

from ply.yacc import yacc

class uCParser():
    def p_statement_list(p):
        ''' statements : statements statement
                       | statement
        '''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[1] + (p[2]) 

    def p_assign_statement (p):
        ''' statement : ID = expr
        '''
        p[0] = ('assign', p[1], p[3])
        
    def p_print_statement (p):
        ''' statement : PRINT ( expr )
        '''
        p[0] = ('print', p[3])
        
    def p_binop_expr (p):
        ''' expr : expr + expr
                 | expr * expr
        '''
        p[0] = (p[2], p[1], p[3])
        
    def p_num_expr (p):
        ''' expr : NUM
        '''
        p[0] = ('num', p[1])
        
    def p_name_expr (p):
        ''' expr : ID
        '''
        p[0] = ('id', p[1])
        
    def p_compound_expr (p):
        ''' expr : ( expr )
        '''
        p[0] = p[2]
    
    def p_error (p):
        if p:
            print("Error near the symbol %s" % p.value)
        else:
            print("Error at the end of input")

    precedence = (
        ('left', '+'),
        ('left', '*')
        )

parser = yacc(write_tables=False)

parser.parse('a = 3*4')
