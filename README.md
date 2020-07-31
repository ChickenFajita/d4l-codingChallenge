## d4l-codingChallenge
>“Please write a program in your prefered language that will send out emails to recipients from a huge list (1 Mio entries) in a performant way. You do not need to send real emails but just fake the email sending by waiting for half a second.”

This task focuses on methods to reduce efficiency.

The obvious problem is the huge workload of 1 Mio entries. Therefore it comes to mind that we would like to divide the workload.
Due to a python program running sequentially and synchronously, it would take 0.5*1 000 000 seconds, which is not feasible.


# How to tackle this problem?

For dividing this workload either multiprocessing or multithreading comes to mind. 

Firstly, we have to differentiate between multiprocessing and multithreading as they oftenly are mistaken as one and the same thing.
If we think in pictures threads can be imagined as literal threads as in threading a needle. Processes are kind of programs on their own.
Both methods divide larger problems into chunks that will be solved by multiple threads or processes, but there is a big difference in performance on different kinds of problems.
Therefore I will lay out characteristics of both in bullet points:

**Multithreading**
- use shared memory -> needs sophisticated locking mechanisms to avoid data hazards
- multiple processes executed on one core (Hyperthreading)
- quick spawning, lightweight
- optimal for I/O heavy tasks

**Multiprocessing**
- each process has its own memory space -> a lot of overhead
- one core can take one process
- more overhead due to multiple python interpreter instances, storage (de-)allocation
- optimal for processing heavy tasks


Important is also the kind of problem we are facing. Multiprocessing and Threading loses efficiency the more the sequential part of the problem is, where synchronisation is needed.

[Amdahl's Law](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Amdahl.png/660px-Amdahl.png)

Here we have a big number of tasks which are quick to solve. Not a lot of processing power is needed, which means that there is little need to communicate inbetween. I expected both to perform similarly with threading having an edge, because of its synergy with I/O tasks. Therefore I tried both and looked at the times


**Results**

Workers | Multithreading | Multiprocessing
--------|----------------|----------------
1 | 
2
5
10
50
100
