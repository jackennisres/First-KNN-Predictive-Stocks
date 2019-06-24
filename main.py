import Stock
import ManicuredStock

def equalLists(listA, listB):
  #print(len(listA))
  #print(len(listB))
  for i in range(len(listA)):
    if listA[i] != listB[i]:
      return False
  return True

def standard_prediction(l, y, best_config):
  import numpy as np
  #new_data = np.transpose(new_data)
  neul = np.transpose(l)
  
  for count in range(1, 11):
    from sklearn.neighbors import KNeighborsClassifier
    clf = KNeighborsClassifier(n_neighbors=count)

    from sklearn.model_selection import train_test_split as tts
    #print(len(neul))
    #print(len(y))
    xTrain, xTest, yTrain, yTest = tts(neul, y, random_state=0)
    clf.fit(xTrain, yTrain)
    score = clf.score(xTest, yTest) * 100
    neighbors = count

    if best_config.score < score:
      poss = {}
      for i in range(len(data)):
        for ii in range(len(l)):
          if equalLists(data[i], l[ii]):
            poss[i] = i
      best_config.pots = poss

      best_config.score = score
      best_config.data = l
      best_config.neighbors = neighbors
  
  print("Current Best: {}".format(best_config.score))
  return best_config

def recursive_predict(l, y, best_config):

  print("Items: {}".format(len(l)))
  def addIrregular(stuff):
    items = []
    items.append(stuff[0])
    
    for item in stuff[2:]:
      items.append(item)
    return items


  import numpy as np
  #new_data = np.transpose(new_data)
  neul = np.transpose(l)

  from Config import Config as Config
  aConfig = Config([], 0, 0)
  bConfig = Config([], 0, 0)

  if len(l) <= 2 or best_config.score > 95:
    return best_config

  elif len(l) > 2:
    best_config = standard_prediction(l[1:], y, best_config)
    best_config = standard_prediction(addIrregular(l), y, best_config)
    
    aConfig = recursive_predict(l[1:], y, best_config)
    bConfig = recursive_predict(addIrregular(l), y, best_config)

  
  elif len(l) == 1:
    best_config = recursive_predict(l[1:], y, best_config)
    aConfig = standard_prediction(l[1:], y, best_config)
  
  else:

    if best_config.score < aConfig.score:
      best_config.score = aConfig.score
      best_config.data = aConfig.data
      best_config.neighbors = aConfig.neighbors
    
    if best_config.score < bConfig.score:
      best_config.score = bConfig.score
      best_config.data = bConfig.data
      best_config.neighbors = bConfig.neighbors

  return best_config





ndaq = Stock.Stock("NDAQ")
dji = Stock.Stock("^DJI")
microsoft = Stock.Stock("GPRO")

m_ndaq = ManicuredStock.ManicuredStock(ndaq)
m_dji = ManicuredStock.ManicuredStock(ndaq)
m_microsoft = ManicuredStock.ManicuredStock(microsoft)

stock_features = []
stock_features.append(m_ndaq.boxify())
print("Appended NDAQ")
stock_features.append(m_dji.boxify())
print("Appended DJI")
stock_features.append(m_microsoft.boxify())
print("Here we go!")


data = []
for cats in stock_features:
  for items in cats:
    data.append(items)

print("FULL CAT {}".format(len(data)))

from Config import Config as Config
best = Config(data, 0, 0) 


best = recursive_predict(data, microsoft.y_answer, best)




print("****************************************")
print("****** Neighbors: {} ********************".format(best.neighbors))
print("****** Best Score: {:.2f} ***************".format(best.score))
print("****** Features: {:.2f} ***************".format(len(best.data)))
print("****** Positions: {} ***************".format(len(best.pots)))
print("****************************************")


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split as tts

knn = KNeighborsClassifier(n_neighbors=best.neighbors)


print("# of features: {}".format(len(best.data)))
print("# of items in f1 {}".format(len(best.data[0])))
print("# of items in f2 {}".format(len(best.data[1])))
print("Number of y items {}".format(len(microsoft.y_answer)))

import numpy as np
new_data = np.transpose(best.data)



xTrain, xTest, yTrain, yTest = tts(new_data, microsoft.y_answer, random_state=0)

knn.fit(xTrain, yTrain)

dataSet = []
for item in best.pots:
  print("Index from og list: {}".format(item))
  print("Data from point {}".format(data[item][0]))
  dataSet.append(data[item][1])

print("DATASET: {}".format(dataSet))
dataSet = np.transpose(dataSet)

print(xTrain)
print("ACC: {}".format(knn.score(xTest, yTest)))
#dataSet = np.transpose(dataSet)
prediction = knn.predict(dataSet.reshape(1, -1))
print(prediction)

print("Finito")