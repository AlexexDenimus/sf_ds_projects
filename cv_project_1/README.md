# Проект CV-1. Угадай знаменитость

## Оглавление  
[1. Описание проекта](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_1/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_1/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_1/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_1/README.md#Этапы-работы-над-проектом)    
[5. Выводы](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_1/README.md#Выводы) 

### Описание проекта    
По фото определить одну из 5 знаменитостей.

:arrow_up:[к оглавлению](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_1/README.md#Оглавление)


### Какой кейс решаем?    
На вход подается изображение одной из 5 знаменитостей. Модель должна определить кто из знаменитостей изображен на фото.

**Условия соревнования:**  
- Используем предобученную модель.

**Метрика качества**     
accuracy на валидационной выборке > 0.85


### Краткая информация о данных
Предствлен набор фото 5 различных знаменитостей, разделенные на обучающий и валидационный наборы.
  
:arrow_up:[к оглавлению](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_1/README.md#Оглавление)


### Этапы работы над проектом  
1. Создать класс для работы с фото и переводом фото в тензор объект
2. Переопределить 3 послених сверточных слоя и слой классификатора
3. Переобучить модель
4. Визуализировать данные

:arrow_up:[к оглавлению](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_1/README.md#Оглавление)

### Выводы:  
Полученная модель способна различать 5 знаменитостей между собой

:arrow_up:[к оглавлению](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_1/README.md#Оглавление)
