def function():

    words = ["hello", 3, "ai", 13, "era"]
    index = [0, 1, 2, 3, 4]

    output = ""

    print()

    for i in index:

        info = "Controlling index: " + str(i + 1) + "/" + str(len(index))

        if str(words[i]).isdigit() == False:

            info = info + " " + words[i] + " included"
        
            output = output + words[i] + " "

        else:

            info = info + " " + str(words[i]) + " not included"

        print(info)

    print()
    print(output)
    print()


function()