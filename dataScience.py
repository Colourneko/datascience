from sklearn import cluster
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.DataFrame({
 'x': [11, 21, 28, 17, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53,
55, 61, 62, 70, 72, 10],
 'y': [39, 36, 30, 52, 53, 46, 55, 59, 63, 70, 66, 63, 58, 23,
14, 8, 18, 7, 24, 10]
})
myKmeans = cluster.KMeans(n_clusters=2)
myKmeans.fit(dataset)
centroids = myKmeans.cluster_centers_
labels = myKmeans.labels_


plt.scatter(dataset['x'],dataset['y'],s=10)
plt.scatter(centroids[0],centroids[1],s=100)
plt.show()

import pandas as pd
def LinearSearch(list, item):
    index = 0
    found = False
# Match the value with each data element
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index = index + 1
    return found

df = pd.DataFrame([
    ['45583 ', '677862', 'John','Doe','2000-09-19', True,'2018-08-07'],
    ['54543', '877653', 'Xman','Xsir','1970-03-10', False,'2018-06-07'],
    ['343323', '344565', 'Agro','Waka','1973-02-15', False,'2018-05-05'],
    ['45583','677864','John', 'Doe','2000-09-19', True,'2018-03-02'],
['22331','344553','Kal','Sorts','1975-01-02',True,'2018-04-15']])
df.columns = ['personal_ID', 'application_ID', 'f_name', 'sur_name','DOB','decision','decision_date']
df


def BubbleSort(list):
 lastElementindex = len(list) - 1
 print(0, list)
 for idx in range(lastElementindex):
  if list[idx] > list[idx + 1]:
   list[idx], list[idx + 1] = list[idx + 1], list[idx]
  print(idx + 1, list)
 return list


def BinarySearch(list, item):
 first = 0
 last = len(list) - 1
 found = False

 while first <= last and not found:
  midpoint = (first + last) // 2
  if list[midpoint] == item:
   found = True
  else:
   if item < list[midpoint]:
    last = midpoint - 1
   else:
    first = midpoint + 1
  return found


list = [12, 33, 11, 99, 22, 55, 90]
sorted_list = BubbleSort(list)
print(LinearSearch(list, 12))


def LinearSearch(list, item):
 index = 0
 found = False
 # Match the value with each data element
 while index < len(list) and found is False:
  if list[index] == item:
   found = True
  else:
   index = index + 1
 return found


list = [12, 33, 11, 99, 22, 55, 90]
print(LinearSearch(list, 12))


def SelectionSort(list):
 for fill_slot in range(len(list) - 1, 0, -1):
  max_index = 0
  for location in range(1, fill_slot + 1):
   if list[location] > list[max_index]:
    max_index = location
  list[fill_slot], list[max_index] = list[max_index], list[fill_slot]


list = [26, 17, 20, 11, 23, 21, 13, 28, 24, 14, 12, 22, 16, 15, 19, 25]
SelectionSort(list)
print(list)


def ShellSort(list):
 distance = len(list) // 2
 while distance > 0:
  for i in range(distance, len(list)):
   temp = list[i]
   j = i
   while j >= distance and list[j - distance] > temp:
    list[j] = list[j - distance]
    j = j - distance
   list[j] = temp
  distance = distance // 2
 return list


list = [26, 17, 20, 11, 23, 21, 13, 28, 24, 14, 12, 22, 16, 15, 19, 25]
nlist = [1400, 460, 4300, 2700, 570, 410, 4500, 210, 700]

ShellSort(list)
ShellSort(nlist)
print(list)
print(nlist)


def MergeSort(list):
 if len(list) > 1:
  mid = len(list) // 2
  left = list[:mid]
  right = list[mid:]

  MergeSort(left)
  MergeSort(right)

  a = 0
  b = 0
  c = 0

  while a < len(left) and b < len(right):
   if left[a] < right[b]:
    list[c] = left[a]
    a = a + 1
   else:
    list[c] = right[b]
    b = b + 1
   c = c + 1
  while a < len(left):
   list[c] = left[a]
   a = a + 1
   c = c + 1

  while b < len(right):
   list[c] = right[b]
   b = b + 1
   c = c + 1
 return list


list = [44, 16, 83, 7, 67, 21, 34, 45, 10]
MergeSort(list)
print(list)


def InsertionSort(list):
 for i in range(1, len(list)):
  j = i - 1
  element_next = list[i]
  while (list[j] > element_next) and (j >= 0):
   list[j + 1] = list[j]
   j = j - 1
  list[j + 1] = element_next
 return list


x = [25, 21, 22, 24, 23, 27, 26]
InsertionSort(x)

#Pass 1 of Bubble Sort
def BubbleSort(list):
    lastElementindex = len(list)-1
    print(0,list)
    for idx in range(lastElementindex):
        if list[idx]>list[idx+1]:
            list[idx],list[idx+1]=list[idx+1],list[idx]
        print(idx+1,list)
    return list
x = [25,21,22,24,23,27,26]
y = [32,34,31,35,36,37,38,39,33]

BubbleSort(x)