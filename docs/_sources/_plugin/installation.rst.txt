Installation
============

PyMOL KVFinder-web Tools is a PyMOL v2 plugin for detecting and characterizing biomolecular cavities at a KVFinder-web service.

`PyMOL v2 <https://pymol.org/2/>`_ is required if you wish to use PyMOL KVFinder-web Tools.

Afterwards, install the required Python packages from [requirements.txt](https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools/blob/master/requirements.txt) file on PyMOL's Python.

```bash
pip3 install -r requirements.txt
```

or directly,

```bash
pip3 install pyqt5 toml typing
```

Now, download the latest version of PyMOL KVFinder-web Tools from [here](https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools/releases/latest/download/PyMOL-KVFinder-web-Tools.zip).

1. Open PyMOL;
2. Go to **Plugin** menu and select **Plugin Manager** option;
3. The **Plugin Manager** window will open, go to the **Install New Plugin** tab;
4. Under **Install from local file** group, click on **Choose file...**;
5. The **Install Plugin** window will open, select the `PyMOL-KVFinder-web-Tools.zip`;
6. The **Select plugin directory** window will open, select `/home/user/.pymol/startup` and click **OK**;
7. The **Confirm** window will open, click on **OK**;
8. The **Sucess** window will open, confirming that the plugin has been installed;
9. Restart PyMOL;
10. **PyMOL KVFinder-web Tools** is ready to use under **Plugin** menu.

Or, if you clone this [repository](https://github.com/LBC-LNBio/PyMOL-KVFinder-web-Tools), instead of selecting `PyMOL-KVFinder-web-Tools.zip` (Step 5), user must select `__init__.py` of PyMOL-KVFinder-web-Tools-CNPEM directory.
