Examples
========

Default Behavior
----------------

.. code-block:: python

    def f(x=[]):
        x.append(2)
        return x


.. code-block:: python

    >>> a = f()
    >>> a
    [2]
    >>> f()
    >>> a
    [2, 2]


Altered Behavior
----------------

.. code-block:: python

    from stabledefaults import stabledefaults

    @stabledefaults()
    def f(x=[]):
        x.append(2)
        return x


.. code-block:: python

    >>> a = f()
    >>> a
    [2]
    >>> f()
    >>> a
    [2]
