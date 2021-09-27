"""
  Patika.dev Python Temel Proje - 2

  2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
  Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
  
  Örnek olarak:

  input: [[1, 2], [3, 4], [5, 6, 7]]

  output: [[7, 6, 5], [4, 3], [2, 1]]

"""
def reverse(input_List):

  reversed_list = [elem[::-1] for elem in input_List]
  rev_of_rev = []
  for i in range(1,len(reversed_list)+1):
    rev_of_rev.append(reversed_list[-i])

  return rev_of_rev

inputList = [[1, 2], [3, 4], [5, 6, 7]]
reverse(inputList)
