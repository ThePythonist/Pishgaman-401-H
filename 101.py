students = [
    {"name": "Arshia", "age": 18, "job": "Backend Developer"},
    {"name": "Ahmad", "age": 13, "job": "Frontend Developer"},
    {"name": "Ali", "age": 14, "job": "Security Engineer"},
    {"name": "Arad", "age": 16, "job": "Data Engineer"},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: red;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Job</th>
  </tr>

"""

for person in students:
    html += f"""
  <tr>
    <td>{person['name']}</td>
    <td>{person['age']}</td>
    <td>{person['job']}</td>
  </tr>
    """

html += """
</table>

</body>
</html>
"""

open("Table.html","w").write(html)
print("Done")