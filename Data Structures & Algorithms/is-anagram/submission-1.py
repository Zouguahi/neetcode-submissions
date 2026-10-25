class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic={}
        t_dic={}
        if len(s)!=len(t):
            return False
        for element in s :
            s_dic[element]=s_dic.get(element,0)+1
        for element in t :
            t_dic[element]=t_dic.get(element,0)+1
        return s_dic==t_dic