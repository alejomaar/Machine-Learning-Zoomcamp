#### Motivation

In the age of data and machine learning, information may not be as anonymous as you think. Your identity and characteristics may be revealed if other information about you is obtained. This project looks at how a personality test can reveal your male or female gender.

# Overview

This project is based on 10 questions, about personal preferences of each person. For each question, a user will answer agree or disagree on a scale of 1 to 5. The challenge of this project is that at the end of the test, the ml algorithm can predict the user's gender.

## Business context

Good morning recruit! It's good to have you here! In our company PSYCAR needs to collect demographic information about our customers. For legal reasons we cannot collect the name or gender of the person, but we can collect any other type of information.

We need you to build a personality test, to understand if the person who answered it is male or female, since we need this information for our next marketing campaign.

Just be careful not to design a very long quiz, as the user might abandon it.

Thanks,

Mr McManager

## Contents of the folder

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
