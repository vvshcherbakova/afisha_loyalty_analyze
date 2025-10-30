#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# <b> Валентина, привет!👋</b>
# 
# Меня зовут Алексей Гриб, и я буду ревьюером твоего проекта. 
# 
# Сразу хочу предложить в дальнейшем общаться на "ты" - надеюсь, так будет комфортнее:) Но если это неудобно, обязательно дай знать, и мы придумаем что-нибудь ещё!
#     
# Цель ревью - не искать ошибки в твоём проекте, а помочь тебе сделать твою работу ещё лучше, устранив недочёты и приблизив её к реальным задачам специалиста по работе с данными. Поэтому не расстраивайся, если что-то не получилось с первого раза - это нормально, и это поможет тебе вырасти!
#     
# Ты можешь найти мои комментарии, обозначенные <font color='green'>зеленым</font>, <font color='gold'>желтым</font> и <font color='red'>красным</font> цветами, например:
# 
# <br/>
# 
# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> похвала, рекомендации «со звёздочкой», полезные лайфхаки, которые сделают и без того красивое решение ещё более элегантным.
# </div>
# 
# <br/>
# 
# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> некритичные ошибки или развивающие рекомендации на будущее. 
# </div>
# 
# 
# <br/>
# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# критичные ошибки, которые обязательно нужно исправить.
# </div>
# 
#     
# Пожалуйста, не удаляй мои комментарии, они будут особенно полезны для нашей работы в случае повторной проверки проекта. 
#     
# Ты также можешь задавать свои вопросы, реагировать на мои комментарии, делать пометки и пояснения - полная творческая свобода! Но маленькая просьба - пускай они будут отличаться от моих комментариев, это поможет избежать путаницы в нашем общении:)
# Например, вот так:
#     
# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# *твой текст*
# </div>
#     
# Давай посмотрим на твой проект!

# # ЗДРАВТСТВУЙТЕ! ВАШИХ КОММЕНТАРИЕВ НЕТ В КОДЕ. ГДЕ ИХ СМОТРЕТЬ? ОТПРАВЛЯЮ СНОВА, ОЧЕНЬ ЖДУ ОТВЕТ.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#  
# <b>Все отлично!👍:</b> Не сохранились комментарии при отправке. Восстановил из проверенного файла. За итерацию эта отправка считаться, конечно, не будет, я также возьму в приоритет твой проект на время следующих проверок.

# # Анализ лояльности пользователей Яндекс Афиши

# ## Этапы выполнения проекта
# 
# ### 1. Загрузка данных и их предобработка
# 
# ---
# 
# **Задача 1.1:** Напишите SQL-запрос, выгружающий в датафрейм pandas необходимые данные. Используйте следующие параметры для подключения к базе данных `data-analyst-afisha`:
# 
# - **Хост** — `rc1b-wcoijxj3yxfsf3fs.mdb.yandexcloud.net`
# - **База данных** — `data-analyst-afisha`
# - **Порт** — `6432`
# - **Аутентификация** — `Database Native`
# - **Пользователь** — `praktikum_student`
# - **Пароль** — `Sdf4$2;d-d30pp`
# 
# Для выгрузки используйте запрос из предыдущего урока и библиотеку SQLAlchemy.
# 
# Выгрузка из базы данных SQL должна позволить собрать следующие данные:
# 
# - `user_id` — уникальный идентификатор пользователя, совершившего заказ;
# - `device_type_canonical` — тип устройства, с которого был оформлен заказ (`mobile` — мобильные устройства, `desktop` — стационарные);
# - `order_id` — уникальный идентификатор заказа;
# - `order_dt` — дата создания заказа (используйте данные `created_dt_msk`);
# - `order_ts` — дата и время создания заказа (используйте данные `created_ts_msk`);
# - `currency_code` — валюта оплаты;
# - `revenue` — выручка от заказа;
# - `tickets_count` — количество купленных билетов;
# - `days_since_prev` — количество дней от предыдущей покупки пользователя, для пользователей с одной покупкой — значение пропущено;
# - `event_id` — уникальный идентификатор мероприятия;
# - `service_name` — название билетного оператора;
# - `event_type_main` — основной тип мероприятия (театральная постановка, концерт и так далее);
# - `region_name` — название региона, в котором прошло мероприятие;
# - `city_name` — название города, в котором прошло мероприятие.
# 
# ---
# 

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#  
# <b>Все отлично!👍:</b> Хорошее вступление!
#     
# В нём есть всё, что необходимо, чтобы понять суть проекта с первых строк отчёта!

# In[1]:


# Используйте ячейки типа Code для вашего кода,
# а ячейки типа Markdown для комментариев и выводов


# In[2]:


# При необходимости добавляйте новые ячейки для кода или текста


# In[3]:


#!pip install sqlalchemy
#№!pip install psycopg2
#!pip install psycopg2-binary
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
np.set_printoptions(threshold=np.inf) 
import matplotlib.pyplot as plt
import matplotlib as mb
import seaborn as sns
get_ipython().system('pip install scypy')
get_ipython().system('pip install phik')
from phik import phik_matrix
from dotenv import load_dotenv
import os


# In[4]:


pip freeze


# In[5]:

load_dotenv()


# In[6]:

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(
    os.getenv('DB_USER'),
    os.getenv('DB_PASSWORD'),
    os.getenv('DB_HOST'),
    os.getenv('DB_PORT'),
    os.getenv('DB_NAME')
)


# In[7]:


engine = create_engine(connection_string)


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Библиотеки импортировали, коннектор сделали - отлично!

# In[8]:


query = '''
select
  user_id,
  device_type_canonical,
  order_id,
  created_dt_msk as order_dt,
  created_ts_msk as order_ts,
  currency_code,
  revenue,
  tickets_count,
  extract('days' from created_dt_msk - lag(created_dt_msk) over(partition by user_id order by created_dt_msk)) as days_since_prev,
  event_id,
  event_name_code as event_name,
  event_type_main,
  service_name,
  region_name,
  city_name
from afisha.purchases
left join afisha.events using (event_id)
left join afisha.city using (city_id)
left join afisha.regions using (region_id)
where device_type_canonical in ('mobile', 'desktop') and event_type_main != 'фильм'
order by user_id
'''


# In[9]:


df = pd.read_sql_query(query, con=engine)


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Данные успешно загружены.

# ---
# 
# **Задача 1.2:** Изучите общую информацию о выгруженных данных. Оцените корректность выгрузки и объём полученных данных.
# 
# Предположите, какие шаги необходимо сделать на стадии предобработки данных — например, скорректировать типы данных.
# 
# Зафиксируйте основную информацию о данных в кратком промежуточном выводе.
# 
# ---

# In[10]:


df.info()


# На стадии предобработки данных можно скорректировать типы данных (object) и понизить их разрядность (если это возможно). Возможно заменить пустые данные значениями. Удалить дубликаты если они есть.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Данные изучены, намечены шаги по обработке.

# ---
# 
# ###  2. Предобработка данных
# 
# Выполните все стандартные действия по предобработке данных:
# 
# ---
# 
# **Задача 2.1:** Данные о выручке сервиса представлены в российских рублях и казахстанских тенге. Приведите выручку к единой валюте — российскому рублю.
# 
# Для этого используйте датасет с информацией о курсе казахстанского тенге по отношению к российскому рублю за 2024 год — `final_tickets_tenge_df.csv`. Его можно загрузить по пути `https://code.s3.yandex.net/datasets/final_tickets_tenge_df.csv')`
# 
# Значения в рублях представлено для 100 тенге.
# 
# Результаты преобразования сохраните в новый столбец `revenue_rub`.
# 
# ---
# 

# In[11]:


exchange = pd.read_csv('https://code.s3.yandex.net/datasets/final_tickets_tenge_df.csv')


# In[12]:


# преобразовываем формат из object в формат даты, иначе выдает ошибку
exchange['data'] = exchange['data'].astype('datetime64[ns]')


# In[13]:


merged_df = pd.merge(df, exchange, left_on=['order_dt', 'currency_code'],right_on=['data','cdx'], how='left')


# In[14]:


merged_df['revenue_rub'] = merged_df.apply(lambda row: row['revenue'] * (row['curs'] / row['nominal'])                                            if row['currency_code'] == 'kzt' else row['revenue'], axis=1)


# In[15]:


# удаляю лишние столбцы 
merged_df = merged_df.drop(['data','nominal','curs','cdx'], axis=1)


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Выручка приведена к единой валюте.

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> Решение с `apply` неэффективно, так как применяет функцию построчно ко всей таблице. 
#         
# Лучше использовать маску с `.loc`:
#         
# ```python
# # Создаем Series (словарь) из курсов: 'data' -> 'curs'
# # Это нужно сделать один раз, а не на каждой строке.
# rate_map = exchange_rates.set_index('data')['curs']
# 
# # Используем .map() для "подтягивания" курса в df по дате 'order_dt'
# # Это C-оптимизированная операция, во много раз быстрее apply
# df['rate'] = df['order_dt'].map(rate_map)
# 
# # Инициализируем новую колонку значением по умолчанию
# df['revenue_rub'] = df['revenue']
# 
# # Создаем маску (условие) для строк, которые нужно конвертировать
# mask = df['currency_code'] == 'kzt'
# 
# # Выполняем векторизированную операцию ТОЛЬКО для нужных строк
# df.loc[mask, 'revenue_rub'] = df['revenue'] * df['rate'] / 100
# ```

# ---
# 
# **Задача 2.2:**
# 
# - Проверьте данные на пропущенные значения. Если выгрузка из SQL была успешной, то пропуски должны быть только в столбце `days_since_prev`.
# - Преобразуйте типы данных в некоторых столбцах, если это необходимо. Обратите внимание на данные с датой и временем, а также на числовые данные, размерность которых можно сократить.
# - Изучите значения в ключевых столбцах. Обработайте ошибки, если обнаружите их.
#     - Проверьте, какие категории указаны в столбцах с номинальными данными. Есть ли среди категорий такие, что обозначают пропуски в данных или отсутствие информации? Проведите нормализацию данных, если это необходимо.
#     - Проверьте распределение численных данных и наличие в них выбросов. Для этого используйте статистические показатели, гистограммы распределения значений или диаграммы размаха.
#         
#         Важные показатели в рамках поставленной задачи — это выручка с заказа (`revenue_rub`) и количество билетов в заказе (`tickets_count`), поэтому в первую очередь проверьте данные в этих столбцах.
#         
#         Если обнаружите выбросы в поле `revenue_rub`, то отфильтруйте значения по 99 перцентилю.
# 
# После предобработки проверьте, были ли отфильтрованы данные. Если были, то оцените, в каком объёме. Сформулируйте промежуточный вывод, зафиксировав основные действия и описания новых столбцов.
# 
# ---

# In[16]:


#кол-во пропусков
merged_df.isnull().sum()


# В датафрейме пустые значения присутствуют только в поле days_since_prev - 21 933 пропуска

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Нет анализа пропусков - это первое задание в этом блоке.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Результат нужно прокомментировать.

# In[17]:


# преобразовываем типы данных
for column in ['user_id','device_type_canonical','currency_code','event_name','event_type_main','service_name'               ,'region_name','city_name']:
    merged_df[column] = merged_df[column].astype('string')
    
for column in ['revenue','days_since_prev','revenue_rub']:
    merged_df[column] = pd.to_numeric(merged_df[column], downcast='float')    


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Типы данных скорректированы.

# In[18]:


merged_df['device_type_canonical'].unique()


# In[19]:


merged_df['currency_code'].unique()


# In[20]:


merged_df['event_type_main'].unique() 


# In[21]:


merged_df['service_name'].unique()  


# In[22]:


regions = merged_df['city_name'].unique()


# In[23]:


for region  in regions : print(region)


# В поле event_type_main есть значения - "другое" - которые обозначают отсутствие информации

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Тут нужно в явном виде вывести на экран значения категориальных признаков, задействованных в проекте, и проверить их на предмет ошибок.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[24]:


plt.figure(figsize=(10, 5))
sns.histplot(data=merged_df, x='tickets_count', bins = 100).set( title = 'Распределение значений по кол-ву билетов', 
                                                                 ylabel = 'Частота',
                                                                 xlabel = 'Кол-во билетов')
plt.show()

plt.figure(figsize=(20, 5))
sns.boxplot(data=merged_df, x = 'revenue_rub').set(title='Распределение значений выручки в руб.')


plt.show()


# In[25]:


merged_df.describe()


# In[26]:


revenue_99th_percentile = merged_df['revenue_rub'].quantile(0.99)

filtered_df = merged_df[merged_df['revenue_rub'] <= revenue_99th_percentile]


# In[27]:


# смотрим сколько данных отфильтровано
a, b = len(merged_df), len(filtered_df)
print(a, b, round((a-b)/a*100, 2))


# In[28]:


filtered_df['user_id'].nunique()


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Численные признаки изучены, удалены выбросы.

# ---
# 
# ### 3. Создание профиля пользователя
# 
# В будущем отдел маркетинга планирует создать модель для прогнозирования возврата пользователей. Поэтому сейчас они просят вас построить агрегированные признаки, описывающие поведение и профиль каждого пользователя.
# 
# ---
# 
# **Задача 3.1.** Постройте профиль пользователя — для каждого пользователя найдите:
# 
# - дату первого и последнего заказа;
# - устройство, с которого был сделан первый заказ;
# - регион, в котором был сделан первый заказ;
# - билетного партнёра, к которому обращались при первом заказе;
# - жанр первого посещённого мероприятия (используйте поле `event_type_main`);
# - общее количество заказов;
# - средняя выручка с одного заказа в рублях;
# - среднее количество билетов в заказе;
# - среднее время между заказами.
# 
# После этого добавьте два бинарных признака:
# 
# - `is_two` — совершил ли пользователь 2 и более заказа;
# - `is_five` — совершил ли пользователь 5 и более заказов.
# 
# **Рекомендация:** перед тем как строить профиль, отсортируйте данные по времени совершения заказа.
# 
# ---
# 

# Текущий способ получения профиля довольно громоздкий - стоит его оптимизировать. Используй agg и словарь, где ключом будет название признака, а значением - агрегация, которая к столбцу применяется.
# 
# Для получения даты первого и последнего заказа можно использовать агрегации first и last без применения shift().
# 
# Также при оценке среднего интервала нужно работать с исходным признаком days_since_prev, а не счиать его вручную.
# 
# Так как на текущем этапе есть системные ошибки, которые повлияют на результаты дальнейшего исследования, остальную часть проекта будет смысл проверять, когда ошибки будут исправлены

# In[29]:


sorted_df = filtered_df.sort_values(by=['user_id', 'order_ts'], ascending = True)


# In[30]:


min_max_orders = sorted_df.groupby('user_id')[['order_ts']].agg(min_order_ts = ('order_ts','first'), 
                                                                max_order_ts = ('order_ts','last'))


# In[31]:


# присоединяю столбец с минимальной датой заказа к датафрейму
df_merged = pd.merge(sorted_df, min_max_orders, left_on=['user_id'], right_on =['user_id'], how = 'left')  


# In[32]:


# добавляю флаг первого заказа на пользователя 
df_merged['is_first_order'] = df_merged['order_ts'] == df_merged['min_order_ts']


# In[33]:


#df_merged['days_since_prev'] = df_merged['days_since_prev'].fillna(value=0)


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Пропуски в `days_since_prev` заполнять не нужно - нули будут влиять на расчёт статистик. Агрегация `mean` игнорирует `NaN`, поэтому можно считать среднее без обработки пропусков.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[34]:


client_profile_first_cats = df_merged.loc[df_merged['is_first_order'] == True].groupby('user_id')[['device_type_canonical','service_name','region_name','event_type_main','order_id']].agg(first_order_device = ('device_type_canonical','min'), first_order_region = ('region_name','min'), first_service_name = ('service_name','min'), first_event_type = ('event_type_main','min'))                                                 


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> С учётом фильтра `'is_first_order' == True` стастистики считаются только по одной транзакции, что неверно - см.ниже:

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено. Агрегация `min` тут работает корректно только за счёт флага `is_first_order`, но в целом лучше использовать `first`.

# In[35]:


a = client_profile_first_cats.reset_index()
a['user_id'].duplicated().sum()


# In[36]:


client_profile_ttl = df_merged.groupby('user_id')[['order_id','revenue_rub','days_since_prev','tickets_count']].agg(total_orders_cnt = ('order_id','count'), avg_revenue_rub = ('revenue_rub','mean'),date_difference_d = ('days_since_prev','mean'), avg_cnt_per_order = ('tickets_count','mean'))


# In[37]:


client_profile = pd.merge(min_max_orders, client_profile_first_cats, left_on=['user_id'], right_on =['user_id'], how = 'left')  
client_profile = pd.merge(client_profile, client_profile_ttl, left_on=['user_id'], right_on =['user_id'], how = 'left')  


# In[38]:


# переименовываю столбец
client_profile = client_profile.rename(columns={'count': 'total_orders_cnt'})


# In[39]:


# совершил ли пользователь 2 и более заказа;
client_profile['is_two'] = client_profile['total_orders_cnt'] >= 2

# совершил ли пользователь 5 и более заказов.
client_profile['is_five'] = client_profile['total_orders_cnt'] >= 5


# In[40]:


client_profile = client_profile.reset_index()


# In[41]:


client_profile = client_profile[['user_id','min_order_ts','max_order_ts','first_order_device','first_order_region','first_service_name','first_event_type'                            ,'total_orders_cnt','avg_revenue_rub','avg_cnt_per_order','date_difference_d','is_two','is_five']].drop_duplicates()


# In[42]:


client_profile['user_id'].duplicated().sum()


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Текущий способ получения профиля довольно громоздкий - стоит его оптимизировать. Используй `agg` и словарь, где ключом будет название признака, а значением - агрегация, которая к столбцу применяется. 
#     
# Для получения даты первого и последнего заказа можно использовать агрегации `first` и `last` без применения `shift()`. 
#     
# Также при оценке среднего интервала нужно работать с исходным признаком `days_since_prev`, а не счиать его вручную.
#     
# Так как на текущем этапе есть системные ошибки, которые повлияют на результаты дальнейшего исследования, остальную часть проекта будет смысл проверять, когда ошибки будут исправлены.

# **Комментарий студента:** Честно говоря, не понимаю, почему этот пункт обязателен к доработке. Действительно есть более элегантные способы к решению, но те, которые я использую - работают. Считаю, что такое должно помечаться желтым - как рекомендуемое решение, но никак не неверное.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Комментарий может считаться рекомендацией только в том случае, если текущее решение, хоть и неоптимальное, но корректно работает.
#     
# В твоём случае оно не работает коректно, так как оставляет дубликаты на уровне `user_id` - смысл профиля пользователя в том, чтобы на одного пользователя была одна строка. В твоём профиле большое количество дубликатов по `user_id`:
#     
# ![image.png](attachment:image.png)
#     
# Сответственно далее все выводы в текущем решении получены на неправильных данных, и их нецелесообразно проверять до тех пор, пока они не будут построены на правильных данных.
#     
# Ещё раз обращаю внимание на важность использования группировки - без неё в решении будут дубликаты. Словарь метрик и `agg` - самый простой способ, но ты можешь использовать и любой другой способ агрегации. Конечная цель - получить профиль, где на одного пользователя будет одна строка.
#     
# После этого все расчёты и выводы ниже нужно будет обновить.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Профиль по-прежнему считается неверно, и это делает часть выводов далее невалидными. Далее смогу проверить проект частично - задания, где задействованы статистики из `client_profile_first_cats`, проверять не буду, так как они всё ещё построены по неправильным данным - эти задания нужно будет актуализировать.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Теперь всё корректно. Вот способ проще, с агрегацией и `agg`, как я предлага изначально:
#     
# ```python
# def create_user_profile_optimized(df):
#     df_work = df[['user_id', 'created_ts_msk', 'region_name', 'service_name',
#                    'event_type_main', 'revenue', 'tickets_count', 'days_since_prev',
#                    'device_type_canonical']].sort_values(['user_id', 'created_ts_msk'])
# 
#     result = df_work.groupby('user_id').agg(
#         first_order_date=('created_ts_msk', 'min'),
#         last_order_date=('created_ts_msk', 'max'),
#         first_device=('device_type_canonical', 'first'),
#         first_region=('region_name', 'first'),
#         first_service=('service_name', 'first'),
#         first_event_type=('event_type_main', 'first'),
#         total_orders=('user_id', 'count'),
#         avg_revenue=('revenue', 'mean'),
#         avg_tickets_count=('tickets_count', 'mean'),
#         avg_days_between_orders=('days_since_prev', 'mean')
#     ).reset_index()
# 
#     result['is_two'] = (result['total_orders'] >= 2).astype(int)
#     result['is_five'] = (result['total_orders'] >= 5).astype(int)
# 
#     return result     
# ```

# ---
# 
# **Задача 3.2.** Прежде чем проводить исследовательский анализ данных и делать выводы, важно понять, с какими данными вы работаете: насколько они репрезентативны и нет ли в них аномалий.
# 
# Используя данные о профилях пользователей, рассчитайте:
# 
# - общее число пользователей в выборке;
# - среднюю выручку с одного заказа;
# - долю пользователей, совершивших 2 и более заказа;
# - долю пользователей, совершивших 5 и более заказов.
# 
# Также изучите статистические показатели:
# 
# - по общему числу заказов;
# - по среднему числу билетов в заказе;
# - по среднему количеству дней между покупками.
# 
# По результатам оцените данные: достаточно ли их по объёму, есть ли аномальные значения в данных о количестве заказов и среднем количестве билетов?
# 
# Если вы найдёте аномальные значения, опишите их и примите обоснованное решение о том, как с ними поступить:
# 
# - Оставить и учитывать их при анализе?
# - Отфильтровать данные по какому-то значению, например, по 95-му или 99-му перцентилю?
# 
# Если вы проведёте фильтрацию, то вычислите объём отфильтрованных данных и выведите статистические показатели по обновлённому датасету.

# In[43]:


total_users_cnt = client_profile['user_id'].count()
avg_revenue_per_order = round(client_profile['avg_revenue_rub'].mean(),1)
share_2_plus_orders =  round(client_profile['is_two'].sum() / client_profile['user_id'].count(),1)*100
share_5_plus_orders =  round(client_profile['is_five'].sum() / client_profile['user_id'].count(),1)*100

print(f'Общее количество пользователей: {total_users_cnt}\nСредняя выручка с одного заказа: {avg_revenue_per_order}\nДоля пользователей, совершивших 2 и более заказа: {share_2_plus_orders}%\nДоля пользователей, совершивших 5 и более заказов: {share_5_plus_orders}%')


# In[44]:


client_profile[['total_orders_cnt','avg_cnt_per_order','date_difference_d']].describe()


# Довольно сильно различие заметно в кол-ве заказов - разброс виден исходя из среднего и стандартного отклонения. Исключу выбросы по 99% перцентилю, так как эти данные могут исказить результаты анализа (не по 95, так как в этом случае будет исключено 5% данных, что, как мне кажется, слишком много).

# In[45]:


orders_99th_percentile = client_profile['total_orders_cnt'].quantile(0.99)

client_profile_f = client_profile[client_profile['total_orders_cnt'] <= orders_99th_percentile]


# In[46]:


# смотрим сколько данных отфильтровано
a, b = len(client_profile), len(client_profile_f)
print(f'Изначальный датафрейм: {a}\nОтфильтрованный датафрейм: {b}\nДоля: {round((a-b)/a*100, 2)}%')


# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Статистики по профилям пользователей изучены, удалены выбросы.

# ---
# 
# ### 4. Исследовательский анализ данных
# 
# Следующий этап — исследование признаков, влияющих на возврат пользователей, то есть на совершение повторного заказа. Для этого используйте профили пользователей.

# 
# 
# #### 4.1. Исследование признаков первого заказа и их связи с возвращением на платформу
# 
# Исследуйте признаки, описывающие первый заказ пользователя, и выясните, влияют ли они на вероятность возвращения пользователя.
# 
# ---
# 
# **Задача 4.1.1.** Изучите распределение пользователей по признакам.
# 
# - Сгруппируйте пользователей:
#     - по типу их первого мероприятия;
#     - по типу устройства, с которого совершена первая покупка;
#     - по региону проведения мероприятия из первого заказа;
#     - по билетному оператору, продавшему билеты на первый заказ.
# - Подсчитайте общее количество пользователей в каждом сегменте и их долю в разрезе каждого признака. Сегмент — это группа пользователей, объединённых определённым признаком, то есть объединённые принадлежностью к категории. Например, все клиенты, сделавшие первый заказ с мобильного телефона, — это сегмент.
# - Ответьте на вопрос: равномерно ли распределены пользователи по сегментам или есть выраженные «точки входа» — сегменты с наибольшим числом пользователей?
# 
# ---
# 

# In[47]:


# считаю кол-во пользователей по типу первого мероприятия
first_event_type_g = client_profile_f.groupby('first_event_type')['user_id'].count().reset_index().sort_values(by='user_id', ascending = False)
# кол-во пользователей
total_cnt = client_profile_f['user_id'].count()
# доля клиентов по типам мероприятий
share_types = first_event_type_g['user_id']/total_cnt*100
# объединение таблиц
first_event_type_g = pd.merge(first_event_type_g, share_types,left_index=True, right_index=True, how='left')
# переименовываю столбец
first_event_type_g = first_event_type_g.rename(columns={'user_id_x': 'users_cnt', 'user_id_y': 'share'})
#вывожу результат
first_event_type_g


# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Некоторые замечания и рекомендации⚠️:</b> Доли удобнее считать с помощью `value_counts(normalize=True)`.

# По результатам группикровки, видно что для большинства клиентов концерты являются мероприятием входа на платформу - 44%.

# In[48]:


# считаю кол-во пользователей по типу первого мероприятия
first_device_g = client_profile_f.groupby('first_order_device')['user_id'].count().reset_index().sort_values(by='user_id', ascending = False)
# доля клиентов по типу устройства
share_types = first_device_g['user_id']/total_cnt*100
# объединение таблиц
first_device_g = pd.merge(first_device_g, share_types, left_index=True, right_index=True, how='left')
# переименовываю столбец
first_device_g = first_device_g.rename(columns={'user_id_x': 'users_cnt', 'user_id_y': 'share'})
#вывожу результат
first_device_g


# Большая часть клиентов начала пользоваться сервисом с мобильного устройства - 82.8%

# In[49]:


# считаю кол-во пользователей по типу первого мероприятия
first_region_g = client_profile_f.groupby('first_order_region')['user_id'].count().reset_index().sort_values(by='user_id', ascending = False)
# доля клиентов по типу устройства
share_types = first_region_g['user_id']/total_cnt*100
# объединение таблиц
first_region_g = pd.merge(first_region_g, share_types, left_index=True, right_index=True, how='left')
# переименовываю столбец
first_region_g = first_region_g.rename(columns={'user_id_x': 'users_cnt', 'user_id_y': 'share'})
#вывожу результат
first_region_g.head(10)


# У бОльшего кол-ва пользователь регион проведения мероприятия по первому заказу - Каменевский регион, 32.7%

# In[50]:


# считаю кол-во пользователей по типу первого мероприятия
first_service_g = client_profile_f.groupby('first_service_name')['user_id'].count().reset_index().sort_values(by='user_id', ascending = False)
# доля клиентов по типу устройства
share_types = first_service_g['user_id']/total_cnt*100
# объединение таблиц
first_service_g = pd.merge(first_service_g, share_types, left_index=True, right_index=True, how='left')
# переименовываю столбец
first_service_g = first_service_g.rename(columns={'user_id_x': 'users_cnt', 'user_id_y': 'share'})
#вывожу результат
first_service_g.head(10)


# "Билеты без проблем" - наиболее частый сервис для овершения первого заказа

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Все выводы точно отражают данные из таблиц.
# 
# Верно указано, что для большинства клиентов (44%) концерты являются мероприятием входа на платформу.
# 
# Правильно отмечено, что большая часть клиентов (82.8%) начала пользоваться сервисом с мобильного устройства.
# 
# Корректно определено, что регионом проведения мероприятия по первому заказу у большинства пользователей (32.7%) является Каменевский регион.
# 
# Точно указано, что Билеты без проблем - наиболее частый сервис для совершения первого заказа. Все приведенные процентные значения соответствуют данным в колонке share соответствующих таблиц.

# ---
# 
# **Задача 4.1.2.** Проанализируйте возвраты пользователей:
# 
# - Для каждого сегмента вычислите долю пользователей, совершивших два и более заказа.
# - Визуализируйте результат подходящим графиком. Если сегментов слишком много, то поместите на график только 10 сегментов с наибольшим количеством пользователей. Такое возможно с сегментами по региону и по билетному оператору.
# - Ответьте на вопросы:
#     - Какие сегменты пользователей чаще возвращаются на Яндекс Афишу?
#     - Наблюдаются ли успешные «точки входа» — такие сегменты, в которых пользователи чаще совершают повторный заказ, чем в среднем по выборке?
# 
# При интерпретации результатов учитывайте размер сегментов: если в сегменте мало пользователей (например, десятки), то доли могут быть нестабильными и недостоверными, то есть показывать широкую вариацию значений.
# 
# ---
# 

# In[51]:


# считаю кол-во пользователей по типу первого мероприятия
first_event_type_g_2 = client_profile_f.groupby(['first_event_type','is_two'])['user_id'].count().reset_index().sort_values(by=['first_event_type','is_two'], ascending = False)
# кол-во пользователей 
first_event_type_g_2 = first_event_type_g_2.loc[first_event_type_g_2['is_two'] == True,['first_event_type','user_id']]
# объединение таблиц
first_event_type_g_2 = pd.merge(first_event_type_g_2, first_event_type_g, left_on = 'first_event_type', right_on = 'first_event_type', how='left')
# удаляю лишний столбец
first_event_type_g_2 = first_event_type_g_2.drop(['share'], axis=1)
first_event_type_g_2['is_two_share'] = round(first_event_type_g_2['user_id']/first_event_type_g_2['users_cnt']*100,2)
first_event_type_g_2


# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Некоторые замечания и рекомендации⚠️:</b> Доли удобнее считать с помощью агрегации `mean` к `is_two`.

# In[52]:


## график
first_event_type_graph = first_event_type_g_2.reset_index(drop=True, inplace=False)
#first_event_type_g_2.drop(columns=first_event_type_g_2.columns[index], axis=1)
first_event_type_graph =  first_event_type_graph.set_index('first_event_type', inplace=False)

first_event_type_graph[['is_two_share']].sort_values(by='is_two_share').plot(kind='bar',
    title='Доля пользователей с 2 и более заказами по типу мероприятия',
    rot = 50,
    xlabel = 'Тип первого мероприятия',
    ylabel = 'Доля пользователей с 2 и более заказами',
    legend = False,
    )
plt.axhline(y = first_event_type_graph['is_two_share'].mean())
plt.show()


# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Некоторые замечания и рекомендации⚠️:</b> На графиках этого типа можно отобразить средний уровень возврата по выборке с помощью `axhline` - так будет проще анализировать точки входа.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[53]:


# считаю кол-во пользователей по типу первого устройства
first_device_g_2 = client_profile_f.groupby(['first_order_device','is_two'])['user_id'].count().reset_index().sort_values(by=['first_order_device','is_two'], ascending = False)
# кол-во пользователей 
first_device_g_2 = first_device_g_2.loc[first_device_g_2['is_two'] == True,['first_order_device','user_id']]
# объединение таблиц
first_device_g_2 = pd.merge(first_device_g_2, first_device_g, left_on = 'first_order_device', right_on = 'first_order_device', how='left')
# удаляю лишний столбец
first_device_g_2 = first_device_g_2.drop(['share'], axis=1)
first_device_g_2['is_two_share'] = round(first_device_g_2['user_id']/first_device_g_2['users_cnt']*100,2)
first_device_g_2


# In[54]:


## график
first_device_g_graph = first_device_g_2.reset_index(drop=True, inplace=False)
#first_event_type_g_2.drop(columns=first_event_type_g_2.columns[index], axis=1)
first_device_g_graph =  first_device_g_graph.set_index('first_order_device', inplace=False)

first_device_g_graph[['is_two_share']].sort_values(by='is_two_share').plot(kind='bar',
    title='Доля пользователей с 2 и более заказами по устройствам',
    rot = 50,
    xlabel = 'Тип устройства',
    ylabel = 'Доля пользователей с 2 и более заказами',
    legend = False
)
plt.axhline(y = first_device_g_graph['is_two_share'].mean())
plt.show()


# In[55]:


# считаю кол-во пользователей по типу первого региона
first_region_g_2 = client_profile_f.groupby(['first_order_region','is_two'])['user_id'].count().reset_index().sort_values(by=['first_order_region','is_two'], ascending = False)
# кол-во пользователей 
first_region_g_2 = first_region_g_2.loc[first_region_g_2['is_two'] == True,['first_order_region','user_id']]
# объединение таблиц
first_region_g_2 = pd.merge(first_region_g_2, first_region_g, left_on = 'first_order_region', right_on = 'first_order_region', how='left')
# удаляю лишний столбец
first_region_g_2 = first_region_g_2.drop(['share'], axis=1)
first_region_g_2['is_two_share'] = round(first_region_g_2['user_id']/first_region_g_2['users_cnt']*100,2)
first_region_g_2 = first_region_g_2.sort_values(by='users_cnt', ascending = False)
first_region_g_2.head(20)


# In[56]:


first_region_g_2.tail(20)


# In[57]:


last_20_regions = first_region_g_2.tail(20)
last_20_regions['is_two_share'].mean()


# In[58]:


top_20_regions = first_region_g_2.head(20)
top_20_regions['is_two_share'].mean()


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Тут и далее следует использовать понятные имена для именования переменных - согласно стандарту написания кода на `Python`, имена переменных должны быть "говорящими", то есть кратко описывать суть хранимых данных.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[59]:


top_10_regions = first_region_g_2.head(10)
top_10_regions = top_10_regions.reset_index(drop=True, inplace=False)


# In[60]:


top_10_regions = top_10_regions[['is_two_share','first_order_region']]


# In[61]:


top_10_regions = top_10_regions.set_index('first_order_region', inplace=False)


# In[62]:


## график
top_10_regions.sort_values(by='is_two_share').plot(kind='barh',
    title='Доля пользователей с 2 и более заказами по региону',
    rot = 10,
    xlabel = 'Регион 1го заказа',
    ylabel = 'Доля пользователей с 2 и более заказами',
    legend = False
)

plt.show()


# In[63]:


# считаю кол-во пользователей по типу первого мероприятия
first_service_g_2 = client_profile_f.groupby(['first_service_name','is_two'])['user_id'].count().reset_index().sort_values(by=['first_service_name','is_two'], ascending = False)
# кол-во пользователей 
first_service_g_2 = first_service_g_2.loc[first_service_g_2['is_two'] == True,['first_service_name','user_id']]
# объединение таблиц
first_service_g_2 = pd.merge(first_service_g_2, first_service_g, left_on = 'first_service_name', right_on = 'first_service_name', how='left')
# удаляю лишний столбец
first_service_g_2 = first_service_g_2.drop(['share'], axis=1)
first_service_g_2['is_two_share'] = round(first_service_g_2['user_id']/first_service_g_2['users_cnt']*100,2)
first_service_g_2 = first_service_g_2.sort_values(by='is_two_share', ascending = False)
first_service_g_2


# In[64]:


## график
top_10_service = first_service_g_2.head(10)
#b['is_two_share'].mean()
top_10_service = top_10_service.reset_index(drop=True, inplace=False)


# In[65]:


top_10_service = top_10_service[['is_two_share','first_service_name']]


# In[66]:


top_10_service = top_10_service.set_index('first_service_name', inplace=False)


# In[67]:


## график
top_10_service.sort_values(by='is_two_share').plot(kind='bar',
    title='Доля пользователей с 2 и более заказами по сервису ',
    rot = 50,
    xlabel = 'Сервис первого заказа',
    ylabel = 'Доля пользователей с 2 и более заказами',
)
plt.axhline(y = top_10_service['is_two_share'].mean())
plt.show()


# In[68]:


top_10_service['is_two_share'].mean()


# Чаще всего в Яндекс.Афишу возвращаются пользователи - посетившие первым мероприятием выставки, сделавшие первый заказ с компьютера, сделавшие заказ через "Зе Бест!"
# Успешная точка входа через сервис "Зе Бест!" - в этом сегменте клиенты совершают повторный заказ чаще, чем в среднем по выборке.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Вывод точно определяет сегменты пользователей, которые чаще всего возвращаются на Яндекс.Афишу:
# 
# По типу первого мероприятия: выставки действительно показывают самую высокую долю возврата (64.01%) согласно таблице.
# 
# По типу устройства: компьютер (desktop) имеет более высокую долю возврата (63.81%), чем мобильные устройства (60.81%).
# 
# По билетному оператору: сервис Зе Бест! показывает наивысшую долю возврата (100%) на графике, что делает его "успешной точкой входа" (хотя и основанной на малом числе пользователей, как правило).

# ---
# 
# **Задача 4.1.3.** Опираясь на выводы из задач выше, проверьте продуктовые гипотезы:
# 
# - **Гипотеза 1.** Тип мероприятия влияет на вероятность возврата на Яндекс Афишу: пользователи, которые совершили первый заказ на спортивные мероприятия, совершают повторный заказ чаще, чем пользователи, оформившие свой первый заказ на концерты.
# - **Гипотеза 2.** В регионах, где больше всего пользователей посещают мероприятия, выше доля повторных заказов, чем в менее активных регионах.
# 
# ---

# Гипотеза 1 - не подтверждается, пользователи, которые совершили первый заказ на концерты чаще совершают повторный заказ, чем пользователи, оформившие свой первый заказ на спортивные мероприятия
# 

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Вывод о том, что гипотеза не подтверждается, является верным. Данные из таблицы показывают, что доля возврата у пользователей, купивших билеты на концерты (61.83%), действительно выше, чем у пользователей, купивших билеты на спортивные мероприятия (55.79%).

# Гипотеза 2 - отвергается, в менее активных регионах многие имеют более высокую долю возврата, чем самые крупные. Например, Шанырский регион (500 пользователей) имеет долю возврата 67.2%, что заметно выше, чем у Каменевского региона (7085 пользователей, 62.4%).

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Гипотеза предполагает, что в регионах с большим числом пользователей доля повторных заказов выше.
# 
# Данные показывают обратное: 
#     
# ![%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-28%20%D0%B2%2023.58.53.png](attachment:%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-28%20%D0%B2%2023.58.53.png)    
#     
# Многие менее активные регионы (с меньшим users_cnt) имеют более высокую долю возврата (is_two_share), чем самые крупные. Например, Шанырский регион (500 пользователей) имеет долю возврата 67.2%, что заметно выше, чем у Каменевского региона (7085 пользователей, 62.4%). Еще более мелкие регионы из второй таблицы показывают еще более высокие доли возврата (хотя эти данные могут быть нестабильны из-за малого числа пользователей).
# 
# Следовательно, данные не подтверждают, а скорее опровергают Гипотезу 2.
#     
#     
#     
# Далее проект нужно актуализировать, так как он построен на неправильных данных.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Для того, чтобы это проверить, я считала средние значения по этой доле, и среднее значение доли повторных заказов в регионах топ 20 выше (60.24%), чем в 20 последних регионах (54.24%). Я исправлю вывод, но прошу обхяснить мне, почему так делать нельзя.
#     
# </div>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> В текущем описании твой подход не был бы ошибочным, но на прошлой итерации ты не указала, что сравнивала топ-20 активных и топ-20 неактивных - было только сказано, что сравнивалась средняя доля по топ-10 с долей менее активных регионов вообще без указания, сколько регионов было включено в расчёт средних, поэтому я валидировал вывод "в лоб": 
#     
# ![%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-30%20%D0%B2%2008.34.27.png](attachment:%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-30%20%D0%B2%2008.34.27.png)
#     
# Твоё пояснение, которое ты та дала выше, было ключевым, и при его наличии замечания бы не было.

# ---
# 
# #### 4.2. Исследование поведения пользователей через показатели выручки и состава заказа
# 
# Изучите количественные характеристики заказов пользователей, чтобы узнать среднюю выручку сервиса с заказа и количество билетов, которое пользователи обычно покупают.
# 
# Эти метрики важны не только для оценки выручки, но и для оценки вовлечённости пользователей. Возможно, пользователи с более крупными и дорогими заказами более заинтересованы в сервисе и поэтому чаще возвращаются.
# 
# ---
# 
# **Задача 4.2.1.** Проследите связь между средней выручкой сервиса с заказа и повторными заказами.
# 
# - Постройте сравнительные гистограммы распределения средней выручки с билета (`avg_revenue_rub`):
#     - для пользователей, совершивших один заказ;
#     - для вернувшихся пользователей, совершивших 2 и более заказа.
# - Ответьте на вопросы:
#     - В каких диапазонах средней выручки концентрируются пользователи из каждой группы?
#     - Есть ли различия между группами?
# 
# Текст на сером фоне:
#     
# **Рекомендация:**
# 
# 1. Используйте одинаковые интервалы (`bins`) и прозрачность (`alpha`), чтобы визуально сопоставить распределения.
# 2. Задайте параметру `density` значение `True`, чтобы сравнивать форму распределений, даже если число пользователей в группах отличается.
# 
# ---
# 

# In[69]:


client_profile_f_1 = client_profile_f.loc[client_profile_f['is_two'] == True]
plt.figure(figsize=(20, 5))
sns.histplot(data=client_profile_f_1, x='avg_revenue_rub', bins = 70).set(title = 'Распределение значений средней выручки с 2+ заказами', 
                                                                 ylabel = 'Частота',
                                                                 xlabel = 'Среднняя выручка'                                                                
                                                                 )
plt.show()


# In[70]:


client_profile_f_2 = client_profile_f.loc[client_profile_f['is_two'] == False]
plt.figure(figsize=(20, 5))
sns.histplot(data=client_profile_f_2, x='avg_revenue_rub', bins = 70).set(title = 'Распределение значений средней выручки с 1 заказом', 
                                                                 ylabel = 'Частота',
                                                                 xlabel = 'Среднняя выручка'
                                                                 )
plt.show()


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Графики нужно наложить друг на друга и нормировать - в этом ключевая идея сравнения, так как именно таким образом мы можем найти интервалы, где один сегмент преобладает над другим.

# In[71]:


sns.histplot(data=client_profile_f,x='avg_revenue_rub', kde = True,hue='is_two', alpha=0.3, bins=50) 

# Подпишите график и ось Y
plt.title('График распределения средней выручки в зависимости от количества заказов')
plt.ylabel('Количество')
plt.xlabel('Ср. выручка')
plt.show()


# У клиентов совершивших один заказ пользователи концентрируются в диапазоне выручки от 0 до 1500, со смещением в диапазоне от 0 до 500.
# У клиентов с 2 и более заказами заметно выше частота пользователей в диапазоне от 0 до 500, с пиокм в значении 500.
# Различия есть в частоте пользователей - в сегменте с клиентами, у которых было 2+ заказов - клиентов с выручкой ниже 1000 больше.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Описание того, где концентрируются пользователи, в целом верное: для обеих групп основная масса действительно находится в диапазоне до 1000-1500, при этом для группы 2+ заказов пик верно отмечен в районе 500.

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> В выводах указано, что у пользователей с 1 заказом есть "смещение" в диапазон 0-500, а у группы 2+ пик "в значении 500". На графиках разница более явная: у группы с 1 заказом (нижний график) пик находится в самом начале, очень близко к нулю. У группы 2+ (верхний график) пик смещен вправо и находится в районе 400-500. Вывод не акцентирует на этом внимание.

# ---
# 
# **Задача 4.2.2.** Сравните распределение по средней выручке с заказа в двух группах пользователей:
# 
# - совершившие 2–4 заказа;
# - совершившие 5 и более заказов.
# 
# Ответьте на вопрос: есть ли различия по значению средней выручки с заказа между пользователями этих двух групп?
# 
# ---
# 

# In[72]:


client_profile_f_3 = client_profile_f.loc[(client_profile_f['is_two'] == True) & (client_profile_f['is_five'] == False)]
plt.figure(figsize=(20, 5))
sns.histplot(data=client_profile_f_3, x='avg_revenue_rub', bins = 70).set(title = 'Распределение значений средней выручки с 2-5 заказами', 
                                                                 ylabel = 'Частота',
                                                                 xlabel = 'Среднняя выручка'
                                                                 )
plt.show()


# In[73]:


client_profile_f_4 = client_profile_f.loc[client_profile_f['is_five'] == True]
plt.figure(figsize=(20, 5))
sns.histplot(data=client_profile_f_4, x='avg_revenue_rub', bins = 70).set(title = 'Распределение значений средней выручки с 5+ заказами', 
                                                                 ylabel = 'Частота',
                                                                 xlabel = 'Среднняя выручка'
                                                                 )
plt.show()


# Разница между текущими 2мя сегментами есть: в сегменте клиентов с 5+ заказами пользователи в значениях ср. выручки сконцентрированы около значения 500. В сегменте 2-5 такого явно не видно, распределение довольно равномерное. В сегменте 2-5 заказов средняя выручка немного больше, чем в сегменте 5+.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Вывод о том, что в сегменте пользователей с 5 и более заказами средняя выручка концентрируется около значения 500, полностью верный - это хорошо видно на нижнем графике.

# ---
# 
# **Задача 4.2.3.** Проанализируйте влияние среднего количества билетов в заказе на вероятность повторной покупки.
# 
# - Изучите распределение пользователей по среднему количеству билетов в заказе (`avg_tickets_count`) и опишите основные наблюдения.
# - Разделите пользователей на несколько сегментов по среднему количеству билетов в заказе:
#     - от 1 до 2 билетов;
#     - от 2 до 3 билетов;
#     - от 3 до 5 билетов;
#     - от 5 и более билетов.
# - Для каждого сегмента подсчитайте общее число пользователей и долю пользователей, совершивших повторные заказы.
# - Ответьте на вопросы:
#     - Как распределены пользователи по сегментам — равномерно или сконцентрировано?
#     - Есть ли сегменты с аномально высокой или низкой долей повторных покупок?
# 
# ---

# In[74]:


#категоризация по среднему кол-ву билетов в заказе
client_profile_f['cnt_tickets_cat'] = pd.cut(client_profile_f['avg_cnt_per_order'], bins=[0, 2, 3, 5,12],                                              labels=["1-2", "2-3", "3-5", "5+"], right=False)


# In[75]:


#для проверки корректности категоризации
#a = client_profile_f.loc[client_profile_f['cnt_tickets_cat'] == '1-2']
#print(a['avg_cnt_per_order'].sort_values().unique())


# In[76]:


total_count = client_profile_f['user_id'].count()
cat_count = client_profile_f.groupby('cnt_tickets_cat')['user_id'].count()
cat_count =  pd.DataFrame(cat_count) 
cast_share = round(cat_count/total_count,2)*100
cast_share.reset_index()
cat_count.reset_index()


# In[77]:


cat_stat = pd.merge(cast_share, cat_count, left_on = ['cnt_tickets_cat'], right_on =  ['cnt_tickets_cat'], how = 'left')
cat_stat.reset_index()


# In[78]:


cat_stat = cat_stat.rename(columns={'user_id_x': 'share', 'user_id_y': 'cnt'})


# In[79]:


cat_stat


# В сегментах по среднему количеству билетов в заказе пользователи распределены неравномерно - в сегментах с 2-3 билетами и 3-5 билетами находится 86% клиентов.
# Самая низкая доля повторных покупок в сегменте 5+ (18.8%), самая высокая доля - в сегменте 2-3 (73.6%)

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Вывод о том, что пользователи распределены по этим сегментам неравномерно, абсолютно верный. Расчет, показывающий, что 86% всех клиентов находятся в категориях 2-3 билета и 3-5 билетов, также соответствует данным из таблицы.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> В задании требовалось для каждого сегмента рассчитать долю пользователей, совершивших повторные заказы. 
#     
# Однако в представленной таблице колонка share показывает долю пользователей каждого сегмента от их общего числа, так как в сумме значения дают 100%. Вывод "Самая низкая доля повторных покупок в сегменте 5+ (3%)" неверный. Эти 3% - это доля клиентов, которые входят в сегмент 5+, а не их показатель возвращаемости. Фактически, анализ не отвечает на главный вопрос задачи о том, как среднее количество билетов влияет на вероятность повторной покупки.

# In[80]:


total_count_2 = client_profile_f['user_id'].count()
total_count_2_groupped = client_profile_f.groupby('cnt_tickets_cat',as_index=False)['user_id'].count()
cat_count_2 = client_profile_f.groupby(['cnt_tickets_cat','is_two'],as_index=False)['user_id'].count()
#cat_count_2 =  pd.DataFrame(cat_count_2) 
#cat_count_2.reset_index(name='cnt_tickets_cat').to_string(index=False)
#cast_share_2 = round(cat_count_2[]/total_count,2)*100
#cast_share.reset_index()
#cat_count.reset_index()
#cat_count_2.describe()  #.value_counts(normalize=True)
#total_count_2_groupped
cat_count_2_merged = pd.merge(cat_count_2, total_count_2_groupped, left_on = ['cnt_tickets_cat'], right_on =  ['cnt_tickets_cat'], how = 'left')
cat_count_2_merged['share'] = round(cat_count_2_merged['user_id_x']/cat_count_2_merged['user_id_y']*100,2)
cat_count_2_merged[['cnt_tickets_cat','share']].loc[cat_count_2_merged['is_two']==True]


# ---
# 
# #### 4.3. Исследование временных характеристик первого заказа и их влияния на повторные покупки
# 
# Изучите временные параметры, связанные с первым заказом пользователей:
# 
# - день недели первой покупки;
# - время с момента первой покупки — лайфтайм;
# - средний интервал между покупками пользователей с повторными заказами.
# 
# ---
# 
# **Задача 4.3.1.** Проанализируйте, как день недели, в которой была совершена первая покупка, влияет на поведение пользователей.
# 
# - По данным даты первого заказа выделите день недели.
# - Для каждого дня недели подсчитайте общее число пользователей и долю пользователей, совершивших повторные заказы. Результаты визуализируйте.
# - Ответьте на вопрос: влияет ли день недели, в которую совершена первая покупка, на вероятность возврата клиента?
# 
# ---
# 

# In[81]:


client_profile_f['day_of_week']= client_profile_f['min_order_ts'].dt.weekday


# In[82]:


cnt_day_of_week = client_profile_f.groupby('day_of_week')['user_id'].count()
cnt_day_of_week


# In[83]:


second_orders = client_profile_f.loc[(client_profile_f['is_two']==True)]
for_days_share = second_orders.groupby('day_of_week')['user_id'].count()
for_days_share


# In[84]:


second_orders_days_share = round(for_days_share/cnt_day_of_week*100,2)


# In[85]:


second_orders_days_share


# In[86]:


day_of_week_data = pd.merge(cnt_day_of_week,second_orders_days_share,left_on = ['day_of_week'],                            right_on = ['day_of_week'], how = 'left').reset_index()
day_of_week_data = day_of_week_data.rename(columns={'user_id_x': 'cnt', 'user_id_y': 'share'})


# In[87]:


day_of_week_data


# In[88]:


day_of_week_data.plot(
  kind='bar',
  x='day_of_week',
  y='cnt',
  alpha=0.5,
  color='lightgreen',
  edgecolor='k',
  title='Число пользователей по дням недели',
  xlabel = 'День недели',
  ylabel='Кол-во пользователей',
  legend = False    
)
plt.axhline(y=day_of_week_data['cnt'].mean())
plt.show()


# In[89]:


day_of_week_data.plot(
  kind='bar',
  x='day_of_week',
  y='share',
  alpha=0.5,
  color='lightgreen',
  edgecolor='k',
  title='Доля пользователей с повторными заказами по дням недели',
  xlabel = 'День недели',
  ylabel='Доля пользователей с повторными заказами',
  legend = False
)
plt.axhline(y=day_of_week_data['share'].mean())
plt.show()


# Несмотря на то, что в целом кол-во совершенных заказов по дням недели немного различается (например, в воскресение заметно меньше заказов). Выглядит так, будто сильной взаимосвязи между днем недели и возвращаемостью клиента нет.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Анализ выполнен полностью и корректно. Вывод о том, что день недели первой покупки не оказывает сильного влияния на возвращаемость клиента, абсолютно верен. Таблица с данными это подтверждает: значения доли вернувшихся пользователей находятся в очень узком диапазоне, всего от 59.43% до 63.04%. Наблюдение о том, что в воскресенье было меньше первых заказов, также соответствует данным из колонки cnt.

# ---
# 
# **Задача 4.3.2.** Изучите, как средний интервал между заказами влияет на удержание клиентов.
# 
# - Рассчитайте среднее время между заказами для двух групп пользователей:
#     - совершившие 2–4 заказа;
#     - совершившие 5 и более заказов.
# - Исследуйте, как средний интервал между заказами влияет на вероятность повторного заказа, и сделайте выводы.
# 
# ---
# 

# In[90]:


second_orders.groupby('is_five')['date_difference_d'].mean()


# In[91]:


df = second_orders[['date_difference_d','is_five']]


# In[92]:


correlation_matrix=df.phik_matrix(interval_cols=['date_difference_d']).sort_values(by='date_difference_d',ascending=False)
print("Корреляция переменных с 'rating':")
print(correlation_matrix['date_difference_d'])


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Не забывай настраивать `interval_cols` при использовании `phik`.

# У пользователей с 5+ заказами среднее время между заказами на 57%  меньше, чем у пользователей, совершивших 2-4 заказа. По результатам коррелляционного анализа взаимосвязь есть.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Основной вывод о том, что у пользователей с 5 и более заказами средний интервал между покупками значительно короче, является верным и подтверждается этими цифрами.

# ---
# 
# #### 4.4. Корреляционный анализ количества покупок и признаков пользователя
# 
# Изучите, какие характеристики первого заказа и профиля пользователя могут быть связаны с числом покупок. Для этого используйте универсальный коэффициент корреляции `phi_k`, который позволяет анализировать как числовые, так и категориальные признаки.
# 
# ---
# 
# **Задача 4.4.1:** Проведите корреляционный анализ:
# - Рассчитайте коэффициент корреляции `phi_k` между признаками профиля пользователя и числом заказов (`total_orders`). При необходимости используйте параметр `interval_cols` для определения интервальных данных.
# - Проанализируйте полученные результаты. Если полученные значения будут близки к нулю, проверьте разброс данных в `total_orders`. Такое возможно, когда в данных преобладает одно значение: в таком случае корреляционный анализ может показать отсутствие связей. Чтобы этого избежать, выделите сегменты пользователей по полю `total_orders`, а затем повторите корреляционный анализ. Выделите такие сегменты:
#     - 1 заказ;
#     - от 2 до 4 заказов;
#     - от 5 и выше.
# - Визуализируйте результат корреляции с помощью тепловой карты.
# - Ответьте на вопрос: какие признаки наиболее связаны с количеством заказов?
# 
# ---

# In[93]:


client_profile_for_corr = client_profile_f[['first_order_device','first_order_region','first_service_name',                                                   'first_event_type','total_orders_cnt','is_two','is_five',                                            'cnt_tickets_cat','day_of_week','avg_cnt_per_order','avg_revenue_rub','date_difference_d']] 
correlation_matrix=client_profile_for_corr.phik_matrix(interval_cols = ['total_orders_cnt','date_difference_d','avg_revenue_rub','avg_cnt_per_order'],                                                         
                                                                bins = {'total_orders_cnt':5,'date_difference_d':5,'avg_revenue_rub':5,'avg_cnt_per_order':5})


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Подскажи, почему в `interval_cols` передан только `total_orders_cnt` и почему было выбрано 3 бина?

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Про бины - честно говоря, мне недоконца понятно как выбирать их количество, пролистала теорию на счет этого и не нашла информации. Пробовала погуглить, ответа нормального не нашлось.

# In[94]:


print("Корреляция переменных с 'total_orders_cnt':")
print(correlation_matrix['total_orders_cnt'])


# In[95]:


sns.heatmap(correlation_matrix).set(title='Матрица корреляций')
plt.show()


# In[96]:


#категоризация по общему числу заказов
client_profile_f['cnt_tickets_cat_v2'] = pd.cut(client_profile_f['total_orders_cnt'], bins=[0, 2, 5, 153],                                              labels=["1", "2-4", "5+"], right=False)


# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> Фактически категоризация выполняется по общему числу закзаов, а не среднему - стоит скорректировать комментарий.

# In[97]:


#для проверки корректности категоризации
a = client_profile_f.loc[client_profile_f['cnt_tickets_cat_v2'] == '5+']
print(a['total_orders_cnt'].sort_values().unique())


# In[98]:


client_profile_f.groupby('cnt_tickets_cat_v2')['user_id'].count()


# In[99]:


client_profile_f


# In[100]:


client_profile_for_corr = client_profile_f[['first_order_device','first_order_region','first_service_name',                                                   'first_event_type','cnt_tickets_cat_v2','is_two','is_five','day_of_week',                                           'avg_cnt_per_order','date_difference_d','avg_revenue_rub']] 
correlation_matrix=client_profile_for_corr.phik_matrix(interval_cols = ['avg_cnt_per_order','date_difference_d','avg_revenue_rub'])


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Не забывай про настройку `interval_cols`.

# In[101]:


correlation_matrix


# In[102]:


sns.heatmap(correlation_matrix).set(title='Матрица корреляций')
plt.show()


# Наиболее связанные параметры с кол-вом заказов - среднее кол-во билетов в заказе, разница во времени между заказами и средняя выручка. Не очень значительная связь также есть с регионом первого заказа и сервисом, в котором он был совершен.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Вывод о том, какие параметры наиболее связаны с количеством заказов, верный. Он соответствует данным из корреляционной матрицы. Переменная, обозначающая число заказов (cnt_tickets_cat_v2), действительно показывает самую сильную связь со средним количеством билетов в заказе (0.383) и разницей во времени между заказами (0.391).

# ### 5. Общий вывод и рекомендации
# 
# В конце проекта напишите общий вывод и рекомендации: расскажите заказчику, на что нужно обратить внимание. В выводах кратко укажите:
# 
# - **Информацию о данных**, с которыми вы работали, и то, как они были подготовлены: например, расскажите о фильтрации данных, переводе тенге в рубли, фильтрации выбросов.
# - **Основные результаты анализа.** Например, укажите:
#     - Сколько пользователей в выборке? Как распределены пользователи по числу заказов? Какие ещё статистические показатели вы подсчитали важным во время изучения данных?
#     - Какие признаки первого заказа связаны с возвратом пользователей?
#     - Как связаны средняя выручка и количество билетов в заказе с вероятностью повторных покупок?
#     - Какие временные характеристики влияют на удержание (день недели, интервалы между покупками)?
#     - Какие характеристики первого заказа и профиля пользователя могут быть связаны с числом покупок согласно результатам корреляционного анализа?
# - Дополните выводы информацией, которая покажется вам важной и интересной. Следите за общим объёмом выводов — они должны быть компактными и ёмкими.
# 
# В конце предложите заказчику рекомендации о том, как именно действовать в его ситуации. Например, укажите, на какие сегменты пользователей стоит обратить внимание в первую очередь, а какие нуждаются в дополнительных маркетинговых усилиях.

# **Информация о данных:** Данные были импортированы и проверены на дубликаты, были отфильтрованы и исключены из анализа 0.99% данных, являющихся выбросами (99 процентиль). Так как в исходных данных была информация не только о рублевых операциях, но и об опрерациях с казахской валютой, было необходимо добавить курс этой валюты к общему датафрейму, для того, чтобы вычислять дальнейшие значения выручки в рублевом эквиваленте. В датафрейме пустые значения присутствуют только в поле days_since_prev - 21 933 пропуска. Была проведена замена на 0.

# **Основные результаты анализа**:
# - в отфильтрованном датафрейме содержатся данные по 21 854 пользователях и их заказах.
# - для большинства клиентов концерты являются мероприятием входа на платформу - 44%. 
# - у бОльшего кол-ва пользователь регион проведения мероприятия по первому заказу - Каменевский регион, 32.7%.
# - большая часть клиентов начала пользоваться сервисом с мобильного устройства - 82.8%.
# - "Билеты без проблем" - наиболее частый сервис для совершения первого заказа.
# - в исследовании были сформулированы 2 гипотезы.
# - Гипотеза 1. Тип мероприятия влияет на вероятность возврата на Яндекс Афишу: пользователи, которые совершили первый заказ на спортивные мероприятия, совершают повторный заказ чаще, чем пользователи, оформившие свой первый заказ на концерты.\
# Гипотеза 1 - не подтверждается, пользователи, которые совершили первый заказ на концерты чаще совершают повторный заказ, чем пользователи, оформившие свой первый заказ на спортивные мероприятия
# 
# - Гипотеза 2. В регионах, где больше всего пользователей посещают мероприятия, выше доля повторных заказов, чем в менее активных регионах.\
# Гипотеза 2 - отвергается, в менее активных регионах многие имеют более высокую долю возврата, чем самые крупные. Например, Шанырский регион (500 пользователей) имеет долю возврата 67.2%, что заметно выше, чем у Каменевского региона (7085 пользователей, 62.4%).
# 
# - У клиентов совершивших один заказ пользователи концентрируются в диапазоне выручки от 0 до 1500, со смещением в диапазоне от 0 до 500.
# У клиентов с 2 и более заказами заметно выше частота пользователей в диапазоне от 0 до 500, с пиокм в значении 500.
# Различия есть в частоте пользователей - в сегменте с клиентами, у которых было 2+ заказов - клиентов с выручкой ниже 1000 больше.
# - Разница между текущими сегментами 5+ и 2-5 есть: в сегменте клиентов с 5+ заказами пользователи в значениях ср. выручки сконцентрированы около значения 500. В сегменте 2-5 такого явно не видно, распределение довольно равномерное. В сегменте 2-5 заказов средняя выручка немного больше, чем в сегменте 5+.
# 
# - чаще всего в Яндекс.Афишу возвращаются пользователи - посетившие первым мероприятием выставки, сделавшие первый заказ с компьютера, сделавшие заказ через "Зе Бест!"
# Успешная точка входа через сервис "Зе Бест!" - в этом сегменте клиенты совершают повторный заказ чаще, чем в среднем по выборке.
# 
# - В сегментах по среднему количеству билетов в заказе пользователи распределены неравномерно - в сегментах с 2-3 билетами и 3-5 билетами находится 86% клиентов.
# Самая низкая доля повторных покупок в сегменте 5+ (18.8%), самая высокая доля - в сегменте 2-3 (73.6%)
# 
# - Несмотря на то, что в целом кол-во совершенных заказов по дням недели немного различается (например, в воскресенье заметно меньше заказов). Выглядит так, будто сильной взаимосвязи между днем недели и возвращаемостью клиента нет.
# 
# - У пользователей с 5+ заказами среднее время между заказами на 57% меньше, чем у пользователей, совершивших 2-4 заказа. По результатам коррелляционного анализа взаимосвязь есть.
# - Наиболее связанные параметры с кол-вом заказов - среднее кол-во билетов в заказе, разница во времени между заказами и средняя выручка. Не очень значительная связь также есть с регионом первого заказа и сервисом, в котором он был совершен.

# Исходя из проведенного анализа, могу порекоммендовать команде маректинга обратить внимание на клиентов из сегмента 5+, по которым доля повторных покупок аномально низкая, возможно необходимо предложить таким клиентам спциальные условия при оформлении крупного заказа. Интересно также, что чаще всего возвращаются клиенты сервиса Зе Бест, возможно, в нем это делать удобнее для пользователей, если это возможно, расширить взаимодействие афиши с этим сервисом. 

# ### 6. Финализация проекта и публикация в Git
# 
# Когда вы закончите анализировать данные, оформите проект, а затем опубликуйте его.
# 
# Выполните следующие действия:
# 
# 1. Создайте файл `.gitignore`. Добавьте в него все временные и чувствительные файлы, которые не должны попасть в репозиторий.
# 2. Сформируйте файл `requirements.txt`. Зафиксируйте все библиотеки, которые вы использовали в проекте.
# 3. Вынести все чувствительные данные (параметры подключения к базе) в `.env`файл.
# 4. Проверьте, что проект запускается и воспроизводим.
# 5. Загрузите проект в публичный репозиторий — например, на GitHub. Убедитесь, что все нужные файлы находятся в репозитории, исключая те, что в `.gitignore`. Ссылка на репозиторий понадобится для отправки проекта на проверку. Вставьте её в шаблон проекта в тетрадке Jupyter Notebook перед отправкой проекта на ревью.

# **Вставьте ссылку на проект в этой ячейке тетрадки перед отправкой проекта на ревью.**
# https://github.com/vvshcherbakova/afisha_loyalty_analyze

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Файл с проектом, зависимостями и `.gitignore` размещены в репозитории.

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> Можно было бы добавить также `README.md` с описанием проекта и выводом.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> В версии, которую ты заливаешь на `GitHub`, не стоит оставлять параметры подключения в явном виде - это может привести к несанкционированному доступу к данным, что чревато их потереей или изменением. Лучшее решение - локально создать `.env` файл, из которого с помощью `os` эти параметры подключения передаются в код. А файл `.gitignore` поможет не отслеживать этот файл для репозитория.
#     
# Файл `.env` может выглядеть так:
# 
# ```python
# DB_NAME="..."
# DB_HOST="..."
# DB_PORT="..."
# DB_USER="..."
# DB_PASSWORD="..."
# ```
#     
# В самом проекте мы можем обращаться к сохраненным параметрам с помощью библиотеки `dotenv`, чтобы загрузить переменные окружения, и `os`, чтобы обратиться к ним:
#     
# ```python
# import os
# import dotenv
#     
# load_dotenv() # автоматически ищет .env в текущей директории
#     
# connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(
#     os.getenv('DB_USER'),
#     os.getenv('DB_PASSWORD'),
#     os.getenv('DB_HOST'),
#     os.getenv('DB_PORT'),
#     os.getenv('DB_NAME'),
# )
# ```

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# # Комментарий ревьюера: общий вывод по проекту.
# 
# Валентина, проект получился на довольно хорошем уровне - отличная работа над проектом, молодец!
# 
# Мне нравится твой аналитический подход к выполнению проекта, ты соблюдаешь структуру работы, выполняешь её последовательно - это очень хорошо! Шаги проекта выполнены по порядку согласно плану проекта, нет смысловых и структурных ям. Важно, что не забываешь про выводы.
#     
# Над проектом ещё стоит поработать - есть рекомендации по дополнению некоторых твоих шагов проекта. Такие рекомендации я отметил жёлтыми комментариями. Будет здорово, если ты учтёшь их - так проект станет структурно и содержательно более совершенным.
#     
# Также в работе есть критические замечания. К этим замечаниям я оставил пояснительные комментарии красного цвета, в которых перечислил возможные варианты дальнейших действий. Уверен, ты быстро с этим управишься:)
#     
# Если о том, что нужно сделать в рамках комментариев, будут возникать вопросы - оставь их, пожалуйста, в комментариях, и я отвечу на них во время следующего ревью.
#     
# Также буду рад ответить на любые твои вопросы по проекту или на какие-либо другие, если они у тебя имеются - оставь их в комментариях, и я постараюсь ответить:)
#     
# Жду твой проект на повторном ревью. До встречи:)
