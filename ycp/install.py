from sys import argv as _a
from os.path import join as _j

def core(target):
    with open(_j(target, ""), 'w') as fp: fp.write("""\
chmod u+x $0

alias shshebang='echo "#!/bin/sh" > '
alias newline=echo >> '
makesh() {
    shshebang $1
    newline $1
    echo 'chmod u+x $0' >> $1
    newline $1
}
gensh() {
    makesh $1
    echo $2 >> $1
}

youtubeclipsrc = 'cd ~/.youtubeclip/file
chmod u+x ../playlist/$1.ycp
../playlist/$1.ycp
mpv --playlist=../playlist/$1.txt'

installYoutubeClip(){
    gensh youtube 'mpv https://www.youtube.com/watch?v=$1'
    gensh ycp 'python -m ycp $1'
    gensh youtubeclip "$youtubeclipsrc"
    
    chmod u+x $(dirname "$0")/ycp
    chmod u+x $(dirname "$0")/youtube
    chmod u+x $(dirname "$0")/youtubeclip
}

uninstallYoutubeClip() {
    rm $(dirname "$0")/ycp
    rm $(dirname "$0")/youtube
    rm $(dirname "$0")/youtubeclip
    rm $0
}""")

def main():
   core(_a[1] if len(_a) > 0 else input())

if __name__ == "__main__": main()