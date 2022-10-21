from __future__ import division
from functools import reduce
import math
import GrobalParament
#结巴分词准确率不高
import jieba
#北大这个库中文分词准确率高点
import pkuseg

def TF_IDF_Compute(file_import_url_temp,file_export_url_temp,*words):
    #words=words_input
    file_import_url=file_import_url_temp.replace('\\','/')
    file_export_url=file_export_url_temp.replace('\\','/')
    data_source=open(file_import_url,'r',encoding='utf-8')
    datas=data_source.readlines()
    print(type(data_source))
    word_in_afile_stat={}
    word_in_allfiles_stat={}
    files_num=0
    seg = pkuseg.pkuseg()
    for data in datas:
        if data!="":
            #data_temp={}
            data_temp_1=[]
            data_temp_2=[]
            data_temp_1=data.split('\\t') #file name and key words of a file
            #seg_list = jieba.cut(data_temp_1[1], cut_all=True)
            seg_list = seg.cut(data_temp_1[1])
            data_temp_2=','.join(seg_list).split(",")#key words of a file

            file_name=data_temp_1[0]
            data_temp_len=len(data_temp_2)
            files_num+=1
            #print data_temp_2
            for word in words:
                if word in data_temp_2:
                    #print word
                    if not word in word_in_allfiles_stat.keys():
                        word_in_allfiles_stat[word]=1
                    else:
                        word_in_allfiles_stat[word]+=1

                    if not file_name in word_in_afile_stat.keys():
                        word_in_afile_stat[file_name]={}
                    if not word in word_in_afile_stat[file_name].keys():
                        word_in_afile_stat[file_name][word]=[]
                        word_in_afile_stat[file_name][word].append(data_temp_2.count(word))
                        word_in_afile_stat[file_name][word].append(data_temp_len)
            #data=data_source.readline()
    data_source.close()
    if (word_in_afile_stat) and (word_in_allfiles_stat) and (files_num !=0):
        TF_IDF_result={}
        for filename in word_in_afile_stat.keys():
            TF_IDF_result[filename]={}
            for word in word_in_afile_stat[filename].keys():
                #关键字在文章里面的个数
                word_n=word_in_afile_stat[filename][word][0]
                #文章总词数
                word_sum=word_in_afile_stat[filename][word][1]
                with_word_sum=word_in_allfiles_stat[word]
                #TF_IDF_result[filename][word]=(math.exp(word_n/word_sum))*(math.log10(files_num/with_word_sum))
                TF_IDF_result[filename][word]=((word_n/word_sum))*(math.log10(files_num/with_word_sum))
                # TF_IDF_result[filename][word]=((word_in_afile_stat[filename][word][0])/(word_in_afile_stat[filename][word][1]))*math.log10((word_in_allfiles_stat[word])/files_num)
        TF_IDF_total={}
        for filename in TF_IDF_result.keys():
            #lambda表达式，冒号前面是参数
            #函数reduce的两个参数：1）函数：lambda x,y:x+y；2）迭代对象：TF_IDF_result[filename].values()
            #这里根据函数lambda x,y:x+y，是计算迭代对象TF_IDF_result[filename].values()的和
            TF_IDF_total[filename]=reduce(lambda x,y:x+y,TF_IDF_result[filename].values())
        result_temp=[]
        #sorted：第一个参数是迭代对象，key参数是用来比较的元素，reverse：排序规则，reverse = True 降序
        result_temp=sorted(TF_IDF_total.items(),key=lambda x:x[1],reverse=True)
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
                