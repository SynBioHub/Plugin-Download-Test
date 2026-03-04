# Plugin-Download-Test
A very small test plugin to test the download interface is working for SynBioHub. Could be the basis for python based download plugins. You can use this repo as a template.

# Install
## Using docker
Run `docker run --publish 8089:5000 --detach --name python-test-plug synbiohub/plugin-download-test:snapshot`
Check it is up using localhost:8089.

## Using Python
Run `pip install -r requirements.txt` to install the requirements. Then run `FLASK_APP=app python -m flask run --port 5000`. A flask module will run at localhost:5000/.  
