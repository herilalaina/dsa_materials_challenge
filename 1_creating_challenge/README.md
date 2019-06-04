This is a template that help for creating a challenge in Codalab.

To create a challenge, you need to follow theses steps:
* Get your data then split it in train, valid, test (ex in `sample_data`)
* Create a baseline that works (ex in `sample_code_submission/model.py`)
* Create a description of your challenge (ex in `html_pages`)
* Define how to read your data, train your baseline and make a prediction (ex in `ingestion_program/ingestion.py`)
* Define your metric in `scoring_program/metric.txt`
* Complete `utilities/competition.yaml`

To create a bundle of your challenge, run:
```bash
cd utilities
python make_bundles.py
```

It will generate a bundle that can be uploaded to the platform (ex. codalab.lri.fr or your own codalab server).
