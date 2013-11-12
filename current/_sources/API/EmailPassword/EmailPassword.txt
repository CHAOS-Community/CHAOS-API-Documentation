EmailPassword
=============

.. module:: EmailPassword
   :noindex:

   .. extension:: EmailPassword

      .. action:: Login

         :param email: the user's email
         :param password: the user's password
         :param sessionGUID: the GUID of a recently created session

         :returns: :code:`CHAOS.Portal.Authentication.Exception.LoginException` on error
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
