# automlk
Automated and distributed machine learning toolkit
--------------------------------------------------

This toolkit is designed to be integrated within a python project, but also independently through the interface of the app.

The framework is designed with similar principles than auto-sklearn, with the following improvements:
- web interface (flask) to review the datasets, the search results and graphs
- distributed architecture with multiple search workers
- include sklearn models, but also Xgboost, LightGBM, CatBoost and keras Neural Networks
- 2nd level ensembling with model selection and stacking
- can be used in competition mode (to generate a submit file from a test set), on public mode (separate train set and public set) and standard mode.

We have provided some public datasets to initialize the framework and compare results with best scores.

Find the documentation [here](http://automlk.readthedocs.io/en/latest/)

Usage:
-----
- create a dataset
- launch the search in auto mode: this will search the best pre-processing steps, machine learning models and ensembles
- review the results through with the web interface


Requirements:
------------
- category_encoders

optional:
- lightGBM
- Xgboost
- Catboost
- Keras with Theano or Tensorflow

- Redis (for in memory key/value storage and queues)

Installation:
------------
download and then install:

.. code-block:: python

    python setup.py install

References:
----------
Feurer, Matthias, et al. "Efficient and robust automated machine learning." Advances in Neural Information Processing Systems. 2015.
