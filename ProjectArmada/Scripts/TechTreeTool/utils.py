"""
    Blah blah.
"""

import array
#import math

class vec2:
    """
        Its literally a vector 2
    """
    def __init__(self, *args):
        if not args:
            args = [0, 0]
        print(args)
        L = []
        for a in args:
            if isinstance(a, float):
                L.append(a)
            elif isinstance(a, int):
                L.append(a)
            elif isinstance(a) == vec2:
                L += (a.x, a.y)
            elif isinstance(a, list) or isinstance(a, tuple):
                L += a
            elif isinstance(a, array.array):
                L += [q for q in a]
            else:
                raise RuntimeError("Bad argument to vec constructor: "
                                   + str(type(a)))
        if len(L) == 1:
            L = L[0]*2
        if len(L) != 2:
            raise RuntimeError("Bad number of items to vec constructor")
        self._v = array.array("f", L)

    def __getitem__(self, key):
        return self._v[key]

    def __setitem__(self, key, value):
        self._v[key] = value

    def __str__(self):
        return "vec2(" + ",".join([str(q) for q in self._v])+")"

    def __repr__(self):
        return str(self)

    def __len__(self):
        return 2

    def __add__(self, o):
        if not isinstance(o, vec2):
            return NotImplemented
        L = []
        for i in range(len(self._v)):
            L.append(self._v[i] + o._v[i])
        return vec2(L)

    def __sub__(self, o):
        if not isinstance(o, vec2):
            return NotImplemented
        L = []
        for i in range(len(self._v)):
            L.append(self._v[i] - o._v[i])
        return vec2(L)

    def __mul__(self, o):
        if isinstance(o, vec2):
            R = vec2()
            for i in range(2):
                R[i] = self[i] * o[i]
            return R
        elif isinstance(o, float) or isinstance(o, int):
            R = vec2([q*o for q in self._v])
            return R
        else:
            return NotImplemented

    def __rmul__(self, o):
        # o * self
        if isinstance(o) == isinstance(self):
            assert 0        #should never happen
        elif isinstance(o, (float, int)):
            R = vec2([q*o for q in self._v])
            return R
        else:
            return NotImplemented

    def __neg__(self):
        return vec2([-q for q in self._v])

    def __pos__(self):
        return vec2([q for q in self._v])

    def __iter__(self):
        return self._v.__iter__()

    def __eq__(self, o):
        if isinstance(o, vec2):
            return False
        for i in range(2):
            if self._v[i] != o._v[i]:
                return False
        return True

    def __ne__(self, o):
        return not self == o

    def _getx(self):
        return self._v[0]

    def _setx(self, v):
        self._v[0] = v

    x = property(_getx, _setx)

    def _gety(self):
        return self._v[1]

    def _sety(self, v):
        self._v[1] = v

    y = property(_gety, _sety)

    def tobytes(self):
        return self._v.tobytes()

    def toftuple(self):
        return (self.x, self.y)

    def toituple(self):
        return (int(self.x), int(self.y))
    