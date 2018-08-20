# Class 0 grasp genome files from ftp according to their assembly ID
import gzip
import pandas as pd
import re
import shutil
import urllib


def ftp_grasp(accession_list, aim_path):
    """
    Grasp genome file from NCBI ftp with accession.

    @ parameter:
    accession_list: txt file, the accession numbers.
    aim_path: string, path to store genome files.

    @ return:
    list of string, path of downloaded genome files.
    """
    acc_list = accession_list
    print(acc_list)
    ftp_urls, file_names = form_url(acc_list)
    zip_list = gen_grasp(ftp_urls, aim_path, file_names)
    res = unzip(zip_list)
    # os.system("rm "+aim_path+'*.gz') # delete all compress packages.
    return res


def form_url(acc_list):
    """
    Assemble proper URL to request NCBI-ftp from accession list.

    @ paramter:
    acc_list: pd.Dataframe.

    @ return:
    url_list: list of string containing urls of .fna.gz files.
    files: list of file names.
    """
    ftp_dirs = []
    url_list = []
    files = []
    ftp_base = 'ftp://ftp.ncbi.nlm.nih.gov/genomes/all/'
    for i in range(0, len(acc_list)):
        temp = acc_list[i].split('_')
        tempx = temp[1].split('.')
        ftp_dirs.append(ftp_base + temp[0] + '/' + tempx[0][:3] + '/' + tempx[0][3:6] + '/' + tempx[0][6:9] + '/')
    for url in ftp_dirs:
        urlpath = urllib.request.urlopen(url)
        string = urlpath.read().decode('utf-8')
        pattern = re.compile('.*')
        filelist = pattern.findall(string)
        filelist = [i for i in filelist if i.startswith('d')]
        for filename in filelist:
            filename = filename.split(' ')[-1][:-1]
            temp_url = url + filename + '/' + filename + '_genomic.fna.gz'
            url_list.append(temp_url)
            files.append(filename + '_genomic.fna.gz')
    print(files)
    return url_list, files


def gen_grasp(ftp_urls, aim_path, file_names):
    """
    Grasp files from corresponding urls and save then under specified path.

    @ parameter:
    ftp_urls: strings, the url.
    aim_path: string, the directory where you want to save your files.

    @ return:
    list of string, path of downloaded files.
    """
    res = []
    for url, file in zip(ftp_urls, file_names):
        aim = aim_path + file
        urllib.request.urlretrieve(url, aim)
        res.append(aim)
    return res


def unzip(zip_list):
    """
    Decompress .fna.gz into .fna files.

    @ return:
    list of string, path of zipped files.
    """
    for p in zip_list:
        with gzip.open(p, 'rb') as f_in, open(p[:-3], 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    res = [path[:-3] for path in zip_list]
    return res

# ftp_grasp('../test_files/genome_example.xlsx', '.')