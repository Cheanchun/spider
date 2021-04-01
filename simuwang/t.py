with open('t.txt', mode='r', encoding='u8') as fp:
    content = fp.readline().strip()
    while content:
        # print(content.strip())
        p_name = content.split()[0].strip()
        p_url = content.split()[1].strip()
        p_code = p_url.rsplit('/')[-1].split('.')[0]
        print('|'.join([p_name,p_url,p_code]))
        content = fp.readline().strip()
