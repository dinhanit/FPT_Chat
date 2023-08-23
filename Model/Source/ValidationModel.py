from SetModel import Model
from Tokenize import Tokenize

name_model = "SetModel/ProModel_6Epoch/Model"
data_return = Tokenize("DataSet/test/sentsPro.txt","DataSet/test/sentiments.txt")
M = Model(name_model)
M.Eval(data_return)
