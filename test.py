import cgi

form = cgi.FieldStorage()
tname = form.getvalue('textname','')

print("Hello python")
print(tname)

