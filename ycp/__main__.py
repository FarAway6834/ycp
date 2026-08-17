from sys import argv

formatext = ".ycp"

def LineCompile(stream, youtube = "https://www.youtube.com/watch?v={}".format, tscache = "../file/{}".format, nonshap = "#".__ne__, over7 = (7).__lt__):
    for line in stream:
        L = len(line)   
        p = L and nonshap(line[0])
        if p and over7(L):
            cmd, data = line[:7], line[8:]
            match cmd:
                case "youtube": yield youtube(data)
                case "tscache": yield tscache(data)
                case _: yield line
        elif p and line.strip():
            yield line

def FileCompile(playlist, bc = f"{{}}{formatext}".format, ac = "{}.txt".format, eqformatext = formatext.__eq__):
    playlist, fit_format = playlist[:-4], eqformatext(playlist[-4:])
    assert fit_format, f"this file's ext isn't youtubeclip playlist file. ext must be ycp"
    with open(bc(playlist)) as bc:
        with open(ac(playlist), 'w') as ac:
            ac.writelines(LineCompile(bc))

def main():    
    if len(argv) == 1:
        argv.append(input())
        main()
    else:
        FileCompile(argv[1])

if __name__ == "__main__": main()