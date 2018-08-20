from Bio import SeqIO


class Saver:
    """
    Save the result of MLST as a fasta file.
    """

    def __init__(self, res_lst, save_path):
        self.res_lst = res_lst
        self.save_path = save_path
        self.write_file()

    def write_file(self):
        with open(self.save_path, 'w') as out_handle:
            SeqIO.write(self.res_lst, out_handle, "fasta")
