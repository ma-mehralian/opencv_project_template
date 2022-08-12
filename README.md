# OpenCV Project Template

I create this repository to show how my C++ computer vision projects with OpenCV structured.
**This document is not complete (In progress...)**

## project structure

Each project may contains multiple **applications**.
For example, one of these applications can be a GUI and the other can be a shared library for other projects usage.
Each application may contatins multiple **modules**. Modules allow us to keep the features of our project in separate, smaller pieces.

As a result the root folder structure is like:

```text
<project_name>
 ├── apps/
 ├── cmake/
 ├── docs/
 ├── modules/
 ├── scripts/
 ├── CMakeLists.txt
 └── README.md
```

- `apps` : Apps targets are usually executable or shared library.
- `cmake`*: cmake files used for other dependencies (.cmake files).
- `docs`*: project documents like installation, ... (doxygen or .md files).
- `modules`: Modules targets are usually static library.
- `scripts`*: some scripts like Devops, ... (shell, .py files).

*Optional items are marked with an asterisk(***)*

## App Structure

For each application folder structure is like:

```text
<app_name>
 ├── data/
 ├── docs/
 ├── src/
 ├── CMakeLists.txt
 └── README.md
```

- `data`* - containing non-source code aspects of the app (icon files, ...)
- `docs`* - module documents (doxygen or .md files).
- `src` - app source files (.h and .cpp files).

*Optional items are marked with an asterisk(***)*

## Module Structure

For each module folder structure is like:

```text
<module_name>
 ├── data/
 ├── docs/
 ├── examples/
 │   ├── example_title.cpp
 │   └── ...
 ├── include/
 │   └── <module_name>/
 │       ├── xxx.h
 │       └── ...
 ├── src/
 ├── test/
 │   ├── func1_text.cpp
 │   └── ...
 ├── CMakeLists.txt
 └── README.md
```

- `data`* - containing non-source code aspects of the module (model files, ...)
- `docs`* - module documents (doxygen or .md files).
- `examples` - example usage of the module.
- `include` - PUBLIC module header files (.h files).
- `src` - PRIVATE module source files (.h and .cpp files).
- `test` - tests files

*Optional items are marked with an asterisk(***)*
