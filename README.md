# KBE-welding-trajectory
In this final assignment we were challenged with producing a program that automated CAD-design of welding lines. More specifically, the walls of a maze was supposed to be welded to a base plane. This was made possible by programming the geometric calculations and running the program in Siemens NX. We also made a more independent program that takes in 2D images of the maze and generates images in 2D of the welding lines. By accepting both part and image files, the program can assist the engineer both on a more conceptual level(images) aswell as more concrete CAD design. Therefore the system compliments the designer on different stages in the development, which we thought was a neat way of implementing the KBE methodology. KBE was in focus for capture and systematically reuse of engineering knowledge, with the final goal of reducing time and costs of repetitive product development tasks. We have learned plenty from the previous assignments which came to good use in this last iteration. Agreeing early on the geometric, constantly thinking scalability and striving for generalisation are just examples of how the previous iterations has made us better KBE engineers.

<h3>CAD-solution</h3>

Welding lines maze example 1  |  Welding lines maze example 2   |  Welding lines maze example 3  
:----------------------------:|:----------------------------:|:----------------------------:
![](https://github.com/torsteinhov/KBE-welding-trajectory/blob/main/product_photos/maze_v2_1.png)  |  ![](https://github.com/torsteinhov/KBE-welding-trajectory/blob/main/product_photos/maze_v3_1.png)   |   ![](https://github.com/torsteinhov/KBE-welding-trajectory/blob/main/product_photos/maze_v4_1.png)
![](https://github.com/torsteinhov/KBE-welding-trajectory/blob/main/product_photos/maze_v2_3.png)  |  ![](https://github.com/torsteinhov/KBE-welding-trajectory/blob/main/product_photos/maze_v3_3.png)   |   ![](https://github.com/torsteinhov/KBE-welding-trajectory/blob/main/product_photos/maze_v4_3.png)

<h3>Image-solution</h3>

2D maze (input)  |  2D maze with welding lines in cyan (output)
:----------------------------:|:----------------------------:
<img src="https://github.com/torsteinhov/KBE-welding-trajectory/blob/main/product_photos/2Dmaze3.jpg" width=78%> |  ![](https://github.com/torsteinhov/KBE-welding-trajectory/blob/main/product_photos/2Dmaze3_weldinglines.png)
<img src="https://github.com/torsteinhov/KBE-welding-trajectory/blob/main/product_photos/2Dmaze4.jpg" width=82%>  |  ![](https://github.com/torsteinhov/KBE-welding-trajectory/blob/main/product_photos/2Dmaze4_weldinglines.png)

<h2>How to run:</h2>

<h3>Preparations before running:</h3>

+ Install all required libraries: ```pip install -r requirements.txt```
+ Add local path in ```views.py``` and ```prtGenerator.py```
+ Disable cache in local browser: ```Ctrl+Shift+I -> Network -> Press "Disable cache"```

<h3>Run:</h3>

+ Run run.py
+ Interact with webpage, upload user data and files from in the Generator tab:
  + test data is provided at: ```ImgWeldLinesGenerator\Img_mazes``` for image files
  + test data is provided at: ```prt\testFiles``` for .prt files
+ **Image**:
  + Your image is processed and presented to you, usually takes about 5 seconds.
+ **CAD**:
  + Run prtGenerator.py in the Developer tab, in Siemens NX.
 

<h2>User Interface</h2>

Start page  |  Generator page
:----------------------------:|:----------------------------:
<img src="https://user-images.githubusercontent.com/77832956/115846369-1e5a2680-a422-11eb-9ff4-421625b80ee8.jpg" width=100%> |  ![](https://user-images.githubusercontent.com/77832956/115842601-48114e80-a41e-11eb-878e-b97c349ae885.jpg)


<h2>Calculations</h2>

<h3>Image Processing:</h3>

+ Takes in image file and converts to greyscale, using Pillow library.
+ Takes greyscale image and converts to binary format, every shade of grey gets converted to black, representing a wall. It is now ready to process.
+ Based on binary black/white pixels 0 and 1, it finds the edges of the walls/black-pixels and edits the white pixels surrounding the wall/black-pixels, illustrating the weld.
+ Transforms the processed binary format back to an image, with final welding lines added in cyan.

<h4>Assumptions</h4>

+ Since we work with pixels, we assume that the customer uploads images of high enough resolution for the result to be representable.

<h3>CAD Processing:</h3>

+ Takes in part file and gets all lines from all faces of all objects.
+ Selects the face with most lines(this is the base plane).
+ Converts NXOpen.Point3d object to coordinates which is a more accessible format for calculating.
+ Removes the border lines of the base plane, this is calculated by finding the longest lines along each axis. We now posess only the lines to be welded.
+ Iterate through each line and adds geometry(cylinder and sphere) to illustrate the weld, using calculations regarding size, position and direction.

<h4>Assumptions</h4>

+ Only welds to one side of the base plane per iteration. By this we mean that it can not weld to multiple levels along the z-axis => constant z-axis.
+ At this level of development, the program only handles straight lines, not curves. This means that welding a circle will be challenging, only because of challenges illustrating curves as a combination of cylinders and spheres. The logic for finding these curved lines is already in-place.


<h2>Architecture</h2>
<p align="center">
<img src="https://user-images.githubusercontent.com/77832956/115675298-c1da0700-a34e-11eb-88c4-8b991c29da0b.png">
</p>

<h2>UML Sequence Diagram</h2>
<p align="center">
<img src="https://user-images.githubusercontent.com/77832956/115674167-aae6e500-a34d-11eb-9e72-1df951941983.png">
</p>

<h2>Program files with corresponding methods</h2>
<br>
<h3>Views.py</h3>

**The server. Handles the HTML by retrieving user data and parcing the data. Checks user data up against constrains. Adds orders to the LogOrder.txt. Handles all the different webpages on the website.**

| Method | Functionality |
| --- | --- |
| index() | runs the Homepage |
| about() | runs the About page |
| imgOrder() | runs the Generator page |
| allowed_image(filename) | checks if image format is allowed |
| allowed_cad(filename) | checks if prt format is allowed |
| allowed_image_filesize(filesize) | checks wether file size is allowed |
| saveFileNewName(oldName, newName) | saves the old file with new name, based on customer input |
| updateLogFile(name, email, company, infile, outfile) | updates the Log file with corresponding information given to the function |
| imgResult() | Runs the image processing and returns the final solution in image format. If it is a .prt file you get sent to /prtResult.html with a message to wait for a consultant. |

<h3>ImgGenerator.py</h3>

**Main processing unit behind the Image Generator. Takes in a 2D maze in image format and returns image with welding lines around the maze walls. This is done by transforming to binary format and doing calculations on each pixel.**

| Method | Functionality |
| --- | --- |
| convert2binary(filename) | takes in a file, and based on the Pillow library, transforms the image to greyscale. It then makes all shades of grey to black, and then transforms the image to binary format, with only black and white pixels illustrated in 0's and 1's. Adds white pixels around the image in case of walls being all the way to the edge. Returns a binary maze |
| makeWeldLines(binaryMaze) | Based on the binary maze, calculates where the edges of the maze is, and adds cyan colored pixels around the walls, illustrating the weld. Returns a binaryMaze with processed numbers representing the pixels |
| convert2Img(pixels, saveName) | takes in the processed binary maze and transforms the array maze to a image format. The edited pixels is now illustrated with a cyan color. Saves the image |
| runImgGenerator(filename, saveName) | Runs all the functions above to produce the processed image |

<h3>partReading.py</h3>

**Handles NX objects and gives us the functionality to do operations on the objects, parts, faces, lines and points in the corresponding .prt file.**

| Method | Functionality |
| --- | --- |
| loadPRTFile(path) | loads the .prt file in Siemens NX |
| getFaces(theSession) | returns all objects in the .prt file |
| processPart(partObject) | returns all parts in the given object |
| processBodyFaces(bodyObject) | returns all faces on the given part |
| processFace(faceObject) | returns all the lines in the given face |
| processEdge(edgeObject) | returns all points in the given line |


<h3>lineSlicer.py</h3>

**Takes in a bunch of NXOpen.Point3d objects and by using calculations, produces NXOpen objects as cylinders and spheres to illustrate the final welding lines.**

| Method | Functionality |
| --- | --- |
| findBasePlane(path) | returns the face with most edges |
| findPoints(line) | returns a list with two points, illustrating the start- and endpoint of that specific input line |
| removeBorderLines(basePlane) | Removes the longest lines along the x-axis aswell as the y-axis and returns the lines remaining, this results in removing the lines making up the base plane |
| buildWeldingLines(weldinglines) | Takes in the final welding lines and builds NX objects to illustrate the weld. This is done by using data as size, direction and position of the lines to produce cylinders and spheres. |

<h3>prtGenerator.py</h3>

**The program that you run in Siemens NX, under the developer tab. Runs the uploaded file, and after generated, updates logFile and saves the final file with filename based on user data**

| Method | Functionality |
| --- | --- |
| saveGeneratedCADFile(path, filename) | saves the session as a new .prt file, based on the user data |
| readLogFile(yourLocation) | reads the log file(represents manufacturing order) and locates which files that have not been generated|
| updateLogFile(order, newLogLine, yourLocation) | updates the log file such that generated part files gets marked as generated, and therefore will not be generated next iteration |
| main() | runs the functions such that the new file gets modified in the logFile and saved as a new .prt file |

<h2>Improvements from previous KBE projects</h2>

+ We upgraded to a new system regarding hosting the server and handling the HTML. This was mainly because we lacked functionality to upload files. The parsing of parameters was also more intuitive since the flask framework did a better job supporting this.
+ We did a much better job on agreeing on geometry and architecture early to avoid misunderstandings and complications during the development.
+ We have become better on supporting scalable solutions. We now strive to make functions as general as possible for increasing the chance of reusability aswell as making it scalable and KBE-friendly.
+ The UI is easier to interact with, supporting the Don Normans Principles of Design.

<h2>Further development</h2>

+	The updating and writing to logOrder.txt should be made bulletproof by not allowing white spaces and the letters "??????".
+	Even though we are happy with the structure of the log file, we still think there are room for improvements. This is something we think comes with experience, and is very individually for each project.  
+	The timestamp in the logfile should be implemented when saving the corresponding file. As the program stands right now, the same user data can not upload a file twice.
+	The prtGenerator.py should be extended to work for all shapes. This means changes in the functions that does the calculation. We tried multiple fixes for this but with time limitations and limited knowledge in NX Open, this was the best solution for us.
+	There is a debug where occasionally, when adding multiple CAD orders to the logfile and running, it only manages to load the weld of the first one, on all the objects. This needs more debugging to fix, we are not quite sure of why this happens.
+	It would be cool if the program could be fully automated, so that we don???t need to run the website, aswell as the prtGenerator.py.
+	It should also be implemented a database to store the different files and user data.

<h2>Conclusions from working on KBE Systems:</h2>

+ It has been interesting working on automation of repetitive CAD operations in Siemens NX. We have learned that even though you have agreed on technology, libraries and architecture, the actual implementation of the logic may still present many challenges.
+ Working on these projects has been very rewarding. Every project has shown the value of the programs. All projects has resulted in a functional system that will cut down on cost and time for product development, aswell as improving product quality(precision) and redusing time to market. All of these aspects are goals that we want to achieve when making these KBE systems.
+ We have learned about the great potential that lies in the industry, regarding KBE systems. Automating tasks is something all industries are striving for, and with the possibilities that comes with computer programming, the experience and knowledge of employees can "easily" be interpret and used in algorithms.
+ Fur future development of KBE systems, we would like to have more interaction with the customer aswell as the employee that are getting his tasks automated. This is to better capture knowledge to be used in the calculations, since basing everything on our own intuition can in larger applications be a naive approach. In this specific assignment, having a discussion with an experienced welder would also have been very helpful.
