from src.prepocess import add_two_to_sepal_length, read_json_file
from src.train import evaluate_lr_model, split_data, train_lr_model


if __name__ == "__main__":

    file_path = "data/iris.json"
    file_store = "data/iris.json"
    # file_store = "data/iris_v2.json"

    # data = read_json_file(file_path)
    # print(f"Data Loaded:\n{data.head()}")
    # data_transform = add_two_to_sepal_length(file_path,file_store) 
    # print(f"Data Transformed and Stored:\n{data_transform.head()}")

    X_train, X_test, y_train, y_test = split_data(file_path)

    lr_model = train_lr_model(X_train,y_train)
    y_pred = lr_model.predict(X_test)
    acc = evaluate_lr_model(y_pred,y_test)
    print(f"Accuracy : {acc}")