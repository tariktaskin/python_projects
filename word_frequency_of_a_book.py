def pdf_to_text():
    from pdfminer.high_level import extract_text

    text = extract_text('book.pdf')
    print(text)
    y=open("text.txt", "w+")
    y.write(text)
    y.close()

pdf_to_text()


import json
book=open("text.txt","r+")
readfile= book.read()

create_txt=""
for a in readfile:
    create_txt+=a

make_dict={}

for a in create_txt.split():
    if a not in make_dict:
        make_dict[a]=create_txt.split().count(a)

sort_dict= sorted(make_dict.items(), key=lambda x: x[1], reverse=True)

result = json.dumps(sort_dict)
open_new_file= open("histogram.txt", "w+")
open_new_file.write(result)
open_new_file.close()
