class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_list = []
        num_str = map(str,digits)
        stri = "".join(num_str)
        stri_num = int(stri) +1
        stri_num_str = str(stri_num)
        for i in range(len(stri_num_str)):
            num_list.append(int(stri_num_str[i]))
        

        return (num_list)
     