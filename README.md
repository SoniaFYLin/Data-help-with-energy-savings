
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

1. Do those commercial buildings usually consume more energy than residential buildings?
2. Should we consider to restrofit older buildings to eliminate the waste of energy?
3. What factors are the top3 cruicial impact factors for the energy comsumption of the buildings?

The full set of files related to this project is from the WiDS Datathon 2022.


## File Descriptions <a name="files"></a>

There are 3 notebooks available here to showcase work related to the above questions.  Each of the notebooks is exploratory in searching through the data pertaining to the questions showcased by the notebook title.  Markdown cells were used to assist in walking through the thought process for individual steps.  

1) break_into_data_building_and_facility_types.jynb
2) missing_value_handling_and_year_built
3) ML_model-feature_importance

There is an additional `.py` file that runs the necessary code to help handle categorical data.

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://medium.com/@josh_2774/how-do-you-become-a-developer-5ef1c1c68711).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to WiDS Datathin 2020 for the data.  You can find the Licensing for the data and other descriptive information at the Kaggle link available [here](https://www.kaggle.com/stackoverflow/so-survey-2017/data). 

