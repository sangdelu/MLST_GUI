from model import genome


class Genome_list:
    """
    Path_lst: string, pathes of the downloaded genomes
    """

    def __init__(self, path_lst):
        self.path_lst = path_lst
        self.genome_lst = []
        self.get_initial_genomes()

    def get_initial_genomes(self):
        for i in self.path_lst:
            g = genome.Genome(i)
            self.add_genome(g)

    def add_genome(self, new_genome):
        self.genome_lst.append(new_genome)
        print('Genome added:')
        print(new_genome.title)

    def del_genome(self, genome_title):
        exi = False
        for g in self.genome_lst:
            if genome_title == g.get_title():
                self.genome_lst.remove(g)
                self.del_path(g.get_path())
                exi = True
        if exi == False:
            print('No such a genome.')

    def add_path(self, path):
        if path not in self.path_lst:
            self.path_lst.append(path)
        else:
            print('Path is already in path list.')

    def del_path(self, path):
        if path in self.path_lst:
            self.path_lst.remove(path)
        else:
            print('No such a path.')

    def get_genome_titles(self):
        gt = []
        for g in self.genome_lst:
            gt.append(g.get_title())
        return gt
