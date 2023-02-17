.. _parKVFinder: https://github.com/LBC-LNBio/parKVFinder

.. _Wiki: https://github.com/LBC-LNBio/parKVFinder/wiki

****************************************
Welcome to KVFinder-web's documentation!
****************************************

Welcome to the **KVFinder-web** documentation, this page was built to help you get started with our web-based application for cavity detection and characterization.

KVFinder-web overview
#####################

KVFinder-web :cite:p:`kvfinder-web` is an open-source web-based application of `parKVFinder`_ software for cavity detection and spatial characterization of any type of biomolecular structure. 

We provide a publicly available KVFinder-web service at https://kvfinder-web.cnpem.br.

KVFinder-web components
#######################

The KVFinder-web application has two independent components: a RESTful web service and easy-to-use clients.

RESTful web service
*******************

The KVFinder-web service, a RESTful web service, handles requests from the clients, manages accepted jobs and performs cavity detection and characterization on accepted jobs. 

* :ref:`kvfinder-web-service`

.. toctree::
   :caption: RESTful web service
   :hidden:

   _web_service/index

.. seealso::
   **KVFinder-web service** repository: https://github.com/LBC-LNBio/KVFinder-web-service

Clients
*******

The clients (i.e., HTTP Client, PyMOL KVFinder-web Tools, KVFinder-web portal) sends job via HTTP requests to the web service, customize parKVFinder detection parameters and process job results.

* :ref:`kvfinder-web-portal`: a graphical web portal;

* :ref:`pymol-kvfinder-web-tools`: a graphical PyMOL plugin.

* :ref:`http-client`: an example of a Python HTTP client;

.. toctree::
   :caption: Clients
   :hidden:

   _web_portal/index
   _plugin/index
   _http_client/index


.. seealso::
   **KVFinder-web portal** repository: https://github.com/LBC-LNBio/KVFinder-web-portal
   **PyMOL KVFinder-web Tools** repository: https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools


parKVFinder
###########

parKVFinder :cite:`parkvfinder` uses grid-and-sphere-based methods to detect, characterize and visualize any type of biomolecular cavity. The cavity detection procedure applies a dual-probe algorithm based on the theory of mathematical morphology, originally implemented in KVFinder :cite:`kvfinder`.

parKVFinder has a standalone version available as an easy-to-use PyMOL plugin with an intuitive graphical user interface that allows users to explore customizable parameters for cavity detection and characterization. In it, spatial characterization (shape, volume, area, and surrounding residues) is performed in each detected cavity. 

.. seealso::
   The standalone version of **parKVFinder** is available at this GitHub repository: https://github.com/LBC-LNBio/KVFinder-web-portal. For more information, see the parKVFinder Wiki_.

.. toctree::
   :caption: GitHub repositories
   :hidden:

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
   _about/funding
   _about/license
