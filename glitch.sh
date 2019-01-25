#!/usr/bin/env bash

wdir="$HOME/Programming/rice/glitchlock/"

termX=$(xdpyinfo | grep dimensions | cut -d ' ' -f7 | cut -d 'x' -f 1)
termY=$(xdpyinfo | grep dimensions | cut -d ' ' -f7 | cut -d 'x' -f 2)

icon="$wdir/icon.png"
glitch="$wdir/glitch.py"
glitcharr="$wdir/glitcharr.py"
tmpbg='/tmp/screen.jpg'
tmpimg='/tmp/tmp.png'
quotes="$wdir/quotes.txt"

drawBoxes() {
    POINTSIZE="20"
    FONT="DejaVu-Sans-Mono"
    STR=`"$wdir/boxes.py"`
    convert -size $termX'x'$termY $1 -fill "rgba( 0, 215, 0 , 0.1 )" -stroke "rgba( 0, 215, 0 , 0.1 )" \
        -font $FONT -pointsize $POINTSIZE -gravity center \
        -draw "text 0,0 '$STR'" $1

}

overlayText() {
    gen="shuf -n 1 $quotes"
    txt=""
    while [ $RANDOM -gt 5000 ]
    do
      txt=$txt" "$($gen)
      if [ $RANDOM -gt 30000 ]
      then
          txt=$txt$'\n'
      fi
    done
    locX=$(($RANDOM%$termX))
    locY=$(($RANDOM%$termY))
    convert -size $termX'x'$termY $1 -fill red -stroke purple \
        -font "Think-Nothing" -pointsize 80 \
        -draw "text $locX,$locY '$txt'" $1
}

if [ -z "$1" ]
then
    scrot "$tmpbg"
    overlayText "$tmpbg"
    drawBoxes "$tmpbg"
    $glitch "$tmpbg"
    $glitcharr "$tmpbg"
    convert "$tmpbg" "$icon" -gravity center -composite -matte "$tmpbg"
fi

feh "$tmpbg"
