file_name = 'day-8-input.txt'
with open(file_name) as f:
    content = f.readlines()
newcontent = []
for x in content:
    c = (x.strip()).split(' ')
    nc = {}
    nc["name"] = c[0]
    if c[1] == 'inc':
        nc["inc"] = True
    elif c[1] == 'dec':
        nc["inc"] = False
    nc["val"] = int(c[2])
    nc["condition"] = ' '.join(c[4:7])
    nc["reg_val"] = 0
    exec(nc["name"] + ' = nc["reg_val"]')
    newcontent.append(nc)
exec('maxvalever = ' + newcontent[0]["name"])
for nc in newcontent:
    if eval(nc["condition"]):
        if nc["inc"]:
            exec(nc["name"] + ' += nc["val"]')
        else:
            exec(nc["name"] + ' -= nc["val"]')
        e = eval('maxvalever <= ' + nc["name"])
        if e:
            exec('maxvalever = ' + nc["name"])
exec('maxval = ' + newcontent[0]["name"])
for nc in newcontent:
    e = eval('maxval <= ' + nc["name"])
    if e:
        exec('maxval = ' + nc["name"])

print 'Maximum value at end {}'.format(maxval)
print 'Maximum value {}'.format(maxvalever)
