from urllib.request import urlopen
import json
import subprocess, shlex

allProjects     = urlopen("https://git.developers.burberry.com/api/v3/projects?private_token=8i-wiTydb4kThCGmkAaE")
allProjectsDict = json.loads(allProjects.read().decode())
[for thisProject in allProjectsDict if thisProject['namespace']['name'] == ]: 
    try:
        thisProjectURL  = thisProject['ssh_url_to_repo']
        command='git clone ' +thisProjectURL
        # command     = shlex.split('git clone %s' % thisProjectURL)
        resultCode  = subprocess.Popen(command)
        print (command)

    except Exception as e:
        print("Error on %s: %s" % (thisProjectURL, e.strerror))