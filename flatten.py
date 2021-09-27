"""

  Patika.dev Python Temel Proje - 1

  1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
  Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
  
  Örnek olarak:

  input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

  output: [1,'a','cat',2,3,'dog',4,5]

"""

def Flatten(input_List):
  output_List = []

  for i in input_List:
    if type(i) ==  list:
      output_List.extend(Flatten(i))
    else:
      output_List.append(i)

  return output_List


input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
Flatten(input)
