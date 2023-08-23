from SetModel import Model
from VniAcronym import Acronym

A = Acronym()
M = Model('SetModel/Final3/Model')

while True:
    input_text = input('Nhan xet: ')
    input_text = A.Solve_Acr(input_text)
    label,cof = M.Predict(input_text)
    print(input_text)
    print(label,cof)

