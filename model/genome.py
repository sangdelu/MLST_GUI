from Bio import SeqIO


class Genome:
    """
    Each genome consists of seq, header and path.
    Each path should be a single fasta file.
    """
    def __init__(self, path):
        self.path = path
        self.title = ''
        self.genome_seq = ''
        # Only read the first genome in fasta file
        self.read_genome()

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, self.title, "deleted")

    def read_genome(self):
        genome = list(SeqIO.parse(self.path, "fasta"))[0]
        self.title = genome.id
        self.genome_seq = genome.seq

    def get_title(self):
        return self.title

"""


    def set_title(self, title):
        self.title = title

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    def get_genome_seq(self):
        return self.genome_seq

    def set_genome_seq(self, genome_seq):
        self.genome_seq = genome_seq

    def get_unzip(self):
        return self.if_unzip

    def set_unzip(self, if_unzip):
        self.if_unzip = if_unzip
"""