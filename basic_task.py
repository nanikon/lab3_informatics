def basic_task(filename):
    with open(filename, 'rt', encoding='utf-8') as f:
        data = f.readlines()[1:]
    result = []
    n = 0
    for elem in data:
        if elem.count('<') == 2:
            b = elem.replace('>', '<').replace('</', '<').split('<')
            result.append('\t' * n + b[1] + ': ' + b[2])
        elif elem.count('</') == 1:
            n -= 1
        else:
            result.append('\t' * n + elem.replace('>', '<').split('<')[1] + ':')
            n += 1
    with open('output.yaml', 'wt', encoding='utf-8') as f:
        f.write('\n'.join(i for i in result))


if __name__ == "__main__":
    basic_task('input.xml')