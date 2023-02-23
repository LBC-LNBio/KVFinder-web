.. _requirements.txt: https://github.com/LBC-LNBio/KVFinder-web-service/blob/master/requirements.txt

.. _http-client:

HTTP client
===========

Besides our interactive graphical clients, we provide an example of a simple Python HTTP client to interact with KVFinder-web service via ``requests`` package. 

This client provides an example of a template in Python that can be run to access our web service and parse the output data. It is composed of two objects: 

- ``KVJob``: create a job using a pdb file with hard-coded parameters;
- ``KVClient``: create the HTTP client with server url and port and methods to run, submit and get results of a job.

Installation
------------

To install the Python dependencies from `requirements.txt`_, run:

.. code-block:: bash
    
    pip3 install -r requirements.txt

Tutorial
--------

First of all, to execute our example of a Python HTTP client, you must import ``http_client`` objects:

.. code-block:: python

    >>> from http_client import KVJob, KVClient

Then, you must create and configure a KVHTTPClient with server url and port.

.. code-block:: python

    >>> client = KVClient("http://kvfinder-web.cnpem.br", path="/api")

With the client created, you must create a job and run it, so run:

.. code-block:: python

    >>> job = KVJob("examples/1FMO.pdb")
    >>> client.run(job)
    {'id': '4990580026958948489', 'status': 'running', 'output': None, 'created_at': '2023-02-17T21:14:46.518650658Z', 'started_at': '2023-02-17T21:14:47.837688140Z', 'ended_at': None, 'expires_after': '1day'}
    Job completed!

After completion, you can print the results or save it to files:

.. code-block:: python

    >>> print(job.report)
    # TOML results file for parKVFinder software
    
    title = "parKVFinder results file"

    [FILES_PATH]
    INPUT = "/jobs/1/protein.pdb"
    OUTPUT = "./KV_Files/KVFinderWeb/KVFinderWeb.KVFinder.output.pdb"
    LIGAND = "./ligand.pdb"

    [PARAMETERS]
    RESOLUTION = "Low"
    STEP_SIZE = 0.60

    [RESULTS]
    # Volume, area and interface residues information for each cavity

        [RESULTS.VOLUME]
        # Volume unit is cubic angstrom
        KAA = 151.85
        KAB = 42.77
        KAC = 60.05
        KAD = 39.96
        KAE = 9.50
        KAF = 529.42
        KAG = 17.28
        KAH = 32.18
        KAI = 44.93
        KAJ = 35.64
        KAK = 9.29
        KAL = 99.58
        KAM = 20.09
        KAN = 7.99
        KAO = 11.23

        [RESULTS.AREA]
        # Area unit is square angstrom
        KAA = 121.32
        KAB = 50.89
        KAC = 58.60
        KAD = 46.49
        KAE = 19.75
        KAF = 460.40
        KAG = 35.16
        KAH = 43.86
        KAI = 54.54
        KAJ = 46.74
        KAK = 19.76
        KAL = 111.94
        KAM = 26.75
        KAN = 16.03
        KAO = 17.33

        [RESULTS.RESIDUES]
        # Interface residues for each cavity
        # ["residue number","chain identifier","residue name"]
        KAA = [["306","E","Y"],["14","E","S"],["15","E","V"],["18","E","F"],["19","E","L"],["100","E","F"],["152","E","L"],["155","E","E"],["156","E","Y"],["292","E","K"],["302","E","W"],["303","E","I"]]
        KAB = [["156","E","Y"],["18","E","F"],["22","E","A"],["25","E","D"],["26","E","F"],["29","E","K"],["97","E","A"],["98","E","V"],["99","E","N"]]
        KAC = [["313","E","P"],["141","E","P"],["142","E","H"],["144","E","R"],["145","E","F"],["148","E","A"],["299","E","T"],["300","E","T"],["305","E","I"],["310","E","V"],["311","E","E"]]
        KAD = [["106","E","L"],["95","E","L"],["98","E","V"],["99","E","N"],["100","E","F"],["103","E","L"],["104","E","V"],["105","E","K"]]
        KAE = [["181","E","Q"],["123","E","V"],["124","E","A"],["125","E","G"],["175","E","D"],["176","E","Q"]]
        KAF = [["327","E","F"],["49","E","L"],["50","E","G"],["51","E","T"],["52","E","G"],["53","E","S"],["54","E","F"],["55","E","G"],["56","E","R"],["57","E","V"],["70","E","A"],["72","E","K"],["74","E","L"],["84","E","Q"],["87","E","H"],["88","E","T"],["91","E","E"],["104","E","V"],["120","E","M"],["121","E","E"],["122","E","Y"],["123","E","V"],["127","E","E"],["166","E","D"],["168","E","K"],["170","E","E"],["171","E","N"],["173","E","L"],["183","E","T"],["184","E","D"],["186","E","G"],["187","E","F"],["200","E","G"],["201","E","T"]]
        KAG = [["314","E","F"],["131","E","H"],["138","E","F"],["142","E","H"],["146","E","Y"],["174","E","I"]]
        KAH = [["350","E","F"],["33","E","P"],["89","E","L"],["92","E","K"],["93","E","R"],["96","E","Q"],["349","E","E"]]
        KAI = [["330","E","Y"],["49","E","L"],["126","E","G"],["127","E","E"],["129","E","F"],["130","E","S"],["326","E","N"],["327","E","F"],["328","E","D"]]
        KAJ = [["336","E","R"],["55","E","G"],["56","E","R"],["73","E","I"],["74","E","L"],["75","E","D"],["115","E","N"],["335","E","I"]]
        KAK = [["217","E","K"],["163","E","I"],["191","E","V"],["193","E","G"],["195","E","T"],["215","E","Y"],["216","E","N"]]
        KAL = [["223","E","A"],["165","E","R"],["166","E","D"],["167","E","L"],["199","E","C"],["200","E","G"],["201","E","T"],["204","E","Y"],["205","E","L"],["206","E","A"],["209","E","I"],["219","E","V"],["220","E","D"],["222","E","W"]]
        KAM = [["273","E","L"],["222","E","W"],["238","E","F"],["253","E","G"],["254","E","K"],["255","E","V"]]
        KAN = [["256","E","R"],["229","E","Y"],["237","E","P"],["238","E","F"],["249","E","K"],["254","E","K"],["255","E","V"]]
        KAO = [["277","E","L"],["207","E","P"],["208","E","E"],["211","E","L"],["213","E","K"],["275","E","V"]]

.. code-block:: python

    >>> print(job.cavity)
    ATOM      1  HS  KAA   259      -6.600 -11.400 -10.800  1.00  0.00
    ATOM      2  H   KAA   259      -6.600 -11.400 -10.200  1.00  0.00
    ...
    ATOM   5146  HS  KAO   259      25.800  -9.600 -10.800  1.00  0.00
    ATOM   5147  HS  KAO   259      26.400  -9.600 -11.400  1.00  0.00

.. code-block:: python

    >>> job.save(cavity="cavity.pdb", report="report.toml", log="job.log")

For more information about our example of a Python HTTP client, the source code is available `here <https://github.com/LBC-LNBio/KVFinder-web-service/blob/master/http_client.py>`_.
