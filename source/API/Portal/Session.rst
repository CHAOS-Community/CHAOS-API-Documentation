Session
=======

.. module:: Portal
   :noindex:

   .. extension:: Session

      .. action:: Get

         Gets the current session.

         :returns: The current session

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

      .. action:: Create

         Creates a session, which can be authenticated via the
         :act:`EmailPassword/Login` method.

         :param: None
         :returns: The created session

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

      .. action:: Update

         Refreshes the current session – in effect extending its lifetime.

         :returns: The current session

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

      .. action:: Delete

         Deletes the current session – the equivalent of logging out.

         :returns: The number of affected rows in the database
