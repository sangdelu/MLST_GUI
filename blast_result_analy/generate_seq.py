from model import result
from model import res_lst

# Slice sequences from genome.


def in_silico_PCR(genome_lst, filtered_df):
    """
    Find the sequence that we need and is limited by primers in cooperating gene.

    @ parameter:
    genome_lst: a genome_lst
    filtered_df: filtered dataframe with seed ids, start and end alignment site, and gb ids.

    @ return:
    res_seq: res_lst.
    """
    # seed_ind = seed_index(filtered_df)
    res = do_PCR(genome_lst, filtered_df)
    return res


def do_PCR(genome_lst, filtered_df):
    """
    Query the sequence limited by primers in genome.

    @ return:
    pandas.Dataframe: GB id and string which is the sequence we want.
    """
    r_lst = res_lst.Res_list()
    for index, row in filtered_df.iterrows():
        # print(row["Start"], row["End"])
        seed = row['Seed_id']  # [:-3]
        #print(seed)
        gb, start, end = row['Gb'], row['Start'], row['End']
        #print(gb, start, end)
        for genome in genome_lst:
            if genome.title == gb:
                cutted_seq = cut_seq(start, end, genome)
                #print(cutted_seq)
                res = result.Result(gb,seed,cutted_seq,start,end)
                r_lst.add_res(res)
    return r_lst


def cut_seq(start, end, genome):
    """
    Cut sequence from genome.
    """
    if start > end:
        pcr_res = genome.genome_seq[end:start]
    else:
        pcr_res = genome.genome_seq[start:end]
    return pcr_res


def seed_index(filtered_df):
    """
    Get list of paired seeds' index. From seed_up and seed_down.

    @return:
    list of ints.
    """
    seed_list_ori = filtered_df['Seed_id'].tolist()
    seed_list = [i[:-3] for i in seed_list_ori]
    ind = []
    for i in range(0, len(seed_list) - 1):
        if seed_list[i] == seed_list[i + 1]:
            ind.append(i)
    return ind

# in_silico_PCR(ftp_res, matched_gb, 'test1.fna')
