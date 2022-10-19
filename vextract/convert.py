'''
Various functions for working with svgpathtools (paths, attributes) objects.
'''

import re
import svgpathtools as spt
from webcolors import rgb_percent_to_hex

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


def hexify(svg):
    '''
    Change rgb percentage format to hex color code in an svg object.

    <svg> is of the format loaded by svgpathtools.svg2paths.

    pdf2svg uses color specification like e.g.:
        rgb(83.921814%,68.62793%,82.35321%)

    For various reasons it's preferable to have the fill and stroke
    colors in hex.

    returns an svg with all the % color codes replaced by hex.
    '''

    paths, attributes = svg

    for i, attr in enumerate(attributes):
        if 'style' in attr:
            attributes[i]['style'] = style_string_to_hex(attr['style'])

    return (paths, attributes)


def apply_tmatrix(svg):
    '''
    Some svg paths use a transformation matrix.

    <svg> is of the format loaded by svgpathtools.svg2paths.

    This function applies the transformation matrix to every
    path in the svg and returns un updated svg.
    '''
    paths, attributes = svg

    for i in range(len(paths)):
        path = paths[i]
        attr = attributes[i]
        
        if 'transform' in attr:
            transform = attr['transform']
            paths[i] = spt.path.transform(path, spt.parser.parse_transform(transform))

    return (paths, attributes)
