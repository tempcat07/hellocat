def get_median(test):
    test.sort()
    lentest = len(test)
    middle = int(lentest/2)
    if  lentest % 2 == 0:
        return int(sum(test[middle-1:middle+1])/2)
    else:  return test[middle]



    #программу, которая создаёт список my_list, содержащий длины слов из списка raw_list (дан в начале кода),
#и находит сумму минимального и максимального элементов нового списка (my_list).
#Результат вычислений (сумма минимального и максимального элементов списка my_list)
#присвойте переменной result.
raw_list = ['переменные', 'циклы', 'условия', 'списки', 'словари', 'файлы', 'функции']
my_list=[]
for i in raw_list:
    my_list.append(len(i))
my_list.sort()
result=my_list[0]+my_list[-1]
my_list
result

def count_letters(sentence, average=False):
    listn=[]
    long= sentence.split()
    result=0
    if average==False:
        for n in long:
        	listn.append(len(n))
            
        result=listn
    return result


    