from SetModel import Model
from Tokenize import Tokenize
data_train_return = Tokenize("DataSet/train/sents.txt","DataSet/train/sentiments.txt")
data_test_return = Tokenize("DataSet/test/sents.txt","DataSet/test/sentiments.txt")

StartTrain = Model("wonrax/phobert-base-vietnamese-sentiment")
# for i in range(5,20,3):
#     StartTrain.Train(data_train_return,data_test_return,epoch = i,save_model = "ProModel4_"+str(i)+"Epoch")
StartTrain.Train(data_train_return,data_test_return,epoch = 5,save_model = "NotProcess")
