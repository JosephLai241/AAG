    ____________________________
    ________    |__    |_  ____/
    _______  /| |_  /| |  / __  
    ______  ___ |  ___ / /_/ /  
         /_/  |_/_/  |_\____/   

# Table of Contents

* [Introduction](#introduction)
* [Walkthrough](#walkthrough)
    + [List All Available Fonts](#list-all-available-fonts)
    + [Generate Examples for All Fonts](#generate-examples-for-all-fonts)
    + [Generate Custom ASCII Art](#generate-custom-ascii-art)
    + [Generate ASCII Art From a Random Font](#generate-ascii-art-from-a-random-font)

# Introduction

ASCII art generator written in Python ([`pyfiglet`](https://pypi.org/project/pyfiglet/)).

I wanted to make some ASCII art for my Raspberry Pi's MOTD and wondered if I could program something in Python that could generate it for me. I did some Googling and found `pyfiglet`, which is a full port of [FIGlet](http://www.figlet.org/) into Python and would allow me to make such a program. 

I figured I could recreate it into a tool like [URS](https://github.com/JosephLai241/Universal-Reddit-Scraper) and put it on my Github profile since URS is the only other repo I have so far, so here is the final product. Enjoy!

# Walkthrough

There are four flags you can use with this program: `-l`, `-e`, `-m`, and `-r`.

## List All Available Fonts

`$ ./AAG.py -l`

Use this flag to see a list of all available fonts and their corresponding number. You will need the number to create your ASCII art.

## Generate Examples for All Fonts

`$ ./AAG.py -e`

This flag will provide examples for each font. 

## Generate Custom ASCII Art

`$ ./AAG.py -m FONT_NUM TEXT`

This flag is used to generate your ASCII art.

It takes 2 arguments - The font number and the string you want to generate art for.

## Generate ASCII Art From a Random Font

`$ ./AAG.py -r TEXT`

If you're feeling adventurous, let AAG choose the font for you.
