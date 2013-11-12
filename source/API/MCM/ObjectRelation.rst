ObjectRelation
==============


.. module:: MCM
   :noindex:

   .. extension:: ObjectRelation

      ``ObjectRelation`` can be used to create relations between objects in
      the CHAOS database. The relation can optionally be annotated with
      metadata.

      .. action:: Set

         Sets a relation between two Objects, optionally with metadata tied
         to the connection.

         :param object1Guid: GUID of the first object of the relation
         :param object2Guid: GUID of the second object of the relation
         :param objectRelationTypeID: ID of the type of the relation
         :param sequence:
         :type sequence: integer, optional
         :param metadataGuid: GUID of the metadata
         :type metadataGuid: optional
         :param metadataSchemaGuid: the GUID of the MetadataSchema the metadata conforms to
         :type metadataSchemaGuid: optional
         :param languageCode: language of the metadata as a language code
         :param metadataXml: metadata for the relation
         :returns: The number of affected rows in the database

         Annotating the relation with metadata is optional and thus
         ``metadataXml`` and ``languageCode`` can be empty.

      .. action:: Delete

         Delete a relation between two Objects.

         :param object1Guid: GUID of the first object of the relation
         :param object2Guid: GUID of the second object of the relation
         :param objectRelationTypeID: ID of the type of the relation
         :returns: The number of affected rows in the database
