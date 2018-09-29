# file: helloworld.py

import webbrowser

my_word = raw_input('Enter a noun: ')

# changing original - print("HELLO WORLD, says " + my_word)
f = open('helloworld.html','w')

greeting = """ <!Doctype HTML>
    <html>
    <head>
    <title>World Greetings</title></head>
    <body><p>Hello world, says %s</p></body>
    </html> """

greeting_world = greeting % my_word

f.write(greeting_world)
f.close()


filename = 'file:///Users/RubbaDubDub/GitHub/hello-world' + '/helloworld.html'
webbrowser.open_new_tab(filename)
