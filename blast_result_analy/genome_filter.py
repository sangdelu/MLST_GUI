import pandas as pd
from data_inout import ncbi_eutils


# Get genome data, only used for online-blast result.

def match_gb(ori_records, aim):
    """
    Select matched id from dataframe and excel file containing aim species.

    @ parameters:
    df: dataframe
    aim: string, path of xlsx file containing aim species' gb id and other information.

    @ return:
    pandas.DataFrame: of matched records
    """
    aim_list = gb_parser(aim)
    gb_aim = aim_list['Gb_aim'].tolist()
    match_records = pd.DataFrame()
    ori_records = ori_records.fillna(0)
    for gb in gb_aim:
        if gb != 0:
            match_records = match_records.append(ori_records.loc[ori_records['Gb'] == gb])
        else:
            # Todo: print strain
            print('No Gb in this record.')
    return match_records


def gb_parser(aim):
    """
    Select gb id from original xlsx file.

    @ return:
    list of strings, containing gb id.
    """
    aim_list = pd.read_excel(aim)
    aim_cols = aim_list[['Species', 'Strain', 'Gb']]
    aim_cols = aim_cols.rename(index=str, columns={'Species': 'Species_aim', 'Strain': 'Strain_aim', 'Gb': 'Gb_aim'})
    return aim_cols


def get_genome(match_records, in_path):
    """
    Download aim genomes from NCBI with gb id.

    @ parameters:
    match_records: pandas.DataFrame.

    @ return:
    pandas.DataFrame: add path of genome files to last column.
    genome files should be named after gb id.
    """
    if len(match_records) !=0:
        ncbi_eutils.gb_grasp(match_records['Gb'].tolist(), in_path)
    else:
        print('No match items!')


#matched_gb = match_gb(test, '130_references/101_accession_test.xlsx')
#matched_gb.head()
