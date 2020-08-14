Context
-------

The aim is to carry out descriptive statistics (mean, std, min, max, quartiles (25%, 50%, 75%) of the extracted features for the two databases:

Audio features
-------------

 The complete list of the implemented features is presented below:

Prosodics features
------
* Duration: The duration of an audio time series, feature matrix, or filename
* Energy: The sum of squares of the signal values, normalized by the respective frame length
* Pitch: The pitch analysis, optimized for speech

Spectrales features
-------
* MFCCs: The Mel Frequency Cepstral Coefficients from a cepstral representation
* LPCs: The coefficients of a linear filter on an audio time series
* Formants: Its performs a short-term spectral analysis, approximating the spectrum of each analysis frame by a number of formants

Voice activity features
------
* ZCR: The rate of sign-changes of the signal during the duration of a particular frame

Voice quality features
-------
* HNR: The degree of acoustic periodicity, also called Harmonics-to-Noise Ratio (HNR)
* Shimmer: The average absolute difference between the amplitudes of consecutive periods, divided by the average amplitude
* Jitter : The average absolute difference between consecutive periods, divided by the average period.


