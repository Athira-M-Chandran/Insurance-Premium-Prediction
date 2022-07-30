# Insurance-Premium-Prediction
The goal of this project is to give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. This can assist a person in concentrating on the health side of an insurance policy rather than the ineffective part.

### Conda Environment

Creating conda enivronment
```
conda create -p venv python==3.7 -y
```
Activate conda environment
```
conda init.exe
conda activate venv/
```
### Requirements

write libraries to install in requirements.txt

create and run setup.py (Project name, version, author etc.)
```
python setup.py install
```

### GIT commands
To Add files to git
```
git add .
```
OR
```
git add <file_name>
```
 
> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
To check all version maintained by git
```
git log
```
To create version/commit all changes by git
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main
```
To check remote url
```
git remote -v
```

### To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = athiramchandran90@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = <>


### BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

To list docker image
```
docker images
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```
To check running container in docker
```
docker ps
```
To stop docker conatiner
```
docker stop <container_id>
```

### Install ipkernel
```
pip install ipykernel
```

**Data Drift: When your datset stats gets change we call it as data drift**

### Flow


1. Initialize current timestamp in constant
2. Then start with logger (to track) and Exception( To Handle if unexpected thing happen)

3. Define the structure in config_enity.py
> Framing the requirements for the configuration

4. Create config.yaml and util.py
> yaml file is more readable compared to json file. util file is similar to helper function. It is a not a part of pipeline but may required in pipeline files. It is like how to load pickle object, yaml file 

5. constant.py
> Like initialize the filenames and foldernames

6. configuration.py
> Will create informations to create folders

7. artifact_enitity.py
> the output file paths

8. data_ingestion.py
> download data and split it into train and test data

9. pipeline.py
10. 
