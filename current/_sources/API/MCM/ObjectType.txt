ObjectType
==========

.. module:: MCM
   :noindex:

   .. extension:: ObjectType

      .. action:: Set

         Creates or updates an ObjectType.

         :auth logged_in:
         :auth system_manage_permission:
         :param id: ID of the (new) ObjectType
         :param name: Name of the (new) ObjectType
         :returns: The updated or new ObjectType

         If the no ObjectType with the specific ``id`` exists a
         new ObjectType is created.

      .. action:: Get

         Gets all ObjectTypes.

         :returns: A list of ObjectTypes

      .. action:: Delete

         Deletes an ObjectType.

         :auth logged_in:
         :auth system_manage_permission:
         :param id: ID of the ObjectType to delete
         :returns: The number of affected rows in the database
