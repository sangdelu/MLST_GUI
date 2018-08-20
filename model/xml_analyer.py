from blast_result_analy import blast_analy
from blast_result_analy import generate_seq
from blast_result_analy import genome_filter

import os


class Analyzer:
    def __init__(self, xml_path, out_path,genome_lst):
        self.xml_path = xml_path
        self.genome_lst = genome_lst
        self.out_path = out_path

    def analyze(self):
        # A dataframe, including
        # 'Seed_id': seed_id, 'Gi': gi, 'Gb': gb, 'Strain': strain, 'Start': start_site, 'End': end_site
        filtered_blast_res = blast_analy.blast_analy(self.xml_path, 'local')
        res = generate_seq.in_silico_PCR(self.genome_lst, filtered_blast_res)
        return res