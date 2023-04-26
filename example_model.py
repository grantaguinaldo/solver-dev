import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import argparse

parser = argparse.ArgumentParser(description='Solve Simple Model.')
parser.add_argument('--solver', type=str, required=True, metavar='', help='Solver')
args = parser.parse_args()
solver = args.solver

model = pyo.ConcreteModel()

# declare decision variables
model.x = pyo.Var(domain=pyo.NonNegativeReals)

# declare objective
model.profit = pyo.Objective(
    expr = 40*model.x,
    sense = pyo.maximize)

# declare constraints
model.demand = pyo.Constraint(expr = model.x <= 40)
model.laborA = pyo.Constraint(expr = model.x <= 80)
model.laborB = pyo.Constraint(expr = 2*model.x <= 100)
opt = pyo.SolverFactory(solver).solve(model, tee=True)
model.display()
