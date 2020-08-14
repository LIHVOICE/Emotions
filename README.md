
Speech Emotion Classification
=========================

Introduction
------------


The detection of emotions in the voice is an application of recognition
vocal which brings together a set of processes aimed at identifying and classifying the emotions that
contains speech signals. 

As part of the [Colives Diabeties](https://www.colive-diabetes.org/) project, the Digital Epidemiology eHealth of the luxembourg institute of health is implementing this project whose purpose is to create a speech classification system, which recognizes the class (emotion) of this speech. 
 
We use the [RAVLESS](https://zenodo.org/record/1188976#.XrFuWfk6_z5) database which lists eight main emotions: joy, anger, sadness, fear, disgust, surprise, calm, neutral

and the [MELD](https://github.com/declare-lab/MELD) database which lists the same emotions exept calm.

For the conformity of the two bases, this emotion was excluded.
  


This project is based on knowledge from: Audio Signal Processing for Speech,
Machine Learning (ML), Deep Learning.

What Does this Repository Contain
--------------------------------------------------

* Datasets management
* Signal Preprocessing
* Features statistics of the two databases
* Machines learning approaches for each emotion
* Deep learning approaches
    


Dependencies
------------


* Scipy
* Scikit Learn
* Imblearn
* Xgboost
* Joblib
* Librosa
* Spafe
* Parselmouth
* Essentia
* Numpy
* Seaborn
* pandas
* Matplotlib
* Tensorflow
* Keras



```python

```
