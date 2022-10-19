# vextract
**Vector extraction of data from scientific publications**

# Purpose
**This project has two purposes:**
1. To present a set of tools and methods for extracting data from graphs in scientific publications using the vector image data.
2. To demonstrate the use of these methods to extract and analyze the electrical resistance data in Figures 1a and 2b of [Nature 586, 373-377 (2020)](https://www.nature.com/articles/s41586-020-2801-z).

**The project is documented in several places, including:**
1. this github repository,
2. a data repository on [Zenodo](https://zenodo.org/), and
3. an arXiv publication: [arXiv.org](https://arxiv.org/),

# Getting started

## Extracted data
If you are interested only in analyzing the extracted data with the tools of your choice, you can find the
data in csv files under data/extracted_data/CSH-Fig1a and data/extracted_data/CSH-Fig2b.

## Extraction and Analysis Methods
To see how the extraction and analysis was performed, rendered jupyter-lab notebooks
in the notebooks/ directory illustrate the entire process from start to finish.

## Running the notebooks yourself

1. I install jupyterlab in a custom environment to ensure reproducibility.  For this, I use [Poetry](https://python-poetry.org/).  If you do not have poetry installed, you can do so using:

    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    
2. You will also need to have the `pdf2svg` utility installed if you want to be able to run the extraction code yourself.  On debian-based systems, this can be installed with:

    ```
    apt install pdf2svg
    ```

3. Next clone the repository:

    ```
    git clone git@github.com:jhamlin-ufl/vextract.git
    ```
    
4. Change directory into the cloned repository:

    ```
    cd vextract
    ```

5. Install the environment

    ```
    poetry install
    ```

5. Run jupyterlab in the new environment:

    ```
    poetry run jupyter-lab
    ```

# Manifest
    ├── data
    │   ├── extracted_data
    │   │   ├── Be22Re-Fig3
    │   │   │   └── 15_GPa.csv
    │   │   ├── CSH-Fig1a
    │   │   │   ├── 174_GPa.csv
    │   │   │   ├── 210_GPa.csv
    │   │   │   ├── 220_GPa.csv
    │   │   │   ├── 243_GPa.csv
    │   │   │   ├── 250_GPa.csv
    │   │   │   ├── 258_GPa.csv
    │   │   │   └── 267_GPa.csv
    │   │   └── CSH-Fig2b
    │   │       ├── 00_T.csv
    │   │       ├── 01_T.csv
    │   │       ├── 03_T.csv
    │   │       ├── 06_T.csv
    │   │       └── 09_T.csv
    │   ├── source_data
    │   │   └── 31_ReBe22_OmniDAC_Run1_15p0bar_14p9GPa_Warming_At5K_Withoutlaser_V34I25_0p1mA
    │   └── svg_files
    ├── notebooks
    │   ├── 01_Be22Re-Fig3_extract.ipynb
    │   ├── 02_CSH-Fig1a_extract.ipynb
    │   ├── 03_CSH-Fig2b_extract.ipynb
    │   └── 04_article_plots.ipynb
    ├── poetry.lock
    ├── publication_figures
    │   ├── Fig02.pdf
    │   ├── Fig03.pdf
    │   ├── Fig04.pdf
    │   ├── Fig05.pdf
    │   ├── Fig06.pdf
    │   └── Fig07.pdf
    ├── pyproject.toml
    ├── README.md
    └── vextract
        ├── convert.py
        ├── filter.py
        ├── __init__.py
        ├── svg.py
        └── unwrap.py

## Disclaimer
The extracted data included in the data/Fig1a_data and data/Fig2b_data
folders are not the original, source raw data files that were used to create
the plots in
[Nature 586, 373-377 (2020)](https://www.nature.com/articles/s41586-020-2801-z).
The extracted data likely has a lower precision than the original data.
Please consider this carefully when analyzing the data.
