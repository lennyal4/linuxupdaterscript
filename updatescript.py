from consolemenu import *
from consolemenu.items import *
from bash import *

def main():
	menu=ConsoleMenu("WELCOME TO THE MAIN MENU","here you should find all the tools you need to get basic things done from the command line.")
#this should be update
	update=MenuItem("update",) #the update command is sudo dnf update
	install_package=MenuItem("install one or more packages",)#the user should be able to 
	search_packages=MenuItem("find package(s)",)#user should be able to fund packages
#find and install drivers =MenuItem("find and install drivers") 
#this function which may become a application on it's own has to be able to find and install neccessary drivers for computer based on model very experimental. if someone wants to collaborate for this or knows somewhere i could get help feel free to share
	ping=MenuItem("ping",)# will be able to ping and test for internet connectivity
	connect_to_wireless=MenuItem("connect to wifi",)#with this i hope to make a application like wifi-menu but for non-arch systems that will be easy to use

if __name__=="__main__":
	main()
