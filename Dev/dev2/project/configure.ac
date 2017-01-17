#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.67])
AC_INIT([softdev-mistery_foo], [0.0.1], [alessandrogbl@gmail.com])
AC_CONFIG_SRCDIR([src/main/main.c])
AC_CONFIG_HEADERS([config.h])
AM_INIT_AUTOMAKE([subdir-objects foreign])
# Checks for programs.
AC_PROG_CC
AM_PROG_CC_C_O
# Checks for libraries.
AC_SEARCH_LIBS([mistery_value], [magic voodoo mistery])
AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include "mistery.h"]], [[return mistery_value(1);]])],[AC_MSG_NOTICE([ the function uses 1 params]) AC_DEFINE([MISTERY_VALUE_ONEPARAM],[1], [one or two params])] ,[AC_MSG_NOTICE([the function uses  2 param])])
# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

AC_CONFIG_FILES([Makefile
                 src/lib_foo/Makefile
                 src/main/Makefile])
AC_OUTPUT
