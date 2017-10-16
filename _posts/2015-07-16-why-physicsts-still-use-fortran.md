---
id: 1865
title: Why physicists still use Fortran
comments: true
date: 2015-07-16T03:34:17+00:00
author: delton137
layout: post
guid: https://moreisdifferent.wordpress.com/?p=1865
permalink: /2015/07/16/why-physicsts-still-use-fortran/
geo_public:
  - "0"
publicize_twitter_user:
  - moreisdifferent
publicize_google_plus_url:
  - https://plus.google.com/+DanElton/posts/5Esc1fBFgtt
publicize_tumblr_url:
  - http://.tumblr.com/post/124638830328
publicize_path_id:
  - 55add66c5aac17191828cc3a
publicize_linkedin_url:
  - 'https://www.linkedin.com/updates?discuss=&scope=90218007&stype=M&topic=6029127370756153344&type=U&a=v7Qt'
dsq_thread_id:
  - "6139014258"
categories:
  - programming
  - research
tags:
  - fortran
  - HPC
  - programming
---
> “I don’t know what the programming language of the year 2000 will look like, but I know it will be called FORTRAN.” &#8211;  Charles Anthony Richard Hoare, circa 1982

Fortran is rarely used today in industry &#8212; one ranking ranks it behind [29 other languages](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html). However, Fortran is still a dominant language for the large scale simulation of physical systems, ie. for things like the astrophysical modeling of stars and galaxies, hydrodynamics codes (cf. [Flash](http://flash.uchicago.edu/site/flashcode/)), large scale molecular dynamics, electronic structure calculation codes (cf. [SIESTA](http://departments.icmab.es/leem/siesta/)), large scale climate models, etc.  In the field of high performance computing (HPC), of which large scale numerical simulation is a subset, there are only two languages in use today &#8212; C/C++ and “modern Fortran” (Fortran 90/95/03/08). The popular [Open MPI](https://en.wikipedia.org/wiki/Open_MPI) libraries for parallelizing code were developed for these two languages. So basically, if you want fast code that an run on many processors, you are limited to these two options. Modern Fortran also has a feature called &#8216;[coarrays](https://en.wikipedia.org/wiki/Coarray_Fortran)&#8216; which puts parallelization features directly into the language. Coarrays started as an extension of Fortran 95 and were incorporated into Fortran 2008 standard.

The heavy use of Fortran by physicists often confounds computer scientists and other outsiders who tend to view Fortran as a historical anachronism.

What I would like to do in this article is explain why Fortran is still a useful language. I am not advocating that physics majors learn Fortran &#8212; since most physics majors will end up in research, their time may be better invested in learning C/C++ (or just sticking with Matlab/Octave/Python). What I would like to explain is why Fortran is still used, and show that it is not merely because physicists are ‘behind the time’ (although this is sometimes true &#8211; about a year ago I saw a physics student working on a Fortran 77 code, and both the student and adviser were unaware of Fortran 90). Computer scientists should (and do) consider the continued dominance of Fortran in numerical computing as a challenge.<!--more-->

Before digging in I feel obligated to discuss a bit of history, since when many hear “Fortran” they immediately think of punch cards and code with line numbers. The original specification for Fortran was written in 1954.  Early Fortran (designated in allcaps as FORTRAN) was, by modern standards hellish, but it was incredible leap forward from previous programming, which was done in assembly. FORTRAN was often programed with punch cards, as is not-so-fondly recalled by Prof. Miriam Forman here at Stony Brook. Fortran has through many revisions, the most well known are the 66, 77, 90, 95, 03, and 08 standards.

It is often said that the reason Fortran is still used is that it is _fast._ But is it the fastest? The website <http://benchmarksgame.alioth.debian.org> allows for a [comparison of several benchmarks between C and Fortran](http://benchmarksgame.alioth.debian.org/u64q/fortran.html). On most of the benchmarks, Fortran and C/C++ are the fastest.  Note that Python, which is the darling of computer scientists, is usually about 100 times slower, but that is the nature of interpreted code.  Python is unsuited for heavy numerical computation but highly suited for many other things. Interestingly, C/C++ beats Fortran on all but two of the benchmarks, although they are fairly close on most. However, the two benchmarks where Fortran wins (n-body simulation and calculation of spectra) are the most physics-y. The results vary somewhat depending on whether one compares a single core or quad core machine with Fortran lagging a bit more behind C/C++ on the quad core. The benchmarks where Fortran is much slower than C/C++ involve processes where most of the time is spent reading and writing data, for which Fortran is known to be slow.

So, altogether, C/C++ is just as fast as Fortran and often a bit faster.  The question we really should be asking is “why do physics professors continue to advise their students to use Fortran rather than C/C++?”

## Fortran has legacy code

Given the long history of Fortran, it is no surprise that a large amount of legacy code in physics is written in Fortran. Physicists usually try to minimize the amount of coding they do, therefore, if legacy code exists they will use it. Even if old code is hard to read, poorly documented, and not the most efficient, it is often faster to use old validated code than to write new code. Physicists are not in the business of writing code, after all, they are trying to understand the nature of reality. Professors usually have this legacy code on hand (often code they wrote themselves decades ago) and pass this code on to their students. This saves their students time, and also takes uncertainty out of the debugging process.

## Fortran is easier for physics students to learn than C/C++

Overall, I think Fortran is easier to learn than C/C++. Fortran 90 and C are very similar, but Fortran is easier to code in for reasons I will discuss. C is a fairly primitive languages, so physicists who go the C/C++ route tend to look into object oriented coding. Object oriented coding can be useful, especially with massive software projects, but it takes significantly more time to learn. One has to learn abstract concepts like classes and inheritance. The paradigm of object oriented coding is very different from the procedural paradigm used in Fortran. Fortran is based on a simple procedural paradigm that is closer to what actually happens &#8216;under the hood&#8217; inside a computer. When optimizing / vectorizing code for speed the procedural paradigm seems easier to work under.  Physicists generally have an understanding of how computers work and are inclined to think in terms of physical processes, such as the transfer of data from disk to RAM and from RAM to CPU cache. This is in contrast to mathematicians, who prefer to think in terms of abstract functions and logic. It is also in contrast to the way one thinks about object oriented code. Optimizing object oriented code seems more difficult to me than procedural code. Objects are very bulky structures compared the physicist&#8217;s data structure of choice: the array.

## Point of ease 1: Fortran array handling features

** Arrays (or in physics-speak, matrices) lie at the heart of all physics calculations. Fortran 90+ incorporates array handling features, similar to [APL](https://en.wikipedia.org/wiki/APL_(programming_language)) or Matlab/Octave. Arrays can be copied, multiplied by a scalar, or multiplied together quite intuitively as:

<pre class="brush: plain; title: ; notranslate" title="">A = B
A = 3.24*B
C = A*B
B = exp(A)
norm = sqrt(sum(A**2))
</pre>

Here, A, B, C are arrays, with some dimensions (for instance, they all could 10x10x10). C = A*B gives an element-by-element multiplication of A and B, assuming A and B are the same size. To do a matrix multiplication, one would use C = matmul(A,B). Almost all of the intrinsic functions in Fortran (Sin(), Exp(), Abs(), Floor(), etc) can take arrays as arguments, leading to easy of use and very neat code. Similar C/C++ code simply does not exist. In the base implementation of C/C++, merely copying an array requires cycling through all the elements with _for_ loops or a call to a library function. Trying to feed an array into the wrong library function in C will return an error. Having to use libraries instead of intrinsic functions means the resulting code is never as neat, as transferable, or as easy to learn.

In Fortran, array elements are indexed using the simple syntax A\[x,y,z], whereas in C/C++ one has to use A[x\]\[y\][z].  Arrays are indexed starting at 1, which conforms to the way physicists talk about matrices, unlike C/C++ arrays, which start at 0. The following Fortran code shows a few more array features:

<pre class="brush: plain; title: ; notranslate" title="">A = (/ i , i = 1,100 /)
B = A(1:100:10)
C(10:) = B
</pre>

First a vector A is created using an _implicit do_ loop, also called an _array constructor_. Next, a vector B is created from every 10th element of A using a &#8216;stride&#8217; of 10 in the subscript. Finally, array B is copied into array C, starting at element 10. Fortran supports declaring arrays with indices that are zero or negative:

<pre class="brush: plain; title: ; notranslate" title="">double precision, dimension(-1:10) :: myArray
</pre>

A negative index may sound silly, but I have heard that they can be very useful &#8211; imagine a negative index as an area with &#8216;extra space&#8217; for annotations. Fortran also supports [vector-valued indices](http://www.fortran.gantep.edu.tr/local/HPFCourse/HTMLHPFCourseNotesnode102.html). For instance, we can extract elements 1, 5, and 7 from a Nx1 array A into a 3&#215;1 array B using:

<pre class="brush: plain; title: ; notranslate" title="">subscripts = (/ 1, 5, 7 /)
B = A(subscripts)
</pre>

Fortran also incorporates [masking](http://www.fortran.gantep.edu.tr/local/HPFCourse/HTMLHPFCourseNotesnode100.html) of arrays in all intrinsic functions. For instance, if we want to take the log of a matrix on all of the elements where it is greater than zero we use

<pre class="brush: plain; title: ; notranslate" title="">log_of_A = log(A, mask= A .gt. 0)
</pre>

Alternatively we may want to take all the negative points in an array and set them to 0. This can be done in one line using the &#8216;where&#8217; command:

<pre class="brush: plain; title: ; notranslate" title="">where(my_array .lt. 0.0) my_array = 0.0
</pre>

Dynamically allocating and deallocating arrays in Fortran is easy. For instance, to allocate a 2D array:

<pre class="brush: plain; title: ; notranslate" title="">real, dimension(:,:), allocatable :: name_of_array
allocate(name_of_array(xdim, ydim))
</pre>

C/C++[ requires the following code](http://www.eskimo.com/~scs/cclass/int/sx9b.html):

<pre class="brush: cpp; title: ; notranslate" title="">int ** array;
array = malloc(nrows * sizeof(double * ));

for(i = 0; i &amp;lt; nrows; i++){
     array[i] = malloc(ncolumns * sizeof(double));
}
</pre>

To deallocate an array in Fortran, we use

<pre class="brush: plain; title: ; notranslate" title="">deallocate(name_of_array)
</pre>

In C/C++, we have:

<pre class="brush: cpp; title: ; notranslate" title="">for(i = 0; i &amp;lt; nrows; i++){
    free(array[i]);
}
free(array);
</pre>

## Point of ease 2: Little need to worry about pointers / memory allocation

In languages like C/C++ , all variables are passed by value, unless they are arrays, which are passed by reference. However, in many scenarios passing an array by value may make more sense &#8211; consider if our data consists of the positions of 100 molecules at different timesteps. Now we may want to analyze the motion of a single molecule. We take a ‘slice’ of the array (a subarray) corresponding to the coordinates of the atoms in that molecule and pass it to a function. Now we are going to do a complicated series of analyses on that subarray. If we used pass by reference, the values being pointed to are going to be non-contiguous in memory. Because of the way CPUs access memory, manipulating non-contiguous data is _slow_. If we pass by value, however, we create a new array in memory which is contiguous. For instance, when passing a slice of a large array into a function to be operated on, the compiler may create a new location in memory if this is deemed more efficient. This may in fact be much more efficient, if the array can be stored in the CPU&#8217;s cache. To the physicist&#8217;s delight, the compiler does all the ‘dirty work’ of optimizing memory use.

In Fortran, variables are usually passed by reference, not by value. Under the hood the Fortran compiler automatically optimizes the passing so as to be most efficient. To a physics professor, a Fortran compiler is a much more trusted optimizer of memory usage than any physics student! As a result of all this, from what I have seen physicists rarely use pointers, although Fortran-90+ [does contain pointers.](http://www.personal.psu.edu/jhm/f90/lectures/42.html)

# A few other points regarding Fortran vs C

Fortran has several features that allow the programmer to give information to the compiler which assists in debugging and optimization. In this way, coding errors can be caught at compile-time, rather than at run-time. For instance, any variable can be declared as a parameter, that is, something which doesn&#8217;t change.

<pre class="brush: cpp; title: ; notranslate" title="">double precision, parameter :: hbar = 6.63e-34
</pre>

If a parameter is ever changed in the code, the compiler returns an error. In C, there is something similar called a_ [const](https://en.wikipedia.org/wiki/Const_(computer_programming)):_

<pre class="brush: cpp; title: ; notranslate" title="">double const hbar = 6.63e-34
</pre>

The problem is that a &#8216;const real&#8217; is a different type than a normal &#8216;real&#8217;. If a function that takes a &#8216;real&#8217; is fed a &#8216;const real&#8217;, it will return an error. It is easy to imagine how this can lead to problems with interoperability between codes.

Fortran also has an &#8216;intent&#8217; specification tells the compiler whether an argument being passed to a function or subroutine is an input, and output, or both an input and output. The use of &#8216;intent&#8217; specifiers helps the compiler optimize code and increases code readability and robustness.

There are other similar features in Fortran, used to varying degrees. For instance, Fortran 95 introduced the idea of declaring a function as &#8216;pure&#8217;. A pure function does not have any side effects &#8211; it only changes variables that are arguments to the function and not any other global variables. A special case of a pure function is an &#8216;elemental&#8217; function, which is a function that takes a scalar argument and returns a scalar, and is meant to operate on the elements of an array. The knowledge that a functions are &#8216;pure&#8217; or &#8216;elemental&#8217; can lead to additional optimizations by the compiler, especially when the code is being parallized.

# What is the future?

In scientific computation, Fortran remains dominant and will not being going away anytime soon.  In [a survey of Fortran users](https://software.intel.com/en-us/blogs/2015/03/27/doctor-fortran-in-the-future-of-fortran) at the 2014 Supercomputing Convention, 100% of respondents said they thought they would still be using Fortran in five years.  The survey also showed that a large number of people were using mixed code with C overwhelmingly the second language (90%). Anticipating the increased mixing of Fortran and C code, the Fortran 2015 specification will have greater features for code interoperability.  Increasingly, Fortran code is being called by higher-level codes written in Python. The computer scientists who bash physicists for using Fortran fail to realize that Fortran remains uniquely suited for doing what it was named for &#8211; FOrmula TRANslation, or converting physics formulas into code. Many are also unaware that Fortran has continued to develop, incorporating new features as time passage (albeit slowly). Calling modern Fortran (Fortran 90+) &#8216;old&#8217; is like calling C++ old because C was first developed around 1973.  On the other hand, even the most modern Fortran standard (2008) retains backwards compatibility to Fortran 77 and most of Fortran 66. In this sense the continued usefulness of Fortran is a challenge to computer scientists. Recently, researchers at MIT have decided to tackle this challenge with full force by developing [a brand new language for HPC called Julia](http://newsoffice.mit.edu/2014/high-performance-computing-programming-ease), first released in 2012. If Julia will actually overtake Fortran remains to be seen. I suspect in any case it will take quite a long time.

## Further reading:

1. [&#8220;The Ideal HPC Programming Language&#8221;](https://queue.acm.org/detail.cfm?id=1820518) &#8211; A software engineer does a detailed analysis (quite above my head) and concludes Fortran comes closest to the ideal language for HPC.

2. [Is Fortran faster than C?](http://stackoverflow.com/questions/146159/is-fortran-faster-than-c) &#8211; The first answer to this StackOverflow question explains why Fortran&#8217;s assumption of no aliasing of memory makes it faster than C.

3. [Implicit None](http://implicitnone.com/about/) &#8211; a blog written by a Fortran enthusiast
