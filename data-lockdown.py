for i in range(int(input())):
    links = []
    sizes = []
    for i in range(int(input())):
        link, size = input().split(' ')
        links.append(link)
        sizes.append(size)
    for i in range(len(links)):
        if ".lmco.com" in links[i]: 
            continue
        else:
            if int(sizes[i]) > 1000:
                print(links[i], sizes[i])
            