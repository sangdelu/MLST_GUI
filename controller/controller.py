import tkinter.filedialog
from model import downloader
from model import genome_lst
from model import local_blaster
from model import genome
from model import seed_lst
from model import xml_analyer
from model import res_lst
from Bio import SeqIO
from viewer import viewer


class Controller:
    def __init__(self):
        self.view = viewer.Viewer()
        self.genome_dir = ''
        self.seed_path = ''
        self.out_path = ''
        self.genome_path_lst = []
        self.gb_list_file = ''
        self.res_name = ''
        self.s_lst = None
        self.g_lst = genome_lst.Genome_list(self.genome_path_lst)
        self.result = res_lst.Res_list()
        self.bind_view()
        self.blast_path = ''
        self.xml_path = ''
        self.res_path = ''

    def bind_view(self):
        self.view.bt_choose_genome.bind("<Button-1>", self.genome_open)
        self.view.bt_choose_seed.bind("<Button-1>", self.seed_open)
        self.view.bt_show_seed.bind("<Button-1>", self.show_seed)
        self.view.bt_show_genome.bind("<Button-1>", self.show_genome)
        self.view.bt_download.bind("<Button-1>", self.download)
        self.view.bt_compute.bind("<Button-1>", self.compute)
        self.view.bt_show_res.bind("<Button-1>", self.show_res)
        self.view.bt_save.bind("<Button-1>", self.res_save)
        self.view.bt_choose_down.bind("<Button-1>", self.get_download_lst)
        self.view.bt_blast.bind("<Button-1>", self.choose_blast)

    def choose_blast(self, event):
        path = tkinter.filedialog.askdirectory()
        if len(path) > 0:
            self.blast_path = path + '/bin/'
        self.view.set_text('\n BLAST location: ' + path + '\n')

    def read_seed(self, event):
        lster = seed_lst.Seed_list(self.seed_path)
        self.s_lst = lster.read_seeds()

    def show_seed(self, event):
        returned_text = ''
        for i in self.s_lst.seed_lst:
            returned_text = returned_text + '>' + i.id + '\n'
            returned_text = returned_text + i.seq + '\n'
        self.view.set_text(returned_text)

    def show_genome(self, event):
        returned_text = ''
        for i in self.g_lst.genome_lst:
            returned_text = returned_text + '>' + i.title + '\n'
        self.view.set_text(returned_text)

    def show_res(self, event):
        returned_text = ''
        for i in self.result.res_lst:
            returned_text = returned_text + i.genome_title + ' ' + i.seed_title + '\n'
            returned_text = returned_text + 'start from ' + str(i.start) + 'end at ' + str(i.end) + '\n'
            returned_text = returned_text + i.seq + '\n'
        self.view.set_text(returned_text)

    def compute(self, event):
        blast = local_blaster.Local_blaster(self.g_lst, self.seed_path, self.out_path, self.res_name, self.blast_path)
        self.xml_path = blast.res
        res_analyzer = xml_analyer.Analyzer(self.xml_path, self.out_path, self.g_lst.genome_lst)
        self.result = res_analyzer.analyze()
        self.view.set_text('\n Analysis finished. \n')

    def get_download_lst(self, event):
        path = tkinter.filedialog.askopenfilename()
        if len(path) > 0:
            self.gb_list_file = path
            self.genome_dir = path.rsplit('/', 1)[0] + '/'
        self.view.set_text(path + '\n Download list loaded. \n')

    def download(self, event):
        dl = downloader.Downloader(self.gb_list_file, self.genome_dir)
        td = []
        for d in dl.download_lst:
            if d.strip('\n') not in self.g_lst.get_genome_titles():
                td.append(d.strip('\n'))
        td = list(filter(None, td))
        dl.download_lst = td
        dl.to_download()
        new_genomes = dl.final_lst
        for ng in new_genomes:
            self.g_lst.add_path(ng)
            temp_genome = genome.Genome(ng)
            self.g_lst.add_genome(temp_genome)
        if dl.final_lst is not []:
            self.view.set_text(dl.final_lst)
            self.view.set_text('\n Download finished. \n')

    def genome_open(self, event):
        # Combine with button
        # Open multiple files, return path list
        returned_lst = tkinter.filedialog.askopenfilename(
            multiple=True)  # show an "Open" dialog box and return the path to the selected file
        if len(returned_lst) > 0:
            self.view.set_text('\n Genomes are loaded. \n')
            self.genome_path_lst = list(returned_lst)
        self.g_lst = genome_lst.Genome_list(self.genome_path_lst)

    def seed_open(self, event):
        # Combine with button
        # show an "Open" dialog box and return the path to the selected file
        self.seed_path = tkinter.filedialog.askopenfilename()
        # print(self.seed_path + '\n')
        self.s_lst = seed_lst.Seed_list(self.seed_path)
        self.view.set_text('\n Seed are loaded. \n')

    def res_save(self, event):
        f = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".fasta")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        SeqIO.write(self.result.pack_res(), f, "fasta")
        self.res_path = f.name
        f.close()
        self.view.set_text('\n Please check your result at ' + self.res_path + '\n')
