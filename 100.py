header = input("Header : ")
par = input("Paragraph : ")

content = f"""
<h1> {header} </h1>
<p> {par} </p>
"""

open("index.html","w").write(content)
print("Done")