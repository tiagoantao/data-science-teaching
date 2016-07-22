********************
Parallel Programming
********************

Parallel, concurrent and distributed
====================================

The nomenclature around high-performance computing is a bit confusing, lets
clear that first.

The easiest concept to grasp is **distributed computing**: this is normally
applied to to an environment composed of many physical computers like in
a compute cluster.

**Parallel computing** is when you run pieces of code simultaneously. For
example when you have several processes running on different computers (in
a distributed system). Of course you can also have parallel computing on a
single computer, for example by starting multiple processes at the same
time in a computer with multi-processing capabilities (in practice all
modern computers)

**Concurrency** is when you split computation in chunks that can be executed
in any particular order (or, at least some units can). *Concurrency says
nothing about how the computation will actually occur*. So you can divide
your code in bits that can be executed in parallel, but the underlying platform
might end up running everything sequentially. This is fundamental in Python
as you will see.

I called this chapter *Parallel Progamming* because that is what we are
trying to do: speeding up computation via simultaneous execution,
which is achieved by parallelism. Now,you will have to design your code that
can handle concurrency, and you *might* want run it on a distrubuted system
(the majority of our code was actually developed and run on a single computer).



Pythonic issues
===============

GIL
---

asyncio
-------


Threads, cores, processors, granularity, ...
============================================

The notion of thread can vary quite a bit (it has a hardware version and
several software ones). The same with the relationship
between (hardware) thread, core. And core and processor.

We will not go into details here, as I believe that above explanation is
enough for our purposes. But be aware that this story is not finished.

We will address the issue of computation granularity (and inter-process
communication) in later chapters and in a very practical, hands-on way.
