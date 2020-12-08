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
    
    '''Сначала устанавливаем число равное середине  возможного диапазона, а потом уменьшаем или увеличиваем его в зависимости 
    от того, больше оно или меньше нужного, но уже опираясь на правило, что число будет находится в середине 
    предполагаемого диапазона исходя из предыдущих шагов.
            Функция принимает загаданное число и возвращает число попыток'''
    
    count = 1      # счетчик попыток
    predict = 50   # указатель стремящийся к загаданному числу (и станет им)
    limax = 101    # верхний предел + 1  
    limin = 0      # нижний предел -1
    
    while number != predict:
        print(number,predict)
        count+=1
        if number > predict:
            limin = predict
            predict += (limax - limin)/2
            
        elif number < predict:
            limax = predict
            predict -= (limax - limin)/2
    return(count)   # выход из цикла, если угадали
                    # Проверяем
score_game(game_core_tempcat)
    
