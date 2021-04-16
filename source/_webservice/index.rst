Overview
========

KVFinder-web service is a RESTful web service that runs `parKVFinder <https://github.com/LBC-LNBio/parKVFinder>`_ software to detect and chacterize cavities. The web service has Web-Queue-Worker architecture style and each of these modules is built in a separated Docker container, making available to execute on different platforms and Cloud services. 

The web server module receives HTTP POST requests in JSON. If the request is valid, it returns a response with an unique id. Otherwise, it returns an HTTP error code with an error message. This id is create by the web server that applies a hash function into the received data, which include detection parameters and the molecular structures. 

The queue module uses Ocypod software to managed accepted jobs sent by the web server module. 

The worker module communicate with queue module, requesting "queued" jobs, that will be processed with parKVFinder software. After completion, the job results are sent back to the queue module and made available to the client via the web server module. The client must send a HTTP request with an id and the web server module returns "queued", "running", or "completed" together with its respective results. 

Web service configuration
=========================

The web service has a Job timeout of **30 minutes** (maximum time that a accepted job could run on the KVFinder-web service), completed jobs will be available on the web service up to **1 day** after completion, and the maximum payload (maximum size of the JSON) of the data sent to the KVFinder-web service is **1 Mb**.

Further, the KVFinder-web service has some limitations, compared to a local installation of parKVFinder, that are:

    - Cavity representation will be always filtered (cavity files will consume less space on the web service);
    - The custom box (Box adjustment mode) cannot be much bigger than the 3D grid in order to avoid unnecessary calculations;
    - The grid spacing must be 0.6 A to avoid unnecessary time-consuming jobs;
    - The Probe In and Probe Out sizes must be smaller than to 5 and 50 A, respectively, to avoid unnecessary time-consuming jobs;
    - The Removal distance is limited must be smaller than 10 A to avoid unnecessary time-consuming jobs.

.. note:: 

    If users are creating a locally configured KVFinder-web service, these limitation could be lifted from the source code.

Publicly available KVFinder-web service
=======================================

We provide a publicly available KVFinder-web service (http://parkvfinder.cnpem.br), running in a Cloud environment. Hence, users may opt to run jobs on our public KVFinder-web service or on a locally configured server.

Local installation
==================

To run the KVFinder-web service in Linux distributions, it is necessary to install docker-compose and its dependencies. To install it:

.. code-block:: bash

    sudo apt install docker-compose

.. note::

    Users can use their preferred package manager to install ``docker-compose`` tool.

After the docker-compose installation and copy/clone of this repository. To start KVFinder-web service, you can execute the command bellow at the root  of KVFinder-web-service repository (where docker-compose.yml file is located):

.. code-block:: bash
    
    docker-compose up

To start the KVFinder-web service in background:

.. code-block:: bash
    
    docker-compose up -d

To interrupt an active KVFinder-web service instance, run:

.. code-block:: bash
    
    docker-compose down

To stop and erase the volumes that store the queue module data and the job folders and files, run:

.. code-block:: bash

    docker-compose down --volumes

The KVFinder-web service uses port 8081 by default. If the local installation was successfully, the locally configured KVFinder-web service is available at: http://localhost:8081. If you access the url on a browser, it should display a text message like: "KVFinder Web".

The queue information can be accessed at: http://localhost:8023/info.

To use the PyMOL KVFinder-web Tools, users must change the server url and port hardcoded on the `__init__.py <https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools/blob/main/PyMOL-KVFinder-web-tools/__init__.py>`_ file and reinstall the client plugin on PyMOL.

From:

.. code-block:: bash

    # Server                                 #
    server = "http://parkvfinder.cnpem.br"   #
    # Port                                   #
    port = "8081"                            #

to:

.. code-block:: bash

    # Server                                 #
    server = "http://localhost"              #
    # Port                                   #
    port = "8081"                            #

.. note:: 

    If the KVFinder-web service is on another computer on your network, you must provide the IP Address instead of localhost.

Extra configuration
-------------------

After changes in the source code, the containers must be rebuild.

.. code-block:: bash
    
    docker-compose build

or

.. code-block:: bash

    docker-compose up --build

To start more than one worker module and thus make KVFinder-web service capable of running more than one job simultaneously. For instance, to start with two worker modules:

.. code-block:: bash

    docker-compose up --scale kv-worker=2

API reference
=============

- Create a job: POST /create
    
    - Method: POST
    - Media type: application/json
    - URL: http://localthost:8081/create

Example of job request:

.. code-block:: json

    {
        "pdb": [
            "MODEL        1\n",
            "ATOM      1  N   GLU E  13      -6.693 -15.642 -14.858  1.00100.00           N  \n",
            "(...)",
            "END\n"
        ],
        "settings": {
            "modes": {
            "whole_protein_mode": true,
            "box_mode": false,
            "resolution_mode": "Low",
            "surface_mode": true,
            "kvp_mode": false,
            "ligand_mode": false
            },
            "step_size": {
            "step_size": 0.0
            },
            "probes": {
            "probe_in": 1.4,
            "probe_out": 4.0
            },
            "cutoffs": {
            "volume_cutoff": 5.0,
            "ligand_cutoff": 5.0,
            "removal_distance": 0.0
            },
            "visiblebox": {
            "p1": { "x": 0.0, "y": 0.0, "z": 0.0 },
            "p2": { "x": 0.0, "y": 0.0, "z": 0.0 },
            "p3": { "x": 0.0, "y": 0.0, "z": 0.0 },
            "p4": { "x": 0.0, "y": 0.0, "z": 0.0 }
            },
            "internalbox": {
            "p1": { "x": -4.0, "y": -4.0, "z": -4.0 },
            "p2": { "x": 4.0, "y": -4.0, "z": -4.0 },
            "p3": { "x": -4.0, "y": 4.0, "z": -4.0 },
            "p4": { "x": -4.0, "y": -4.0, "z": 4.0 }
            }
        }
    }

- Request a job: GET /:id

    - Method: GET
    - URL: http://localhost:8081/:id, where *:id* is the job id received from the web server as submission response.

Example of response obtained for a *job* with status "completed":

.. code-block:: json

    {
        "id": "17275205978013541183",
        "status": "completed",
        "output": {
            "pdb_kv": "ATOM      1  HS  KAA   259     -15.000 -10.200   0.000  1.00  0.00\nATOM      2(...)",
            "report": "# TOML results file for parKVFinder software\n\ntitle = \"parKVFinder results f(...)",
            "log": "==========\tSTART\tRUN\t=========\n\nDate and time: Fri Apr 16 11:40:06 2021\n\nRu(...)",
        },
        "created_at": "2021-04-16T11:40:02.514045822Z",
        "started_at": "2021-04-16T11:40:06.671064517Z",
        "ended_at": "2021-04-16T11:40:17.701426882Z",
        "expires_after": "1day"
    }

.. note:: 

    If the KVFinder-web service is on another computer on your network, you must provide the IP Address instead of localhost.
