# AlbumNameGenerator
#### Short Description:
Generates a random album name and corresponding album cover when you chose a genre from Rap, Pop, or Rock.
#### Project Members: 
Maham Khawar, Lujayn Megally, Lindsey Pagcaliuagan
#### Installing Packages:
#### Detailed Description:
[demoAlbumCover.pdf](https://github.com/lujaynmegally1/AlbumNameGenerator/files/8257617/demoAlbumCover.pdf)
![demoOutput](https://user-images.githubusercontent.com/96907296/158492646-e7082df5-eb54-4e2b-b0c8-b085117d3f8f.png)

This program takes inputs of the length of the desired string and a specific genre (options of rap, pop, and rock). It outputs a randomly-generated album name based on these two input. A list of options of genres (Pop, Rap, or Rock) is presented to the user. The user selects their preferred genre by typing the desired option. The program will recognize the string they inputted and match it to the appropriate text file. For example, if the user inputs the string “Rap,” the program will pull random words from the Rap.txt file. There is exception handling if a user inputs a genre that is not available. For example, if a user inputs “Country” an error will be raised that that is not an available option and to re-input an option. The user also inputs the desired length of the album name. A randomly generated album name will output based on these two arguments. There is an additional function which presents the randomly generated Album Name with a cover, which is selected based on which genre the text is. For example, if the user selects rap, the album cover which is outputted is a specific rap cover art. 
#### Scope and Limitations:
Small pool of words in each text file (50 each) 
Formatting issue on Album Cover with longer strings of text 
#### License:
MIT license
#### References and Acknowledgement:
For formatting text on image: https://www.codegrepper.com/code-examples/python/print+text+on+image+python
Changing font size on image: https://www.blog.pythonlibrary.org/2021/02/02/drawing-text-on-images-with-pillow-and-python/
https://www.blog.pythonlibrary.org/2021/02/02/drawing-text-on-images-with-pillow-and-python/
Generic Album Covers for all genres: https://www.postermywall.com/index.php/posterbuilder/copy/42158d32903e77fc9a1b8101f6331870
