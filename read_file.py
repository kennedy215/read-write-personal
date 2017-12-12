import os

# allows you to open file on the system.

# Great to continue to look into
# def with_this(func):
#     def wrapped(*args, **kwargs):
#         return func(wrapped, *args, **kwargs)
#     return wrapped

# def read_text():
#     # store path of file into var path
#     path = open("/Users/subha/Documents/Programming/Github/read_file/lyrics.txt",'r')
#     # read the contents in path and store in a var contents
#     lyrics = path.read()
#     path.close()
#
# store_text = read_text()


    #
    # # path to open file that will be written
    # new_path = "/Users/subha/Documents/Programming/Github/read_file/write_file.txt"
    # new_lyrics = open(new_path,'w')
    #
    # title = 'Lyrics \n'
    # new_lyrics.write(title)
    # print(title)
    #
    # new_lyrics.write()
    # print()
    #
    # #good practice to close
    # new_lyrics.close()
    # path.close()
    #
    #
    #








# allows you to open file on the system.

# def read_text():
    # store path of file into var path
path = open("/Users/subha/Documents/Programming/Github/read_file/lyrics.txt",'r')
# read the contents in path and store in a var contents
lyrics = path.read()


# read_text()

# def write_text():
    # path to open file that will be written
new_path = "/Users/subha/Documents/Programming/Github/read_file/write_file.txt"
new_lyrics = open(new_path,'w')

title = 'Lyrics \n'
new_lyrics.write(title)
print(title)

new_lyrics.write(lyrics)
print(lyrics)

    #good practice to close

new_lyrics.close()
path.close()

# write_text()
