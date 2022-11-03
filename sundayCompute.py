from __future__ import division
from functools import reduce
from getKeyword import charMatchBySunday
import math
import GrobalParament

###查找文档关键字，并且获取关键字的索引值
def sundayCompute(file_import_url_temp,file_export_url_temp,*words):
    #words=words_input
    file_import_url=file_import_url_temp.replace('\\','/')
    file_export_url=file_export_url_temp.replace('\\','/')
    data_source=open(file_import_url,'r',encoding='utf-8')
    datas=data_source.readlines()
    print(type(data_source))
    word_in_afile_stat={}
    word_in_allfiles_stat={}
    resultsIndexInOneFile = {}
    resultsIndexInAllFile = {}
    files_num=0
    for data in datas:
        if data!="":
            data_temp_1=data.split('\\t') #file name and key words of a file
            file_content = data_temp_1[1]
            file_name=data_temp_1[0]
            files_num += 1
            for word in words:
                #获取匹配到的关键字的第一个下标
                result = charMatchBySunday.find_str_begin(file_content, word)
                if len(result) !=0:
                    if not file_name in word_in_afile_stat.keys():
                        word_in_afile_stat[file_name] = {}
                    if not word in word_in_afile_stat[file_name].keys():
                        word_in_afile_stat[file_name][word] = []
                        word_in_afile_stat[file_name][word].append(len(result))
                    if not file_name in resultsIndexInOneFile.keys():
                        resultsIndexInOneFile[file_name] = {}
                    if not word in resultsIndexInOneFile[file_name].keys():
                        resultsIndexInOneFile[file_name][word] = []
                        resultsIndexInOneFile[file_name][word].append(result)
    data_source.close()
    if (word_in_afile_stat) and (files_num !=0):
        sunday_total = {}
        for filename in word_in_afile_stat.keys():
            # lambda表达式，冒号前面是参数
            # 函数reduce的两个参数：1）函数：lambda x,y:x+y；2）迭代对象：word_in_afile_stat[filename].values()
            # 这里根据函数lambda x,y:x+y，是计算迭代对象word_in_afile_stat[filename].values()的和
            sunday_total[filename] = reduce(lambda x, y: x + y, word_in_afile_stat[filename].values())
        result_temp=[]
        #sorted：第一个参数是迭代对象，key参数是用来比较的元素，reverse：排序规则，reverse = True 降序
        result_temp=sorted(sunday_total.items(),key=lambda x:x[1],reverse=True)
        k=GrobalParament.result_file_num
        result=[]
        for item in result_temp:
            if k!=0:
                result.append(item[0])
                k-=1
            else:
                break

    else:
        result=["None"]
    if GrobalParament.out_to_file:
        export=open(file_export_url,'w')
        for item in result:
            export.write(item+'\n')
        export.close()
    else:
        return result