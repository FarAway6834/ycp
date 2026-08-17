from sys import argv as _a
from os.path import join as _j
from os import system as _s

def core(target):
    fn = _j(target, "youtubeclipsetup")
    with open(fn, 'w') as fp: fp.write("""\
#!/bin/sh

chmod u+x $0

alias shshebang='echo "#!/bin/sh" > '
alias newline='echo >> '
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

youtubeclipsrc='cd ~/.youtubeclip/file
chmod u+x ../playlist/$1.ycp
../playlist/$1.ycp
mpv --playlist=../playlist/$1.txt'

installYoutubeClip(){
    gensh $2/youtube 'mpv https://www.youtube.com/watch?v=$1'
    gensh $2/ycp 'python -m ycp $1'
    gensh $2/youtubeclip "$youtubeclipsrc"
    
    chmod u+x $2/ycp
    chmod u+x $2/youtube
    chmod u+x $2/youtubeclip
}

uninstallYoutubeClip() {
    rm $2/ycp
    rm $2/youtube
    rm $2/youtubeclip
    rm $1
}

if [ "$1" = "install" ]; then
    installYoutubeClip $0 $(dirname "$0")
elif [ "$1" = "uninstall" ]; then
    uninstallYoutubeClip $0 $(dirname "$0")
else
    echo "install or uninstall only allowed"
fi\
""")
    _s(f"chmod u+x {fn}")

def main():
    if len(_a) > 1 : _ = _a[1]
    else: _ = input()
    
    core(_)

if __name__ == "__main__": main()