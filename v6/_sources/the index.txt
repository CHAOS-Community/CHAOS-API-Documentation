=========
The Index
=========

In order to find objects in the database CHAOS uses Solr_.

.. _Solr: http://lucene.apache.org/solr/

Solr is a search engine to which you can send search queries.
Solr uses an ``Index`` for searching. The index has a number of fields.

The :code:`query` argument of the :func:`Object.Get`-function passes its value
on to Solr as a search string.

Fields present in the Solr Index are called ``indexed`` fields.

.. _theindex-solrquerysyntax:

Solr query syntax
-----------------
Let's say that a field named ``Title`` is indexed in Solr.

We could then search for ``hest`` by using the search string
:code:`Title:hest`.

In CHAOS it looks like this:
:chaos_api_link_object_get_apg:`pageSize=5&query=Title:hest`

There is no ``Title`` field in the CHAOS Solr index so we get an error.

There is, however, a field called :code:`DKA-Title_string`, so we can do a
succesfull search like this:
:chaos_api_link_object_get_apg:`pageSize=5&query=DKA-Title_string:hest`

To combine searches in multiple fields, Solr provides the operators :code:`AND`
and :code:`OR`.
You use by inserting them (with spaces) between field searches:
:code:`field1:search_value1 OR field2:search_value2`

.. note:: You cannot have space-characters in a URL. In a URL spaces are represented
          with either :code:`+` or :code:`%20`.

.. When to use `%20` vs `+`? See: http://stackoverflow.com/a/8116989/118608

Here we search for objects with either *hest* or *ukendt* in their title:
:chaos_api_link_object_get_apg:`pageSize=5&query=DKA-Title_string:hest+OR+DKA-Title_string:ukendt`

Spaces (without any operator) are interpreted as :code:`OR`:
:chaos_api_link_object_get_apg:`pageSize=5&query=DKA-Title_string:hest+DKA-Title_string:ukendt`

:code:`AND` cannot be omitted.

.. _theindex-indexedfieldsinchaos:

Indexed fields in CHAOS
-----------------------
In general there is no specification of what fields are indexed in CHAOS -- this
up to the database administrator.

However you *can* expect metadata to be indexed in the following way:

:code:`m<MetadataSchemaGUID>_<LanguageCode>_all`

Searching this field will search through all metadata that has the specified
``LanguageCode`` and ``MetadataSchemaGUID``. You can use this search field to
search for objects in a meaningful way, because you will typically have a
single MetadataSchema that defines how the title, description and so on should
be given. Thus by searching the correct MetadataSchemaGUID you can search the
title and description of objects.
