{
  "targets": [
    {
      "target_name": "kdb",
      "sources": [ "kdb_wrap.cxx" ],
      "include_dirs": [ "/usr/include", "/usr/include/elektra" ],
      "libraries": [ "-L/usr/local/lib", "-lelektra-kdb" ],
      "conditions": [
        [ 'OS=="mac"',
          {
            "xcode_settings": {
              "GCC_ENABLE_CPP_RTTI": "YES",
              "GCC_ENABLE_CPP_EXCEPTIONS" : "YES"
            }
          }
        ],
        [ 'OS=="linux" or OS=="freebsd" or OS=="openbsd" or OS=="solaris"',
          {
            "cflags": [ "-Wno-unused-variable", "-Wno-unused-but-set-variable", "-Wno-unused-but-set-parameter"],
            "cflags_cc": [ "-Wno-unused-variable", "-Wno-unused-but-set-variable", "-Wno-unused-but-set-parameter"],
            "cflags!": [ "-fno-exceptions" ],
            "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ]
          }
        ]
      ]
    }
  ]
}
