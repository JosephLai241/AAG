# ASCII-Art
ASCII art generator written in Python ([`pyfiglet`](https://pypi.org/project/pyfiglet/)) .

<pre>
 ______  ____    ____    ______  ______      ______  ____    ______
/\  _  \/\  _`\ /\  _`\ /\__  _\/\__  _\    /\  _  \/\  _`\ /\__  _\
\ \ \L\ \ \,\L\_\ \ \/\_\/_/\ \/\/_/\ \/    \ \ \L\ \ \ \L\ \/_/\ \/
 \ \  __ \/_\__ \\ \ \/_/_ \ \ \   \ \ \     \ \  __ \ \ ,  /  \ \ \
  \ \ \/\ \/\ \L\ \ \ \L\ \ \_\ \__ \_\ \__   \ \ \/\ \ \ \\ \  \ \ \
   \ \_\ \_\ `\____\ \____/ /\_____\/\_____\   \ \_\ \_\ \_\ \_\ \ \_\
    \/_/\/_/\/_____/\/___/  \/_____/\/_____/    \/_/\/_/\/_/\/ /  \/_/

</pre>

I wanted to make some ASCII art for my Raspberry Pi's MOTD and wondered if I could program something in Python that could generate it for me. I did some Googling and found `pyfiglet`, which is a full port of [FIGlet](http://www.figlet.org/) into Python and would allow me to make such a program. 

I figured I could recreate it into a tool like [URS](https://github.com/JosephLai241/Universal-Reddit-Scraper) and put it on my Github profile since URS is the only other repo I have so far, so here is the final product.

# Walkthrough
On initializing the program, you will be given the option to view a numbered list of all the fonts available, display examples for every font (425 examples), or skipping either option and generating the ASCII art.

![Welcome](https://github.com/JosephLai241/ASCII-Art/blob/assets/Screenshots/Welcome.png)

This is a snippet of the numbered list.

![List Fonts](https://github.com/JosephLai241/ASCII-Art/blob/assets/Screenshots/List%20Fonts.png)

If you choose to display examples, the program will say "Generating 425 examples...", sleep for 1.5 seconds, then display an example for each font.

![Examples 1](https://github.com/JosephLai241/ASCII-Art/blob/assets/Screenshots/Examples%201.png) 

![Examples 2](https://github.com/JosephLai241/ASCII-Art/blob/assets/Screenshots/Examples%202.png) 

After either viewing the numbered list, displaying all examples, or skipping both options, you will then choose the ASCII font you would like to use, or you can allow the program to randomly choose one for you.

![Font Selection](https://github.com/JosephLai241/ASCII-Art/blob/assets/Screenshots/Font%20Selection.png) 

You can refer back to either the numbered list or the examples that were displayed to pick a font. To do so, enter the number that the font corresponds with. The program will display an example again.

![Font Selection Number](https://github.com/JosephLai241/ASCII-Art/blob/assets/Screenshots/Font%20Selection%20Number.png)

Then, enter your text and you will be greeted with your ASCII art.

![Font Selection Number 1](https://github.com/JosephLai241/ASCII-Art/blob/assets/Screenshots/Font%20Selection%20Number%201.png)

Or, if you are feeling adventurous, let the program choose the font for you.

![Font Selection Random](https://github.com/JosephLai241/ASCII-Art/blob/assets/Screenshots/Font%20Selection%20Random.png)
