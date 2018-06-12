import json
import textwrap

fp = open("dataset.json", encoding = "utf8")
file2print = open("f2p.txt","w+",encoding = "utf8")

obj = json.load(fp)

for i in range(len(obj)):
    prettytext = textwrap.fill(obj[i]["txt"],width = 70)
    file2print.write(prettytext + "\n\n")
    print(prettytext+"\n")

file2print.close()

    
