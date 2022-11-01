# Overview

This is a project on predicting Data Science and STEM Salaries. This is done as part of the Machine Learning Engineering course held by Alexey Grigorev.
Credits to Jack Ogozaly for scraping the dataset from level.fyi!
If you want to see the original dataset on kaggle, look at it here: [Dataset](https://www.kaggle.com/jackogozaly/data-science-and-stem-salaries)

## Problem description

There is a lot of variation with regards to Data Science and STEM salaries, ranging from the location that one is based in, to the company one is based in.
Moreover, it is not very convenient to find this information on the internet, with some platforms gatekeeping information about salary.
Therefore, this model takes these variables and conveniently predicts the salary that you'll receive with said variables.

## Contents of the folder

The data folder consists of the original dataset, as well as the cleaned dataset.

The code folder consists of:

<ul>
<li> Data Cleaning & EDA - part of the notebook </li>
<li> Training of model & Hyperparameter Tuning (output & outputless)* - part of notebook </li>
<li> train.py - to train the final model + saving it using pickle </li>
<li> predict.py - to load the model and serve it via a web service </li>
<li> predict-test.py and predict-test-cloud.py - to test the output of the model, depending on where you want to use it </li>
<li> pipenv and pipenv.lock for the virtunal environment using pipenv </li>
<li> Dockerfile for using a Docker container </li>
</ul>
