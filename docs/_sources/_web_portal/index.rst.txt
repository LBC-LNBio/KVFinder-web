.. _kvfinder-web-portal:

KVFinder-web portal
###################

The KVFinder-web portal, developed in R Shiny, delivers the major functionalities of the KVFinder-web service, where users can load a target biomolecule, adjust detection parameters, select run modes, and download and visualize results. The web portal provides a simple and interactive way to analyze and visualize cavities. Volumes and areas are shown in an interactive table that can be downloaded in TOML format. A biomolecule viewer, powered by the NGL engine for R, displays the biomolecular structure with its cavities, which can be downloaded in PDB format, and allows various customizations, such as highlighting cavities and displaying interface residues surrounding them.

Our publicly available KVFinder-web service at https://kvfinder-web.cnpem.br has KVFinder-web portal as the graphical web interface.

Local installation
------------------

To run locally the KVFinder-web portal in Linux distributions, it is necessary to install docker-compose and its dependencies. To install it:

.. code-block:: bash

    sudo apt install docker-compose

After the docker-compose installation and clone of this repository. First, you have to build our KVFinder-web interface:

.. code-block:: bash

    docker build -t kvfinder-web-portal .

To start KVFinder-web interface:

.. code-block:: bash

    docker run -p 3838:3838 kvfinder-web-portal

Tutorial
--------

A comprehensive tutorial demonstrating how to use KVFinder-web portal with our publicly available KVFinder-web service is available in https://kvfinder-web.cnpem.br under **Tutorial** tab. This tutorial explores the four execution modes of KVFinder-web service to detect and characterize cavities.

