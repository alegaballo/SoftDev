 -----------====== Assignment  ======--------------
 
ldd is a tool that lists all the dynamic libraries
required by a program to run. 
For instance, ldd /bin/ls can print something like this:

linux-vdso.so.1 =>  (0x00007ffdc4558000)
libselinux.so.1 => /lib/x86_64-linux-gnu/libselinux.so.1 (0x00007f924ee10000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f924ea47000)
libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3 (0x00007f924e7d6000)
libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f924e5d2000)
/lib64/ld-linux-x86-64.so.2 (0x000055ac570eb000)
libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f924e3b5000)

Your goal is to print the list of the libraries most commonly 
used by the binaries contained in a given directory, specified in
the shell variable DIR_PATH.

For example, if DIR_PATH=/bin/, your program should print:

     99     linux-vdso.so.1 
     99     libc.so.6 
     25     libdl.so.2 
     19     libpthread.so.0 
     18     librt.so.1 
     10     libselinux.so.1 
      5     libntfs-3g.so.79 
      5     libnsl.so.1 
      5     libattr.so.1 
      5     libacl.so.1 
      3     libpcre.so.3 
      3     libglib-2.0.so.0 
      3     libbz2.so.1.0 
      2     libuuid.so.1 
      2     libresolv.so.2 
      2     libproc-3.2.8.so 
      2     libpam_misc.so.0 
      2     libpam.so.0 
      2     libncursesw.so.5 
      2     libncurses.so.5 
      2     libfuse.so.2 
      2     libcrypt.so.1 
      2     libblkid.so.1 
      1     libz.so.1 
      1     libsepol.so.1 
      1     libply.so.2 
      1     libm.so.6 
      1     libexpat.so.1 
      1     libdbus-1.so.3 
      1     libcrypto.so.0.9.8 


 -----------====== Submission  ======--------------

Submit a text file containing in the first line your command
as you would write it on the shell. Your command will be tested invoking:

$> DIR_PATH=/bin/ bash yourfile



