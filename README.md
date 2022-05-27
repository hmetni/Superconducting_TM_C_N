# Superconducting_TM_C_N

[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![DOI](https://zenodo.org/badge/495465721.svg)](https://zenodo.org/badge/latestdoi/495465721)

Dataset and code used in "Predicting the Superconducting Critical Temperature in Transition
Metal Carbides and Nitrides using Machine Learning".

The dataset is contained in the file: *dataset.csv*. It contains the following columns:

**- num**: whether the compound was extracted (EXT) or was found in the SuperCon database (the corresponding compound number)

**- compound**: the compound

**- Tc**: the experimentally measured critical temperature

**- a**: the lattice parameter (estimated in some cases, see paper)

**- elements**: the elements present, therefore the substitution series. (=BASE for pure compounds)

**- 1**, **2**: pure compounds 1 and 2 when the compound is an alloy.

**- perc_1_in_2**: the fraction of compound 1 in the compound

The *dataset_features.csv* contains the above-mentioned columns as well as additional MagPie features generated using matminer. 


To use the code, Python 3 should be installed on the local machine.
A recommended way of installation is through Anaconda, see https://docs.anaconda.com/anaconda/install/index.html. 

First clone this repository into the desired directory and access it using the following two commands from a terminal window:

```angular2html
git clone https://github.com/hmetni/Superconducting_TM_C_N.git
cd Superconducting_TM_C_N
```

Once Anaconda is installed and the repository cloned, create a virtual
environment using: 

```angular2html
conda create --name Superconducting_TM_C_N python=3.7
```

Then activate your newly created environment:

```angular2html
conda activate Superconducting_TM_C_N
```

The next step is to install the requirements. The main packages required for this work are: pandas, scikit-learn, umap, seaborn, matplotlib and matminer.  

Once the requirements are installed, the notebooks can be executed in interfaces such as Jupyter Notebook.
