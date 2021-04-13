Welcome to KVFinder-web's documentation!
========================================

Welcome to the **KVFinder-web** documentation, this page was built to help you get started with our web-based application for cavity detection and characterization.

Overview
--------

KVFinder-web is an open-source web-based application for cavity detection and spatial characterization with `parKVFinder <https://github.com/LBC-LNBio/parKVFinder>`_ software of any type of biomolecular structure. 

The KVFinder-web application has two components: a PyMOL plugin client and a web service. The client (PyMOL KVFinder-web Tools) sends job requests to the web service, customize parKVFinder detection parameters and visualize job results on PyMOL. The KVFinder-web service handles requests from the clients, manages accepted jobs and performs cavity detection and characterization on accepted jobs. 

.. toctree::
   :maxdepth: 1
   :caption: PyMOL KVFinder-web Tools

   _plugin/index

.. toctree::
   :maxdepth: 1
   :caption: KVFinder-web service

   _webservice/index

.. toctree::
   :maxdepth: 1
   :caption: GitHub repositories

   `PyMOL KVFinder-web Tools <https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools>`_
   `KVFinder-web service <https://github.com/LBC-LNBio/parKVFinder-webservice>`_

.. toctree::
   :maxdepth: 1
   :caption: About

   _about/index
