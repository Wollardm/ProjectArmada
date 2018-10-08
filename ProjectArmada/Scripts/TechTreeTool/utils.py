"""
    Blah blah.
"""

import array
#import math

class vec3:
    """
        Its literally a 1x3 vector
    """
    def __init__(self, *args):
        if not args:
            args = [0, 0, 0]
        L = []
        for a in args:
            if isinstance(a, float):
                L.append(a)
            elif isinstance(a, int):
                L.append(a)
            elif isinstance(a, vec3):
                L += (a.x, a.y, a.z)
            elif isinstance(a, (list, tuple)):
                L += a
            elif isinstance(a, array.array):
                L += [q for q in a]
            else:
                raise RuntimeError("Bad argument to vec constructor: "
                                   + str(type(a)))
        if len(L) == 1:
            L = L[0]*3
        while len(L) < 3:
            L.append(0.0)
        if len(L) > 3:
            raise RuntimeError("Bad number of items to vec constructor")
        self._v = array.array("f", L)

    def __getitem__(self, key):
        return self._v[key]

    def __setitem__(self, key, value):
        self._v[key] = value

    def __str__(self):
        return "vec3(" + ",".join([str(q) for q in self._v])+")"

    def __repr__(self):
        return str(self)

    def __len__(self):
        return 2

    def __add__(self, o):
        if isinstance(o, vec3):
            L = []
            for i in range(len(self._v)):
                L.append(self._v[i] + o._v[i])
            return vec3(L)
        elif isinstance(o, tuple):
            L = []
            for i in range(len(self._v)):
                L.append(self._v[i] + o[i])
            return vec3(L)
        return NotImplemented

    def __sub__(self, o):
        if not isinstance(o, vec3):
            return NotImplemented
        L = []
        for i in range(len(self._v)):
            L.append(self._v[i] - o._v[i])
        return vec3(L)

    def __mul__(self, o):
        if isinstance(o, vec3):
            R = vec3()
            for i in range(3):
                R[i] = self[i] * o[i]
            return R
        elif isinstance(o, (float, int)):
            R = vec3([q*o for q in self._v])
            return R
        else:
            return NotImplemented

    def __rmul__(self, o):
        # o * self
        if isinstance(o, (float, int)):
            R = vec3([q*o for q in self._v])
            return R
        return NotImplemented

    def __neg__(self):
        return vec3([-q for q in self._v])

    def __pos__(self):
        return vec3([q for q in self._v])

    def __iter__(self):
        return self._v.__iter__()

    def __eq__(self, o):
        if isinstance(o, vec3):
            return False
        for i in range(3):
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

    def _getz(self):
        return self._v[2]

    def _setz(self, v):
        self._v[2] = v

    z = property(_getz, _setz)

    def tobytes(self):
        """
            Also doing this to avoid bitching.

            Args:
            Returns:
            Raises:
        """
        return self._v.tobytes()

    def to3ftuple(self):
        """
            Also doing this to avoid bitching.

            Args:
            Returns:
            Raises:
        """
        return (self.x, self.y, self.z)

    def to3ituple(self):
        """
            Also doing this to avoid bitching.

            Args:
            Returns:
            Raises:
        """
        return (int(self.x), int(self.y), int(self.z))

    def to2ftuple(self):
        """
            Also doing this to avoid bitching.

            Args:
            Returns:
            Raises:
        """
        return (self.x, self.y)

    def to2ituple(self):
        """
            Also doing this to avoid bitching.

            Args:
            Returns:
            Raises:
        """
        return (int(self.x), int(self.y))

def dot(v, w):
    """
            Also doing this to avoid bitching.

            Args:
            Returns:
            Raises:
    """
    assert type(v) == type(w)
    assert isinstance(v, vec3)
    return sum([v[i] * w[i] for i in range(len(v))])

def length(v):
    """
            Also doing this to avoid bitching.

            Args:
            Returns:
            Raises:
    """
    assert isinstance(v, vec3)
    return dot(v, v) ** 0.5
