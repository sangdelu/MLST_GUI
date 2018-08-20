from Bio.Blast import NCBIXML
import pandas as pd


# Analysis result of blast, getting start, end sites and seed, genome IDs

def blast_analy(blast_result, blast_type):
    """
    Find useful data from balst result.

    @ parameter:
    blast_result: path of xml file.

    @ return:
    pa.dataframe, high e-value species and their alignment.
    """
    xml_handle = open(blast_result)
    records = NCBIXML.parse(xml_handle)
    filtered_res = records_filter(records, blast_type)
    xml_handle.close()
    return filtered_res


def records_filter(records, blast_type):
    """
    Sort and find most possible gene/genome to which seeds all aligned.

    @ return:
    pa.dataframe, high e-value species and their alignment.
    """
    # Extract start and end sites in genome
    # blast_records = records.__next__()
    filtered_res = pd.DataFrame()
    seed_id = []
    align_title = []
    start_site = []
    end_site = []

    for blast_record in records:
        seed_name = blast_record.query  # Show name of seed
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                # if hsp.align_length == hsp.query_end:  Filter alignment of whole-align
                if hsp.sbjct_start > 1:
                    seed_id.append(seed_name)
                    start_site.append(hsp.sbjct_start)
                    end_site.append(hsp.sbjct_end)  # end site of alignment
                    align_title.append(alignment.title)
    gi, gb, strain = separate_title(align_title, blast_type)
    filtered_res = pd.DataFrame(
        {'Seed_id': seed_id, 'Gi': gi, 'Gb': gb, 'Strain': strain, 'Start': start_site, 'End': end_site})
    return filtered_res


def separate_title(raw_title, blast_type):
    """
    Split alignment title into gi, gb and spice name.

    @ return:
    Three lists of string.
    """
    gi = []
    gb = []
    strain = []
    for title in raw_title:
        # For web blast: '|', 1,3,4
        # For local blast: ' ',2; 1,2 no gi
        if blast_type == 'local':
            title = title.split(' ', 2)
            gi.append(None)
            gb.append(title[1])
            strain.append(title[0])
        elif blast_type == 'online':
            title = title.split('|')
            gi.append(title[1])
            gb.append(title[3])
            strain.append(title[4])
    return gi, gb, strain
