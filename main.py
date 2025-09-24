from src.prepocess import add_two_to_sepal_length, read_json_file


if __name__ == "__main__":

    file_path = "data/iris.json"

    data = read_json_file(file_path)
    print(f"Data Loaded:\n{data.head()}")
    data_transform = add_two_to_sepal_length(file_path) 
    print(f"Data Transformed and Stored:\n{data_transform.head()}")