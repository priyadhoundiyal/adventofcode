file_name = 'day-5-input.txt'
data = []
with open(file_name) as f:
    content = f.readlines()
data = [int(x.strip()) for x in content]
l = len(data)
step = i = 0
while i < l:
    current = data[i]
    if current == 0:
        data[i] += 1
    else:
        data[i] += 1
        i += current
    step += 1
print 'Steps taken {}'.format(step)
data = []
step = i = 0
with open(file_name) as f:
    content = f.readlines()
data = [int(x.strip()) for x in content]
l = len(data)
step = i = 0
while i < l:
    current = data[i]
    if current == 0:
        data[i] += 1
    elif current >= 3:
        data[i] -= 1
    else:
        data[i] += 1
    i += current
    step += 1
print 'Steps taken {}'.format(step)
