with open('skeleton.txt') as f:
    lines = f.readlines()


topics = lines[:lines.index(";\n")]
connections = lines[lines.index(";\n")+1:-1]
topics = list(reversed(list(map(lambda x : x[:-1], topics))))
connections = list(map(lambda x : x[:-1], connections))
# for topic in topics:
#     topic = topic[:-1]
# for connection in connections:
#     connection = ""#connection[:-2]

# print(connections)

used = [False for t in topics]



for connection in connections:
    if connection[0] == "<":
        continue
    mid = connection.index(" - ")
    new = connection[:mid]
    old = connection[mid+3:]
    newI = topics.index(new)
    used[newI] = True
    oldI = topics.index(old)
    print(f"#topic{newI}:hover ~ #topic{oldI}"+"{\nbackground-color: lightblue;\nleft: -10px;\ntop: -10px;\nbox-shadow: 10px 10px 10px;\n}\n\n")

print("\n\n\n onto html \n\n\n")

for i, tup in enumerate(zip(topics, used)):
    topic, depends = tup
    if depends:
        print(f"<span class = \"topic\" id=\"topic{i}\"> "+topic+"</span> ")
    else:
        print(f"<span class = \"topic base\" id=\"topic{i}\"> "+topic+"</span> ")
