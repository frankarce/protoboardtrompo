#!/usr/bin/env python
from FIS import *

# Variables
Yes = LinguisticVariable('Yes')
Yes.addMF('L',MF.Triangular(0,33.33, 66.66))
Yes.addMF('M',MF.Triangular(33.33, 66.66, 80))
Yes.addMF('H',MF.Triangular(66.66,80, 100))

Maybe = LinguisticVariable('Maybe')
Maybe.addMF('L',MF.Triangular(0,33.33,66.66))
Maybe.addMF('M',MF.Triangular(33.33, 66.66, 80))
Maybe.addMF('H',MF.Triangular(66.66,80, 100))

No = LinguisticVariable('No')
No.addMF('L',MF.Triangular(0,33.33, 66.66))
No.addMF('M',MF.Triangular(33.33, 66.66, 80))
No.addMF('H',MF.Triangular(66.66,80, 100))


grado = LinguisticVariable('grado', type = 'out' , range = (0,100) )
grado.addMF('VL',MF.Triangular(-20,0, 20))
grado.addMF('L',MF.Triangular(0,20, 40))
grado.addMF('M',MF.Triangular(20, 40, 60))
grado.addMF('H',MF.Triangular(40,60, 80))
grado.addMF('VH',MF.Triangular(60,80, 100))

# Rules
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['L'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['L'])
                                        ,FuzzyProposition(No,No.mfs['L']))))

r1.consequent.append(FuzzyProposition(grado,grado.mfs['VL']))


r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['L'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['L'])
                                        ,FuzzyProposition(No,No.mfs['M']))))

r2.consequent.append(FuzzyProposition(grado,grado.mfs['VL']))


r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['L'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['L'])
                                        ,FuzzyProposition(No,No.mfs['H']))))

r3.consequent.append(FuzzyProposition(grado,grado.mfs['VL']))

r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['L'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['M'])
                                        ,FuzzyProposition(No,No.mfs['L']))))

r4.consequent.append(FuzzyProposition(grado,grado.mfs['VL']))


r5 = FuzzyRule()
r5.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['L'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['M'])
                                        ,FuzzyProposition(No,No.mfs['M']))))

r5.consequent.append(FuzzyProposition(grado,grado.mfs['VL']))


r6 = FuzzyRule()
r6.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['L'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['M'])
                                        ,FuzzyProposition(No,No.mfs['H']))))

r6.consequent.append(FuzzyProposition(grado,grado.mfs['VL']))

r7 = FuzzyRule()
r7.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['L'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['H'])
                                        ,FuzzyProposition(No,No.mfs['L']))))

r7.consequent.append(FuzzyProposition(grado,grado.mfs['L']))


r8 = FuzzyRule()
r8.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['L'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['H'])
                                        ,FuzzyProposition(No,No.mfs['M']))))

r8.consequent.append(FuzzyProposition(grado,grado.mfs['L']))


r9 = FuzzyRule()
r9.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['L'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['H'])
                                        ,FuzzyProposition(No,No.mfs['H']))))

r9.consequent.append(FuzzyProposition(grado,grado.mfs['L']))

r10 = FuzzyRule()
r10.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['L'])
                                        ,FuzzyProposition(No,No.mfs['L']))))

r10.consequent.append(FuzzyProposition(grado,grado.mfs['L']))


r11 = FuzzyRule()
r11.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['L'])
                                        ,FuzzyProposition(No,No.mfs['M']))))

r11.consequent.append(FuzzyProposition(grado,grado.mfs['L']))


r12 = FuzzyRule()
r12.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['L'])
                                        ,FuzzyProposition(No,No.mfs['H']))))

r12.consequent.append(FuzzyProposition(grado,grado.mfs['M']))

r13 = FuzzyRule()
r13.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['M'])
                                        ,FuzzyProposition(No,No.mfs['L']))))

r13.consequent.append(FuzzyProposition(grado,grado.mfs['M']))


r14 = FuzzyRule()
r14.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['M'])
                                        ,FuzzyProposition(No,No.mfs['M']))))

r14.consequent.append(FuzzyProposition(grado,grado.mfs['M']))


r15 = FuzzyRule()
r15.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['M'])
                                        ,FuzzyProposition(No,No.mfs['H']))))

r15.consequent.append(FuzzyProposition(grado,grado.mfs['M']))

r16 = FuzzyRule()
r16.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['H'])
                                        ,FuzzyProposition(No,No.mfs['L']))))

r16.consequent.append(FuzzyProposition(grado,grado.mfs['M']))


r17 = FuzzyRule()
r17.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['H'])
                                        ,FuzzyProposition(No,No.mfs['M']))))

r17.consequent.append(FuzzyProposition(grado,grado.mfs['H']))


r18 = FuzzyRule()
r18.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['M'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['H'])
                                        ,FuzzyProposition(No,No.mfs['H']))))

r18.consequent.append(FuzzyProposition(grado,grado.mfs['H']))

r19 = FuzzyRule()
r19.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['L'])
                                        ,FuzzyProposition(No,No.mfs['L']))))

r19.consequent.append(FuzzyProposition(grado,grado.mfs['H']))

r20 = FuzzyRule()
r20.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['L'])
                                        ,FuzzyProposition(No,No.mfs['M']))))

r20.consequent.append(FuzzyProposition(grado,grado.mfs['H']))


r21 = FuzzyRule()
r21.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['L'])
                                        ,FuzzyProposition(No,No.mfs['H']))))

r21.consequent.append(FuzzyProposition(grado,grado.mfs['H']))

r22 = FuzzyRule()
r22.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['M'])
                                        ,FuzzyProposition(No,No.mfs['L']))))

r22.consequent.append(FuzzyProposition(grado,grado.mfs['VH']))


r23 = FuzzyRule()
r23.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['M'])
                                        ,FuzzyProposition(No,No.mfs['M']))))

r23.consequent.append(FuzzyProposition(grado,grado.mfs['VH']))


r24 = FuzzyRule()
r24.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['M'])
                                        ,FuzzyProposition(No,No.mfs['H']))))

r24.consequent.append(FuzzyProposition(grado,grado.mfs['VH']))

r25 = FuzzyRule()
r25.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['H'])
                                        ,FuzzyProposition(No,No.mfs['L']))))

r25.consequent.append(FuzzyProposition(grado,grado.mfs['VH']))


r26 = FuzzyRule()
r26.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['H'])
                                        ,FuzzyProposition(No,No.mfs['M']))))

r26.consequent.append(FuzzyProposition(grado,grado.mfs['VH']))


r27 = FuzzyRule()
r27.antecedent.append(FuzzyOperator('and',FuzzyProposition(Yes,Yes.mfs['H'])
                                        ,FuzzyOperator('and',FuzzyProposition(Maybe,Maybe.mfs['H'])
                                        ,FuzzyProposition(No,No.mfs['H']))))

r27.consequent.append(FuzzyProposition(grado,grado.mfs['VH']))

reglas = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27]

fis = FIS(reglas)

def eval(a,b,c):
    Yes.current_value = a
    Maybe.current_value = b
    No.current_value = c
    return fis.eval(out_var = 0)

if __name__ == '__main__':
    print eval(100,	0,	0)
