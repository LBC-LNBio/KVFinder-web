Welcome to KVFinder-web's documentation!
########################################

Welcome to the **KVFinder-web** documentation, this page was built to help you get started with our web-based application for cavity detection and characterization.

Overview
--------

KVFinder-web is an open-source web-based application of `parKVFinder <https://github.com/LBC-LNBio/parKVFinder>`_ software for cavity detection and spatial characterization of any type of biomolecular structure. 

The KVFinder-web application has two independent components:

- a RESTful web service: [KVFinder-web service](https://github.com/LBC-LNBio/KVFinder-web-service);
  
- clients, that are:

  - [HTTP Client](https://github.com/LBC-LNBio/KVFinder-web-service/blob/master/http-client.py): a Python script;

  - [KVFinder-web portal](https://github.com/LBC-LNBio/KVFinder-web-portal): a graphical web portal;

  - [PyMOL KVFinder-web Tools](https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools): a graphical PyMOL plugin;

The RESTful web service (KVFinder-web service) handles requests from the clients, manages accepted jobs and performs cavity detection and characterization on accepted jobs. 

The clients (i.e., HTTP Client, PyMOL KVFinder-web Tools, KVFinder-web portal) sends job via HTTP requests to the web service, customize parKVFinder detection parameters and process job results.

We provide a publicly available KVFinder-web service ([https://kvfinder-web.cnpem.br](https://kvfinder-web.cnpem.br)), with [KVFinder-web portal](https://github.com/LBC-LNBio/KVFinder-web-portal) as the graphical web interface.

Furthermore, users can install the standalone version of parKVFinder from this `repository <https://github.com/LBC-LNBio/parKVFinder>`_. For more details, see the parKVFinder `wiki <https://github.com/LBC-LNBio/parKVFinder/wiki>`_.

.. toctree::
   :maxdepth: 1
   :caption: KVFinder-web service

   _web_service/index

.. toctree::
   :maxdepth: 1
   :caption: KVFinder-web portal

   _web_portal/index

.. toctree::
   :maxdepth: 1
   :caption: PyMOL KVFinder-web Tools

   _plugin/index

.. toctree::
   :maxdepth: 1
   :caption: GitHub repositories

   KVFinder-web service <https://github.com/LBC-LNBio/KVFinder-web-service>
   KVFinder-web portal <https://github.com/LBC-LNBio/KVFinder-web-portal>
   PyMOL KVFinder-web Tools <https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools>
   parKVFinder <https://github.com/LBC-LNBio/parKVFinder>

.. toctree::
   :maxdepth: 1
   :caption: About

   _about/issues
   _about/scientific_team
   _about/citing
