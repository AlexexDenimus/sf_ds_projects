# Проект CV-2. Детектирование медицинских масок

## Оглавление  
[1. Описание проекта](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_2/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_2/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_2/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_2/README.md#Этапы-работы-над-проектом)    
[5. Выводы](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_2/README.md#Выводы) 

### Описание проекта    
По фото определить расположение лиц людей, а далее распознать надета ли на них медицинская маска или нет.

:arrow_up:[к оглавлению](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_2/README.md#Оглавление)


### Какой кейс решаем?    
На вход подается изображение. Модель должна определить недета ли на человеке или группе людей на изображении медицинская маска.

**Условия соревнования:**  
- Используем предобученную модель Faster RCNN.
- Используем предобученную модель YOLO.
- Сравнить результаты 2ух моделей

**Метрика качества**     
добиться mean Average Precision > 0.85 на валидационной выборке для каждой модели


### Краткая информация о данных
Предствлен набор из 852 различных фото людей в масках и без. Также приложены аннотации к каждому фото.
  
:arrow_up:[к оглавлению](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_2/README.md#Оглавление)


### Этапы работы над проектом  
1. Создать DataLoader для работы с Faster RCNN
2. Обучить модель Faster RCNN
3. Проверить работу модели Faster RCNN и определить mAP
4. Конвертировать данные в формат YOLO
5. Обучить модель YOLO
6. Проверить работу модели YOLO
7. Сравнить 2 модели

:arrow_up:[к оглавлению](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_2/README.md#Оглавление)

### Выводы:  
В ходе реализации проекта были успешно обучены и протестированы две современные архитектуры для задач обнаружения объектов: YOLO и Faster R-CNN.

:arrow_up:[к оглавлению](https://github.com/AlexexDenimus/sf_ds_projects/tree/master/cv_project_2/README.md#Оглавление)
