from Bio.SeqRecord import SeqRecord


class Result:
    def __init__(self, genome_title, seed_title, seq, start, end):
        """
        :param genome_title: String
        :param seed_title: String
        :param seq: sequence
        """
        self.genome_title = genome_title
        self.seed_title = seed_title
        self.seq = seq
        self.start = start
        self.end = end

    def __del__(self):
        class_name = self.__class__.__name__

    def pack(self):
        return SeqRecord(self.seq, self.genome_title+','+
                         self.seed_title,description=str(self.start)+'..'+str(self.end))
