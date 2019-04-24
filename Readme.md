## Python Docker template

This is a template project for python3 tryouts.

`docker build -t <myimage> .`

Where `<myimage>` is the name of the image you desire to set to your new proyect.
Also, the ending `.` is related to the directory you are building against.

To run the image into a container, you'll run it with the command:

`docker run -t <myimage>`

The -t is to attach to interact with the shell.
Finally, the `<myimage>` is the name of the image we've created early on this example.

Also, you can add some dependencies on the requirements.txt file to work with them just rebuilding the container.