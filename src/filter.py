
import sys
import ctypes

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NC', 'NE', 'NH', 'NV', 'NJ', 'NM', 'NY', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'WA', 'WV', 'WI', 'WY', 'global']

file = ['jan1','jan2','jan3','jan4','jan5','jan6','feb1','feb2','feb3','feb4','feb5','feb6','mar1','mar2','mar3','mar4','mar5','mar6','apr1','apr2','apr3'.'apr5','apr6']

path = '../tsv/' 

fifths = ['low','medium','high','popular','insane']


def chunks(l, n):
  return [l[i:i+n] for i in range(0, len(l), n)]

for state in states:
  d =  {}
  print "Working on " + state
  for file in files:
    f = open(path + state + '/' + file + '/out.tsv', 'rb')
    reader = csv.reader(f, delimiter = '\t')
    for hash, clicks, state, content in reader:
      if hash in d[hash]:
        d[hash]['c'] += int(clicks)
      else:
        d[hash] = {}
        d[hash]['a'] = content
        d[hash]['c'] = 0
    f.close()
  write_state(d, state)


def write_state(d, state):
  print "Writing " + state
  lists = []
  for hash, v in d[state].iteritems():
    clicks = v['c']
    lists.append([hash,clicks])
  lists = sorted(lists, key = lambda x: x[1])
  lists = chunks(lists,5)
  count = 0
  for list in lists:
    dst = path + state + '/tsvs/'
    os.mkdirs(dst) 
    f = open(dst + fiths[count] + '.tsv')
    state_writer = csv.writer(f, delimiter = '\t')
    for l in list:
      clicks = l[0]
      hash = l[1]
      content = d[hash]['a']
      state_writer.writerow([hash, clicks, state, content])
    f.close()


if __name__ == "__main__":
  main()
  print "Finished"
