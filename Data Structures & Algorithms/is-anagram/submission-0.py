class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic={}
        t_dic={}
        if len(s)==len(t):
            for element in s :
                if element in s_dic : 
                    s_dic[element]+=1
                else :s_dic[element]=1
            for element in t :
                if element in t_dic : 
                    t_dic[element]+=1
                else :t_dic[element]=1
            if s_dic==t_dic: return True
        return False