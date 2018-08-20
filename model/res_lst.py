class Res_list:
    def __init__(self):
        self.res_lst = []

    def add_res(self, res):
        # TODO: data type of warning info?
        self.res_lst.append(res)
        if res not in self.res_lst:
            self.add_res(res)

    def del_res(self, res_title):
        exi = False
        for r in self.res_lst:
            if res_title == r.get_title():
                self.seed_lst.remove(r)
                exi = True
        if exi == False:
            print('No such a result.')

    def pack_res(self):
        seq_lst = []
        for r in self.res_lst:
            seq_lst.append(r.pack())
        return seq_lst
