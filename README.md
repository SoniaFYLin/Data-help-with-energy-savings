
### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>
The code should run on Jupyter Notebook using Python versions 3.*. The used libraeies includes Numpy, pandas, Scikit-Learn, TensorFlow, keras, seaborn and matplotlib.   

## Project Motivation<a name="motivation"></a>

Climate change is a global revelant urgant issue that might change our daily life in the short future. Green House Gas(GHG) emission is one of the most important impacts that needs to be mitigated. According to a report issued by the International Energy Agency(IEA), the lifecycle of buildings from construction to demolition were responsible for 37% of global energy emmisions in 2020. Find the more energy comsumption buildings to save energy is an efficent way to help with reducing GHG emission and cost saving. The energy usage for the building and the given year, measured as Site Energy Usage Intensity(Site EUI). Accurate prediction of Site EUI can help policymakers to target the buildings that might maximizie the emission reductions to retrofit them.

In this project, I was interested in knowing what are the cruicial impact factors for energy comsumption of a building and use this information to predict an accurate Site EUI for each building. Below are the particular business questions which can be answered using this dataset. 

1. Are those commercial buildings consumimg more energy comsumptions than residential buildings?
2. Should we consider the priority of retrofitting for older buildings in order to eliminate the waste of energy more efficiently
3. What are the top crucial impact factors for the energy consumption of the buildings based on the observations of data?

The full set of files related to this project is from the WiDS Datathon 2022.


## File Descriptions <a name="files"></a>

There are 3 notebooks available here to showcase work related to the above questions.  Each of the notebooks is exploratory in searching through the data pertaining to the questions showcased by the notebook title.  Markdown cells were used to assist in walking through the thought process for individual steps.  

1) break_into_data_building_and_facility_types.ipynb
   - This file breaks into the details of data types, size of features and provides an analysis details to answer the first question listed above.
2) missing_value_handling_and_year_built.ipynb
   - This file looks into the missing values of each columns and handles each missing features based on their missing propotion and correlations. In addition, the analysis results of 'year_built' column answer the second question listed above. 
3) ML_model-feature_importance.ipyng
   - This file shows the analyses of features importances based on different machine learning models and correlation.

There is an additional file `ManipulateCategory.py`that runs the necessary code to help handle categorical data.

## Results<a name="results"></a>
#### Handle categorical data and missing data
- Finding_1: There are three columns with categorical data which will need to be converted to numerical data type. 
- Finding_2: There are six features with missing values and all of them are numerical data type. 
- Finding_3: year_built has only 2% missing in training data and 0.9% missing in test data. It can be suggested to be filled using mode because the data of 'year_built' shows a left-skewed distribution.
- Finding_4: The correlation of energy_star_rating and site_eui is high. Even this column has 20-30% missing on both training and test datasets, it will needs to be imputed properly.
- Finding_5: The rest of four features, 'days_with_fog', 'direction_max_wind_speed', 'max_wind_speed', 'direction_peak_wind_speed' have high missing rate in both training and test datasets so they should be dropped safely.

#### Question 1: Are those commercial buildings consuming more energy consumptions than residential buildings?
- Finding_1: The average site_eui of commercial buildings is about 7% slightly higher than that of residential buildings. However, the commercial building and residential buildings seems have different behaviors when we break into the different type of facilities. 
- Finding_2: Residential builidings do not have significant difference on site_eui based on different facility types.  Only the buildings that mixed used with the commercial purposes consume slightly more energy.
- Finding_3: Commercial buildings have significant different behavior based on different facility. Some of the types building have significant large or small energy consumption. For instance, the data center, labortory, health_cares and grocery stores institutes have extremely high energy usage, but the warehouses or religion facilities consume less energy. 

#### Question 2: Should we consider the priority of retrofitting for older buildings in order to eliminate the waste of energy more efficiently?
- Finding_1: The means of site_eui have significantly fluctuation year by year before 1900 because here are not many data each year. 
- Finding_2: The means of site_eui didn't show a clear trend based on the year_built for training data 
- Finding_3: If we separate the Residential buildings and Commercial buildings, the Residential buildings have a clear trend of energy usage decrease along the year of built, in particular, after 2000s. However, the data from commercial buildings doesn’t should the same trend. This may due to the many outliers on ‘site_eui’ based on their facility types.

#### Question 3: What are the top crucial impact factors for the energy consumption of the buildings based on the observation of data? 
- Finding_1: ‘energy_star_rating’ is very important for the ‘site_eui’ prediction in most of the machine learning models. In particular, it represented as the top importance feature in Correlation, Random Forest and Neural network models.
- Finding_2: The top 10 important features are mostly related to facility_type. It indicates the facility_type is very important for site_eui prediction.
- Finding_3: A couple of important features are associated to the State_Factor. The ‘State_Factor’ feature is worth to be discussed further.











The main findings of the code can be found at the post available [here](https://medium.com/@admost0118/eliminate-green-house-emission-data-can-help-4eac80bdf250).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to WiDS Datathin 2020 for the data.  You can find the Licensing for the data and other descriptive information at the Kaggle link available [here](https://www.kaggle.com/c/widsdatathon2022/data).

