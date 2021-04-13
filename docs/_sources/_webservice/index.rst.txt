Overview
========

KVFinder-web server has Web-Queue-Worker architecture style and each of these modules is built in a separated Docker container. 

The Web component receives jobs requests in JSON format with detection parameters. If the request is valid, it returns a response with a unique id, based on the provided parameters, corresponding to the accepted job to the client. Otherwise, it returns an HTTP error code with an error message. The client must send a request with an id and the Web component returns "queued", "running" or "completed" together with the respective results. 

The Queue component uses Ocypod software that receives jobs accepted by the Web component. 

The Worker component communicate with Queue component, requesting "queued" jobs, that will be processed with parKVFinder software. After completion, the job results are sent back to the Web component and made available to the client.

Web-service configuration
=========================

.. todo::
    
    Describe configuration:
    - Job timeout: 30 minutes
    - Job expiration: 1 day
    - Maximum payload  (JSON input): 1 Mb

    Limitations:
    - Cavity representation always filtered
    - Custom box cannot be much bigger than the 3D grid
    - Grid spacing must be 0.6 A
    - Probe Out <= 50A
    - Probe In <= 5A
    - Removal distance <= 10A

    Describe JSONs:
    - Inputs
    - Outputs

API reference
=============

- Create a job: 
    
    - Method: POST
    - Media type: application/json
    - URL: http://parkvfinder.cnpem.br:8081/create

- Request a job:

    - Method: GET
    - Media type: application/json
    - URL: http://parkvfinder.cnpem.br:8081/{id}, where id is the job id sent to the user on job submission.

.. note::

    If you are using a local KVFinder-web service on your network, you must provide the IP Address instead of parkvfinder.cnpem.br.

Local configuration
===================

To execute the KVFinder-web service, the ``docker-compose`` tool is required. To install it:

.. code-block:: bash

    apt install docker-compose

.. note::

    Users can use their preferred package manager to install docker-compose tool.

In the first execution or after changes on the source code, the KVFinder-web service must be compiled:

.. code-block:: bash

    docker-compose up --build

To start the KVFinder-web service, use the command below at the root of KVFinder-websevice repository (where docker-compose.yml file is located).

.. code-block:: bash

    docker-compose up

To run the KVFinder-web service on background, run:

.. code-block:: bash

    docker-compose up -d

To interrupt an active KVFinder-web service instance, run:

.. code-block:: bash

    docker-compose down

To erase the volumes that store the Queue component data and the job folders and files, run:

.. code-block:: bash

    docker-compose down --volumes

To start more than one Worker module and thus make KVFinder-web service capable of running more than one job simultaneously. For instance, to start with two Worker modules:

.. code-block:: bash

    docker-compose up --scale kv-worker=2

The local KVFinder-web service is available at: http://localhost:8081.

The queue information can be accessed at: http://localhost:8023/info.

To use the PyMOL KVFinder-web Tools, users must change the server url hardcoded on the `__init__.py <https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools/blob/main/PyMOL-KVFinder-web-tools/__init__.py>` file.

From:

.. code-block:: bash

    # Server                                 #
    server = "http://parkvfinder.cnpem.br"   #

to:

.. code-block:: bash

    # Server                                 #
    server = "http://localhost"              #

.. note:: 

    If the KVFinder-web service is on another computer on your network, you must provide the IP Address instead of localhost.
