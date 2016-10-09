/* File : kdb.i */
%module kdb
%{
#include "kdb.hpp"
%}

namespace kdb
{
        class Key
        {
        public:
                Key ();
        };
};
