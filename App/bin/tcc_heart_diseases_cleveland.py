# flake8: noqa
import os
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, GridSearchCV
from sklearn.metrics import accuracy_score, log_loss, precision_score, recall_score, f1_score
from joblib import dump, load


class HeartDiseaseClassifier:
    def __init__(self):
        self.data = pd.read_csv("cleveland_database.csv")
        self.X = self.data.drop(['condition'], axis=1).copy()
        self.y = self.data['condition'].copy()
        self.X_encoded = pd.get_dummies(
            self.X, columns=['cp', 'restecg', 'slope', 'thal'], dtype=int)

    def train_decision_tree(self):
        # Dividir os dados em treinamento e teste
        X_train, X_test, y_train, y_test = train_test_split(
            self.X_encoded, self.y, random_state=42)

        # Treinar o modelo Decision Tree
        dtc = DecisionTreeClassifier(random_state=42)
        dtc.fit(X_train, y_train)
        return dtc

    def prune_decision_tree(self, dtc):
        # Prune the decision tree
        # Implementar a poda da árvore de decisão
        # ...
        pass

    def grid_search_decision_tree(self):
        # Realizar busca em grid para Decision Tree
        # Implementar a busca em grid para encontrar os melhores hiperparâmetros
        # ...
        pass

    def train_random_forest(self):
        # Treinar o modelo Random Forest
        rf = RandomForestClassifier(random_state=23)
        rf.fit(self.X_encoded, self.y)
        return rf

    def grid_search_random_forest(self):
        # Realizar busca em grid para Random Forest
        kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=23)
        rf = RandomForestClassifier(random_state=23)  # Definir rf aqui
        params = {'max_features': [2, 3, 4, 5, 6, 7]}
        gcv_rf = GridSearchCV(rf, param_grid=params, verbose=3,
                              cv=kfold, scoring='neg_log_loss')
        gcv_rf.fit(self.X_encoded, self.y)
        print("Best Parameters:", gcv_rf.best_params_)
        print("Best Log Loss Score:", gcv_rf.best_score_)
        best_clf = gcv_rf.best_estimator_
        return best_clf

    def evaluate_model(self, model, X_test, y_test):
        # Avaliar o modelo usando métricas
        y_pred = model.predict(X_test)
        y_pred_prob = model.predict_proba(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        logloss = log_loss(y_test, y_pred_prob)
        return accuracy, logloss

    def save_model(self, model, filename):
        # Salvar o modelo usando joblib
        dump(model, filename)
        print(f"Model saved as '{filename}'")

    def load_model(self, filename):
        # Carregar o modelo usando joblib
        return load(filename)

    def predict_with_loaded_model(self, loaded_model, sample_input):
        # Fazer previsões usando o modelo carregado
        prediction = loaded_model.predict([sample_input])
        prediction_proba = loaded_model.predict_proba([sample_input])
        return prediction, prediction_proba


def main():
    # Criar uma instância do classificador
    heart_classifier = HeartDiseaseClassifier()

    # Treinar um Decision Tree
    dtc_model = heart_classifier.train_decision_tree()
    dtc_pruned = heart_classifier.prune_decision_tree(dtc_model)
    dtc_best = heart_classifier.grid_search_decision_tree()

    # Treinar um Random Forest
    rf_model = heart_classifier.train_random_forest()
    rf_best = heart_classifier.grid_search_random_forest()

    # Divisão de dados de treinamento e teste (70% treinamento, 30% teste)
    X_train, X_test, y_train, y_test = train_test_split(
        heart_classifier.X_encoded, heart_classifier.y, test_size=0.3, random_state=42)

    # Avaliar o modelo Random Forest no conjunto de teste
    accuracy, logloss = heart_classifier.evaluate_model(
        rf_best, X_test, y_test)
    print("Random Forest Evaluation:")
    print("Accuracy:", accuracy)
    print("Log Loss:", logloss)

    # Calcular precisão, recall e F1-score
    y_pred = rf_best.predict(X_test)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-Score:", f1)

    # Salvar o modelo treinado
    model_filename = 'best_random_forest_model.joblib'
    heart_classifier.save_model(rf_best, model_filename)

    # Carregar o modelo e fazer previsões
    loaded_model = heart_classifier.load_model(model_filename)
    sample_input = np.array([...])  # Preencher com seus dados de entrada
    prediction, prediction_proba = heart_classifier.predict_with_loaded_model(
        loaded_model, sample_input)
    print("Loaded Model Prediction:", prediction)
    print("Loaded Model Probabilities:", prediction_proba)


if __name__ == "__main__":
    main()
