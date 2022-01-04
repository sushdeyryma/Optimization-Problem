# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 06:52:32 2021

@author: SUSMITA(2125551650)
"""



#import the package
from ortools.linear_solver import pywraplp

#call the solver
solver = pywraplp.Solver.CreateSolver('GLOP')

#define the variables
x_b1= solver.NumVar(0,200, 'x_b1')
x_b2= solver.NumVar(0,300, 'x_b2')
x_b3= solver.NumVar(0,250,'x_b3')
x_t1= solver.NumVar(0,200, 'x_t1')
x_t2= solver.NumVar(0,300, 'x_t2')
x_t3= solver.NumVar(0,250, 'x_t3')


#define the contraints
solver.Add(x_b1+ x_b2+ x_b3<=300)
solver.Add(x_t1+ x_t2+ x_t3<=500)
solver.Add(x_b1 + x_t1 == 200)
solver.Add(x_b2 + x_t2 == 300)
solver.Add(x_b3 + x_t3 == 250)


#define the object function
solver.Minimize( 5* x_b1+ 6*x_b2+ 4 * x_b3 + 6 * x_t1+ 3 * x_t2 + 7* x_t3 )

results = solver.Solve()

if results==pywraplp.Solver.OPTIMAL: print('Optimal Found')

print('x_b1', x_b1.solution_value())
print('x_b2', x_b2.solution_value())
print('x_b3', x_b3.solution_value())
print('x_t1', x_t1.solution_value())
print('x_t2', x_t2.solution_value())
print('x_t3', x_t3.solution_value())

#Group_Member (Name: Susmita Dey,ID: 2125551650; Name: Anika Hossain,ID: 2125179650; Name: Aziza Tahsin Nawshin,ID: 2125243650)