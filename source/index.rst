Welcome to KVFinder-web's documentation!
========================================

Welcome to the **KVFinder-web** documentation, this page was built to help you get started with our web-based application for cavity detection and characterization.

Overview
--------

KVFinder-web is an open-source web-based application of `parKVFinder <https://github.com/LBC-LNBio/parKVFinder>`_ software for cavity detection and spatial characterization of any type of biomolecular structure. 

The KVFinder-web application has two components: a RESTful web service and a PyMOL plugin client. The RESTful web service (KVFinder-web service) handles requests from the clients, manages accepted jobs and performs cavity detection and characterization on accepted jobs. The client (PyMOL KVFinder-web Tools) sends job via HTTP requests to the web service, customize parKVFinder detection parameters and visualize job results on PyMOL.

Users may opt to run jobs on a locally configured server or on our publicly available KVFinder-web service, available at http://parkvfinder.cnpem.br:8081.

Furthermore, users can install the standalone version of parKVFinder from this `repository <https://github.com/LBC-LNBio/parKVFinder>`_. For more details, see the parKVFinder `wiki <https://github.com/LBC-LNBio/parKVFinder/wiki>`_.

.. toctree::
   :maxdepth: 1
   :caption: KVFinder-web service

   _webservice/index

.. toctree::
   :maxdepth: 1
   :caption: PyMOL KVFinder-web Tools

   _plugin/index

.. toctree::
   :maxdepth: 1
   :caption: GitHub repositories

   KVFinder-web service <https://github.com/LBC-LNBio/KVFinder-web-service>
   PyMOL KVFinder-web Tools <https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools>
   parKVFinder <https://github.com/LBC-LNBio/parKVFinder>

.. toctree::
   :maxdepth: 1
   :caption: About

   _about/issues
   _about/scientific_team
   _about/citing
   _about/license
