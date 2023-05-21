# Artist Web Application


## Description 
Django artist application is a web application built using the Django framework. It allows the users to manage and showcase information about
the artists such as Tours and Albums.Users can register and login to the webiste.

This README.md file provides instructions on how to build and run your application on different operating systems.

## Prerequisites
- Python (version X.X.X)
- Docker (version X.X.X)

## Installation

### Cloning the Repository
1. Clone the repository to your local machine:

```
git clone https://github.com/moeketsisegalo/capstone_project_consolidation.git
```


### A NOTE FOR LINUX AND MAC
In order to get your commands working, there are certain commands that need to run when opening your terminal.

### For MacOS, place the following in your ~/.zshrc:


### Setting PATH for Python 3 installed by brew if it is not present

```
export PATH=/usr/local/share/python:$PATH
```
### Configuration for virtualenv
```
export WORKON_HOME=$HOME/.virtualenvs
```
```
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
```
```
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
```
```
source /usr/local/bin/virtualenvwrapper.sh
```



### Setting Up a Virtual Environment (venv)
1. Open a command prompt or terminal.
2. Navigate to the project's root directory.
3. Create a new virtual environment:
- For Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- For Mac/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

### Installing Dependencies
1. Ensure that your virtual environment is active.
2. Install the project's dependencies using pip:
pip install -r requirements.txt


## Running the Application

### Running with venv
1. Ensure that your virtual environment is active.
2. Start the Django development server:
python manage.py runserver

3. Access your application at http://localhost:8000/.

### Running with Docker
1. Build the Docker image:

docker build -t artist-app .

2. Run the Docker container:
docker run -p 8000:8000 artist-app

3. Access your application at http://localhost:8000/.

## Configuration
- The application may require additional configuration depending on your specific environment. Please refer to the project's documentation for detailed instructions.

## Contributing
- If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make changes and commit them: `git commit -am "Add your changes"`.
4. Push the branch to your forked repository: `git push origin feature/your-feature-name`.
5. Submit a pull request.

## License
- Include your license information here.
