This is a simple build system explicitly for c, c++, and my own programming language Macro C (MC). it mainly is for personal use.

# Why another build system?

Because the main purpose is to build my own language. as my language is to close to those language (it compiles to C) then I guess it is worth simple write a build system for the whole family.

# What features will be supported?

this is not a replacement for CMake, it is only a personal project. an will be so minimal, but features will be added as needed.

- at start it only will be able to build executables and static libraries.
- then I probably add support for shared libs
- manage dependencies in a way that I do not know already XD.
- and create MakeFiles and Visual Studios Projects only.

# what makes this build system different

the weird and different thing of this build system is that it is not a program as CMake or Premake, instead it is a library written in python that handles most of complexity by itself and generate the project.

this makes a little bit difficult to start or prepare all the build system but in the other hand it has all the power of the python programming language and is simple and clean. there are no hiding corners.
