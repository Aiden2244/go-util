
OVERVIEW -------------------------------------------------------------------------------

"go-util" is a CLI-based bookmark manager for macOS. It allows you to create an alias
for websites that you can access from the terminal using the "go" keyword. The utility
also allows for the easy addition of new links using the -a flag and the removal of buggy
links using the -r flag. 


HOW TO INSTALL -------------------------------------------------------------------------

If you are interested in using this utility, I am going to assume you have some experience
with shell scripting and adding directories to your path. This is how I would recommend to 
install.

1. Open up your terminal and paste the command 

	$ git clone https://github.com/Aiden2244/go-util.git

This should clone the go-util directory from GitHub


2. Add the "go-util" directory you just downloaded to your PATH. You can do this like so:

	a. Type the command: 

		$ pwd 

	to see your directory. Copy that directory to clipboard.



	b. change to your root directory. You can do this by typing the command: 

		$ cd



	c. Type the command:

		$ nano .zshrc
	
	and add the following line of text to the file that you just opened:

		export PATH="${HOME}/path/you/copied/to/go-util/:${PATH}"
		
	NOTE: in case it was not clear, change the part of the line of text that says
	"path/you/copied/to" to the actual file path where "go-util" is located. 


	d. Press Control + x on your keyboard, then the "y" key, and then enter to save and
	exit the file.

	e. Press Command + q to quit the terminal. You now should just be able to type the
	word 'go' and see an error message if successful.


HOW TO USE -----------------------------------------------------------------------------

Usage:
     go [option] [alias] <link if option='-a'>
Options:
     [alias] -- opens the pre-saved shortcut alias in the default web browser
     -a [alias] [link] -- adds a link associated with the alias to be used later
     -h -- prints this help message
     -l -- displays a list of all saved aliases and their corresponding links
     -r [alias] -- removes the link associated with the alias


Generally speaking, you will type go followed by a user-defined alias that you have previously
associated with a website. This will open the associated website in your default web browser.



To add a link, first copy it from the search bar in your browser. Then come up with a one-word 
(no whitespace) alias for the link. For instance, if you want to access the English Wikipedia
homepage, your link would be "https://en.wikipedia.org/wiki/Main_Page" and a sample alias could
simply be "wiki". The command to add the link for English Wikipedia with the alias "wiki" is:

$ go -a "https://en.wikipedia.org/wiki/Main_Page" wiki



To access that link in the future, simply type the command:

$ go wiki

and it will take you to the link "https://en.wikipedia.org/wiki/Main_Page" in your default browser.



To remove the bookmark wiki and the link associated with it, type:

$ go -r wiki

and it will remove both the alias itself and the link associated with it.



To see a list of all of the links saved in the utility, type:

$ go -l





