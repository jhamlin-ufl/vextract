'''
Functions related to unwrapping components of data.

The concept behind unwrapping has been explained in detail in:
    Room-temperature superconductivity — or not? Comment on Nature 586, 373 (2020) by E. Snider et al.
    https://doi.org/10.1142/S0217979223750012
'''


import numpy as np
import pandas as pd


def line_up(dV0, dT0, dV1, dT1, shift):
    '''
    This is the core of the unwrapping method.
    It operates on two adjacent points.
    
    Take voltage at point i and add or subtract integer multiples of <shift>
    to V_{i} until (dV/dT)_{i} is as close as possible to (dV/dT)_{i-1}.
    Then return the the shifted value of V_{i}.
    
    Note: These could be just as well named dy and dx, but I initially wrote
    this for unwraping voltages from susceptibility data.
    '''
    
    dVdT0 = dV0 / dT0
    dVdT1 = dV1 / dT1
    
    dVdT_plus = (dV1 + shift) / dT1
    dVdT_minus = (dV1 - shift) / dT1
    
    # A dict that maps the dVdT difference to the corresponding dV value. 
    best_dVdT_to_best_dV = {np.abs(dVdT0 - dVdT_plus): dV1 + shift,
                            np.abs(dVdT0 - dVdT1): dV1,
                            np.abs(dVdT0 - dVdT_minus): dV1 - shift}
    
    # Chose the dV that corresponds to the miniumum dVdT difference.
    best_dV = best_dVdT_to_best_dV[min(best_dVdT_to_best_dV.keys())]
    
    # If we are already as close as we can get, return dV1.
    # Otherwise recur with best_dV <- dV1
    return dV1 if (best_dV == dV1) else line_up(dV0, dT0, best_dV, dT1, shift)


def unwrap(Temp, V, shift):
    '''
    <Temp> and <V> are type pd.Series.
    The returned series contains the digitized part of the
    V vs Temp data, i.e. what is left after subtracting the smooth part.
    '''
    
    df = pd.concat([Temp, V], axis=1)
    df.columns = ['Temp', 'V']
    
    df['dT'] = df['Temp'].diff()
    df['dV'] = df['V'].diff()
    
    # This list will contain the 'unwraped' dV values
    dV_smooth_part = []  
    
    # There is a bunch of baloney here for making sure that the
    # unwrapped data is properly aligned with the input data.
    
    # index of the second non NaN containing row in the dataframe
    i_second_nonNaN = 0
    # A counter to identify when we've hit the second non NaN row
    num_nonNaN = 0
    for i in range(len(df)):
        row = df.iloc[i]
        if ~row.isnull().values.any():
            num_nonNaN += 1
            if num_nonNaN == 2:
                i_second_nonNaN = i
                break
        dV_smooth_part.append(row['dV'])
        
    # Iterate through the data, appending elements to the
    # dV_smooth_part list.
    previous_row = df.iloc[i_second_nonNaN - 1].copy()
    for i in range(i_second_nonNaN, len(df)):
        row = df.iloc[i].copy()
        new_dV = line_up(previous_row['dV'],
                         previous_row['dT'],
                         row['dV'],
                         row['dT'],
                         shift)
        dV_smooth_part.append(new_dV)
        previous_row = row
        previous_row['dV'] = new_dV
            
    df['dV_smooth_part'] = dV_smooth_part
    return (df['dV'] - df['dV_smooth_part']).cumsum()
