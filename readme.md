# ClusterCompare: Comparative Behavioral Data Analysis Library

ClusterCompare is a Python library designed for comparative analysis of behavioral data. It provides a convenient and efficient way to analyze and compare behavioral patterns within different populations or datasets.

## Features

- **Data Initialization**: Easily initialize ClusterCompare by providing population data, target data, behavior columns, and optional parameters like key column and target match indicator.
  
  ```python
  cc_instance = CC(population_data, target_data, ['behavior1', 'behavior2'])

# ClusterCompare: Comparative Behavioral Data Analysis Library

ClusterCompare is a Python library designed for comparative analysis of behavioral data. It provides a convenient and efficient way to analyze and compare behavioral patterns within different populations or datasets.

## Features

- **Data Initialization**: Easily initialize ClusterCompare by providing population data, target data, behavior columns, and optional parameters like key column and target match indicator.
  
  ```python
  cc_instance = CC(population_data, target_data, ['behavior1', 'behavior2'])

- **Analysis**: Perform in-depth analysis of behaviors within the given data using the analyse() method.
    ```python
    cc_instance.analyse()
    cc_name, analysis_data = cc_instance.getAnalysis()

- **Comparative Analysis**: Compare behavioral data between different instances of ClusterCompare.

    ```python
    cc_list = [cc_instance1, cc_instance2, cc_instance3]
    compare_data = cc_instance.compare(cc_list)

- **Feature Selection**: Filter the comparative dataset based on specific thresholds.

    ```python
    thresholds = [0.5, 0.7, 0.8]  # Example thresholds
    filtered_data = cc_instance.getFeatures(thresholds)

- **Access Original Data**: Retrieve the original merged dataset for further analysis.

    ```python
    original_data = cc_instance.getDataset()
