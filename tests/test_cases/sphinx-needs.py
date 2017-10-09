"""Example reStructuredText from Sphinx-Needs project.

From http://sphinxcontrib-needs.readthedocs.io/en/latest/

**Some data**

.. req:: My first requirement
   :id: req_001
   :tags: example

   This is an awesome requirement and it includes a nice title,
   a given id, a tag and this text as description.

.. spec:: Spec for a requirement
   :links: req_001
   :status: done
   :tags: important; example

   We haven't set an **ID** here, so sphinxcontrib-needs
   will generated one for us.

   But we have **set a link** to our first requirement and
   also a *status* is given.

**Some text**

Wohooo, we have created :need:`req_001`,
which is linked by :need_incoming:`req_001`.

**A filter**

.. needfilter::
   :tags: example
   :layout: table
"""

print("sphinx-needs defines its own reStructuredText directives.")