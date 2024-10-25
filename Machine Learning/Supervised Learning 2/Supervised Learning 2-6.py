# Hyperparameter optimization
# To find the most suitable hyperparameters for a model

  # Hyperparameters are external factors determined by the user, 
    # such as regularization strength or maximum tree depth
  # Parameters are internal factors determined through training, 
    # such as weights in a regression model or feature importance in a tree model
# How these values are set can significantly improve or degrade model performance
# The goal is to optimize the Objective Function
  # Objective Function: value that one has to maximize (score) or minimize (loss, cost)
  # Search Boundary: Defines the exploration range for hyperparameters
  # Step: The interval used during the search process

# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns

from sklearn.model_selection import train_test_split

# Import regression data
df = pd.read_csv('/path/boston.csv') 
df

# Handling missing values
df['ZN'] = df['ZN'].fillna(0) 
df['CHAS'] = df['CHAS'].fillna(0)

# Remove unnecessary column
df.drop('Unnamed: 0', axis=1, inplace=True) 
df

# Separate data
X = df.loc[:, 'CRIM':'LSTAT'] 
Y = df['target']

# Split data
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0)

# Grid Search
# sklearn.model_selection.GridSearchCV
# A simple and widely used hyperparameter search algorithm 
# explores all possible combinations of the defined ranges and steps
# Wider Ranges and Smaller Steps: The broader the range and the smaller the step, the higher the likelihood of finding the optimal solution; however, this approach can be time-consuming
# Common Practice: Typically, a broad range and larger steps are set initially, and then the range is narrowed down to reduce time

from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor() # 실험에 사용할 모델 생성

params = {
'random_state' : [0],
'n_estimators': [100, 300, 500, 1000], 'learning_rate': [0.1, 0.01, 0.001]
} # Set the range for the parameters to be experimented with

from sklearn.model_selection import GridSearchCV
gs = GridSearchCV(model, params).fit(x_train, y_train) # Experiment all possible combination

# Query experiment result (dict format)
gs.cv_results_

# Query experiment result (DataFrame format)
pd.DataFrame(gs.cv_results_)

# Query best performance score
gs.best_score_

# Query best performance parameters
gs.best_params_

# Query best performance model
gs.best_estimator_

# GradientBoostingRegressor
# GradientBoostingRegressor(learning_rate=0.01, n_estimators=1000, random_state=0)

# Evaluate best performance model
gs.best_estimator_.score(x_test, y_test)

# Random Search
# sklearn.model_selection.RandomizedSearchCV
# Randomly select within the defined range
# This method is generally faster and more efficient than Grid Search, making it the preferred option
# Faster than Grid Search, but may not guarantee an optimized solution
# If the number of samples is large, using random sampling increases the likelihood of finding the optimal solution

from sklearn.model_selection import RandomizedSearchCV
rs = RandomizedSearchCV(model, params).fit(x_train, y_train) # Expriment all possible combination

# Query experiment result (DataFrame format)
pd.DataFrame(rs.cv_results_)

# Bayesian Optimization
# Grid Search and Random Search are independent of each other in their respective search processes
  # They do not use information from each other
# Therefore, the values found cannot be assumed to be optimal
# A model based on Gausain Process statistics that, when applied to multiple hyperparameters with an acquisition function, identifies points where the probability of obtaining the largest value is highest
# It learns the 'shape' of the objective function.
  # Prior Distribution: Based on this, a single exploration function is assumed
  # Exploration: When testing the objective function with new sampling each time, this information is used to update the prior distribution of the new objective function
  # Exploitation: The algorithm tests at locations indicated by the posterior distribution, where there is a high likelihood of finding the global minimum

!pip install optuna plotly

from sklearn.metrics import mean_squared_error
def objective(trial): params = {
  'n_estimators' : trial.suggest_int('n_estimators', 100, 1000),
  'max_depth' : trial.suggest_int('max_depth', 1, 10),
  'ccp_alpha': trial.suggest_discrete_uniform('ccp_alpha', 0.1, 1, 0.1),
  'random_state': 0
}
  
model = GradientBoostingRegressor(**params)
model.fit(x_train, y_train)

return mean_squared_error(y_test, model.predict(x_test))

import optuna

study = optuna.create_study(
  study_name="boston_rfr_opt",
  direction='minimize', # minimize : minimalization, maximize : maximalization 
  sampler=optuna.samplers.TPESampler()
)

study.optimize(objective, n_trials=100)

print(f'Maximum Performance {study.best_trial.values[0]}') 
print('Maximum Performance Parameter')
for key, value in study.best_trial.params.items():
  print(f'  {key}:{value}')

# Visualising optimizaiton result
# Optimization History Plot
optuna.visualization.plot_optimization_history(study)

# Parallel Coordinate Plot
optuna.visualization.plot_parallel_coordinate(study)

# Hyperparameter Importances
optuna.visualization.plot_param_importances(study)

