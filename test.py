import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
# запускаем

def game_core_tempcat(number):
    
    ''' устанавливаем указатель  равным середине  возможного диапазона, а потом уменьшаем или увеличиваем его в зависимости 
    от того, больше оно или меньше загаданного, опираясь на правило, что число будет находится в середине 
    предполагаемого диапазона и исходя из предыдущих шагов.
            Функция принимает загаданное число и возвращает число попыток'''
    
    count = 1           # счетчик попыток
    approxim = 50       # указатель на стремящийся к загаданному числу (и станет равным ему)
    limit_max = 101     # верхний предел + 1     (для решения number = 100)
    limit_min = 0       # нижний предел -1       (для решения number = 1)
    
    while number != approxim:
        
        count += 1
        if number > approxim:
            limit_min = approxim
            approxim += (limit_max - limit_min)//2
            
        elif number < approxim:
            limit_max = approxim
            approxim -= (limit_max - limit_min)//2
    return(count)   # выход из цикла, когда число найдено 

score_game(game_core_tempcat)
    
