
Unzip starting_kit.zip:

```
unzip starting_kit.zip
```


# To participate

All you need to do is to modify sample_code_submission/model.py:
* Define your neural architecture in `__init__` method
* (if necessary) Preprocess your data in `fit` and `predict` method
* Play with the number of epoch in `fit` method

In order to test your code, you can:


### 1- Use bash/shell command

Training is done with the following command in codalab
```bash
cd ingestion_program
python ingestion.py
```

It will generate prediction for train, valid, test set. To see you local score (train, valid), run the following command:
```bash
cd scoring_program/
python score.py
```


### 2- Use jupyter notebook

Run `jupyter notebook` in your terminal then open `Readme.ipynb`.
<b>Set your kernel into `DSA`</b> before running cells.



# Tips to improve your score

Non-exhaustive idea that can improve your score. Please remember that training time is limited to 300sec (it may change).
* Adding more CNN layers
* Adding more epoch
* (if you have time) Data augmentation using skimage (Ex: https://gist.github.com/tomahim/9ef72befd43f5c106e592425453cb6ae)
