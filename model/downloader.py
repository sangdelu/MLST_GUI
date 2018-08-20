from data_inout import ncbi_eutils
from data_inout import ncbi_ftp_parser

class Downloader:
    """
    To download genomes if it wasn't downloaded.
    download_in: String, the file contatins all genome Gb
    that need to be downloaded.
    download_out: aim dir of downloading
    """
    def __init__(self, download_in,download_out):
        self.download_in = download_in
        self.download_out = download_out
        self.download_lst = []
        # path list of downloaded genomes
        self.final_lst = []
        self.import_download_lst()

    def import_download_lst(self):
        with open(self.download_in) as input_handle:
            #self.download_lst = [i for i in input_handle.readlines()]
            self.download_lst = [i for i in input_handle.readlines()]
        input_handle.close()

    def to_download(self):
        #self.final_lst = ncbi_ftp_parser.ftp_grasp(self.download_lst, self.download_out)
        self.final_lst = ncbi_eutils.gb_grasp(self.download_lst, self.download_out)