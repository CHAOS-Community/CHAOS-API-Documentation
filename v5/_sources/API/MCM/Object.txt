Object
======

.. module:: MCM
   :noindex:

   .. extension:: Object

      The ``Object`` extension gets, sets and updates objects in the database.

      .. action:: Get

         Retrieves objects according to a query.

         ``Object/Get`` is the main search and object retrieval function in  CHAOS.

         :param query: the Solr search query (See :doc:`/the index`)
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
         :returns: A list of objects

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
         :returns: * On success: :code:`CHAOS.Portal.DTO.Standard.ScalarResult` with value :code:`1`
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

      .. action:: Create

         Creates an Object.

         :auth logged_in:
         :auth Permission_to_folder: You need to have permission to create objects
                                     in the folder
                                     (``FolderPermission.CreateUpdateObjects``)
         :param guid: The GUID of the new object
         :type guid: optional
         :param objectTypeID: ID of the ObjectType of the new object
         :param folderID: The ID of folder in which the object should be created
         :returns: The created Object

         If no GUID is given, CHAOS will generate a guid for the new object.

      .. action:: Delete

         Deletes an Object.

         :auth logged_in:
         :auth Permission_to_folder: You need to have permission to delete objects
                                     in the folder in which the object resides
                                     (``FolderPermission.DeleteObject``)
         :param guid: The GUID of the object to delete
         :returns: The number of affected rows in the database
