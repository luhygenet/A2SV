class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
      final=[]
      lst=[]
      for i in range(len(list1)):
          if list1[i] in list2:
              ind_common = i
              sums = ind_common + list2.index(list1[i])
              lst.append([sums, ind_common])
      lst.sort()
      low = lst[0][0]
      for i in range(len(lst)):
          if lst[i][0] == low:
              final.append(list1[lst[i][1]])
          else:
              break
          
      return final
              