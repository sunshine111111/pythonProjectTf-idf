import ahocorasick

#####Aho-Corasick算法实现：模式匹配
def make_AC(AC,word_set):
    for word in word_set:
        AC.add_word(word,word)
    return AC

def test_ahocorasick():
    key_list = ['苹果','香蕉','梨']
    AC_KEY = ahocorasick.Automaton()
    AC_KEY = make_AC(AC_KEY,set(key_list))
    AC_KEY.make_automaton()
    test_str_list = ["我最喜欢吃的水果是苹果，苹果又红又大我最喜欢吃的水果是苹果，苹果又红又大我最喜欢吃的水果是苹果，苹果又红又大我最喜欢吃的水果是苹果，苹果又红又大我最喜欢吃的水果是苹果，苹果又红又大","我最喜欢的是香蕉，苹果和梨子，更喜欢香蕉"]
    for content in test_str_list:
        name_list = set()
        index=0
        for item in AC_KEY.iter(content):
            index+=1;
            print(item)
            name_list.add(item[1])
        name_list = list(name_list)
        if len(name_list) > 0:
            print("关键字个数："+str(index))
            print(content,"关键字有：","\t".join(name_list))

if __name__ == '__main__':
    test_ahocorasick()