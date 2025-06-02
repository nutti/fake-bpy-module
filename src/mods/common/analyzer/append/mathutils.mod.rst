.. mod-type:: append

.. module:: mathutils

.. class:: Color

   .. method:: __init__(rgb=(0.0, 0.0, 0.0))

      :type rgb: Sequence[float]

   .. method:: __get__(instance, owner)

      :rtype: :class:`Color`

   .. method:: __set__(instance, value)

      :type value: :class:`Color`

   .. method:: __add__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __sub__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __mul__(other)

      :type other: float
      :rtype: :class:`Color`

   .. method:: __truediv__(other)

      :type other: float
      :rtype: :class:`Color`

   .. method:: __radd__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __rsub__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __rmul__(other)

      :type other: float
      :rtype: :class:`Color`

   .. method:: __rtruediv__(other)

      :type other: float
      :rtype: :class:`Color`

   .. method:: __iadd__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __isub__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __imul__(other)

      :type other: float
      :rtype: :class:`Color`

   .. method:: __itruediv__(other)

      :type other: float
      :rtype: :class:`Color`

   .. method:: __getitem__(key)

      :type key: int
      :rtype: float
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: tuple[float, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: int
      :type value: float
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: slice
      :mod-option arg key: skip-refine
      :type value: collections.abc.Iterable[float] | :class:`Color`
      :mod-option arg value: skip-refine
      :option function: overload

.. class:: Euler

   .. method:: __init__(angles=(0.0, 0.0, 0.0), order='XYZ')

      :type angles: Sequence[float]
      :type order: str

   .. method:: __get__(instance, owner)

      :rtype: :class:`Euler`

   .. method:: __set__(instance, value)

      :type value: :class:`Euler`

   .. method:: __getitem__(key)

      :type key: int
      :rtype: float
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: tuple[float, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: int
      :type value: float
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: slice
      :mod-option arg key: skip-refine
      :type value: collections.abc.Iterable[float] | :class:`Euler`
      :mod-option arg value: skip-refine
      :option function: overload

.. class:: Matrix

   .. method:: __init__(rows=((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)))

      :type rows: Sequence[Sequence[float]]

   .. method:: __get__(instance, owner)

      :rtype: :class:`Matrix`

   .. method:: __set__(instance, value)

      :type value: :class:`Matrix`

   .. method:: __getitem__(key)

      :type key: int
      :rtype: :class:`Vector`
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: tuple[:class:`Vector`, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: int
      :type value: :class:`Vector` | collections.abc.Iterable[float]
      :mod-option arg value: skip-refine
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: slice
      :mod-option arg key: skip-refine
      :type value: collections.abc.Iterable[:class:`Vector` | collections.abc.Iterable[float]] | :class:`Matrix`
      :mod-option arg value: skip-refine
      :option function: overload

   .. method:: __len__()

      :rtype: int

   .. method:: __add__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Matrix`

   .. method:: __sub__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Matrix`

   .. method:: __mul__(other)

      :type other: float
      :rtype: :class:`Matrix`

   .. method:: __matmul__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Matrix`
      :option function: overload

   .. method:: __matmul__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`
      :option function: overload

   .. method:: __radd__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Matrix`

   .. method:: __rsub__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Matrix`

   .. method:: __rmul__(other)

      :type other: float
      :rtype: :class:`Matrix`

   .. method:: __imul__(other)

      :type other: float
      :rtype: :class:`Matrix`

.. class:: Quaternion

   .. method:: __init__(seq=(1.0, 0.0, 0.0, 0.0), angle=0.0)

      :type seq: :class:`Vector`
      :type angle: float

   .. method:: __get__(instance, owner)

      :rtype: :class:`Quaternion`

   .. method:: __set__(instance, value)

      :type value: :class:`Quaternion`

   .. method:: __len__()

      :rtype: int

   .. method:: __getitem__(key)

      :type key: int
      :rtype: float
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: tuple[float, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: int
      :type value: float
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: slice
      :mod-option arg key: skip-refine
      :type value: collections.abc.Iterable[float] | :class:`Quaternion`
      :mod-option arg value: skip-refine
      :option function: overload

   .. method:: __add__(other)

      :type other: :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __sub__(other)

      :type other: :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __mul__(other)

      :type other: float, :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __matmul__(other)

      :type other: typing_extensions.Self
      :mod-option arg other: skip-refine
      :rtype: typing_extensions.Self
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __matmul__(other)

      :type other: :class:`Vector`
      :mod-option arg other: skip-refine
      :rtype: :class:`Vector`
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __radd__(other)

      :type other: :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __rsub__(other)

      :type other: :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __rmul__(other)

      :type other: float, :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __imul__(other)

      :type other: float, :class:`Quaternion`
      :rtype: :class:`Quaternion`

.. class:: Vector

   .. method:: __init__(seq=(0.0, 0.0, 0.0))

      :type seq: Sequence[float]

   .. method:: __get__(instance, owner)

      :rtype: :class:`Vector`

   .. method:: __set__(instance, value)

      :type value: :class:`Vector`

   .. method:: __len__()

      :rtype: int

   .. method:: __getitem__(key)

      :type key: int
      :rtype: float
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: tuple[float, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: int
      :type value: float
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: slice
      :mod-option arg key: skip-refine
      :type value: collections.abc.Iterable[float] | :class:`Vector`
      :mod-option arg value: skip-refine
      :option function: overload

   .. method:: __neg__()

      :rtype: :class:`Vector`

   .. method:: __add__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __sub__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __mul__(other)

      :type other: float
      :rtype: :class:`Vector`
      :option function: overload

   .. method:: __mul__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`
      :option function: overload

   .. method:: __truediv__(other)

      :type other: float
      :rtype: :class:`Vector`

   .. method:: __matmul__(other)

      :type other: :class:`Vector`
      :rtype: float
      :option function: overload

   .. method:: __matmul__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Vector`
      :option function: overload

   .. method:: __radd__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __rsub__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __rmul__(other)

      :type other: float
      :rtype: :class:`Vector`

   .. method:: __rtruediv__(other)

      :type other: float
      :rtype: :class:`Vector`

   .. method:: __iadd__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __isub__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __imul__(other)

      :type other: float
      :rtype: :class:`Vector`

   .. method:: __itruediv__(other)

      :type other: float
      :rtype: :class:`Vector`
