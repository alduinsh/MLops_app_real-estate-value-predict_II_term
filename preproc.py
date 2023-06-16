import pandas as pd


def cat_num_split(df: pd.DataFrame) -> tuple:
    '''Ищем категориальные и числовые признаки в датафрейме'''

    cat_columns = []
    num_columns = []

    for column_name in df.columns:
        if df[column_name].dtypes == object:
            cat_columns += [column_name]
        else:
            num_columns += [column_name]

    return cat_columns, num_columns


def load_data(filename: str) -> pd.DataFrame:
    '''Загружаем датафрейм'''

    ext = filename.split('.')[-1]

    if ext in ['xlsx', 'xls']:
        try:
            df = pd.read_excel(filename)
        
        except:
            print('Ваша таблица корявая')
            return None

    elif ext in ['csv', 'txt']:
        try:
            df = pd.read_csv(filename, sep='\t', encoding='utf-16')
        
        except:
            print('Ваш csv битый')
            return None

    else:
        print('Не знаю такого формата')
        return None

    return df


def get_model_features(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Забираем из датафрейма только те фичи, которые нужны модели
    Предполагается, что './' существует файл model.mtd,
    в котором в виде строки лежит перечень необходимых фич.
    '''

    try:
        with open('model.mtd', 'r', encoding='utf-16') as file_:
            columns = file_.readlines()[0]

    except:
        print('Не могу открыть файл метаданных текущей модели')
        return None

    columns = columns.split(',')[:-1]   # Чтобы убрать /n

    return df[columns]


def get_predict_model_features(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Забираем из датафрейма только те фичи, которые нужны модели
    Предполагается, что './' существует файл model.mtd,
    в котором в виде строки лежит перечень необходимых фич.
    '''

    try:
        with open('model.mtd', 'r', encoding='utf-16') as file_:
            columns = file_.readlines()[0]

    except:
        print('Не могу открыть файл метаданных текущей модели')
        return None

    columns = columns.split(',')[1:-1]   # Чтобы убрать /n и цену

    return df[columns]


def create_adress_feature(df: pd.DataFrame) -> pd.DataFrame:
    '''Добавляем признак "адрес" в датафрейм'''

    df['Столбец1'] = df['Столбец1'].astype('str')
    df['дом'] = df['дом'].astype('str')

    df['адрес'] = df['Столбец1'] + ', ' + df['дом']

    return df


def save_data(df: pd.DataFrame,
              filename: str='./Datasets/train.csv') -> None:
    '''Записываем подготовленную тренировочную выборку на диск'''

    try:
        df.to_csv(filename, index=False, sep='\t')
        print('Датасет сохранён успешно')

    except:
        print('Не могу записать датасет на диск')
