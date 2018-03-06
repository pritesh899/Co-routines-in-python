# Co-routines-in-python


Co-routine feature of Python




Co-routine is similar to subroutine/threads. Python programmers use thread to run multiple functions seemingly at the same time. But there are few issues in using threads:

Special tools are required to coordinate with each other safely. This makes code that uses threads harder to reason about than procedural, single-threaded code. This complexity makes threaded code more difficult to extend and maintain over time.

Threads usually require a lot of memory, about 8MB per executing thread. For few threads running memory is not a problem though. But if we are running thousands of functions simultaneously then memory would be problem. These functions may correspond to user requests to a server, pixels on a screen, particles in a simulation, etc. Running a thread per unique activity just won’t work.

Threads are usually costly to start. If you want to constantly be creating new concurrent functions and finishing them, the overhead of using threads becomes large and slows everything down.

We can use Co-routines in python to solve these issues. Using Co-routines we can have many seemingly simultaneous functions running in Python programs. Co -routines are an extension to generators. Cost of starting a generator co-routine is a function call. Once is it is active, each co-routine uses less than 1KB of memory till they’re exhausted.

Co-routines work by enabling the code consuming a generator to send a value back into the generator function after each yield expression. The generator function receives the value passed to the send function as the result of the corresponding yield expression. A co-routine has more than one entry and exit points.

next is used to make the initial call to prepare the generator for receiving the first send by advancing it to the first yield expression. yield and send together provide the generators with a way to get the next yielded value with respect to external input.
We will discuss the co-routine feature with the help of an example:-
Example:

We want to implement a generator co -routine that implement tree search and comparison program. In normal comparison trees will be searched independently one after the other and with compare with each other after getting the result. By doing so we have the drawback that we do not know the result until we have traversed both the trees. But by using co-routines we can advance independently in each tree and compare as the traversal progresses.

Here to accomplish the task using co-routine yield is used to get the value of the node while traversing inorder. Then the generator repeatedly yields the next value of the node sent in while traversing the tree. The generator function will seemingly run forever, making forward progress in the tress finding the new nodes with each new call to send. Co-routines works same as threads they both are independent functions that can consume inputs from their external source and produce resulting outputs. The only difference between co- routines and threads is that co-routine will pause at each yield expression in the generator function and will resumed after each call to send from the outside.

This kind of behavior helps to allow allows the code consuming the generator to take action after each yield expression in the co- routine. The consuming code can use the generator’s output values to call other functions and update the data structures. By using many separate generators, they all will seem to be running simultaneously, same as the threads in Python.



