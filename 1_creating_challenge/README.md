This is a sample starting kit for the Data Science Africa challenge.
It uses the Microscopy dataset from http://air.ug/microscopy/.

Prerequisites:
Install Anaconda Python 3.6.6, Tensorflow (2.0.0), opencv-python (4.0.1), scikit-image (0.15.0)

or

run your code within the Codalab docker (inside the docker, python 3.6 is called python3):

	`docker run -it -p 8888:8888 -v `pwd`:/home/aux herilalaina/dsa:2.0`

	`DockerPrompt# cd /home/aux`
	`DockerPrompt# python3 ingestion_program/ingestion.py sample_data sample_result_submission ingestion_program sample_code_submission`
	`DockerPrompt# python3 scoring_program/score.py sample_data sample_result_submission scoring_output`
	`DockerPrompt# exit`



Usage:
- The two files sample_*_submission.zip are sample submissions ready to go!

- The file README.ipynb contains step-by-step instructions on how to create a sample submission for the challenge.
At the prompt type:
jupyter-notebook README.ipynb

- modify sample_code_submission to provide a better model

- zip the contents of sample_code_submission (without the directory, but with metadata), or

- download the public_data and run (double check you are running the correct version of python):

  `python ingestion_program/ingestion.py public_data sample_result_submission ingestion_program sample_code_submission`

then zip the contents of sample_result_submission (without the directory).

