'''
Functions for filtering svgpathtools (paths, attributes) objects.
'''

import re

def by_length(svg, length):
    '''
    <svg> is of the format loaded by svgpathtools.svg2paths.

    Return a copy that contains only items where the number
    of path segments is equal to <length>
    '''
    
    paths, attributes = svg

    filtered_paths = []
    filtered_attributes = []
    for i in range(len(paths)):
        if len(paths[i]) == length:
            filtered_paths.append(paths[i])
            filtered_attributes.append(attributes[i])

    return (filtered_paths, filtered_attributes)


def by_style(svg, regex):
    '''
    <svg> is of the format loaded by svgpathtools.svg2paths.

    regex is made by doing e.g. re.compile(pattern)

    Returns a new version of svg where only elements for which
    the style string matches the pattern are included.
    '''

    paths, attributes = svg

    new_paths = []
    new_attributes = []
    for i in range(len(paths)):
        path = paths[i]
        attr = attributes[i]
        if 'style' in attr:
            if regex.findall(attr['style']):
                new_paths.append(path)
                new_attributes.append(attr)
        
    return (new_paths, new_attributes)


def by_fill(svg, color):
    '''
    <svg> is of the format loaded by svgpathtools.svg2paths.

    <color> is a string representing any kind of color specification.

    Return a new svg including only elements with fill color
    matching <color>
    '''

    fill_pattern = re.compile(f'fill:{color}')
    
    return by_style(svg, fill_pattern)


def by_stroke(svg, color):
    '''
    <svg> is of the format loaded by svgpathtools.svg2paths.

    <color> is a string representing any kind of color specification.

    Return a new svg including only elements with fill color
    matching <color>
    '''

    fill_pattern = re.compile(f'stroke:{color}')
    
    return by_style(svg, fill_pattern)


def by_fill_and_length(svg, color, length):
    '''
    Filter by both color (hex) and path length.
    '''

    return by_fill(by_length(svg, length), color)


def by_vlines(svg):
    '''
    Useful for finding axis lines and tic marks.

    <svg> is of the format loaded by svgpathtools.svg2paths.

    return a filtered svg where only vertical lines are included.
    '''

    paths, attributes = by_length(svg, 1)
    
    filtered_paths = []
    filtered_attributes = []
    for i in range(len(paths)):
        path = paths[i]
        attribute = attributes[i]
        x_start = path.start.real
        x_end = path.end.real
        if x_start == x_end:
            filtered_paths.append(path)
            filtered_attributes.append(attribute)
            
    return (filtered_paths, filtered_attributes)


def by_hlines(svg):
    '''
    Useful for finding axis lines and tic marks.

    <svg> is of the format loaded by svgpathtools.svg2paths.

    return a filtered svg where only horizontal lines are included.
    '''

    paths, attributes = by_length(svg, 1)
    
    filtered_paths = []
    filtered_attributes = []
    for i in range(len(paths)):
        path = paths[i]
        attribute = attributes[i]
        x_start = path.start.imag
        x_end = path.end.imag
        if x_start == x_end:
            filtered_paths.append(path)
            filtered_attributes.append(attribute)
            
    return (filtered_paths, filtered_attributes)
