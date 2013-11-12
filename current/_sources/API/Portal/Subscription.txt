Subscription
============

.. module:: Portal
   :noindex:

   .. extension:: Subscription

      .. action:: Get

         Gets a subscription.

         :auth logged_in:
         :param guid: The GUID of the subscription
         :returns: The Subscription with the requested GUID
         :rtype: SubscriptionInfo

      .. action:: Create

         Creates a new subscription.

         :auth logged_in:
         :auth CreateSubscription_permission: The user must have the
                                              SystemPermissons.CreateSubscription
                                              permission
         :param name: The name of the new subscription
         :returns: The new Subscription
         :rtype: SubscriptionInfo

      .. action:: Delete

         Deletes a subscription.

         :auth logged_in:
         :param guid: The GUID of the subscription
         :returns: The number of affected rows in the database

      .. action:: Update

         Renames a subscription.

         :auth logged_in:
         :param guid: The GUID of the subscription
         :param name: The new name of the subscription
         :returns: The number of affected rows in the database
