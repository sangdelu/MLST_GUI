from Bio import SeqIO


class Seed_list:
    def __init__(self, path):
        self.path = path
        self.seed_lst = []
        self.read_seeds()

    def read_seeds(self):
        self.seed_lst = list(SeqIO.parse(self.path, "fasta"))
        for i in self.seed_lst:
            print('Seed added: '+ i.id)


    """
    def add_seed(self, seed):
        # TODO: data type of warning info?
        self.seed_lst.append(seed)
        if seed.path not in self.path:
            self.add_path(seed.get_path())
        else:
            print('This seed already exists.')

    def del_seed(self, seed_title):
        exi = False
        for s in self.seed_lst:
            if seed_title == s.get_title():
                self.seed_lst.remove(s)
                self.del_path(s.get_path())
                exi = True
        if exi == False:
            print('No such a seed.')

     def add_path(self, path):
        if path not in self.path:
            self.path.append(path)
        else:
            print('Path is already in path list.')

    def del_path(self, path):
        if path in self.path_lst:
            self.path_lst.remove(path)
        else:
            print('No such a path.')

    def get_seed_lst(self):
        return self.get_seed_lst()

    def set_seed_lst(self, seed_lst):
        self.seed_lst = seed_lst

    def get_path_lst(self):
        return self.get_path_lst()

    def set_path_lst(self, path_lst):
        self.path_lst = path_lst
        """