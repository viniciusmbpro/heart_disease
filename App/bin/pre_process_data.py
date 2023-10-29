import pandas as pd
from sklearn.preprocessing import StandardScaler


def process_data(input_line):
    # Carregar o conjunto de dados
    data_path = f'/home/viniciusmb/Projects/python/heart_disease/App/bin/processed.cleveland.data'
    column_names = [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
        'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num'
    ]

    data = pd.read_csv(data_path, names=column_names, na_values=['?'])
    data = data.dropna()
    data = data.drop_duplicates()

    data = data.drop('num',axis=1)

    # adicionar input_line ao conjunto de dados
    data = data.append(input_line, ignore_index=True)

    lst_ohe_feat = ['sex','restecg','slope','fbs','cp','exang','thal','ca']
    lst_ohe_out = [pd.get_dummies(data[i], prefix=i) for i in lst_ohe_feat]
    lst_ohe_out.extend([data['age'], data['trestbps'], data['thalach'], data['chol'], data['oldpeak']])

    data = pd.concat(lst_ohe_out, axis=1)

    scaler = StandardScaler()
    columns_to_scale = ['age', 'trestbps', 'thalach', 'oldpeak']
    data[columns_to_scale] = scaler.fit_transform(data[columns_to_scale])
    
    print(data.info())

    # pegar input_line do conjunto de dados
    input_line = data.iloc[-1]

    # transformar input_line em array 2D
    sample_input = input_line.values.reshape(1, -1)

    return sample_input
