import urllib.request
import re


def gb_grasp(gb_list, out_path):
    # esearch
    base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    db = 'nuccore'
    web_list = []
    key_list = []
    efetches = []
    final_list = []

    for query in gb_list:
        url = base + "esearch.fcgi?db=" + db + "&term=" + query + "&usehistory=y"
        # splice esearch result
        output = urllib.request.urlopen(url)
        out = output.read()
        to_slice = str(out)

        web_list.append(re.findall('<WebEnv>.*<\/WebEnv>', to_slice, flags=0)[0][8:-9])
        key_list.append(re.findall('<QueryKey>.*</QueryKey>', to_slice, flags=0)[0][10:-11])

    for web, key in zip(web_list, key_list):
        # efetch
        efetch_url = base + "efetch.fcgi?db=" + db + "&WebEnv=" + web
        efetch_url = efetch_url + "&query_key=" + str(key) + "&retstart=0&rettype=fasta&retmode=text"
        efetches.append(efetch_url)

    for eurl, query in zip(efetches, gb_list):
        file_name = out_path + query + '.fasta'
        with urllib.request.urlopen(eurl) as response, open(file_name, 'wb') as out_file:
            data = response.read()  # a `bytes` object
            out_file.write(data)
            final_list.append(file_name)

    return final_list