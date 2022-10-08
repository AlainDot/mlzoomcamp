08/10/2022

	- Fresh installation of python from internet
		python-3.9.11-amd64.exe

	- Reboot
	
	- Check where is python
		> python WhereIsPythonG.py

	- Create project directory (for the project without Conda!!)
		C:\Users\alain\Documents\prv\IT\mlzc\ProNoCnd

	- run in CMD (as ADMIN !!)
		pip install --upgrade pip
		pip install pipenv
		
		pipenv install numpy scikit-learn==1.0.2 flask waitress requests
		
		pipenv --env
		
    - run application:
		pipenv shell
		python predict.py
		
	- test application	
		pipenv shell
		python test_predict.py
		
	- In Win CMD:
		> cd C:\Users\alain\Documents\prv\IT\mlzc\ProNoCnd
		> docker build -t card-prediction-alain .
		> docker run -it -p 9696:9696 card-prediction-alain:latest     	
