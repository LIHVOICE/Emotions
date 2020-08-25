
Speech Emotion Classification
=========================

Introduction
------------


The detection of emotions in the voice is an application of recognition
vocal which brings together a set of processes aimed at identifying and classifying the emotions that
contains speech signals. 

As part of the [Colives Diabeties](https://www.colive-diabetes.org/) project, the Digital Epidemiology eHealth of the luxembourg institute of health is implementing this project whose purpose is to create a speech classification system, which recognizes the class (emotion) of this speech. 
 
We use the [RAVLESS](https://zenodo.org/record/1188976#.XrFuWfk6_z5) database which lists eight main emotions: joy, anger, sadness, fear, disgust, surprise, calm, neutral

and the [MELD](https://github.com/declare-lab/MELD) database ("folder dev") which lists the same emotions exept calm.

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


* Scipy 1.4.1
* Scikit Learn 0.22.2
* Imblearn 0.4.3
* Xgboost 0.90
* Joblib 0.16.0
* Librosa 0.6.3
* Parselmouth 0.3.3
* Essentia 2.1
* Numpy 1.18.5
* Seaborn 0.10.1
* pandas 1.0.5
* Matplotlib 3.2.2
* Tensorflow 2.3.0
* Keras 2.4.3



```python

```
