Metadata
========

.. module:: MCM
   :noindex:

   .. extension:: Metadata

      .. action:: Set

         Adds metadata to an object.

         :auth logged_in:
         :auth Permission_to_create_objects: The user needs the ``FolderPermission.CreateUpdateObjects``
                                             on the object
         :param objectGuid: the GUID of the object this metadata describes
         :param metadataSchemaGuid: the GUID of the MetadataSchema this metadata conforms to
         :param languageCode: the language of the metadata as a language code
         :param revisionID: an integer representing the revision of the metadata
         :type revisionID: integer
         :param metadataXml: The XML of the metadata
