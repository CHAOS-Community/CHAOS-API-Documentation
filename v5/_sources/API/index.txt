.. container:: custom-index

    .. raw:: html

        <!-- Insert functions into menu -->
        <script type="text/javascript" src='_static/menu_api_functions.js'></script>

===
API
===

The HTTP API for CHAOS is called **Portal**.

Requests to the API have the following URL-structure:

.. code::

    <SERVICE_PATH>/<PROTOCOL_VERSION>/<EXTENSION>/<ACTION>?<ARGUMENTS>

for example

.. code::

    http://api.chaos-systems.com/v4/Object/Get?pageSize=8

Has a

 * ``ServicePath`` that is :code:`http://api.chaos-systems.com`
 * ``ProtocolVersion`` that is :code:`v4`
 * ``Extension`` that is :code:`Object`
 * ``Action`` that is :code:`Get` with one ``Argument``: :code:`pageSize` with a value of
   :code:`8`.

Such an HTTP Request executes the specified ``Action``. |br|
``Arguments`` to an ``Action`` should be passed via the query string as fields
and values, i.e.  :code:`field1=value1&field2=value2...`

``ProtocolVersion`` and its following slash can be omitted. In that case the current
version will be used.

This page documents the ``Actions`` you can use in CHAOS. Each section has a
heading of the form :code:`Extension/Action` which you can simply copy into your
URL.

Each ``Extension`` belongs to a module.

On a succesfull request Portal will return a structure similar to the following:

.. code-editor:: xml

   <PortalResult Duration="CHAOS call duration">
     <ModuleResults>
       <ModuleResult Fullname="Module name" Duration="0" Count="Number of results">
         <Results>
           <Result FullName="Name of object">
              ...
           </Result>
           ...
         </Results>
       </ModuleResult>
     </ModuleResults>
   </PortalResult>

The ``Fullname`` attribute of :code:`<ModuleResult>` will correspond to the name
of module of the extension you called. The ``Count`` attribute tells you how
many :code:`<Result>` elements the :code:`<Results>` tag contains.

:code:`<Result>` will contain a number of elements corresponding to the fields
of the object you requested.

Here's an example result from the action ``Object/Get``:

.. code-editor:: xml

   <PortalResult Duration="84">
     <ModuleResults>
       <ModuleResult Fullname="MCM" Duration="0" Count="2" TotalCount="5">
         <Results>
           <Result FullName="CHAOS.MCM.Data.DTO.Object">
             <GUID>00000000-0000-0000-0000-00007d080016</GUID>
             <ObjectTypeID>36</ObjectTypeID>
             <DateCreated>25-05-2012 15:50:01</DateCreated>
             <Metadatas/>
             <Files/>
             <ObjectRelations/>
           </Result>
           <Result FullName="CHAOS.MCM.Data.DTO.Object">
             <GUID>546f2bc2-dcd4-424e-b695-729e0152bdeb</GUID>
             <ObjectTypeID>36</ObjectTypeID>
             <DateCreated>21-03-2013 17:29:23</DateCreated>
             <Metadatas/>
             <Files/>
             <ObjectRelations/>
           </Result>
         </Results>
       </ModuleResult>
     </ModuleResults>
   </PortalResult>

``TotalCount`` is specific to the ``Object/Get`` action which is
paginated and tells you the total number of results for the request.

.. rubric:: List of modules and their extensions


.. class:: columns


.. toctree::
   Portal/index
   EmailPassword/index
   MCM/index

..
  +----------------------+---------------------+----------------------+
  |Portal module         |EmailPassword module |MCM module            |
  +======================+=====================+======================+
  |:ext:`ClientSettings` |:ext:`EmailPassword` |:ext:`Destination`    |
  +----------------------+---------------------+----------------------+
  |:ext:`Session`        |                     |:ext:`File`           |
  +----------------------+---------------------+----------------------+
  |:ext:`Group`          |                     |:ext:`Folder`         |
  +----------------------+---------------------+----------------------+
  |:ext:`Subscription`   |                     |:ext:`Link`           |
  +----------------------+---------------------+----------------------+
  |:ext:`UserSettings`   |                     |:ext:`Mcm`            |
  +----------------------+---------------------+----------------------+
  |:ext:`User`           |                     |:ext:`Metadata`       |
  +----------------------+---------------------+----------------------+
  |                      |                     |:ext:`MetadataSchema` |
  +----------------------+---------------------+----------------------+
  |                      |                     |:ext:`Object`         |
  +----------------------+---------------------+----------------------+
  |                      |                     |:ext:`ObjectRelation` |
  +----------------------+---------------------+----------------------+
  |                      |                     |:ext:`ObjectType`     |
  +----------------------+---------------------+----------------------+
  |                      |                     |:ext:`UserManagement` |
  +----------------------+---------------------+----------------------+
  |                      |                     |:ext:`UserProfile`    |
  +----------------------+---------------------+----------------------+
