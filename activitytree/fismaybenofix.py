__author__ = 'frank'
from FIS import *

# Variables
Yes = LinguisticVariable('Yes')
Yes.addMF('L',MF.Triangular(-40,0,40))
Yes.addMF('M',MF.Triangular(20,50,80))
Yes.addMF('H',MF.Triangular(60,100,140))


No = LinguisticVariable('No')
No.addMF('L',MF.Triangular(-40,0,40))
No.addMF('M',MF.Triangular(20,50,80))
No.addMF('H',MF.Triangular(60,100,140))

Maybe = LinguisticVariable('Maybe')
Maybe.addMF('L',MF.Triangular(-40,0,40))
Maybe.addMF('M',MF.Triangular(20,50,80))
Maybe.addMF('H',MF.Triangular(60,100,140))


grado = LinguisticVariable('grado', type = 'out' , range = (0,100) )
grado.addMF('VL',MF.Triangular(-20,0,20))
grado.addMF('L',MF.Triangular(20,40,60))
grado.addMF('M',MF.Triangular(40,60,80))
grado.addMF('H',MF.Triangular(60,80,100))
grado.addMF('VH',MF.Triangular(80,100,120))

# Rules
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                        ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['L'])
                                        ,FuzzyProposition(Maybe,Maybe.mfs['L']))))

r1.consequent.append(FuzzyProposition(grado,grado.mfs['VH']))

#
r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                         ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['M'])
                                         ,FuzzyProposition(Maybe,Maybe.mfs['L']))))

r2.consequent.append(FuzzyProposition(grado,grado.mfs['VH']))

r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                         ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['L'])
                                         ,FuzzyProposition(Maybe,Maybe.mfs['M']))))

r3.consequent.append(FuzzyProposition(grado,grado.mfs['VH']))

r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                         ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['M'])
                                         ,FuzzyProposition(Maybe,Maybe.mfs['M']))))

r4.consequent.append(FuzzyProposition(grado,grado.mfs['H']))

r5 = FuzzyRule()
r5.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                         ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['L'])
                                         ,FuzzyProposition(Maybe,Maybe.mfs['L']))))

r5.consequent.append(FuzzyProposition(grado,grado.mfs['H']))

r6 = FuzzyRule()
r6.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                         ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['L'])
                                         ,FuzzyProposition(Maybe,Maybe.mfs['M']))))

r6.consequent.append(FuzzyProposition(grado,grado.mfs['H']))

r7 = FuzzyRule()
r7.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                         ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['L'])
                                         ,FuzzyProposition(Maybe,Maybe.mfs['H']))))

r7.consequent.append(FuzzyProposition(grado,grado.mfs['H']))


r8 = FuzzyRule()
r8.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                         ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['M'])
                                         ,FuzzyProposition(Maybe,Maybe.mfs['L']))))

r8.consequent.append(FuzzyProposition(grado,grado.mfs['M']))

r9 = FuzzyRule()
r9.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                         ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['M'])
                                         ,FuzzyProposition(Maybe,Maybe.mfs['M']))))

r9.consequent.append(FuzzyProposition(grado,grado.mfs['M']))

r10 = FuzzyRule()
r10.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                         ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['M'])
                                         ,FuzzyProposition(Maybe,Maybe.mfs['H']))))

r10.consequent.append(FuzzyProposition(grado,grado.mfs['M']))

r10 = FuzzyRule()
r10.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                         ,FuzzyOperator('and',FuzzyProposition(No,No.mfs['M'])
                                         ,FuzzyProposition(Maybe,Maybe.mfs['H']))))

r10.consequent.append(FuzzyProposition(grado,grado.mfs['M']))

reglas = [r1]#,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27]

fis = FIS(reglas)

def eval(a,b,c):
    Yes.current_value = a
    Maybe.current_value = c
    No.current_value = b
    return fis.eval(out_var = 0)

if __name__ == '__main__':
    print eval(60,	10,	30)
