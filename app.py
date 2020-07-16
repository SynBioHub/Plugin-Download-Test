from flask import Flask, request, abort, send_from_directory
import os, shutil

app = Flask(__name__)

@app.route("/status")
def status():
    return("The Download Test Plugin Flask Server is up and running")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json(force=True)
    rdf_type = data['type']
    
    ########## REPLACE THIS SECTION WITH OWN RUN CODE #################
    #uses rdf types
    accepted_types = {'Attachment', 'Collection', 'CombinatorialDerivation',
                      'Component', 'Constraint', 'ExperimentalData',
                      'Implementation', 'Interaction', 'Model', 'prov:Activity',
                      'prov:Agent', 'Sequence', 'SequenceFeature'}
    
    acceptable = rdf_type in accepted_types
    
    # #to ensure it shows up on all pages
    # acceptable = True
    ################## END SECTION ####################################
    
    if acceptable:
        return f'The type sent ({rdf_type}) is an accepted type', 200
    else:
        return f'The type sent ({rdf_type}) is NOT an accepted type', 415

@app.route("/run", methods=["POST"])
def run():
    cwd = os.getcwd()
    
    temp_dir = os.path.join(cwd, "temp_dir")
    
    #remove to temp directory if it exists
    try:
        shutil.rmtree(temp_dir, ignore_errors=True)
    except:
        print("No To_zip exists currently")
    
    #make temp_dir directory
    os.makedirs(temp_dir)
    
    data = request.get_json(force=True)
    url = data['complete_sbol'].replace('/sbol','')
    instance = data['instanceUrl']
    uri = data['top_level']
    
    try:
        ########## REPLACE THIS SECTION WITH OWN RUN CODE #################
        #read in test.html
        filename = os.path.join(cwd, "Test.html")
        with open(filename, 'r') as htmlfile:
            result = htmlfile.read()
            
        #put in the url, uri, and instance given by synbiohub
        result = result.replace("URL_REPLACE", url)
        result = result.replace("URI_REPLACE", uri)
        result = result.replace("INSTANCE_REPLACE", instance)
        result = result.replace("REQUEST_REPLACE", str(data))
        
        #write out file
        out_name = "Out.html"
        filename = os.path.join(cwd, 'temp_dir', out_name)
        with open(filename, 'w') as out_file:
            out_file.write(result)
        
        #this file could be a zip archive or any path and file name relative to temp_dir
        download_file_name = out_name
        ################## END SECTION ####################################
        
        return send_from_directory(temp_dir,download_file_name)
        # return("Hello")
        
        #clear temp_dir directory
        shutil.rmtree(temp_dir, ignore_errors=True)
        
    except Exception as e:
        print(e)
        abort(400)