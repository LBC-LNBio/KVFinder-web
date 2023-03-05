.. _Wiki: https://github.com/LBC-LNBio/parKVFinder/wiki

****************************************
Welcome to KVFinder-web's documentation!
****************************************

Welcome to the **KVFinder-web** documentation, this page was built to help you get started with our web-based application for cavity detection and characterization.

KVFinder-web overview
#####################

KVFinder-web :cite:p:`kvfinder-web` is an open-source web-based application of an updated version of `parKVFinder`_ software :cite:p:`parkvfinder` (v1.2.0) for cavity detection and characterization of any type of biomolecular structure. The characterization includes spatial, depth, constitutional and hydropathy characterization.

We provide a publicly available KVFinder-web at https://kvfinder-web.cnpem.br.

KVFinder-web components
#######################

The KVFinder-web has two independent components:

* RESTful web service: :ref:`kvfinder-web-service`;

* Graphical web portal: :ref:`kvfinder-web-portal`.

.. toctree::
   :caption: RESTful web service
   :hidden:

   _web_service/index
   _web_portal/index

.. seealso::
   **KVFinder-web service** repository: https://github.com/LBC-LNBio/KVFinder-web-service

   **KVFinder-web portal** repository: https://github.com/LBC-LNBio/KVFinder-web-portal

Client-side applications
************************

In addition to the primary interaction mode of KVFinder-web, we also provide additional client-side applications, such as PyMOL KVFinder-web and an example of a Python HTTP client, which broaden the range of possibilities for user interaction. These clients sends job via HTTP requests to the web service, customize detection parameters and process job results.


* :ref:`pymol-kvfinder-web-tools`: a graphical PyMOL plugin.

* :ref:`http-client`: an example of a Python HTTP client;

.. toctree::
   :caption: Client-side applications
   :hidden:

   _plugin/index
   _http_client/index


.. seealso::

   **PyMOL KVFinder-web Tools** repository: https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools


.. _parkvfinder:

parKVFinder
###########

parKVFinder :cite:`parkvfinder` uses grid-and-sphere-based methods to detect, characterize and visualize any type of biomolecular cavity. The cavity detection procedure applies a dual-probe algorithm based on the theory of mathematical morphology, originally implemented in KVFinder :cite:`kvfinder`. 

Recently, parKVFinder (v1.2.0) has been integrated with additional features, such as depth calculation and Eisenberg & Weiss :cite:p:`eisenbergweiss` hydropathy characterization, which are implemented in pyKVFinder :cite:p:`pykvfinder`.

Now, cavity characterization includes spatial, depth, constitutional and hydropathy properties. The depth characterization defines depths for each cavity point, shown in the B-factor, and calculates the average and maximum depth per cavity. The constitutional characterization includes amino acids that form the identified cavities. The hydropathy characterization maps Eisenberg & Weiss hydrophobicity scale at surface points, shown in the Q-factor, and estimates average hydropathy per cavity.

Furthermore, parKVFinder has a standalone version available as an easy-to-use PyMOL plugin with an intuitive graphical user interface that allows users to explore customizable parameters for cavity detection and characterization. 

.. seealso::
   The standalone version of **parKVFinder** is available at this GitHub repository: https://github.com/LBC-LNBio/parKVFinder. For more information, see the parKVFinder Wiki_.

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
