[![DOI](https://zenodo.org/badge/554353987.svg)](https://zenodo.org/badge/latestdoi/554353987)

# vextract
**Vector extraction of data from scientific publications**

# Purpose
**This project has two purposes:**
1. To present a set of tools and methods for extracting data from graphs in scientific publications using the vector image data.
2. To demonstrate the use of these methods to extract and analyze the electrical resistance data in Figures 1a and 2b of [Nature 586, 373-377 (2020)](https://www.nature.com/articles/s41586-020-2801-z).

**The project is documented in several places, including:**
1. this github repository,
2. a zenodo repository: [zenodo.7226167](https://doi.org/10.5281/zenodo.7226167)
3. an arXiv publication: [arXiv:2210.10766](https://arxiv.org/abs/2210.10766)

### GeSe<sub>4</sub>/MnS<sub>2</sub> update
In late April of 2022, the project was updated to include information on an
analysis that uncovered similarities in electrical resistance data on
GeSe<sub>4</sub> published in a
[2013 dissertation](https://hdl.handle.net/2376/4951)
and data purportedly
[measured on Mn<sub>2</sub>](https://doi.org/10.1103/PhysRevLett.130.129901).

# Getting started

## Extracted data
If you are interested only in analyzing the extracted data with the tools of your choice, you can find the
data in csv files under data/extracted_data/CSH-Fig1a and data/extracted_data/CSH-Fig2b.

## Extraction and Analysis Methods
To see how the extraction and analysis was performed, rendered jupyter-lab notebooks
in the notebooks/ directory illustrate the entire process from start to finish.

## Running the notebooks yourself

1. I install jupyterlab in a custom environment try to ensure reproducibility.
For this, I use [Poetry](https://python-poetry.org/).
If you do not have poetry installed, you can do so using:

    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    
2. You will also need to have the `pdf2svg` utility installed
if you want to be able to run the extraction code yourself.
On debian-based systems, this can be installed with:

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

## Disclaimer
The extracted data included in the data/Fig1a_data and data/Fig2b_data
folders are not the original, source raw data files that were used to create
the plots in
[Nature 586, 373-377 (2020)](https://www.nature.com/articles/s41586-020-2801-z).
The extracted data likely has a lower precision than the original data.
Please consider this carefully when analyzing the data.
