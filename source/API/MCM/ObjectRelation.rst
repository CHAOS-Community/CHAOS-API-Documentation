ObjectRelation
==============


.. module:: MCM
   :noindex:

   .. extension:: ObjectRelation

      ``ObjectRelation`` can be used to create relations between objects in
      the CHAOS database.

      .. action:: Create

         Creates a relation between two Objects.

         :param object1GUID: GUID of the first object of the relation
         :param object2GUID: GUID of the second object of the relation
         :param objectRelationTypeID: ID of the type of the relation
         :param sequence:
         :type sequence: integer, optional
         :returns: The number of affected rows in the database

      .. action:: Delete

         Delete a relation between two Objects.

         :param object1GUID: GUID of the first object of the relation
         :param object2GUID: GUID of the second object of the relation
         :param objectRelationTypeID: ID of the type of the relation
         :returns: The number of affected rows in the database
