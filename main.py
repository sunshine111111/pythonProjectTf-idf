# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import GrobalParament
from TF_IDF_Compute import TF_IDF_Compute
from prepro_file import prepro_file
from sundayCompute import sundayCompute

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#####文档数据预处理
def Preprocess(file_url):
    PreResUrl = GrobalParament.PreprocessResultDir + '/' + GrobalParament.PreprocessResultName
    prepro_file(file_url, PreResUrl)

####tf_idf算法实现
def TF_IDF(*words):
    PreResUrl = GrobalParament.PreprocessResultDir + '/' + GrobalParament.PreprocessResultName
    ResFileUrl = GrobalParament.ResultFileNameDir + '/' + GrobalParament.ResultFileName
    if GrobalParament.out_to_file:
        TF_IDF_Compute(PreResUrl, ResFileUrl, *words)
    else:
        result = TF_IDF_Compute(PreResUrl, ResFileUrl, *words)
        return result

##
def sunday(*words):
    PreResUrl = GrobalParament.PreprocessResultDir + '/' + GrobalParament.PreprocessResultName
    ResFileUrl = GrobalParament.ResultFileNameDir + '/' + GrobalParament.ResultFileName
    if GrobalParament.out_to_file:
        sundayCompute(PreResUrl, ResFileUrl, *words)
    else:
        result = sundayCompute(PreResUrl, ResFileUrl, *words)
        return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Preprocess('C:/Users/zhongxing/fileSearch/test/files1')
    ####tf-idf算法，实现关键字搜索
    sunday("数据")

