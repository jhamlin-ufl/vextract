'''
Various tools for working with the svg files,
and extracting data points.
'''

import os
import re
import numpy as np
import pandas as pd
import svgpathtools as spt

from webcolors import rgb_percent_to_hex

# These two are just for rendering svgs inline in the notebook.
import tempfile
from IPython.display import SVG, display


def style_string_to_dict(style_string):
    '''
    Take an svg style string (e.g. fill:#669ed4;fill-opacity:1;fill-rule:nonzero;stroke:none)
    and return a dictionary of key value pairs representing the various style parameters.

    Not used at the moment, but useful for some purposes.
    '''
    
    item_list = []
    for x in style_string.split(';'):
        splitted = x.split(':')
        if len(splitted) > 1:
            item_list.append(splitted)
            
    return dict(item_list)


def transform_coord(pmin, pmax, cmin, cmax, p):
    '''
    <pmin> and <pmax>: svg coordinates of min and max tic marks.
    <cmin> and <cmax>: physical coordinates of min and max tic marks (e.g. temperatures)
    <p> svg coordinate of the point in question
    
    Return: the physical coordinate of the point.
    '''
    
    return cmin+(cmax-cmin)*(p-pmin)/(pmax-pmin)


def path_centroid(path):
    '''
    Takes a single path entry and finds the centroid.
    Returns a tuple: (<x>, <y>).
    '''
    
    path_starts = [line[0] for line in path]
    xy_list = list(zip(*[(path_start.real, path_start.imag) for path_start in path_starts]))
    return (np.mean(xy_list[0]), np.mean(xy_list[1]))



def display_svg(svg):
    '''
    <svg> is of the format loaded by svgpathtools.svg2paths.

    Display the paths in svg inline in jupyter-lab.
    Useful for identifying different paths (e.g. tic marks).

    Note that this does not apply transformation matrixes.
    '''

    paths, attributes = svg

    if len(paths) == 0:
        print('No paths to display!')
    else:
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_svg = os.path.join(tmp_dir, 'display.svg')
            spt.wsvg(paths, filename=tmp_svg)
            display(SVG(tmp_svg))


def count_fill_colors(svg):
    '''
    <svg> is of the format loaded by svgpathtools.svg2paths.

    Return a pandas series where the index is a hex color code,
    and the value is the number of paths in svg that are that color.
    '''
    
    paths, attributes = svg

    fill_search = re.compile('fill:(#.{6});')

    colors = []
    for i in range(len(paths)):
        attr = attributes[i]
        if 'style' in attributes[i]:
            color = fill_search.findall(attr['style'])  
            if color:
                colors.append(color[0])

    df = pd.DataFrame()
    df['colors'] = colors
    return df['colors'].value_counts()


def style_string_to_hex(style_string):
    '''
    pdf2svg uses color specification like e.g.:
        rgb(83.921814%,68.62793%,82.35321%)

    For various reasons it's preferable to have the
    fill and stroke colors in hex.

    This function takes a style string and replaces the
    rgb percent values with hex colors.
    '''

    fill_pattern = re.compile("fill:rgb\((\d+\.?\d*)\%,(\d+\.?\d*)\%,(\d+\.?\d*)\%\)")
    stroke_pattern = re.compile("stroke:rgb\((\d+\.?\d*)\%,(\d+\.?\d*)\%,(\d+\.?\d*)\%\)")

    try:
        fill_color = rgb_percent_to_hex(fill_pattern.findall(style_string)[0])
        style_string = re.sub(fill_pattern, f'fill:{fill_color}', style_string)
    except IndexError:
        pass

    try:
        stroke_color = rgb_percent_to_hex(stroke_pattern.findall(style_string)[0])
        style_string = re.sub(stroke_pattern, f'stroke:{stroke_color}', style_string)
    except IndexError:
        pass

    return style_string


def path_starts(path):
    '''
    Takes a svgpathtools path and return a tuple of lists: (xs, ys).
    xs is a list of the x coordinates and
    ys is a list of the y coordinates.
    '''

    xs = []
    ys = []
    for line in path:
        x = line.start.real
        y = line.start.imag
        xs.append(x)
        ys.append(y)
        
    return xs, ys
