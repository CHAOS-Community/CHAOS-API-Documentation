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

.. module:: Portal

   .. extension:: ClientSettings

      .. action:: Get

         Get settings of a client.

         :param guid: GUID of the client

      .. action:: Set

         Set settings of a client.

         :param guid: The (new) GUID of the client
         :param name: The (new) name of the client
         :param settings: The new settings of the client
         :type setting: a string



   .. extension:: Session

      .. action:: Create

         Creates a session, which can be authenticated via the
         :act:`EmailPassword/Login` method.

         :param protocolVersion: must have a value of :code:`4`
         :rtype: A :code:`ModuleResult` with a single :code:`Result` with a :code:`SessionGUID`

         .. code-editor:: xml

             <PortalResult Duration="12">
               <ModuleResults>
                 <ModuleResult Fullname="Portal" Duration="0" Count="1">
                   <Results>
                     <Result FullName="CHAOS.Portal.DTO.Standard.Session">
                       <SessionGUID>47c72c3c-9126-9549-8517-340c4275e22b</SessionGUID>
                       <UserGUID>c0b231e9-7d98-4f52-885e-af4837faa352</UserGUID>
                       <DateCreated>03-10-2013 14:00:20</DateCreated>
                       <DateModified>03-10-2013 14:00:20</DateModified>
                     </Result>
                   </Results>
                 </ModuleResult>
               </ModuleResults>
             </PortalResult>

         .. seealso::

             * :ref:`Authentication -> Login <authentication-login>`
             * :act:`EmailPassword/Login`


.. module:: EmailPassword

  .. extension:: EmailPassword

    .. action:: Login

      :param email: the user's email
      :param password: the user's password
      :param sessionGUID: the GUID of a recently created session

      :rtype: :code:`CHAOS.Portal.Authentication.Exception.LoginException` on error
              and
              :code:`CHAOS.Portal.DTO.Standard.UserInfo` on success

      http://api.danskkulturarv.dk/EmailPassword/Login?email=test@example.org&password=mysecret

      .. code-editor:: xml

        <PortalResult Duration="23">
          <ModuleResults>
            <ModuleResult Fullname="EmailPassword" Duration="0" Count="1">
              <Results>
                <Result FullName="CHAOS.Portal.DTO.Standard.UserInfo">
                  <GUID>80d15fb4-c1fb-9445-89c6-1a398cbd85e5</GUID>
                  <SystemPermissions>2</SystemPermissions>
                  <Email>admin@danskkulturarv.dk</Email>
                  <SessionDateCreated>03-10-2013 14:25:42</SessionDateCreated>
                  <SessionDateModified>03-10-2013 14:26:14</SessionDateModified>
                </Result>
              </Results>
            </ModuleResult>
          </ModuleResults>
        </PortalResult>


.. module:: MCM

   The ``MCM`` module stands for *Media Content Manager* and does exactly
   that: it contains functions for managing the media in the database.

  .. extension:: Object

    The ``Object`` extension gets, sets and updates objects in the database.

    .. action:: Get

      Retrieves objects according to a query.

      ``Object/Get`` is the main search and object retrieval function in  CHAOS.

      :param query: the Solr search query (See :doc:`the index`)
      :param pageIndex: the index of page that should be returned
      :type pageIndex: optional
      :param pageSize: the number of object returned (one request gives one page)
      :type pageSize: optional
      :param includeMetadata: whether metadata should be returned for each object
      :type includeMetadata: optional
      :param includeFiles: whether files should be returned for each object
      :type includeFiles: optional
      :param includeAccessPoints: whether accessPoints should be returned for each object
      :type includeAccessPoints: optional
      :param includeObjectRelations: whether objectRelations should be returned for each object
      :type includeObjectRelations: optional
      :param includeFolders: whether objectRelations should be returned for each object
      :type includeFolders: optional
      :param accessPointGUID:
      :type accessPointGUID: optional
      :param sessionGUID: the GUID of an authorized session
      :type sessionGUID: optional
      :rtype: A list of objects

      Either an authorized sessionGUID or accessPointGUID must be provided.

      By default no files, metadata, accessPoints or object relations will be
      returned.

    .. action:: SetPublishSettings
       
       Publishes/unpublishes an object on an :code:`accessPointGUID` in a given time
       period (or indefinitely). 
       
       The :code:`accessPointGUID` must exists in the database in order to publish on
       it. As of 7th October 2013 you cannot create an :code:`accessPointGUID` in the
       database via the API.
       
       :auth logged_in:
       :auth Write_permission: you need have write-permission to the AccessPoint
                               you are publishing to.
       :param objectGUID: the GUID of the object for which you want to set :code:`accessPointGUID`
       :param accessPointGUID: the :code:`accessPointGUID` you want to publish on
       :param sessionGUID: the GUID of an authorized session
       :param startDate: the start of publishing period
       :type startDate: optional
       :param endDate: the end of the publishing period
       :type endDate: optional
       :rtype: * On success: :code:`CHAOS.Portal.DTO.Standard.ScalarResult` with value :code:`1`
               * On error: a number of different errors can be given on erroneous dates,
                 accessPointsGUID or objectsGUIDs. If the accessPoint does not exists you will
                 get :code:`CHAOS.Portal.Exception.InsufficientPermissionsException`
       
       *startDate* and *endDate* should be in the format 
       :code:`DD-MM-YYYY HH:MM:SS` where the first :code:`MM` is month and the seconds
       is minutes.
       e.g. :code:`03-10-2013 14:25:42` is the 3rd of October 2013, twenty-five minutes
       and fourty-two seconds past 2 PM.
       
       If no *startDate* is given the object will is unpublished, i.e. it will not be
       accessible from the given accessPoint. That is the following situations will
       unpublish the object:
       
       .. role:: gbg
       
       .. role:: rbg
       
       ================  ================  ================================
         ``SetPublishSettings`` parameters
       --------------------------------------------------------------------
       startDate         endDate           What happens
       ================  ================  ================================
       :rbg:`not given`  :rbg:`not given`  Object is unpublished
       :rbg:`not given`  :gbg:`given`      Object is unpublished
       :gbg:`given`      :rbg:`not given`  Object is published indefinitely
       :gbg:`given`      :gbg:`given`      Object is published in given
                                           time period
       ================  ================  ================================
       
       .. raw:: html
       
         <script>
           // depends on jQuery and Bootstrap
           $(document).ready(function() {
             $('.gbg').parent().addClass('gbg');
             $('.rbg').parent().addClass('rbg');
           });
         </script>
         <style>
           td.gbg { text-align: center; background-color: #F2DEDE; }
           td.rbg { text-align: center; background-color: #DFF0D8; }
         </style>
       
       If *startDate* is given but no *endDate* is given the object will be published
       until you change the publish period or remove the accessPoint.
       
       :chaos_api_link_object_setpublishsettings_apg:`objectGUID=00000000-0000-0000-0000-000000820016&sessionGUID=9755b31c-c0d4-2a47-9605-487b1401d1fa&startDate=01-10-2013+06:00:00`
       
       .. code-editor:: xml
       
         <PortalResult Duration="104">
           <ModuleResults>
             <ModuleResult Fullname="MCM" Duration="0" Count="1">
               <Results>
                 <Result FullName="CHAOS.Portal.DTO.Standard.ScalarResult">
                   <Value>1</Value>
                 </Result>
               </Results>
             </ModuleResult>
           </ModuleResults>
         </PortalResult>
       
       .. seealso::
       
           :ref:`Authentication -> accessPointGUID <authentication-accesspointguid>`

  .. extension:: MetadataSchema

    .. action:: Get

      Gets one or all MetadataSchemas in the database.

      :auth logged_in:
      :auth Read_permission: you will get the MetadataSchemas you have permission to read
      :param metadataSchemaGUID: the GUID of the schema to get
      :type metadataSchemaGUID: optional
      :rtype: A list of MetadataSchemas

      If no ``metadataSchemaGUID`` is given, all MetadataSchemas which the user
      has rights to read are returned.

      .. code-editor:: xml

        <PortalResult Duration="24">
          <ModuleResults>
            <ModuleResult Fullname="MCM" Duration="0" Count="9">
              <Results>
                <Result FullName="CHAOS.MCM.Data.Dto.Standard.MetadataSchema">
                  <GUID>00000000-0000-0000-0000-000063c30000</GUID>
                  <Name>DKA</Name>
                  <SchemaXML>
                  <![CDATA[
                  <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified"><xs:element name="DKA"><xs:complexType><xs:sequence minOccurs="0" maxOccurs="unbounded"><xs:element name="Title" type="xs:string" /><xs:element name="Abstract" type="xs:string" /><xs:element name="Description" type="xs:string" /><xs:element name="Organization" type="xs:string" /><xs:element name="Type" type="xs:string" /><xs:element name="CreatedDate" type="xs:date" minOccurs="0" maxOccurs="unbounded" /><xs:element name="FirstPublishedDate" type="xs:dateTime" /><xs:element name="Identifier" type="xs:string" /><xs:element name="Contributor"><xs:complexType><xs:sequence><xs:element name="Person" minOccurs="0" maxOccurs="unbounded"><xs:complexType><xs:attribute name="Name" type="xs:string" use="required" /><xs:attribute name="Role" type="xs:string" /></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="Creator"><xs:complexType><xs:sequence><xs:element name="Person" minOccurs="0" maxOccurs="unbounded"><xs:complexType><xs:attribute name="Name" type="xs:string" use="required" /><xs:attribute name="Role" type="xs:string" /></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="TechnicalComment" type="xs:string" /><xs:element name="Location" type="xs:string" /><xs:element name="RightsDescription" type="xs:string" /><xs:element name="GeoData" minOccurs="0" maxOccurs="unbounded"><xs:complexType><xs:sequence><xs:element name="Latitude" type="xs:decimal" /><xs:element name="Longitude" type="xs:decimal" /></xs:sequence></xs:complexType></xs:element><xs:element name="Categories"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" name="Category" type="xs:string" /></xs:sequence></xs:complexType></xs:element><xs:element name="Tags"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" name="Tag" type="xs:string" /></xs:sequence></xs:complexType></xs:element><xs:element name="Metafield" minOccurs="0" maxOccurs="unbounded"><xs:complexType><xs:sequence><xs:element name="Key" type="xs:string" /><xs:element name="Value" type="xs:string" /></xs:sequence></xs:complexType></xs:element><xs:element name="ProductionID" type="xs:string" minOccurs="0" maxOccurs="unbounded" /><xs:element name="StreamDuration" type="xs:string" minOccurs="0" maxOccurs="unbounded" /></xs:sequence></xs:complexType></xs:element></xs:schema>
                  ]]>
                  </SchemaXML>
                  <DateCreated>09-04-2012 10:33:42</DateCreated>
                </Result>
              </Results>
            </ModuleResult>
          </ModuleResults>
        </PortalResult>

    .. action:: Update

       Updates a MetadataSchema in the database.

       :auth logged_in:
       :auth Write_permission: you need to have write-permissions to the MetadataSchema
       :param metadataSchemaGUID: the GUID of the schema to update
       :param name: a new (or the same) name for schema
       :param schemaXml: a new (or the same) XML for the schema
       :rtype: The GUID of the updated MetadataSchema

    .. action:: Create

       Adds a new MetadataSchema to the database.

       You need to be logged in to use this feature and the user must have
       administritive rights.

       :auth logged_in:
       :auth system_manage_permission:
       :param name: a new name for the new schema
       :param schemaXml: the XML for the new schema
       :param metadataSchemaGUID: the GUID for new schema
       :type metadataSchemaGUID: optional
       :rtype: The GUID of the created MetadataSchema

       If no ``metadataSchemaGUID`` is given, CHAOS assign a GUID to the new
       schema. The new GUID is returned as a result.
