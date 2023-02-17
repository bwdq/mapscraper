import subprocess
proc = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)

list = ['EU cities regex copy', 'EU cities regex', 'EU cities', 'EU topo', 'pol topo', 'poster', 'rect topo', 'UK cities regex copy', 'UK cities regex', 'UK cities', 'UK topo', 'US Cities regex copy', 'US Cities regex', 'US cities', 'US_topo.txt']

for item in list:
    full_item = "citieslist\\" + item + ".txt"

    reader = open('citieslist\\rect topo.txt').readlines()
    for line in reader:
        a = line
        a = a.replace('.html','')#remove .html
        a = a.replace('\n','')#remove new line
        b = a
        if not b.find("jomi") == -1:
            b = b.replace('https://images.jomidav.com/','')
        if not b.find("mapshow") == -1:
            b = b.replace('https://s3.eu-west-2.amazonaws.com/mapshow/','')
        if not b.find("mapshow.s3") == -1:
            b = b.replace('https://mapshow.s3.eu-west-2.amazonaws.com/','')
        a = a + "/ImageProperties.xml "
        concat = "dezoomify-rs.exe -l -r10 " + a + ".\\maps\\" + b + "\n"
        proc.stdin.write(bytes(concat, 'utf-8'))
        #print(concat)

    proc.stdin.close()
    proc.wait()