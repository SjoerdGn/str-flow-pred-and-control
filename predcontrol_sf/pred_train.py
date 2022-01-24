import joblib
from sklearn.neural_network import MLPRegressor


def mlp(
    X_train,
    y_train,
    random_state=1,
    max_iter=1000,
    solver="adam",
    alpha=0.001,
    learning_rate="adaptive",
    hidden_layer_sizes=100,
    activation="logistic",
):

    reg = MLPRegressor(
        random_state=random_state,
        max_iter=max_iter,
        solver=solver,
        alpha=alpha,
        learning_rate=learning_rate,
        hidden_layer_sizes=hidden_layer_sizes,
        activation=activation,
    ).fit(X_train, y_train)
    return reg


def save_model(model, path):
    joblib.dump(joblib, path)
