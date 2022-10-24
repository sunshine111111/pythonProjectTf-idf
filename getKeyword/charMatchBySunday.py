##Sunday算法：是由BM算法演变而来
#字符搜索：找出所有匹配到的字符串的第一个下标
def m_f_change(f_len, m, f, check_exits):
   if check_exits != -1:
       jump = f_len - check_exits
       m, f = m - f + jump, 0
   else:
       jump = f_len + 1
       m, f = m - f + jump, 0
   return m, f

#找出所有匹配到的字符串的第一个下标
def find_str_begin(main_str, find_str):
   m, f = 0, 0
   m_len, f_len, result = len(main_str), len(find_str), list()
   while m < m_len:
       if main_str[m] == find_str[f]:
           m, f = m + 1, f + 1
           if f == f_len:
               result.append(m - f_len)
               flag = m - f + f_len
               if flag > m_len - 1:
                   return result
               check_exits = find_str.rfind(main_str[flag])
               m, f = m_f_change(f_len,m,f,check_exits)
           continue
       else:
           flag = m - f + f_len
           if flag > m_len - 1:
               return result
           #如果上一步不匹配，则查找上一步中main_str索引后一位的字符，看在find_str中是否存在
           check_exits = find_str.rfind(main_str[flag])
           m,f=m_f_change(f_len,m,f,check_exits)
   else:
       return result
print(find_str_begin('好多人喜欢吃苹果，苹果又大又甜又红','苹果'))
print(find_str_begin('baa','aa'))
print(find_str_begin('foobarfoobar', 'foobar'))
print(find_str_begin('aaabaaabb','aa'))