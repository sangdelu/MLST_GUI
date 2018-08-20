from model import downloader
from model import genome_lst
from model import local_blaster
from model import genome
from model import seed_lst
from model import xml_analyer
from model import saver

genome_dir = ''
genome_path_lst = []
seed_path = ''
gb_list_file = ''
out_path = ''
res_name = ''

"""
Download and prepare sequences.
"""
downloader = downloader.Downloader(gb_list_file, genome_dir)
genome_list = genome_lst.Genome_list(genome_path_lst)
seed_lst = seed_lst.Seed_list(seed_path).read_seeds()


def check_download(dl):
    td = []
    for d in dl.download_lst:
        if d not in genome_list.get_genome_titles():
            td.append(d)
    return td


# add genomes to genome_lst when download.
td_lst = check_download(downloader)
new_genomes = downloader.to_download(td_lst)
for ng in new_genomes:
    genome_list.add_path(ng)
    temp_genome = genome.Genome(ng)
    genome_list.add_genome(temp_genome)

"""
BLAST.
"""
blast = local_blaster.Local_blaster(genome_lst, seed_path, out_path, res_name)

xml_path = blast.res

"""
Compute MLST by analyzing blast's xml file.
"""
res_analyzer = xml_analyer.Analyzer(xml_path, out_path,genome_list)
result = res_analyzer.analyze()

"""
If want to save the result, then save it.
"""
res_path = out_path + 'mlst_res.faa'

saver = saver.Saver(result,res_path)
print('Please check your result at ' + res_path)